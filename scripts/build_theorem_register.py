#!/usr/bin/env python3
"""Build docs/THEOREM_MASTER_REGISTER.{csv,md} from theorems/ cards.

Heuristic epistemic classification — conservative: a card is PROVED only
when its own status/classification language claims a proof; audit-style
cards default to NUMERICALLY_VERIFIED only when they report reproducible
computational checks; unresolved qualifiers force OPEN/CONDITIONAL.
Every row keeps a `notes` field flagging low-confidence classifications.
"""
from __future__ import annotations

import csv
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEOREMS = ROOT / "theorems"
OUT_CSV = ROOT / "docs" / "THEOREM_MASTER_REGISTER.csv"
OUT_MD = ROOT / "docs" / "THEOREM_MASTER_REGISTER.md"

TAXONOMY = [
    "PROVED", "EXACT_CERTIFICATE", "NUMERICALLY_VERIFIED", "CONDITIONAL",
    "CANDIDATE", "HYPOTHESIS", "OPEN", "SUPERSEDED", "QUARANTINED",
]

ID_RE = re.compile(r"^(T\d{3}|S\d{3}|B\d+-B\d+|C60[A-Z0-9_]*|EQC[-A-Z0-9]*|TSMR-[A-Z0-9]+|MQM?-?\d*|Q\d|FACTOR[A-Z_]*)")
DEP_RE = re.compile(r"\bT\d{3}\b")
SCRIPT_RE = re.compile(r"(?:scripts|tests)/[\w./() -]+\.(?:py|json|npz|npy)")


def card_id(path: Path) -> str:
    stem = path.stem
    m = ID_RE.match(stem)
    cid = m.group(1) if m else stem.split("-")[0].split("_")[0]
    # Normalise long slug-ids: drop trailing date stamps.
    cid = re.sub(r"_20\d{2}(-\d{2}-\d{2})?$", "", cid)
    return cid


def title_of(text: str, path: Path) -> str:
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
        if s.startswith("#") and not s.startswith("##"):
            return s.lstrip("#").strip()
    return path.stem.replace("_", " ").replace("-", " ")


def status_lines(text: str) -> list[str]:
    out = []
    for line in text.splitlines()[:80]:
        ls = line.strip().lower()
        if re.search(r"\b(status|classificazione|classification|stato)\b", ls) and len(ls) < 400:
            out.append(line.strip())
    return out


def has_open_qualifier(text: str) -> bool:
    head = text[:6000].lower()
    pats = [
        r"\bopen\b", r"non dimostrat", r"not proved", r"not proven",
        r"restano? open", r"remain(s|ing)? open", r"incomplet",
        r"apert", r"da dimostrare", r"to be (proved|proven|shown|demonstrated)",
        r"unproven", r"senza prova", r"missing proof", r"gap\b",
    ]
    return any(re.search(p, head) for p in pats)


