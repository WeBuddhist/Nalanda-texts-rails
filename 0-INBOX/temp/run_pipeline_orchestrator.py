#!/usr/bin/env python3
"""Orchestrator for commentary-pipeline on Tibetan commentaries.
Runs:
  1. TOC extraction (passes 1-2 in parallel, pass 3 tree, pass 4 QC)
  2. Anchoring (pass 5) + frame nodes
  3. Ingestion into commentary units
  4. Meaning-based resegmentation (parallel windows) + QC
  5. Stamping body IDs + strict text verification
"""

import concurrent.futures
import os
import re
import subprocess
import sys
import time
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parents[2]
INBOX = VAULT_ROOT / "0-INBOX"
COMMENTARY_DIR = INBOX / "commentary"
SEGMENTED_DIR = INBOX / "segmented"
TEMP_DIR = INBOX / "temp"
RESEG_DIR = INBOX / "resegmented"
TOC_INGEST_DIR = TEMP_DIR / "segmented-commentary-with-toc"

LIB_DIR = VAULT_ROOT / "4-SYSTEM" / "Skills" / "seg-toc-lib"
TOC_EXTRACTOR_DIR = LIB_DIR / "toc_tree_extractor"
RESEG_SCRIPTS_DIR = VAULT_ROOT / "4-SYSTEM" / "Skills" / "commentary-resegment" / "scripts"

sys.path.insert(0, str(TOC_EXTRACTOR_DIR))
sys.path.insert(0, str(RESEG_SCRIPTS_DIR))
sys.path.insert(0, str(LIB_DIR))

import extract_toc_tree as ett
import find_toc_contexts as ftc
import resegment


def ensure_dirs(cid: str):
    toc_folder = TEMP_DIR / f"TOC-{cid}"
    (toc_folder / "candidates").mkdir(parents=True, exist_ok=True)
    (toc_folder / "enumerations").mkdir(parents=True, exist_ok=True)
    RESEG_DIR.mkdir(parents=True, exist_ok=True)
    TOC_INGEST_DIR.mkdir(parents=True, exist_ok=True)
    (TEMP_DIR / f"RESEG-{cid}" / "windows").mkdir(parents=True, exist_ok=True)
    return toc_folder


def run_parallel_toc_passes_1_2(cid: str, max_workers: int = 8):
    """Run pass 1 (candidates) and pass 2 (enumerations) in parallel across chunks."""
    src_file = SEGMENTED_DIR / f"{cid}.units.md"
    if not src_file.exists():
        raise FileNotFoundError(f"Segmented file not found: {src_file}")

    toc_folder = ensure_dirs(cid)
    cand_dir = toc_folder / "candidates"
    enum_dir = toc_folder / "enumerations"

    lines = src_file.read_text(encoding="utf-8").splitlines(keepends=True)
    chunks = ett.make_chunks(lines, 150, 25)
    print(f"[{cid}] Chunks: {len(chunks)} (size=150, overlap=25)")

    client = ett.get_client()

    # Pass 1 tasks
    p1_tasks = []
    for idx, start, end, text, numbered in chunks:
        out_f = cand_dir / f"chunk_{idx:03d}.md"
        if not out_f.exists():
            p1_tasks.append((idx, start, end, numbered, out_f))

    # Pass 2 tasks
    p2_tasks = []
    for idx, start, end, text, numbered in chunks:
        out_f = enum_dir / f"chunk_{idx:03d}.md"
        if not out_f.exists():
            p2_tasks.append((idx, start, end, text, out_f))

    def worker_p1(task):
        idx, start, end, numbered, out_f = task
        t0 = time.time()
        res = ett.extract_from_chunk(client, ett.DEFAULT_MODEL, numbered)
        header = f"<!-- chunk {idx:03d} | lines {start}–{end} | source: {cid} -->\n"
        body = "<!-- no candidates -->\n" if (not res or not res.strip() or res.strip().startswith("NO CANDIDATES")) else (res.rstrip() + "\n")
        out_f.write_text(header + body, encoding="utf-8")
        dt = time.time() - t0
        print(f"  [P1 {dt:4.1f}s] chunk_{idx:03d} candidates done")

    def worker_p2(task):
        idx, start, end, text, out_f = task
        t0 = time.time()
        res = ett.extract_enumerations_from_chunk(client, ett.DEFAULT_MODEL, text)
        body = "NO ENUMERATIONS\n" if (not res or res.strip().upper() == "NO ENUMERATIONS") else (res.rstrip() + "\n")
        out_f.write_text(body, encoding="utf-8")
        dt = time.time() - t0
        print(f"  [P2 {dt:4.1f}s] chunk_{idx:03d} enumerations done")

    total_tasks = len(p1_tasks) + len(p2_tasks)
    print(f"[{cid}] Passes 1 & 2 to run: {len(p1_tasks)} P1, {len(p2_tasks)} P2 (workers={max_workers})")

    if total_tasks > 0:
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
            f1 = [ex.submit(worker_p1, t) for t in p1_tasks]
            f2 = [ex.submit(worker_p2, t) for t in p2_tasks]
            concurrent.futures.wait(f1 + f2)
            # check for exceptions
            for f in f1 + f2:
                if f.exception():
                    raise f.exception()

    print(f"[{cid}] Passes 1 & 2 completed.")


