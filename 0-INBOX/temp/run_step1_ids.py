"""Run run_step1.process_text on the ids given on the command line, in parallel."""
import concurrent.futures, sys
sys.path.insert(0, __file__.rsplit("\\", 1)[0].rsplit("/", 1)[0])
import run_step1

if __name__ == "__main__":
    ids = sys.argv[1:]
    with concurrent.futures.ProcessPoolExecutor(max_workers=len(ids)) as ex:
        for cid, passed, info in ex.map(run_step1.process_text, ids):
            print(f"[{cid}] {'PASSED' if passed else 'FAILED'}", info if not passed else info["res_stdout"], flush=True)
