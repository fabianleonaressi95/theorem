#!/usr/bin/env python3
"""Render a compact GitHub Actions summary from audit_runtime JSONL events."""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict
from pathlib import Path


def render(path: Path) -> str:
    events = []
    if path.is_file():
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"{path}:{line_number}: invalid JSONL event: {exc}") from exc

    durations = defaultdict(list)
    failures = []
    active = {}
    completed_cases = None
    total_cases = None
    for event in events:
        name = event.get("phase")
        kind = event.get("event")
        if kind == "phase_started" and name:
            active[name] = event
        elif kind == "phase_completed" and name:
            durations[name].append(float(event.get("elapsed_seconds", 0.0)))
            active.pop(name, None)
        elif kind == "phase_failed":
            failures.append(event)
            if name:
                active.pop(name, None)
        if kind == "audit_configuration":
            total_cases = event.get("total_cases", total_cases)
            completed_cases = event.get("completed_cases", completed_cases)
        elif kind in ("mesh_realization_checkpointed", "mesh_case_summary"):
            completed_cases = event.get("completed_cases", completed_cases)
            total_cases = event.get("total_cases", total_cases)

    lines = [
        "# Audit execution summary",
        "",
        f"- Progress events: **{len(events)}**",
        f"- Completed phases: **{sum(len(v) for v in durations.values())}**",
        f"- Failed phases: **{len(failures)}**",
    ]
    if total_cases is not None:
        lines.append(f"- Mesh realizations checkpointed: **{completed_cases or 0}/{total_cases}**")
    if active:
        lines.append("- Phase(s) active or interrupted at log end: " +
                     ", ".join(f"`{name}`" for name in sorted(active)))
    if failures:
        lines.extend(["", "## Failures"])
        for item in failures:
            lines.append(f"- `{item.get('phase', 'unknown')}`: "
                         f"{item.get('error_type', 'error')} — {item.get('error', '')}")
    if durations:
        lines.extend(["", "## Phase timings", "",
                      "| Phase | Calls | Total (s) | Mean (s) | Max (s) |",
                      "|---|---:|---:|---:|---:|"])
        rows = sorted(durations.items(),
                      key=lambda item: sum(item[1]), reverse=True)
        for name, values in rows:
            total = sum(values)
            mean = total / len(values)
            lines.append(f"| `{name}` | {len(values)} | {total:.3f} | "
                         f"{mean:.3f} | {max(values):.3f} |")
    elif not events:
        lines.extend(["", "No progress log was produced."])
    return "\n".join(lines) + "\n"


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: render_audit_summary.py PROGRESS.jsonl")
    summary = render(Path(sys.argv[1]))
    target = os.environ.get("GITHUB_STEP_SUMMARY")
    if target:
        with Path(target).open("a", encoding="utf-8") as stream:
            stream.write(summary)
    print(summary)


if __name__ == "__main__":
    main()
