"""Report, for every commentary in 0-INBOX/commentary/, how far it has got
through segmentation and TOC insertion.

Checks per commentary ID:
  segmented   0-INBOX/segmented/<id>.units.md (or 0-INBOX/<id>.units.md, temp/<id>.segmented.md / .units.md)
  resegmented 0-INBOX/resegmented/<id>.reseg.md
  toc         0-INBOX/temp/segmented-commentary-with-toc/<id>.toc.md
For each .toc.md it also counts headings, heading depth, paragraph units,
headings without a block ID (title line excluded), and duplicate heading IDs.

Usage:  python 4-SYSTEM/scripts/check_commentary_seg_toc.py [output.md]
Default output: 0-INBOX/commentary-seg-toc-status.md
"""
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]
INBOX = VAULT / "0-INBOX"
COMMENTARY = INBOX / "commentary"
SEGMENTED = INBOX / "segmented"
RESEGMENTED = INBOX / "resegmented"
TEMP = INBOX / "temp"
TOC_DIR = TEMP / "segmented-commentary-with-toc"

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
BLOCK_ID = re.compile(r"\^([A-Za-z0-9-]+)\s*$")


def find_segmented(cid):
    for p in (SEGMENTED / f"{cid}.units.md",
              INBOX / f"{cid}.units.md",
              TEMP / f"{cid}.units.md",
              TEMP / f"{cid}.segmented.md"):
        if p.exists():
            return p
    return None


def inspect_toc(path):
    text = path.read_text(encoding="utf-8")
    headings, ids, missing = 0, [], 0
    max_depth = 0
    paragraphs = 0
    seen_title = False
    for block in re.split(r"\n\s*\n", text):
        block = block.strip()
        if not block:
            continue
        m = HEADING.match(block.splitlines()[0])
        if m and len(block.splitlines()) == 1:
            if not seen_title:  # first heading is the work's title: no ID, not counted
                seen_title = True
                continue
            headings += 1
            bid = BLOCK_ID.search(m.group(2))
            if bid:
                ids.append(bid.group(1))
                max_depth = max(max_depth, bid.group(1).count("-"))
            else:
                missing += 1
        else:
            paragraphs += 1
    dupes = sorted(i for i, n in Counter(ids).items() if n > 1)
    return {
        "headings": headings,
        "depth": max_depth,
        "paragraphs": paragraphs,
        "missing": missing,
        "dupes": dupes,
    }


def rel(p):
    return p.relative_to(VAULT).as_posix() if p else ""


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else INBOX / "commentary-seg-toc-status.md"
    ids = sorted(p.stem for p in COMMENTARY.glob("*.md"))
    rows, n_seg, n_reseg, n_toc, n_issue = [], 0, 0, 0, 0
    for cid in ids:
        seg = find_segmented(cid)
        reseg = RESEGMENTED / f"{cid}.reseg.md"
        reseg = reseg if reseg.exists() else None
        toc = TOC_DIR / f"{cid}.toc.md"
        toc = toc if toc.exists() else None
        n_seg += bool(seg)
        n_reseg += bool(reseg)
        n_toc += bool(toc)
        if toc:
            s = inspect_toc(toc)
            notes = []
            if not s["headings"]:
                notes.append("no TOC headings (title only)")
            if s["missing"]:
                notes.append(f"{s['missing']} heading(s) without block ID")
            if s["dupes"]:
                notes.append("duplicate IDs: " + ", ".join(s["dupes"][:5])
                             + (" …" if len(s["dupes"]) > 5 else ""))
            if not seg and not reseg:
                notes.append("no segmentation file found")
            n_issue += bool(notes)
            toc_cols = (f"✅ | {s['headings']} | {s['depth']} | {s['paragraphs']} | "
                        + ("; ".join(notes) or "OK"))
        else:
            toc_cols = "❌ | | | | "
        status = ("done" if toc else "segmented, needs TOC" if (seg or reseg) else "not started")
        rows.append(f"| {cid} | {'✅' if seg else '❌'} | {'✅' if reseg else '❌'} | "
                    f"{toc_cols} | {status} |")

    lines = [
        "# Commentary segmentation + TOC status",
        "",
        f"Generated {date.today().isoformat()} by `4-SYSTEM/scripts/check_commentary_seg_toc.py`.",
        "",
        f"- Commentaries in `0-INBOX/commentary/`: **{len(ids)}**",
        f"- Segmented (`0-INBOX/segmented/` or temp): **{n_seg}**",
        f"- Resegmented (`0-INBOX/resegmented/`): **{n_reseg}**",
        f"- Segmented with TOC (`0-INBOX/temp/segmented-commentary-with-toc/`): **{n_toc}**",
        f"- TOC files with issues: **{n_issue}**",
        f"- Not yet in TOC folder: **{len(ids) - n_toc}**",
        "",
        "Depth = deepest heading ID segment count (e.g. `^2-1-1-0` → 3). "
        "Units = non-heading paragraph blocks.",
        "",
        "| Commentary | Segmented | Resegmented | TOC file | Headings | Depth | Units | TOC check | Status |",
        "|---|---|---|---|---|---|---|---|---|",
        *rows,
        "",
    ]
    extra = sorted(p.name for p in TOC_DIR.glob("*.toc.md")
                   if p.name[:-len(".toc.md")] not in ids)
    if extra:
        lines += ["## TOC files with no matching commentary", "",
                  *[f"- `{n}`" for n in extra], ""]
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {rel(out) if out.is_relative_to(VAULT) else out}: "
          f"{len(ids)} commentaries, {n_seg} segmented, {n_reseg} resegmented, "
          f"{n_toc} with TOC, {n_issue} TOC issue(s)")


if __name__ == "__main__":
    main()
