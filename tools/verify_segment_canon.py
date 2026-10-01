"""Verify every current consultation row against the source and target bytes."""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
MANIFEST = REPO / "evidence/FULL_SOURCE_MANIFEST.jsonl"
LEDGER = REPO / "evidence/SEGMENT_CANON_USE.jsonl"
STATUS = REPO / "evidence/DRAFT_STATUS.json"
PASSAGES = REPO / "evidence/CANON_PASSAGES.jsonl"


def rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def checked_file(relative: str) -> bytes:
    path = (REPO / relative).resolve(strict=True)
    assert path.is_relative_to(REPO.resolve()) and path.is_file(), relative
    return path.read_bytes()


def check_span(blob: bytes, span: dict) -> None:
    start, end = span["byte_start"], span["byte_end"]
    assert isinstance(start, int) and isinstance(end, int) and 0 <= start < end <= len(blob)
    assert sha256(blob[start:end]) == span["sha256"]
    assert span["line_start"] == blob[:start].count(b"\n") + 1
    assert span["line_end"] == blob[:end].count(b"\n") + 1


def main() -> None:
    manifest = {row["unit_id"]: row for row in rows(MANIFEST)}
    assert len(manifest) == 722
    status = json.loads(STATUS.read_text(encoding="utf-8"))
    unit_checks = {row["unit_id"]: row for row in status["current_checks"]["unit_checks"]}
    assert set(unit_checks) == set(manifest)
    passages = {row["passage_id"] for row in rows(PASSAGES)}
    assert len(passages) == 29
    ledger = rows(LEDGER)
    assert len(ledger) == 7825
    assert len({row["segment_id"] for row in ledger}) == len(ledger)
    used_passages = {pid for row in ledger for pid in row["canon_passages_consulted"]}
    assert len(used_passages) == 28
    groups: dict[str, list[dict]] = defaultdict(list)
    for row in ledger:
        groups[row["unit_id"]].append(row)
    assert set(groups) == set(manifest)
    translated = 0
    for uid, unit_rows in groups.items():
        item = manifest[uid]
        source_path = item["source_path"]
        assert source_path.startswith("content/") and ".." not in Path(source_path).parts
        source = checked_file("upstream/" + source_path)
        target = checked_file("bn-Beng-IN/" + source_path)
        assert len(source) == item["source_bytes"] and sha256(source) == item["source_sha256"]
        assert sha256(target) == unit_checks[uid]["target_sha256"]
        assert len(unit_rows) == unit_checks[uid]["source_blocks"] == unit_checks[uid]["target_blocks"]
        previous_source_end = previous_target_end = 0
        for number, row in enumerate(unit_rows, 1):
            assert row["segment_id"] == f"{uid}-B{number:03d}"
            assert row["source_path"] == source_path
            assert row["translation_path"] == "bn-Beng-IN/" + source_path
            assert row["source_file_sha256"] == sha256(source)
            assert row["translation_file_sha256"] == sha256(target)
            check_span(source, row["source_span"])
            check_span(target, row["translation_span"])
            assert row["source_span"]["byte_start"] >= previous_source_end
            assert row["translation_span"]["byte_start"] >= previous_target_end
            previous_source_end = row["source_span"]["byte_end"]
            previous_target_end = row["translation_span"]["byte_end"]
            if row["status"] == "translated_semantically_reviewed":
                assert row["canon_passages_consulted"]
                assert set(row["canon_passages_consulted"]) <= passages
            else:
                assert row["status"] == "unchanged_structural_or_formal"
                assert not row["canon_passages_consulted"]
            assert row["consultation_role"] and row["consultation_record"] and row["qa"]
            translated += row["status"] == "translated_semantically_reviewed"
    assert translated == 6673
    print(json.dumps({"status": "passed", "units": len(groups), "segments": len(ledger),
                      "translated_segments": translated, "canon_passages_used": len(used_passages),
                      "ledger_sha256": sha256(LEDGER.read_bytes())}))


if __name__ == "__main__":
    main()