def classify(text: str, fname: str) -> tuple[str, str]:
    head = text[:8000]
    low = head.lower()
    fname_l = fname.lower()
    sl = " ".join(status_lines(text)).lower()

    # Explicit quarantine/supersession first — only via status lines or
    # filename markers; body mentions of "superseded" refer to other work.
    sl_head = " ".join(status_lines(text)[:3]).lower()
    if re.search(r"\bsuperseded\b|\bsuperseeded\b", sl_head) or "superseded" in fname.lower():
        return "SUPERSEDED", "card-level superseded marker"
    if re.search(r"\bquarantined?\b", sl_head) or "quarantined" in fname.lower():
        return "QUARANTINED", "card-level quarantine marker"

    # Strong OPEN markers.
    if re.search(r"\bstatus\b[^\n]{0,80}\bopen\b|\*\*open\b|open —|open -", sl):
        return "OPEN", "explicit OPEN status"
    if "_open_" in fname_l or fname_l.endswith("_open.md") or " open " in " " + fname_l:
        return "OPEN", "filename OPEN marker"

    # Exact certificate.
    if re.search(r"exact[_ ]certificate|certificato esatto|exact spectral certification|exact representation", low):
        return "EXACT_CERTIFICATE", "exact-certificate language"

    # Proof claims — must not be contradicted by open qualifiers.
    proof_claim = bool(re.search(
        r"\b(proved|proven|dimostrat[oaie]|teorema dimostrato|proposizione dimostrata|"
        r"dimostrazione completa|established|formalized?)\b", sl))
    if proof_claim and not has_open_qualifier(text):
        if re.search(r"conditional|a condizione|purché|provided that|assuming|sotto ipotesi", sl):
            return "CONDITIONAL", "proof claim with explicit hypotheses"
        return "PROVED", "explicit proof claim, no open qualifier found"
    if proof_claim and has_open_qualifier(text):
        return "CONDITIONAL", "partial proof claim with open remainder"

    # Conditional language.
    if re.search(r"\bconditional\b|\bcondizionat|a condizione|purché|provided that|"
                 r"assuming\b|sotto ipotesi|hypothesized", sl):
        return "CONDITIONAL", "explicit conditional language"

    # Numerical/audit verification.
    if re.search(r"\baudit\b|audited|verification|verifica|numerical|numerical verification|"
                 r"residual|residuo|benchmark|crossaudit|cross-audit", fname_l + " " + low[:3000]):
        if re.search(r"\bverified\b|verificat|confirmed|confermato", sl):
            return "NUMERICALLY_VERIFIED", "audit/verification card with verified marker"
        return "NUMERICALLY_VERIFIED", "audit/benchmark card (heuristic)"

    # Candidate / conjecture.
    if re.search(r"\bcandidate\b|\bcandidat|\bconjecture\b|\bcongettura\b|plausible", sl + " " + low[:3000]):
        return "CANDIDATE", "candidate/conjecture language"
    if re.search(r"\bhypothes", sl):
        return "HYPOTHESIS", "hypothesis language"

    # Program/framework records without proof claims.
    if re.search(r"research programme|framework|protocol|roadmap|dossier|programma", low[:2000]):
        return "OPEN", "programme/framework record without proof claim"

    return "OPEN", "no status evidence found — conservative default"


def extract_deps(text: str, self_id: str) -> list[str]:
    deps = sorted(set(DEP_RE.findall(text)) - {self_id})
    return deps


def extract_refs(text: str) -> tuple[list[str], list[str]]:
    scripts, tests = [], []
    for m in SCRIPT_RE.findall(text):
        for tok in m.split():
            p = tok.strip().rstrip(".,;)")
            if "/" in p and re.search(r"\.(py|json|npz|npy)$", p):
                (tests if p.startswith("tests/") else scripts).append(p)
    return sorted(set(scripts)), sorted(set(tests))


def area_of(fid: str, title: str) -> str:
    t = (fid + " " + title).lower()
    rules = [
        ("C60", "fullerene/C60"), ("fullerene", "fullerene"), ("Q6", "Q6 lattice"),
        ("RGS", "RGS"), ("PRISM", "PRISM"), ("QLG", "QLG"), ("krist", "Krist-All"),
        ("antitwin", "Anti-Twin"), ("se3", "SE(3)"), ("cartan", "Cartan"),
        ("feec", "FEEC/DEC"), ("hodge", "Hodge"), ("rumin", "Rumin"),
        ("morandotti", "Morandotti"), ("jitterbug", "Jitterbug"),
        ("vesica", "Vesica"), ("volterra", "Volterra"), ("lindblad", "Lindblad"),
        ("mckay", "McKay"), ("2i", "binary icosahedral"), ("supergolden", "supergolden"),
        ("whitney", "Whitney-Hodge"), ("tsmr", "TSMR morphodynamics"),
        ("eqc", "EQC"), ("mqm", "MQM"), ("hysteresis", "hysteresis"),
        ("k0", "K0 spectral"), ("golden", "golden geometry"),
    ]
    for key, area in rules:
        if key in t:
            return area
    return "general"


