#!/usr/bin/env python3
"""Run the root-text TOC extraction (passes 1–6, no ingest) on the Gemini API for every
text still to do in the batch, several texts in parallel, and update the batch report
after each text.

    venv/Scripts/python.exe -X utf8 0-INBOX/temp/root-toc/run_gemini_batch.py --mode low
    venv/Scripts/python.exe -X utf8 0-INBOX/temp/root-toc/run_gemini_batch.py --mode medium

    --mode low     small + medium texts, gemini-3.8-flash, thinking low
    --mode medium  large texts,          gemini-3.8-flash, thinking medium
    --procs N      texts processed at the same time (default 3; each is its own process)
    --workers N    parallel Gemini calls inside one text (default 4)
    --limit N      stop after N texts (for a test run)
    --only ID ...  run just these ids (must be in the mode's size classes)
    --reset-running  put texts left "running" by a crashed / stopped run back to "todo"
    --retry-failed   also take texts whose status is "failed"

Per text: (1) root_text_build.py segment → 0-INBOX/temp/root-seg-v2/<id>/prepared.md (only
when missing; deterministic), (2) root_toc_gemini.py → 0-INBOX/temp/TOC-<id>/ (the same
place the Claude batch used, so the later ingest finds the tree there), (3) its result is
written to 0-INBOX/temp/root-toc/status.json and 0-INBOX/ROOT-TOC-BATCH.md is re-rendered.
Logs: 0-INBOX/temp/root-toc/logs/<id>.log. The low and medium runs can go at the same
time: they take different texts, and status.json is written under a lock file.
Ctrl+C stops after the texts in progress are killed; re-run with --reset-running.
"""
import argparse, importlib.util, json, os, subprocess, sys, threading, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
PY = sys.executable
SEGMENT = VAULT / "4-SYSTEM/Skills/seg-toc-lib/root_text_build.py"
RUNNER = VAULT / "4-SYSTEM/scripts/seg-toc-benchmark/root_toc_gemini.py"
LOCK = HERE / "status.lock"
LOGS = HERE / "logs"
MODES = {"low": ("gemini-3.8-flash", "low", {"small", "medium"}),
         "medium": ("gemini-3.8-flash", "medium", {"large"})}

spec = importlib.util.spec_from_file_location("status", HERE / "status.py")
st = importlib.util.module_from_spec(spec)
spec.loader.exec_module(st)
local = threading.Lock()


class locked:
    """Exclusive access to status.json across threads and across processes."""
    def __enter__(self):
        local.acquire()
        t0 = time.time()
        while True:
            try:
                self.fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                return self
            except FileExistsError:
                if time.time() - LOCK.stat().st_mtime > 120:   # stale lock from a killed run
                    LOCK.unlink(missing_ok=True)
                elif time.time() - t0 > 300:
                    local.release()
                    raise RuntimeError(f"cannot get {LOCK} — delete it if no run is active")
                time.sleep(0.2)

    def __exit__(self, *a):
        os.close(self.fd)
        LOCK.unlink(missing_ok=True)
        local.release()


def claim(sizes, retry_failed, only):
    with locked():
        d = st.load()
        for i, r in d.items():
            if r.get("size") not in sizes or (only and i not in only):
                continue
            if r["status"] == "todo" or (retry_failed and r["status"] == "failed"):
                r["status"], r["run"] = "running", f"started {time.strftime('%H:%M')}"
                st.save(d)
                st.render(d)
                return i
    return None


def record(i, fields):
    with locked():
        d = st.load()
        d[i].update(fields)
        st.save(d)
        st.render(d)


