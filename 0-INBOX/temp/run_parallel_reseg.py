import concurrent.futures
import sys
import time
from pathlib import Path

# Add commentary-resegment scripts directory
reseg_scripts_dir = Path("4-SYSTEM/Skills/commentary-resegment/scripts").resolve()
sys.path.insert(0, str(reseg_scripts_dir))
import resegment

def main():
    cid = sys.argv[1] if len(sys.argv) > 1 else "Di_3CEo_"
    max_workers = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    
    vault_root = Path(".").resolve()
    input_path = vault_root / "0-INBOX" / "segmented" / f"{cid}.toc.md"
    staging_dir = vault_root / "0-INBOX" / "temp" / f"RESEG-{cid}" / "windows"
    output_path = vault_root / "0-INBOX" / "resegmented" / f"{cid}.reseg.md"
    log_path = vault_root / "0-INBOX" / "resegmented" / f"{cid}.ops.md"
    
    staging_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Loading {input_path}...")
    frontmatter, blocks = resegment.parse_file(input_path)
    total = len(blocks)
    heading_count = sum(1 for b in blocks if resegment.is_heading(b))
    print(f"Blocks: {total} (headings: {heading_count}, content: {total - heading_count})")
    
    windows = resegment.make_windows(blocks, resegment.DEFAULT_WINDOW_SIZE, resegment.DEFAULT_OVERLAP)
    print(f"Windows: {len(windows)}")
    
    to_call = []
    for win in windows:
        already = resegment.load_window_result(staging_dir, win["idx"])
        if already is None:
            to_call.append(win)
            
    print(f"Windows to process: {len(to_call)} / {len(windows)}")
    
    client = resegment.get_client()
    # a dropped connection otherwise hangs a worker forever (seen 2026-10-13): give every
    # request a 20-minute ceiling so it errors out and is retried
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=client._api_client.api_key,
                          http_options=types.HttpOptions(timeout=20 * 60 * 1000))
    
    def worker(win):
        t0 = time.time()
        try:
            ops = resegment.call_llm_for_window(client, resegment.DEFAULT_MODEL, win)
            resegment.save_window_result(staging_dir, win, ops)
            dt = time.time() - t0
            print(f"  [{dt:4.1f}s] Window {win['idx']+1}/{len(windows)} done: {len(ops)} op(s)", flush=True)
            return win["idx"], len(ops), None
        except Exception as e:
            dt = time.time() - t0
            print(f"  [{dt:4.1f}s] Window {win['idx']+1}/{len(windows)} FAILED: {e}", flush=True)
            return win["idx"], 0, e

    if to_call:
        print(f"Running {len(to_call)} windows with {max_workers} worker threads...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [executor.submit(worker, win) for win in to_call]
            for f in concurrent.futures.as_completed(futures):
                idx, n_ops, err = f.result()
                if err:
                    print(f"Error on window {idx+1}: {err}")
                    
    # Check if all completed
    window_results = []
    missing = []
    for win in windows:
        res = resegment.load_window_result(staging_dir, win["idx"])
        if res is None:
            missing.append(win["idx"] + 1)
        else:
            window_results.append(res)
            
    if missing:
        print(f"FAILED: missing windows: {missing}")
        sys.exit(1)
        
    print("\nCombining operations...")
    ops_raw, conflicts = resegment.combine_operations(window_results, blocks)
    ops_valid, validation_errors = resegment.validate_operations(ops_raw, blocks)
    print(f"Operations to apply: {len(ops_valid)}")
    
    result_blocks = resegment.apply_operations(blocks, ops_valid)
    print(f"Blocks: {len(blocks)} -> {len(result_blocks)}")
    
    ok, err_msg = resegment.check_integrity(input_path, frontmatter, result_blocks)
    if not ok:
        print(f"INTEGRITY ERROR: {err_msg}")
        sys.exit(2)
        
    print("Integrity check passed!")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    resegment.write_output(output_path, frontmatter, result_blocks)
    resegment.write_ops_log(log_path, ops_valid, validation_errors, conflicts, blocks, result_blocks, cid)
    print(f"Wrote {output_path}")
    print(f"Wrote {log_path}")

if __name__ == "__main__":
    main()
