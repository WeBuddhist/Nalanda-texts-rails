#!/usr/bin/env python3
"""List commentary files in 0-INBOX/commentary that are not yet in
0-INBOX/processed/commentaries (matched by filename).

Usage:
    python 4-SYSTEM/scripts/list_unprocessed_commentaries.py [--src DIR] [--done DIR] [--out FILE]
"""
import argparse
from pathlib import Path

VAULT = Path(__file__).resolve().parents[2]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--src", type=Path, default=VAULT / "0-INBOX" / "commentary")
    ap.add_argument("--done", type=Path, default=VAULT / "0-INBOX" / "processed" / "commentaries")
    ap.add_argument("--out", type=Path, help="optionally write the list to this file")
    args = ap.parse_args()

    src = {p.name for p in args.src.iterdir() if p.is_file() and p.suffix == ".md"}
    done = {p.name for p in args.done.iterdir() if p.is_file() and p.suffix == ".md"}
    missing = sorted(src - done)

    for name in missing:
        print(name)
    print(f"\n{len(missing)} of {len(src)} not yet processed ({len(done)} in processed)")

    if args.out:
        args.out.write_text("\n".join(missing) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