SUB_ENV = {**os.environ, "PYTHONUTF8": "1", "PYTHONIOENCODING": "utf-8"}


def run_cmd(cmd, env=None):
    print(f"Running: {' '.join(str(c) for c in cmd)}", flush=True)
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env or SUB_ENV,
    )
    out_lines = []
    for line in p.stdout:
        print(line, end="", flush=True)
        out_lines.append(line)
    p.wait()
    if p.returncode != 0:
        raise RuntimeError(f"Command failed with code {p.returncode}: {' '.join(str(c) for c in cmd)}")
    return "".join(out_lines)


def run_toc_tree_and_qc(cid: str):
    """Run extract_toc_tree.py to assemble candidates, build tree, and QC/repair."""
    src_file = SEGMENTED_DIR / f"{cid}.units.md"
    toc_folder = TEMP_DIR / f"TOC-{cid}"
    tree_file = toc_folder / f"toc-tree-{cid}.md"

    # Call extract_toc_tree.py
    cmd = [
        sys.executable,
        "-X", "utf8",
        str(TOC_EXTRACTOR_DIR / "extract_toc_tree.py"),
        str(src_file),
        "--commentary-id", cid,
    ]
    print(f"[{cid}] Running tree build & QC...")
    run_cmd(cmd)

    if not tree_file.exists():
        raise FileNotFoundError(f"Tree file was not generated: {tree_file}")
    return tree_file


def add_frame_nodes_and_anchor(cid: str):
    """Add front/back matter frame nodes if needed and anchor the tree with find_toc_contexts.py."""
    toc_folder = TEMP_DIR / f"TOC-{cid}"
    tree_file = toc_folder / f"toc-tree-{cid}.md"
    src_file = SEGMENTED_DIR / f"{cid}.units.md"

    tree_text = tree_file.read_text(encoding="utf-8")
    src_text = src_file.read_text(encoding="utf-8")
    src_lines = [l.strip() for l in src_text.splitlines() if l.strip()]

    # Check if frame node I is present
    if not re.search(r"^\s*\*\s*I\.\s*", tree_text, re.MULTILINE):
        # find front matter context
        first_non_h = ""
        for l in src_lines:
            if not l.startswith("#"):
                first_non_h = l[:80]
                break
        if first_non_h:
            # Insert I. ཀླད་ཀྱི་དོན། right after ## དཀར་ཆག
            m = re.search(r"(##\s+.*?Table of Contents.*?\n)", tree_text)
            if m:
                insert_pos = m.end()
                frame_line = f"* I. ཀླད་ཀྱི་དོན། [[{first_non_h}]]\n"
                tree_text = tree_text[:insert_pos] + frame_line + tree_text[insert_pos:]
                print(f"[{cid}] Added frame node I. ཀླད་ཀྱི་དོན།")

    # Check if back matter colophon frame node is present
    if not re.search(r"^\s*\*\s*b\.\s*", tree_text, re.MULTILINE):
        # check last 10 non-empty lines for colophon indicator (མཛད་པ, རྫོགས་སོ, བསྒྱུར་བ)
        colo_line = ""
        for l in reversed(src_lines[-10:]):
            if any(k in l for k in ["རྫོགས་སོ", "མཛད་པ", "འགྱུར་བྱང", "སློབ་དཔོན"]):
                colo_line = l[:80]
                break
        if colo_line:
            tree_text = tree_text.rstrip() + f"\n* b. མཇུག་བྱང། [[{colo_line}]]\n"
            print(f"[{cid}] Added frame node b. མཇུག་བྱང།")

    tree_file.write_text(tree_text, encoding="utf-8")

    # Now run find_toc_contexts.py
    cmd = [
        sys.executable,
        "-X", "utf8",
        str(TOC_EXTRACTOR_DIR / "find_toc_contexts.py"),
        str(tree_file),
        str(src_file),
    ]
    print(f"[{cid}] Anchoring tree...")
    run_cmd(cmd)

    # Ensure tree is written back cleanly
    return tree_file


