# Decision occurrence evidence layout

The Bengali translation decision log retains all 320 decisions and all 26,232 exact target-line occurrences at the 411-unit source checkpoint. It uses compact occurrence references so the public evidence can continue to grow through the complete edition without reaching GitHub's per-file size limit. The earlier expanded representation remains accessible at immutable source revision `c6b64427f776cf7ef53e4da5da1f0b755ebc5ac3`.

`TRANSLATION_DECISION_LOG.jsonl` uses schema `openlogic-bn-translation-decision/3`. Each decision retains the chosen Bengali, English concept, rationale, consulted canon identities and scope, alternatives, confidence, review question and up to three representative exact source blocks. Its `target_occurrences` list retains occurrence ID, unit ID, source segment ID, target line, both block SHA-256 values and the matched Bengali rendering. `TRANSLATION_DECISION_INDEX.json` uses index schema `/2` and contains the same compact decision records. `TRANSLATION_DECISION_OCCURRENCES.csv` is a flat view of all occurrences. The readable `TRANSLATION_DECISION_LOG.md` and provisional-priority view remain available.

To reconstruct an occurrence's exact source and target context:

1. Find its `source_segment_id` in `DRAFT_SEGMENT_CANON_USE.jsonl`.
2. Use that segment's `source_path` with `upstream/`, and its `translation_path` directly. The segment provides exact UTF-8 byte offsets, line spans, file hashes and block SHA-256 values for both sides.
3. Read each file at the recorded byte offsets and verify its block SHA-256. The source is the frozen upstream file from revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`; the target line contains the indexed Bengali rendering.

The compact files omit repeated full source blocks, target lines, rationale and review questions from every CSV row. That information is still present in the frozen source and target files, the segment index or the per-decision records. Every occurrence can be reconstructed and checked; no occurrence or decision was dropped. Final PDF and printed-page locators remain pending until cumulative reader pagination.
