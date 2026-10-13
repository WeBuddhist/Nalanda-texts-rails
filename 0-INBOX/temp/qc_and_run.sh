#!/usr/bin/env bash
# QC an agent-built tree (both checkers) and start run_batch_pipeline.py for it.
# Usage (vault root): bash 0-INBOX/temp/qc_and_run.sh ID
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
id=$1; D=0-INBOX/temp/TOC-$id; T=$D/toc-tree-$id.md; U=0-INBOX/temp/PIPE-$id/$id.units.md; L=4-SYSTEM/Skills/seg-toc-lib
grep -qE "ཚིགས་བཅད་{?[0-9]+}?།" $T && { cp $T $T.placeholders; python -X utf8 0-INBOX/temp/fill_verse_ordinals.py $T; }
python -X utf8 $L/qc_check_tree.py $T --corpus $U --out $D/toc-tree-qc-$id.md >/dev/null; a=$?
python -X utf8 $L/qc_tree_vs_source.py $T --source $U --out $D/toc-tree-qc-source-$id.md >/dev/null; b=$?
echo "$id: qc_check_tree=$a qc_tree_vs_source=$b"
grep '^- ' $D/toc-tree-qc-source-$id.md | grep -v "not near pointer" | cut -c1-160
grep '^- ' $D/toc-tree-qc-$id.md | grep -v "unparseable\|not attested" | cut -c1-160
cp $T 0-INBOX/temp/PIPE-$id/closing-tree-$id.md
nohup python -u -X utf8 0-INBOX/temp/run_batch_pipeline.py $id > 0-INBOX/temp/batch-logs/pipe-$id.log 2>&1 &
