#!/usr/bin/env python3
"""
Ingest RegCopilot chunks into Supabase via the ingest-chunks Edge Function.

Reads ~/Portfolio/RegCopilot/chunks/ingest_payload.json (produced by chunk_regs_v2.py)
and POSTs each regulation's chunks in batches of BATCH_SIZE.

Usage:
  python3 ingest_chunks.py            # ingest all
  python3 ingest_chunks.py gdpr dora  # ingest only those regulation_ids
  DRY_RUN=1 python3 ingest_chunks.py  # print plan, don't POST
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

ENDPOINT = "https://oaemzcszpcqufuwrwual.supabase.co/functions/v1/ingest-chunks"
SECRET = os.environ.get("INGEST_SECRET", "regcopilot-ingest-2026")
PAYLOAD_PATH = Path("/Users/mehreenhimani/Portfolio/RegCopilot/chunks/ingest_payload.json")
BATCH_SIZE = 10  # chunks per POST — well under any reasonable body-size limit
DRY_RUN = os.environ.get("DRY_RUN") == "1"

def post_batch(reg_id, chunks):
    body = json.dumps({"regulation_id": reg_id, "chunks": chunks}).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "x-ingest-secret": SECRET,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as e:
        return None, f"URLError: {e.reason}"

def main():
    if not PAYLOAD_PATH.exists():
        print(f"ERROR: {PAYLOAD_PATH} not found. Run chunk_regs_v2.py first.", file=sys.stderr)
        sys.exit(2)

    payload = json.loads(PAYLOAD_PATH.read_text())
    only = set(sys.argv[1:]) or None  # filter by regulation_id if args passed

    total_planned = 0
    total_sent = 0
    total_ok = 0
    failures = []

    for group in payload:
        reg_id = group["regulation_id"]
        if only and reg_id not in only:
            continue
        chunks = group["chunks"]
        n = len(chunks)
        total_planned += n
        n_batches = (n + BATCH_SIZE - 1) // BATCH_SIZE
        print(f"\n=== {reg_id}: {n} chunks in {n_batches} batches of <= {BATCH_SIZE} ===")

        for i in range(0, n, BATCH_SIZE):
            batch = chunks[i:i+BATCH_SIZE]
            label = f"{reg_id} batch {i//BATCH_SIZE + 1}/{n_batches} ({len(batch)} chunks)"
            if DRY_RUN:
                print(f"  [dry-run] {label}")
                continue
            status, body = post_batch(reg_id, batch)
            total_sent += len(batch)
            ok = status is not None and 200 <= status < 300
            if ok:
                total_ok += len(batch)
                print(f"  OK   {label}  -> HTTP {status}")
            else:
                failures.append({"reg_id": reg_id, "batch_start": i, "status": status, "body": body[:100]})
                print(f"  FAIL {label}  -> HTTP {status}: {body[:200]}")
                # Stop on first failure so we don't compound errors
                print("  Stopping early.")
                break
            time.sleep(0.1)  # gentle on the function

        if failures:
            break

    print("\n--- Summary ---")
    print(f"Planned: {total_planned} chunks")
    print(f"Sent:    {total_sent} chunks")
    print(f"OK:      {total_ok} chunks")
    if failures:
        print(f"Failures: {len(failures)}")
        for f in failures:
            print(f"  {f['reg_id']} @ batch_start={f['batch_start']}  HTTP {f['status']}: {f['body'][:200]}")
        sys.exit(1)

if __name__ == "__main__":
    main()