def main() -> int:
    rows = []
    uncertain = []
    for path in sorted(THEOREMS.rglob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        fid = card_id(path)
        title = title_of(text, path)
        status, why = classify(text, path.name)
        deps = extract_deps(text, fid)
        scripts, tests = extract_refs(text)
        rel = path.relative_to(ROOT).as_posix()
        rows.append({
            "id": fid, "title": title, "area": area_of(fid, title),
            "statement": "", "hypotheses": "", "status": status,
            "proof_type": "", "proof_ref": "", "scripts": ";".join(scripts),
            "tests": ";".join(tests), "datasets": "", "quantitative": "",
            "dependencies": ";".join(deps), "limits": "", "next_check": "",
            "last_update": "", "file": rel, "status_note": why,
        })
        if why.startswith(("no status", "audit/benchmark card (heuristic)")):
            uncertain.append((fid, path.name, why))

    # Fill statement/hypotheses/limits from card text where cheaply extractable.
    for r in rows:
        text = (ROOT / r["file"]).read_text(encoding="utf-8", errors="replace")
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        # First non-heading paragraph after title.
        body = []
        for l in lines[1:]:
            if l.startswith("#"):
                break
            if not l.startswith("**") and not l.startswith("|"):
                body.append(l)
            if len(" ".join(body)) > 300:
                break
        r["statement"] = " ".join(body)[:300]
        for l in lines[:40]:
            if re.search(r"ipotesi|hypothes|assume|assumption|purché|provided", l, re.I):
                r["hypotheses"] = l[:300]
                break
        for l in lines[:60]:
            if re.search(r"non (è|e) (una )?prova|does not claim|non dimostra|limitation|limiti", l, re.I):
                r["limits"] = l[:300]
                break
        m = re.search(r"\*\*Date:\*\*\s*([^\n]+)|Data:\s*([0-9-]+)", text[:1500])
        if m:
            r["last_update"] = (m.group(1) or m.group(2)).strip()
        # proof type heuristic
        if r["status"] == "PROVED":
            r["proof_type"] = "analytic (claimed)"
        elif r["status"] == "EXACT_CERTIFICATE":
            r["proof_type"] = "exact certificate"
        elif r["status"] == "NUMERICALLY_VERIFIED":
            r["proof_type"] = "computational audit"
        elif r["status"] in ("OPEN", "CANDIDATE", "HYPOTHESIS"):
            r["proof_type"] = "none / incomplete"
        else:
            r["proof_type"] = "mixed / see card"

    fieldnames = ["id", "title", "area", "statement", "hypotheses", "status",
                  "proof_type", "proof_ref", "scripts", "tests", "datasets",
                  "quantitative", "dependencies", "limits", "next_check",
                  "last_update", "file", "status_note"]
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow(r)

    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    with OUT_MD.open("w", encoding="utf-8") as fh:
        fh.write("# Theorem master register\n\n")
        fh.write(f"Generated by `scripts/build_theorem_register.py` from `theorems/` "
                 f"({len(rows)} cards). Do not edit by hand — regenerate.\n\n")
        fh.write(
            "> **Epistemic-status caveat (2026-11-27):** statuses are "
            "machine-assisted heuristics derived from card text, not author-"
            "certified classifications. Rows whose `status_note` begins with "
            "`no status` or `audit/benchmark card (heuristic)` are low-"
            "confidence and MUST NOT be cited externally as PROVED/"
            "NUMERICALLY_VERIFIED etc. without explicit author sign-off. "
            "No heuristic status was promoted to PROVED; original card "
            "evidence remains authoritative.\n\n"
        )
        fh.write("## Status distribution\n\n")
        fh.write("| Status | Count |\n|---|---|\n")
        for s in TAXONOMY:
            fh.write(f"| {s} | {counts.get(s, 0)} |\n")
        fh.write("\n## Cards\n\n")
        fh.write("| ID | Title | Area | Status | File | Note |\n|---|---|---|---|---|---|\n")
        for r in rows:
            title = r["title"].replace("|", "\\|")[:90]
            fh.write(f"| {r['id']} | {title} | {r['area']} | {r['status']} | `{r['file']}` | {r['status_note']} |\n")

    print(f"rows={len(rows)}")
    for s in TAXONOMY:
        print(f"  {s}: {counts.get(s, 0)}")
    print(f"uncertain={len(uncertain)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
