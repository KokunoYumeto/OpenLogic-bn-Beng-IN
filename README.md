# ওপেন লজিক — বাংলা (ভারত)

OpenLogic-এর ভারতীয় বাংলা সংস্করণ তৈরির চলমান প্রকল্প। সম্পূর্ণ উৎসের ৭২২টি TeX একক অনুবাদ করাই লক্ষ্য। এখন প্রকাশযোগ্য পাঠে সেট অধ্যায়ের আটটি উৎস-একক আছে: OLP-0004–OLP-0010 এবং OLP-0721। পূর্ণাঙ্গ সংস্করণ এখনও সম্পূর্ণ হয়নি।

This is an **in-progress, machine-translated Bengali (India) edition**, not a completed 722-unit edition. The initial reader covers eight source units: the six ordinary Sets sections, their chapter driver, and the superseded alternative proof explanation integrated at the same subject location. All exercises, captions, mathematical examples and the original editorial note in those units are translated. The edition is continuing through the entire frozen corpus.

Source authority: [Open Logic Project](https://github.com/OpenLogicProject/OpenLogic), revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. `upstream/` preserves the pristine English archive, including all 722 content files and upstream/component licenses. `bn-Beng-IN/content/` contains source-aligned translations. English files in `upstream/` are **not** counted as translations.

International programme: [OpenLogic translations hub](https://github.com/KokunoYumeto/OpenLogic-translations). This edition links back to the hub; hub maintenance belongs to its programme coordinator.

## Evidence and review

West Bengal university mathematics is represented by NSOU's EMT-03 Bengali algebra/set-theory material. SCERT Tripura's Bengali Class XI mathematics workbook is a separately labelled regional witness. Official Suri Vidyasagar College philosophy readings provide university-level quantification terminology. See `evidence/` for source identities, page/image hashes, passage roles, provisional term decisions and actual consultation records. These witnesses inform Bengali usage; OpenLogic determines the mathematics. No Bangladesh source has silently replaced Indian Bengali evidence.

The canon PDFs and page images are local research copies and are **not redistributed**. Their original rights notices remain applicable. Citation records and short terminology observations do not imply an open license for those third-party works.

Review is automated/model-based. No independent human review is claimed or required as a release gate. Current checks cover source/translation block alignment, formula skeletons, references, environments, identifiers, token parity, Unicode normalization, semantic comparisons and reverse-paraphrase samples. PDF build, glyph and visual checks are reported per release; the status file states the exact scope. Provisional terms remain explicitly marked.

## Build

Run `python tools/prepare_sets_print.py`, then `pwsh -File tools/build_sets_windows.ps1`. Requirements: Python 3, XeLaTeX/MiKTeX, fontspec, ucharclasses, standard AMS packages, TikZ, hyperref and Latin Modern Roman. Pinned Noto Serif Bengali fonts and their SIL Open Font License are in `fonts/`. The Windows builder acquires `Global\InterlanguageTeXSlotV1` before any TeX process, captures the process tree, disables shell escape/package installation, and holds the mutex across all passes and log checks.

The reader builder currently targets the completed Sets tranche. It includes OLP-0721 in context and does not pretend that a detached supplement or ordinary 642-file graph covers the full corpus. The remaining alternative wrappers and Proof Theory part will be integrated explicitly as their translations are completed.

## License

OpenLogic source and this translation: Creative Commons Attribution 4.0 International, with upstream attribution and component exceptions preserved. See `upstream/LICENSE.md` and the source component notices. Noto fonts: SIL Open Font License 1.1. Translation changes are identified by the `bn-Beng-IN/` directory and the machine-translation status above.
