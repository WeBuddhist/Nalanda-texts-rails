"""Footnote-free PIPE-<id>/<id>.units.md working copies (as run_batch_pipeline.py makes them).
Usage (vault root): python -X utf8 0-INBOX/temp/prep_pipe.py ID [ID ...]"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_batch_pipeline as rb
for cid in sys.argv[1:]:
    body, foot = rb.split_footnotes(Path(f"0-INBOX/segmented/{cid}.units.md").read_text(encoding="utf-8"))
    assert foot == rb.split_footnotes(Path(f"0-INBOX/commentary/{cid}.md").read_text(encoding="utf-8"))[1], cid
    w = Path(f"0-INBOX/temp/PIPE-{cid}"); w.mkdir(exist_ok=True)
    (w / f"{cid}.units.md").write_text(body, encoding="utf-8"); (w / f"{cid}.footnotes.md").write_text(foot, encoding="utf-8")
    print(cid, len(body.split("\n")), "lines", len(body), "chars")
