#!/usr/bin/env python3
"""Copy Nalanda docx work markdown into ``1-SOURCES/Text/`` as a flat intake.

Reads every ``*/works/*.md`` under ``0-INBOX/Nalanda_docx/`` (also accepts the
older ``Nalanda-docx`` name), copies them into ``1-SOURCES/Text/<filename>.md``
(no pandita subfolders), and writes a combined ``text_catalog.json`` from each
pandita's ``works.json``.

This is an intake script: it creates whole files from reviewed inbox material.
It does not rewrite existing source content in place beyond replacing files it
previously wrote under the same flat filenames.

    python3 4-SYSTEM/scripts/nalanda-docx-to-text.py
    python3 4-SYSTEM/scripts/nalanda-docx-to-text.py --dry-run
    python3 4-SYSTEM/scripts/nalanda-docx-to-text.py --clean

On case-insensitive filesystems (typical macOS), pairs such as ``3C9A.md`` and
``3C9a.md`` cannot coexist. The catalog marks the missing side as
``missing_case_collision``.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


VAULT = Path(__file__).resolve().parents[2]
DEFAULT_DEST = VAULT / "1-SOURCES" / "Text"
CATALOG_NAME = "text_catalog.json"
KEEP_NAMES = {".gitkeep", ".DS_Store"}
# Prefer the current inbox folder name; fall back to the older hyphenated name.
_SOURCE_CANDIDATES = (
    VAULT / "0-INBOX" / "Nalanda_docx",
    VAULT / "0-INBOX" / "Nalanda-docx",
)


def default_source() -> Path:
    """Return the first existing Nalanda docx inbox path, or the preferred default."""
    for candidate in _SOURCE_CANDIDATES:
        if candidate.is_dir():
            return candidate
    return _SOURCE_CANDIDATES[0]


@dataclass(frozen=True)
class CopyStats:
    """Summary counts from one intake run."""

    source_md: int
    copied: int
    overwritten: int
    works_catalogued: int
    files_present: int
    case_collisions: int
    missing: int


def discover_markdown(source: Path) -> list[Path]:
    """Return every work markdown file under the Nalanda-docx tree.

    Args:
        source: Root of the Nalanda-docx inbox tree.

    Returns:
        Sorted paths to ``*.md`` files (typically under ``*/works/``).
    """
    return sorted(source.rglob("*.md"))


def clear_destination(dest: Path, *, dry_run: bool) -> list[str]:
    """Remove prior intake outputs from the destination folder.

    Keeps ``.gitkeep``. Removes pandita subfolders and flat ``*.md`` /
    ``text_catalog.json`` files from earlier runs.

    Args:
        dest: ``1-SOURCES/Text`` path.
        dry_run: If True, only report what would be removed.

    Returns:
        Human-readable descriptions of removed (or would-be-removed) paths.
    """
    removed: list[str] = []
    if not dest.exists():
        return removed

    for child in sorted(dest.iterdir()):
        if child.name in KEEP_NAMES:
            continue
        removed.append(str(child.relative_to(VAULT)))
        if dry_run:
            continue
        if child.is_dir():
            shutil.rmtree(child)
        else:
            child.unlink()
    return removed


def copy_flat(source_files: list[Path], dest: Path, *, dry_run: bool) -> tuple[int, int]:
    """Copy markdown files into ``dest`` using basename only.

    Args:
        source_files: Source markdown paths.
        dest: Flat destination directory.
        dry_run: If True, do not write.

    Returns:
        ``(copied, case_overwrites)`` counts. ``case_overwrites`` counts
        source files whose basename case-folds onto an earlier copy.
    """
    if not dry_run:
        dest.mkdir(parents=True, exist_ok=True)

    copied = 0
    case_overwrites = 0
    seen_lower: set[str] = set()

    for src in source_files:
        lower = src.name.lower()
        if lower in seen_lower:
            case_overwrites += 1
        seen_lower.add(lower)
        if not dry_run:
            shutil.copy2(src, dest / src.name)
        copied += 1
    return copied, case_overwrites


def load_works_json(source: Path) -> list[dict]:
    """Load every pandita ``works.json`` in folder-name order.

    Args:
        source: Nalanda-docx root.

    Returns:
        List of parsed JSON objects, each with ``pandita`` and ``works``.

    Raises:
        FileNotFoundError: If no ``works.json`` files are found.
        json.JSONDecodeError: If a works.json file is invalid.
    """
    paths = sorted(source.glob("*/works.json"))
    if not paths:
        raise FileNotFoundError(f"no works.json under {source}")
    return [json.loads(path.read_text(encoding="utf-8")) for path in paths]


def _disk_basenames(dest: Path) -> set[str]:
    """Return exact-case ``*.md`` basenames present under ``dest``."""
    if not dest.exists():
        return set()
    return {name for name in os.listdir(dest) if name.endswith(".md")}


def build_catalog(
    source: Path,
    dest: Path,
    *,
    assumed_basenames: set[str] | None = None,
) -> dict:
    """Combine pandita works.json files and annotate file presence.

    Args:
        source: Nalanda-docx root (for works.json).
        dest: Flat Text destination (for presence checks).
        assumed_basenames: Optional basename set for dry-run simulation
            when the destination has not been written yet.

    Returns:
        Catalog dict ready to serialize as ``text_catalog.json``.
    """
    actual_names = (
        assumed_basenames if assumed_basenames is not None else _disk_basenames(dest)
    )
    lower_to_actual: dict[str, list[str]] = {}
    for name in actual_names:
        lower_to_actual.setdefault(name.lower(), []).append(name)

    panditas: list[dict] = []
    works_catalogued = 0
    files_present = 0
    case_collisions = 0
    missing = 0

    for data in load_works_json(source):
        pandita = data["pandita"]
        works_out: list[dict] = []
        for work in data.get("works", []):
            works_catalogued += 1
            filename = work["filename"]
            entry = {
                **work,
                "pandita": pandita,
                "path": f"1-SOURCES/Text/{filename}",
            }
            if filename in actual_names:
                entry["file_status"] = "present"
                files_present += 1
            else:
                rivals = lower_to_actual.get(filename.lower(), [])
                if rivals:
                    entry["file_status"] = "missing_case_collision"
                    entry["collides_with"] = rivals[0]
                    case_collisions += 1
                    missing += 1
                else:
                    entry["file_status"] = "missing"
                    missing += 1
            works_out.append(entry)

        panditas.append({
            "pandita": pandita,
            "work_count": len(works_out),
            "files_present": sum(
                1 for item in works_out if item["file_status"] == "present"
            ),
            "works": works_out,
        })

    return {
        "corpus": "Nalanda Masters collected works (from Nalanda-docx)",
        "source": str(source.relative_to(VAULT)) if source.is_relative_to(VAULT) else str(source),
        "destination": "1-SOURCES/Text",
        "layout": "flat",
        "files": files_present,
        "works_catalogued": works_catalogued,
        "files_missing": missing,
        "case_collisions": case_collisions,
        "note": (
            "Flat layout: all markdown files live directly under 1-SOURCES/Text/ "
            "(no pandita subfolders). Pandita attribution is retained on each "
            "work entry and in the panditas[] grouping. On case-insensitive "
            "filesystems, colliding IDs (e.g. 3C9A.md vs 3C9a.md) are marked "
            "file_status=missing_case_collision."
        ),
        "pandita_count": len(panditas),
        "panditas": panditas,
    }


def write_catalog(catalog: dict, dest: Path, *, dry_run: bool) -> Path:
    """Write ``text_catalog.json`` under ``dest``.

    Args:
        catalog: Catalog object from :func:`build_catalog`.
        dest: Destination directory.
        dry_run: If True, skip writing.

    Returns:
        Path to the catalog file (written or would-be path).
    """
    path = dest / CATALOG_NAME
    if not dry_run:
        dest.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(catalog, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return path


def run(
    source: Path,
    dest: Path,
    *,
    clean: bool,
    dry_run: bool,
) -> CopyStats:
    """Execute the flat intake copy and catalog build.

    Args:
        source: Nalanda-docx inbox root.
        dest: ``1-SOURCES/Text`` destination.
        clean: Clear prior destination outputs before copying.
        dry_run: Report actions without writing.

    Returns:
        Aggregate :class:`CopyStats`.

    Raises:
        FileNotFoundError: If the source tree is missing.
    """
    if not source.is_dir():
        raise FileNotFoundError(f"source not found: {source}")

    if clean:
        removed = clear_destination(dest, dry_run=dry_run)
        print(f"{'would remove' if dry_run else 'removed'} {len(removed)} items from {dest}")

    source_files = discover_markdown(source)
    copied, overwritten = copy_flat(source_files, dest, dry_run=dry_run)

    if dry_run:
        # First-wins by case-fold: simulate what a case-insensitive FS keeps.
        assumed: dict[str, str] = {}
        for src in source_files:
            assumed.setdefault(src.name.lower(), src.name)
        catalog = build_catalog(
            source, dest, assumed_basenames=set(assumed.values())
        )
    else:
        catalog = build_catalog(source, dest)

    catalog_path = write_catalog(catalog, dest, dry_run=dry_run)
    print(
        f"{'would write' if dry_run else 'wrote'} catalog "
        f"({catalog['works_catalogued']} works, {catalog['files']} present, "
        f"{catalog['case_collisions']} case collisions) -> {catalog_path}"
    )

    return CopyStats(
        source_md=len(source_files),
        copied=copied,
        overwritten=overwritten,
        works_catalogued=int(catalog["works_catalogued"]),
        files_present=int(catalog["files"]),
        case_collisions=int(catalog["case_collisions"]),
        missing=int(catalog["files_missing"]),
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments.

    Args:
        argv: Optional argument list (defaults to ``sys.argv[1:]``).

    Returns:
        Parsed namespace.
    """
    parser = argparse.ArgumentParser(
        description=(
            "Copy Nalanda-docx work markdown flat into 1-SOURCES/Text/ "
            "and write text_catalog.json."
        )
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=None,
        help=(
            "Nalanda docx inbox root "
            "(default: 0-INBOX/Nalanda_docx or 0-INBOX/Nalanda-docx)"
        ),
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=DEFAULT_DEST,
        help=f"Flat Text destination (default: {DEFAULT_DEST})",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove prior *.md, text_catalog.json, and subfolders under --dest first",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would happen without writing files",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point.

    Args:
        argv: Optional argument list.

    Returns:
        Process exit code (0 on success, 1 on error).
    """
    args = parse_args(argv)
    source = (args.source or default_source()).resolve()
    try:
        stats = run(
            source,
            args.dest.resolve(),
            clean=args.clean,
            dry_run=args.dry_run,
        )
    except (FileNotFoundError, json.JSONDecodeError, OSError, KeyError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(
        f"source_md={stats.source_md} copied={stats.copied} "
        f"overwritten={stats.overwritten} present={stats.files_present} "
        f"case_collisions={stats.case_collisions} missing={stats.missing}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
