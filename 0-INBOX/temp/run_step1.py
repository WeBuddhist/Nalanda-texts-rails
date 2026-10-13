#!/usr/bin/env python3
"""Run Step 1 (commentary-segmentation --units) in parallel across 8 target commentary files."""

import concurrent.futures
import os
import re
import subprocess
import sys
import time
from pathlib import Path

TARGETS = [
    "Gu_3CFP",
    "Gu_3CFQ",
    "Gu_3CFR",
    "Gu_3CFU",
    "Gu_3CFV",
    "Gu_3CFW",
    "Gu_3CFX",
    "Gu_3CFY",
]

BASE_DIR = Path(r"C:\Users\geshe lobzang tseten\repos\Nalanda-texts-rails")
COMMENTARY_DIR = BASE_DIR / "0-INBOX" / "commentary"
SEGMENTED_DIR = BASE_DIR / "0-INBOX" / "segmented"
TEMP_DIR = BASE_DIR / "0-INBOX" / "temp"
SEG_SCRIPT = BASE_DIR / "4-SYSTEM" / "Skills" / "commentary-segment" / "scripts" / "segment_commentary.py"
VERIFY_SCRIPT = BASE_DIR / "4-SYSTEM" / "scripts" / "verify_segmentation.py"


def process_text(cid: str):
    t0 = time.time()
    src_path = COMMENTARY_DIR / f"{cid}.md"
    out_path = SEGMENTED_DIR / f"{cid}.units.md"
    rep_path = SEGMENTED_DIR / f"{cid}.segreport.tsv"
    log_path = SEGMENTED_DIR / f"{cid}.seg.log"

    if not src_path.exists():
        return cid, False, f"Source file {src_path} does not exist"

    # Backup existing if needed
    if cid == "Gu_3CFQ" and out_path.exists():
        bak_dir = TEMP_DIR / "Gu_3CFQ-prev-runs"
        bak_dir.mkdir(parents=True, exist_ok=True)
        bak_path = bak_dir / "Gu_3CFQ.units.md.bak"
        if not bak_path.exists():
            bak_path.write_bytes(out_path.read_bytes())

    src_text = src_path.read_text(encoding="utf-8")
    m = re.search(r"\n(\[\^\d+\]:[\s\S]*)$", src_text)
    if m:
        body = src_text[:m.start(1)]
        foot = m.group(1).strip()
    else:
        body = src_text
        foot = ""

    tmp_in = TEMP_DIR / f"step1_{cid}_in.md"
    tmp_out = TEMP_DIR / f"step1_{cid}_out.md"
    tmp_in.write_text(body, encoding="utf-8")

    cmd = [
        sys.executable,
        str(SEG_SCRIPT),
        str(tmp_in),
        str(tmp_out),
        "--units",
        "--enum-chain", "broad",
        "--colophon-guard",
        "--report", str(rep_path),
    ]

    res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        return cid, False, f"Segmentation script failed: {res.stderr}\n{res.stdout}"

    body_out = tmp_out.read_text(encoding="utf-8").rstrip()
    if foot:
        final_text = body_out + "\n\n" + foot + "\n"
    else:
        final_text = body_out + "\n"

    out_path.write_text(final_text, encoding="utf-8")

    # Run verification
    v_res = subprocess.run(
        [sys.executable, str(VERIFY_SCRIPT), str(src_path), str(out_path)],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    passed = ("✓ PASS" in v_res.stdout) or ("Result: PASS" in v_res.stdout) or (v_res.returncode == 0)

    # Write log
    log_content = (
        f"=== Step 1 Segmentation: {cid} ===\n"
        f"Exit: {res.returncode}\n"
        f"Stdout:\n{res.stdout}\n"
        f"Stderr:\n{res.stderr}\n\n"
        f"=== Verify Report ===\n"
        f"Exit: {v_res.returncode}\n"
        f"{v_res.stdout}\n"
    )
    log_path.write_text(log_content, encoding="utf-8")

    # Clean up temp
    try:
        tmp_in.unlink(missing_ok=True)
        tmp_out.unlink(missing_ok=True)
    except Exception:
        pass

    dt = time.time() - t0
    status_summary = {
        "cid": cid,
        "time": round(dt, 2),
        "passed": passed,
        "verify_summary": v_res.stdout.strip(),
        "res_stdout": res.stdout.strip(),
    }
    return cid, passed, status_summary


def main():
    SEGMENTED_DIR.mkdir(parents=True, exist_ok=True)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Starting parallel Step 1 segmentation for {len(TARGETS)} texts...")
    t_start = time.time()

    results = {}
    with concurrent.futures.ProcessPoolExecutor(max_workers=min(8, os.cpu_count() or 4)) as executor:
        future_to_cid = {executor.submit(process_text, cid): cid for cid in TARGETS}
        for future in concurrent.futures.as_completed(future_to_cid):
            cid = future_to_cid[future]
            try:
                cid, passed, info = future.result()
                results[cid] = (passed, info)
                print(f"[{cid}] {'PASSED' if passed else 'FAILED'} in {info['time']}s")
            except Exception as e:
                results[cid] = (False, str(e))
                print(f"[{cid}] EXCEPTION: {e}")

    total_time = time.time() - t_start
    print(f"\nAll done in {total_time:.2f}s")

    all_passed = all(p for p, _ in results.values())
    if not all_passed:
        print("Some texts failed verification!")
        sys.exit(1)
    else:
        print("All 8 texts PASSED verification!")


if __name__ == "__main__":
    main()
