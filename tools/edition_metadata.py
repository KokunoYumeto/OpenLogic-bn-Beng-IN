"""Shared identity for this corrected edition; fixed dates keep builds reproducible."""

from datetime import date, datetime, timezone
import json

EDITION_DATE = "2026-10-01"
MODIFIED_UTC = EDITION_DATE + "T00:00:00Z"
FIXED_ZIP_TIME = (*date.fromisoformat(EDITION_DATE).timetuple()[:3], 0, 0, 0)
SOURCE_DATE_EPOCH = str(int(datetime.fromisoformat(MODIFIED_UTC.replace("Z", "+00:00")).timestamp()))
SOURCE_REVISION = "9620cc73f9c8e0ad003c514a5d3748f29611c4c0"
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
