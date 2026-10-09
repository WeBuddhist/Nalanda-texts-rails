#!/usr/bin/env python3
"""
Run a pipeline VARIANT over the 8-file benchmark, re-asking the LLM only where the
variant changed the prompt.

    python3 variant.py seg     <ver>      # segmentation            → 1-segmented.md
    python3 variant.py ingest  <ver>      # anchored tree → headings → 2-after-ingest.md
    python3 variant.py reseg   <ver>      # dump windows, fill from cache, list what is new
    python3 variant.py qc      <ver>      # apply reseg, run QC, fill from cache, list new
    python3 variant.py finish  <ver>      # QC repair → 4-final.md, body IDs, scores

Every LLM prompt is hashed; if the exact same prompt was answered in any earlier run
(v1 or another variant), that answer is reused. So a variant is compared with v1 on
the same model answers wherever its change does not reach — the difference in the
scores is the change, not resampling noise.

Config: 0-INBOX/bench8/config.json (files, declared settings, variant definitions).
"""
import hashlib
import os
import json
import shutil
import subprocess
import sys
from pathlib import Path

V = Path('.').resolve()
CFG = json.loads((V / '0-INBOX/bench8/config.json').read_text(encoding='utf-8'))
SEG = '4-SYSTEM/Skills/commentary-segment/scripts/segment_commentary.py'
ING = '4-SYSTEM/Skills/seg-toc-lib/toc_tree_ingest.py'
RES = '4-SYSTEM/Skills/commentary-resegment/scripts/resegment.py'
QC = '4-SYSTEM/Skills/commentary-resegment/scripts/qc_check.py'
B = '4-SYSTEM/scripts/seg-toc-benchmark'
ROOT = CFG['root']


PY = sys.executable          # 'python3' does not exist on most Windows installs
TMP = V / '0-INBOX/temp'     # not /tmp — works on Windows too


def run(cmd, check=True):
    cmd = [PY if c == 'python3' else c for c in cmd]
    env = dict(os.environ, PYTHONUTF8='1', PYTHONIOENCODING='utf-8')
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', env=env)
    if check and r.returncode not in (0,):
        raise SystemExit(f"FAILED {' '.join(cmd)}\n{r.stdout[-800:]}\n{r.stderr[-800:]}")
    return r


def vdef(ver):
    return CFG['variants'][ver]


def d(fid, ver):
    p = V / '0-INBOX/bench8' / fid / ver
    p.mkdir(parents=True, exist_ok=True)
    return p


