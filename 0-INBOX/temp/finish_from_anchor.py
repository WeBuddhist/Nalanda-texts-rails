"""Finish run_toc_only for an id whose TOC tree is already built: anchor -> ingest -> stamp."""
import shutil, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_toc_only as r
orch = r.orch

cid = sys.argv[1]
work = orch.TEMP_DIR / f"PIPE-{cid}"
body = (work / f"{cid}.units.md").read_text(encoding="utf-8")
foot = (work / f"{cid}.footnotes.md").read_text(encoding="utf-8")
src = orch.COMMENTARY_DIR / f"{cid}.md"
orch.SEGMENTED_DIR = work
r.add_front_frame(cid, body)
orch.add_frame_nodes_and_anchor(cid)
orch.run_ingest(cid)
final = work / f"{cid}.final.md"
final.write_text((work / f"{cid}.toc.md").read_text(encoding="utf-8").rstrip() + "\n\n" + foot, encoding="utf-8")
orch.run_cmd([sys.executable, "-X", "utf8", str(orch.LIB_DIR / "toc_tree_ingest.py"), "ingest",
              "--tree", str(orch.TEMP_DIR / f"TOC-{cid}" / f"toc-tree-{cid}.json"), "--commentary", str(final),
              "--stamp-body-ids", "--verify-against", str(src)])
shutil.copyfile(final, orch.TOC_INGEST_DIR / f"{cid}.toc.md")
print(f"[{cid}] DONE -> {orch.TOC_INGEST_DIR / f'{cid}.toc.md'}", flush=True)
