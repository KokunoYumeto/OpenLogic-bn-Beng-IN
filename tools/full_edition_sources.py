"""Bind full-reader translations to the current ledger or historical status."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


UNIT_LEDGER = "units.jsonl"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def load_target_hashes(repo: Path, manifest: list[dict]) -> tuple[dict[str, str], dict[str, str]]:
    sources = {row["unit_id"]: row for row in manifest}
    if len(sources) != len(manifest):
        raise ValueError("duplicate unit ID in full source manifest")

    ledger = repo / UNIT_LEDGER
    if ledger.exists():
        data = ledger.read_bytes()
        hashes = {}
        for line in data.decode("utf-8").splitlines():
            row = json.loads(line)
            uid = row["id"]
            source = sources.get(uid)
            if source is None or uid in hashes:
                raise ValueError(f"{uid}: unexpected or duplicate unit in {UNIT_LEDGER}")
            if (row["src"], row["path"], row["src_sha256"], row["state"]) != (
                "olp", source["source_path"], source["source_sha256"], "current",
            ):
                raise ValueError(f"{uid}: source identity or state differs from the full source manifest")
            original = (repo / "upstream" / source["source_path"]).read_bytes()
            header = f"blob {len(original)}\0".encode("ascii")
            if (
                len(original) != source["source_bytes"]
                or hashlib.sha256(original).hexdigest() != row["src_sha256"]
                or hashlib.sha1(header + original).hexdigest() != row["src_blob"]
            ):
                raise ValueError(f"{uid}: English source bytes differ from {UNIT_LEDGER}")
            target_hash = row["tr_sha256"]
            if not isinstance(target_hash, str) or not re.fullmatch(r"[a-f0-9]{64}", target_hash):
                raise ValueError(f"{uid}: invalid translation SHA-256 in {UNIT_LEDGER}")
            hashes[uid] = target_hash
        if hashes.keys() != sources.keys():
            raise ValueError(f"{UNIT_LEDGER} is missing units from the full source manifest")
        return hashes, {"unit_ledger_sha256": hashlib.sha256(data).hexdigest()}

    status = (repo / "evidence/DRAFT_STATUS.json").read_bytes()
    record = json.loads(status)
    checks = record["current_checks"]
    rows = checks["unit_checks"]
    hashes = {row["unit_id"]: row["target_sha256"] for row in rows}
    if (
        len(rows) != record["draft_scope"]["translated_count"]
        or len(hashes) != len(rows)
        or hashes.keys() != sources.keys()
    ):
        raise ValueError("historical draft status does not cover the full source manifest")
    if checks["segment_index_sha256"] != digest(repo / "evidence/SEGMENT_CANON_USE.jsonl"):
        raise ValueError("historical segment index SHA-256 differs from draft status")
    return hashes, {"draft_status_sha256": hashlib.sha256(status).hexdigest()}