def process(i, model, thinking, workers):
    LOGS.mkdir(exist_ok=True)
    log = (LOGS / f"{i}.log").open("a", encoding="utf-8")
    log.write(f"\n=== {time.strftime('%Y-%m-%d %H:%M:%S')} {model} {thinking}\n")
    log.flush()
    t0 = time.time()
    work = VAULT / f"0-INBOX/temp/root-seg-v2/{i}"
    if not (work / "prepared.md").exists():
        # segment exits 2 when it stops before grouping — that is normal; prepared.md is what we need
        subprocess.run([PY, "-X", "utf8", str(SEGMENT), "segment", str(VAULT / f"0-INBOX/root/{i}.md"),
                        str(work)], stdout=log, stderr=subprocess.STDOUT, cwd=VAULT)
    if not (work / "prepared.md").exists():
        return {"status": "failed", "note": "segment step wrote no prepared.md — see the log",
                "run": f"{model} {thinking}"}
    out = VAULT / f"0-INBOX/temp/TOC-{i}"
    p = subprocess.run([PY, "-X", "utf8", str(RUNNER), i, "--model", model, "--thinking", thinking,
                        "--workers", str(workers), "--out", str(out)],
                       stdout=log, stderr=subprocess.STDOUT, cwd=VAULT)
    log.close()
    mins = round((time.time() - t0) / 60, 1)
    summ = out / "summary.json"
    if p.returncode != 0 or not summ.exists():
        tail = (LOGS / f"{i}.log").read_text(encoding="utf-8").strip().splitlines()[-1:]
        return {"status": "failed", "note": f"Gemini run failed: {tail[0][:160] if tail else ''}",
                "run": f"{model} {thinking} · {mins} min"}
    s = json.loads(summ.read_text(encoding="utf-8"))
    state = work / "state.json"
    form = json.loads(state.read_text(encoding="utf-8")).get("form", "") if state.exists() else ""
    f = {"status": s["status"], "form": form, "units": s.get("units", ""), "chunks": s.get("chunks", ""),
         "parts": s.get("parts", 0), "nodes": s.get("nodes", 0),
         "qc4": s.get("qc4", ""), "qc6": "" if s.get("qc6") is None else f"{s['qc6']} flags",
         "run": f"{model.replace('gemini-', '')} {thinking} · ${s.get('cost_usd', 0):.2f} · {mins} min"}
    notes = ["Gemini run — review the top-level parts"] if s["status"] == "done" else []
    if s.get("unanchored"):
        notes.append(f"{s['unanchored']} node(s) without an anchor ([[?]])")
    if not state.exists():
        notes.append("SEGMENT: state.json missing — fix before ingest")
    f["note"] = "; ".join(notes)
    return f


def worker(n, args, model, thinking, sizes, stop, counter):
    while not stop.is_set():
        with local:
            if args.limit and counter[0] >= args.limit:
                return
            counter[0] += 1
        i = claim(sizes, args.retry_failed, set(args.only or []))
        if not i:
            return
        print(f"[p{n}] {time.strftime('%H:%M:%S')} start {i}", flush=True)
        try:
            f = process(i, model, thinking, args.workers)
        except Exception as e:                      # never leave a text marked running
            f = {"status": "failed", "note": f"batch error: {e}"[:200]}
        record(i, f)
        print(f"[p{n}] {time.strftime('%H:%M:%S')} {f['status']:8} {i}  {f.get('run', '')}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", required=True, choices=MODES)
    ap.add_argument("--procs", type=int, default=3)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--reset-running", action="store_true")
    ap.add_argument("--retry-failed", action="store_true")
    args = ap.parse_args()
    model, thinking, sizes = MODES[args.mode]
    with locked():
        d = st.load()
        if any("size" not in r for r in d.values()):
            sys.exit("run categorise.py first (texts have no size class)")
        if args.reset_running:
            for r in d.values():
                if r["status"] == "running" and r.get("size") in sizes:
                    r["status"], r["run"] = "todo", ""
            st.save(d)
            st.render(d)
        todo = sum(1 for r in d.values() if r.get("size") in sizes and r["status"] == "todo")
    print(f"mode {args.mode}: {model} thinking {thinking} · sizes {sorted(sizes)} · {todo} to do · "
          f"{args.procs} at a time", flush=True)
    stop, counter = threading.Event(), [0]
    ts = [threading.Thread(target=worker, args=(n + 1, args, model, thinking, sizes, stop, counter))
          for n in range(args.procs)]
    for t in ts:
        t.start()
    try:
        while any(t.is_alive() for t in ts):
            time.sleep(1)
    except KeyboardInterrupt:
        stop.set()
        print("stopping: texts in progress stay 'running' — re-run with --reset-running")
    print("done")


if __name__ == "__main__":
    main()
