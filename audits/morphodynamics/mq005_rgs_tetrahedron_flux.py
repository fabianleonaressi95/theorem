"""Importable MQ-005 audit API.

The executable, provenance-preserving audit lives in
scripts/audit_mq005_rgs_tetrahedron_flux.py. This module provides the same
build_audit function to the repository's focused pytest suite.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

_SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "audit_mq005_rgs_tetrahedron_flux.py"
_SPEC = importlib.util.spec_from_file_location("_mq005_rgs_tetrahedron_flux_script", _SCRIPT)
if _SPEC is None or _SPEC.loader is None:
    raise ImportError(f"cannot load MQ-005 audit script at {_SCRIPT}")
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)

build_audit = _MODULE.build_audit
