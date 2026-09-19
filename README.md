# ওপেন লজিক — বাংলা (ভারত)

OpenLogic-এর ভারতীয় বাংলা সংস্করণ তৈরির চলমান প্রকল্প। হিমায়িত উৎসের ৭২২টি TeX এককের মধ্যে বর্তমানে ২৯৯টি একক অনূদিত: OLP-0004–OLP-0300, OLP-0719 এবং OLP-0721। এই খসড়া *Q-তে প্রতিনিধিত্বযোগ্যতা* পর্যন্ত পৌঁছেছে। আরও ৪২৩টি এককের অনুবাদ বাকি, তাই এটি পূর্ণাঙ্গ সংস্করণ নয়।

This is an **in-progress, machine-translated Bengali (India) edition** of the Open Logic Project. The source-aligned draft contains 299 translated units through *Representability in Q*: OLP-0004–OLP-0300, OLP-0719, and OLP-0721. Another 423 units remain untranslated.

## Read the current edition

- [Read the 299-unit Bengali reader online](https://kokunoyumeto.github.io/OpenLogic-bn-Beng-IN/)
- [Download the v0.3.0 prerelease](https://github.com/KokunoYumeto/OpenLogic-bn-Beng-IN/releases/tag/v0.3.0-through-representability)

The release includes a standalone offline HTML reader and a validated, reflowable EPUB 3. It has no PDF because this edition is built directly as semantic HTML with native MathML; the online HTML is the readable preview.

## Scope and provenance

Source authority: [Open Logic Project](https://github.com/OpenLogicProject/OpenLogic), revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. The source manifest SHA-256 is `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`.

`upstream/` preserves the pristine English archive, including all 722 content files and upstream/component licenses. `bn-Beng-IN/content/` contains the aligned translations. English files in `upstream/` are not counted as translations. The cumulative reader includes each translated unit once and suppresses driver imports that would duplicate content.

The international programme is listed at the [OpenLogic translations hub](https://github.com/KokunoYumeto/OpenLogic-translations).

## Evidence and review

Terminology work uses documented Indian Bengali witnesses, including West Bengal university mathematics and philosophy materials and separately labelled Tripura educational material. OpenLogic remains the authority for mathematical content. The local canon PDFs and page images are research copies and are not redistributed; `evidence/` publishes source identities, hashes, passage roles, terminology decisions, correction records, and consultation receipts.

Review is automated and model-based. No independent human review is claimed. Checks cover source/translation block alignment, formula structure, references, environments, identifiers, token parity, Unicode normalization, semantic comparisons, reverse-paraphrase samples, reader structure, and rendered-page inspection. `python tools/check_source_draft.py` replays the public 299-unit source checks. `evidence/DRAFT_STATUS.json` records the source scope, and `evidence/CUMULATIVE_READER_299_QA.json` records the reader build.

The validated reader contains 299 unit markers, 18,795 native MathML expressions, 948 numbered environments, 186 proof trees, 51 tableaux, 7 derivations, 32 diagrams, and 867 internal links with none broken. EPUBCheck 5.3.0 reported zero messages, and a cold EPUB rebuild was byte-identical. Representative rendered pages were visually inspected for Bengali shaping, mathematics, contents navigation, diagrams, tableaux, and the final translated units.

## Build

Run:

```powershell
python tools/build_cumulative_semantic_reader.py --epubcheck-jar "C:\path\to\epubcheck-5.3.0.jar"
```

Requirements are Python 3, Pandoc 3.9 or newer, Java, and EPUBCheck 5.3.0. The builder converts the aligned source directly to semantic HTML and EPUB without a TeX engine. It embeds the pinned Noto Serif Bengali fonts from `fonts/`, emits native MathML, converts proof trees, tableaux, derivations, and diagrams to reflowable structures, validates internal links and EPUB packaging, and checks cold-build determinism.

## License

OpenLogic source and this translation: Creative Commons Attribution 4.0 International, with upstream attribution and component exceptions preserved. See `upstream/LICENSE.md` and the source component notices. Noto fonts: SIL Open Font License 1.1. Translation changes are identified by the `bn-Beng-IN/` directory and the machine-translation status above.
