"""Shared identity for this corrected edition; fixed dates keep builds reproducible."""

from datetime import date, datetime, timezone
import json
from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]
PROFILE_PATH = ROOT / "publication/full-edition.json"
PROFILE = json.loads(PROFILE_PATH.read_bytes()) if PROFILE_PATH.is_file() else {}
SOURCE_REVISION = PROFILE.get("source_revision", "9620cc73f9c8e0ad003c514a5d3748f29611c4c0")
if PROFILE:
    contract = tomllib.loads((ROOT / "olp-edition.toml").read_text(encoding="utf-8"))
    if SOURCE_REVISION != contract["pins"]["olp"]["commit"]:
        raise ValueError("The full edition and its frozen English source use different revisions")

EDITION_DATE = PROFILE.get("edition_date", "2026-10-01")
MODIFIED_UTC = EDITION_DATE + "T00:00:00Z"
FIXED_ZIP_TIME = (*date.fromisoformat(EDITION_DATE).timetuple()[:3], 0, 0, 0)
SOURCE_DATE_EPOCH = str(int(datetime.fromisoformat(MODIFIED_UTC.replace("Z", "+00:00")).timestamp()))
REVIEW_MODEL = "gpt-6.1-sol"
REVIEW_EFFORT = "ultra"
HISTORICAL_TRANSLATION_MODELS = ["gpt-5.6-sol", "gpt-6-sol"]


def metadata():
    return {
        "schema": "openlogic-bn-edition-identity/1",
        "edition_date": EDITION_DATE,
        "modified_utc": MODIFIED_UTC,
        "source_date_epoch": SOURCE_DATE_EPOCH,
        "source_revision": SOURCE_REVISION,
        "review_model": REVIEW_MODEL,
        "review_effort": REVIEW_EFFORT,
        "historical_translation_models": HISTORICAL_TRANSLATION_MODELS,
    }


if __name__ == "__main__":
    print(json.dumps(metadata()))
