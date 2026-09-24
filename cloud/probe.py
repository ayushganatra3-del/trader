#!/usr/bin/env python3
"""Read-only public provider diagnostic. Never reads or mutates a portfolio."""
import datetime as dt
import json
from pathlib import Path
import tempfile
import urllib.error

import engine as e


def probe(*, fetcher=None, now=None):
    now = now or dt.datetime.now(e.UTC)
    day = e.london_day(now)
    results = {}
    with tempfile.TemporaryDirectory(prefix="virtual-market-probe-") as folder:
        for symbol in e.SYMBOLS:
            try:
                quote = (fetcher or e.fetch_snapshot)(symbol, Path(folder), day)
                results[symbol] = {"status": "available", "observed_at": quote["observed_at"],
                                   "latest_complete_bar_end": quote["latest_end"], "currency": quote["currency"],
                                   "close_gbp": quote["close"], "fresh_for_new_decisions": quote["fresh"],
                                   "age_seconds": quote["age_seconds"]}
            except (urllib.error.URLError, TimeoutError, ValueError, KeyError, TypeError, IndexError, OSError) as error:
                results[symbol] = {"status": "unavailable", "error": f"{type(error).__name__}: {error}"}
    return {"status": "available" if all(item["status"] == "available" for item in results.values()) else "unavailable",
            "session_day": day, "mode": "read-only diagnostic; no portfolio changes", "symbols": results}


if __name__ == "__main__":
    result = probe()
    print(json.dumps(result, indent=2, allow_nan=False))
    raise SystemExit(0 if result["status"] == "available" else 1)
