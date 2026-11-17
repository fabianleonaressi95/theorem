"""Structured, low-overhead progress and timing for long mathematical audits.

Each event is emitted as one JSON line to stderr and, when AUDIT_PROGRESS_FILE
is set, appended to that file. Events never alter numerical results.
"""
from __future__ import annotations

import json
import os
import sys
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path


def emit(event: str, **fields) -> dict:
    record = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "event": event,
        **fields,
    }
    line = json.dumps(record, sort_keys=True, default=str, separators=(",", ":"))
    print(line, file=sys.stderr, flush=True)
    target = os.environ.get("AUDIT_PROGRESS_FILE")
    if target:
        path = Path(target)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as stream:
            stream.write(line + "\n")
            stream.flush()
    return record


@contextmanager
def phase(name: str, **metadata):
    started = time.monotonic()
    emit("phase_started", phase=name, **metadata)
    try:
        yield
    except BaseException as exc:
        emit(
            "phase_failed", phase=name,
            elapsed_seconds=round(time.monotonic() - started, 6),
            error_type=type(exc).__name__, error=str(exc), **metadata,
        )
        raise
    else:
        emit(
            "phase_completed", phase=name,
            elapsed_seconds=round(time.monotonic() - started, 6), **metadata,
        )


def timed(name: str, function, *args, **kwargs):
    with phase(name):
        return function(*args, **kwargs)