def run_ingest(cid: str):
    """Parse tree to JSON and ingest headings into commentary."""
    toc_folder = TEMP_DIR / f"TOC-{cid}"
    tree_file = toc_folder / f"toc-tree-{cid}.md"
    tree_json = toc_folder / f"toc-tree-{cid}.json"
    src_file = SEGMENTED_DIR / f"{cid}.units.md"
    seg_toc_file = SEGMENTED_DIR / f"{cid}.toc.md"
    inbox_toc_file = TOC_INGEST_DIR / f"{cid}.toc.md"

    # Step 1: parse
    cmd_parse = [
        sys.executable,
        "-X", "utf8",
        str(LIB_DIR / "toc_tree_ingest.py"),
        "parse",
        "--input", str(tree_file),
        "--out", str(tree_json),
    ]
    print(f"[{cid}] Parsing tree...")
    run_cmd(cmd_parse)

    # Copy units to seg_toc_file for in-place ingestion
    seg_toc_file.write_bytes(src_file.read_bytes())

    # Step 2: ingest
    cmd_ing = [
        sys.executable,
        "-X", "utf8",
        str(LIB_DIR / "toc_tree_ingest.py"),
        "ingest",
        "--tree", str(tree_json),
        "--commentary", str(seg_toc_file),
        "--split-frame-nodes",
    ]
    print(f"[{cid}] Ingesting TOC headings...")
    run_cmd(cmd_ing)

    # Also sync to 0-INBOX/temp/segmented-commentary-with-toc/
    inbox_toc_file.write_bytes(seg_toc_file.read_bytes())
    print(f"[{cid}] Synced to {inbox_toc_file}")
    return seg_toc_file


def run_resegment_and_qc(cid: str, max_workers: int = 8):
    """Run parallel resegmentation and QC check."""
    cmd_reseg = [
        sys.executable,
        "-u",
        "-X", "utf8",
        str(TEMP_DIR / "run_parallel_reseg.py"),
        cid,
        str(max_workers),
    ]
    print(f"[{cid}] Running resegmentation...")
    run_cmd(cmd_reseg)

    reseg_file = RESEG_DIR / f"{cid}.reseg.md"
    cmd_qc = [
        sys.executable,
        "-u",
        "-X", "utf8",
        str(RESEG_SCRIPTS_DIR / "qc_check.py"),
        str(reseg_file),
        "--commentary-id", cid,
    ]
    print(f"[{cid}] Running resegment QC...")
    run_cmd(cmd_qc)

    return reseg_file


def run_block_ids(cid: str):
    """Stamp body block IDs and strictly verify against source."""
    toc_folder = TEMP_DIR / f"TOC-{cid}"
    tree_json = toc_folder / f"toc-tree-{cid}.json"
    reseg_file = RESEG_DIR / f"{cid}.reseg.md"
    src_file = COMMENTARY_DIR / f"{cid}.md"

    cmd_stamp = [
        sys.executable,
        "-X", "utf8",
        str(LIB_DIR / "toc_tree_ingest.py"),
        "ingest",
        "--tree", str(tree_json),
        "--commentary", str(reseg_file),
        "--stamp-body-ids",
        "--verify-against", str(src_file),
    ]
    print(f"[{cid}] Stamping body block IDs & verifying text...")
    run_cmd(cmd_stamp)

    print(f"[{cid}] ALL STEPS COMPLETED SUCCESSFULLY!")


def process_commentary(cid: str, max_workers: int = 8):
    t_start = time.time()
    print(f"\n============================================================")
    print(f"STARTING PIPELINE FOR {cid}")
    print(f"============================================================\n")

    print(f"--- STEP 1 & 2: Parallel Pass 1 & 2 Extraction ---")
    run_parallel_toc_passes_1_2(cid, max_workers=max_workers)

    print(f"\n--- STEP 3: TOC Tree Build & QC ---")
    run_toc_tree_and_qc(cid)

    print(f"\n--- STEP 4: Frame Nodes & Context Anchoring ---")
    add_frame_nodes_and_anchor(cid)

    print(f"\n--- STEP 5: Ingest TOC Headings into Commentary ---")
    run_ingest(cid)

    print(f"\n--- STEP 6: Resegmentation & QC ---")
    run_resegment_and_qc(cid, max_workers=max_workers)

    print(f"\n--- STEP 7: Stamp Block IDs & Strict Text Verification ---")
    run_block_ids(cid)

    dt = time.time() - t_start
    print(f"\n============================================================")
    print(f"FINISHED PIPELINE FOR {cid} IN {dt:.1f}s")
    print(f"============================================================\n")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "Gu_3CFR"
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    process_commentary(target, workers)