def h(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def files():
    """BENCH_FILES=a,b restricts a command to those commentary ids."""
    sel = os.environ.get('BENCH_FILES')
    return {k: v for k, v in CFG['files'].items() if not sel or k in sel.split(',')}


def cache():
    """prompt-hash → response path, over every answered prompt in 0-INBOX/temp.
    BENCH_NO_CACHE=1 disables reuse (for repeat runs that must re-sample the model)."""
    c = {}
    if os.environ.get('BENCH_NO_CACHE'):
        return c
    for p in (V / '0-INBOX/temp').glob('RESEG-*/claude/window-*.prompt.md'):
        r = p.with_name(p.name.replace('.prompt.md', '.response.json'))
        if r.exists():
            c[h(p.read_text(encoding='utf-8'))] = r
    for p in (V / '0-INBOX/temp').glob('RESEG-*/qc-calls/call-*.prompt.md'):
        r = p.with_name(p.name.replace('.prompt.md', '.response.txt'))
        if r.exists():
            c[h(p.read_text(encoding='utf-8'))] = r
    return c


def seg(ver):
    for fid, f in files().items():
        flags = []
        for fl in vdef(ver).get('seg', []):
            flags += [x.format(**f) for x in fl.split()]
        out = d(fid, ver) / '1-segmented.md'
        run(['python3', SEG, f['input'], str(out), '--units', '--root', ROOT] + flags)
        ref = V / f'0-INBOX/bench8/{fid}/v1/1-segmented.md'
        same = ref.exists() and out.read_bytes() == ref.read_bytes()
        print(f'{fid:14s} segmented {"(= v1)" if same else "(changed)"}  flags={flags}')


def tree_for(fid, ver):
    t = vdef(ver).get('tree', 'v1')
    f = CFG['files'][fid]
    if t == 'v1' or (isinstance(t, dict) and f['headings'] not in t.get('for', [])):
        return f['v1_tree']
    name = t['name'] if isinstance(t, dict) else t
    return str(V / f'0-INBOX/bench8/{fid}/{name}/toc-tree-anchored.md')


def ingest(ver):
    for fid, f in files().items():
        dd = d(fid, ver)
        out = dd / '2-after-ingest.md'
        shutil.copy(dd / '1-segmented.md', out)
        tree = tree_for(fid, ver)
        TMP.mkdir(parents=True, exist_ok=True)
        js = str(TMP / f'tt-{fid}-{ver}.json')
        run(['python3', ING, 'parse', '--input', tree, '--out', js])
        r = run(['python3', ING, 'ingest', '--tree', js, '--commentary', str(out)] + vdef(ver).get('ingest', []), check=False)
        (dd / 'ingest.log').write_text(r.stdout + r.stderr, encoding='utf-8')
        nf = [l for l in r.stdout.splitlines() if 'Not found' in l or 'split at' in l]
        ref = V / f'0-INBOX/bench8/{fid}/v1/2-after-ingest.md'
        same = ref.exists() and out.read_bytes() == ref.read_bytes()
        print(f'{fid:14s} tree={Path(tree).parent.name}/{Path(tree).name} {"(= v1)" if same else "(changed)"} ' + ' | '.join(x.strip() for x in nf))


def reseg(ver):
    c = cache()
    todo = {}
    for fid in files():
        cid = f'{fid}-{ver}'
        r = run(['python3', f'{B}/claude_reseg_shim.py', 'dump', str(d(fid, ver) / '2-after-ingest.md'),
                 '--commentary-id', cid])
        cd = V / f'0-INBOX/temp/RESEG-{cid}/claude'
        new = []
        for p in sorted(cd.glob('window-*.prompt.md')):
            resp = p.with_name(p.name.replace('.prompt.md', '.response.json'))
            if resp.exists():
                continue
            hit = c.get(h(p.read_text(encoding='utf-8')))
            if hit:
                shutil.copy(hit, resp)
            else:
                new.append(p.name)
        if new:
            todo[fid] = new
        print(f'{fid:14s} windows: {len(list(cd.glob("window-*.prompt.md")))}  new (need LLM): {len(new)}')
    (V / f'0-INBOX/bench8/todo-reseg-{ver}.json').write_text(json.dumps(todo, indent=1))


def qc(ver):
    c = cache()
    todo = []
    for fid in files():
        cid = f'{fid}-{ver}'
        inp = d(fid, ver) / '2-after-ingest.md'
        run(['python3', f'{B}/claude_reseg_shim.py', 'stage', str(inp), '--commentary-id', cid])
        r = run(['python3', RES, str(inp), '--commentary-id', cid, '--apply-only'], check=False)
        (d(fid, ver) / 'reseg.log').write_text(r.stdout + r.stderr, encoding='utf-8')
        if 'Integrity check passed' not in r.stdout:
            raise SystemExit(f'{fid}: resegment failed\n{r.stdout[-1500:]}')
        shutil.copy(V / f'0-INBOX/resegmented/{cid}.reseg.md', d(fid, ver) / '3-reseg-preqc.md')
        qd = V / f'0-INBOX/temp/RESEG-{cid}/qc-calls'
        status = 'no flags'
        for _ in range(3):
            r = run(['python3', f'{B}/claude_generate_shim.py', '--dir', str(qd), '--', QC,
                     f'0-INBOX/resegmented/{cid}.reseg.md'], check=False)
            if r.returncode != 3:
                status = 'done'
                break
            p = qd / 'call-000.prompt.md'
            hit = c.get(h(p.read_text(encoding='utf-8')))
            if hit:
                shutil.copy(hit, qd / 'call-000.response.txt')
                status = 'cache'
                continue
            status = 'NEED LLM'
            todo.append(str(p))
            break
        print(f'{fid:14s} QC: {status}')
    (V / f'0-INBOX/bench8/todo-qc-{ver}.json').write_text(json.dumps(todo, indent=1))


def finish(ver):
    sys.path.insert(0, str(V / B))
    from score import score  # noqa
    res = {}
    for fid, f in files().items():
        cid = f'{fid}-{ver}'
        qd = V / f'0-INBOX/temp/RESEG-{cid}/qc-calls'
        r = run(['python3', f'{B}/claude_generate_shim.py', '--dir', str(qd), '--', QC,
                 f'0-INBOX/resegmented/{cid}.reseg.md'], check=False)
        if r.returncode == 3:
            raise SystemExit(f'{fid}: QC still needs an answer: {qd}')
        out = d(fid, ver) / '4-final.md'
        shutil.copy(V / f'0-INBOX/resegmented/{cid}.reseg.md', out)
        TMP.mkdir(parents=True, exist_ok=True)
        js = str(TMP / f'tt-{fid}-{ver}.json')
        run(['python3', ING, 'ingest', '--tree', js, '--commentary', str(out), '--stamp-body-ids'], check=False)
        res[fid] = {st: score(f['gold'], str(d(fid, ver) / f'{st}.md'))
                    for st in ('1-segmented', '2-after-ingest', '4-final')}
        print(f"{fid:14s} composite {res[fid]['4-final']['composite']:.3f}  ident={res[fid]['4-final']['text_identical']}")
    (V / f'0-INBOX/bench8/scores-{ver}.json').write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding='utf-8')


def rescore(ver):
    """Re-score the stage files already on disk (after a scorer change)."""
    sys.path.insert(0, str(V / B))
    from score import score  # noqa
    res = {}
    for fid, f in files().items():
        res[fid] = {st: score(f['gold'], str(d(fid, ver) / f'{st}.md'))
                    for st in ('1-segmented', '2-after-ingest', '4-final')
                    if (d(fid, ver) / f'{st}.md').exists()}
    (V / f'0-INBOX/bench8/scores-{ver}.json').write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'rescored {ver}')


if __name__ == '__main__':
    {'seg': seg, 'ingest': ingest, 'reseg': reseg, 'qc': qc, 'finish': finish, 'rescore': rescore}[sys.argv[1]](sys.argv[2])
