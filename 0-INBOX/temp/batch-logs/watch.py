import time, re, pathlib, sys
ids = sys.argv[1:]; seen = set(); pat = re.compile(r"Running tree|Anchoring|Ingesting|Stamping|Not found:|letters|Running resegment QC|DONE in|FAILED|Traceback|INTEGRITY|WARNING|missing windows")
d = pathlib.Path(__file__).parent
while True:
    for c in ids:
        try: lines = (d / f"{c}.log").read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError: continue
        age = time.time() - (d / f"{c}.log").stat().st_mtime
        if age > 25 * 60 and (c, "stall", int(age // 1800)) not in seen:
            seen.add((c, "stall", int(age // 1800)))
            print(f"[{c}] STALL: log unchanged for {age/60:.0f} min", flush=True)
        for l in lines:
            if pat.search(l) and (c, l) not in seen:
                seen.add((c, l)); print(f"[{c}] {l.strip()[:200]}", flush=True)
    time.sleep(30)
