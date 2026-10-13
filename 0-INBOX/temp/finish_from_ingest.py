"""Finish run_toc_only for an id whose anchored TOC tree is ready: ingest -> footnotes -> stamp -> verify.
Usage: python finish_from_ingest.py ID [--source-dir=1-SOURCES/Text]"""
import shutil, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_toc_only as r
orch = r.orch
cid = sys.argv[1]
sd = next((a.split("=", 1)[1] for a in sys.argv[2:] if a.startswith("--source-dir=")), None)
if sd:
    orch.COMMENTARY_DIR = (orch.VAULT_ROOT / sd).resolve()
work = orch.TEMP_DIR / f"PIPE-{cid}"
orch.SEGMENTED_DIR = work
orch.run_ingest(cid)
foot = (work / f"{cid}.footnotes.md").read_text(encoding="utf-8")
final = work / f"{cid}.final.md"
final.write_text((work / f"{cid}.toc.md").read_text(encoding="utf-8").rstrip() + "\n\n" + foot, encoding="utf-8")
orch.run_cmd([sys.executable, "-X", "utf8", str(orch.LIB_DIR / "toc_tree_ingest.py"), "ingest",
              "--tree", str(orch.TEMP_DIR / f"TOC-{cid}" / f"toc-tree-{cid}.json"), "--commentary", str(final),
              "--stamp-body-ids", "--verify-against", str(orch.COMMENTARY_DIR / f"{cid}.md")])
shutil.copyfile(final, orch.TOC_INGEST_DIR / f"{cid}.toc.md")
print(f"[{cid}] DONE -> {orch.TOC_INGEST_DIR / f'{cid}.toc.md'}", flush=True)
