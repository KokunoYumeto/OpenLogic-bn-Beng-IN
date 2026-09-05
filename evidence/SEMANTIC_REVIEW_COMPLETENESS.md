# Completeness semantic review (OLP-0126–OLP-0137)

Date: 2026-09-05
Locale: `bn-Beng-IN`
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`
Source manifest SHA-256: `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`

## Scope and result

This review covers the complete reader-reachable Completeness chapter, twelve source units from `completeness.tex` through `downward-ls.tex`. The reviewed units contain 178 source blocks: 153 contain Bengali linguistic translation and 25 are unchanged structural or formal blocks. Every block has an exact source and target span in `SEGMENT_CANON_USE.jsonl`; canon pages are attributed only to translated blocks.

The chapter passed a consolidated source-to-target replay after translation and repair. All twelve source and target block counts agree. Correction-stripped mathematical fragments, protected controls, environment order, OpenLogic semantic tokens and Unicode NFC agree under the exact transformations for `BN-SRC-073` through `BN-SRC-082`. Every finding is marked beside the repaired target passage, asserted by the checker and recorded in `SOURCE_CORRECTIONS.jsonl`.

This is a source-draft review. These units have not been added to the 18-unit public reader, and no new PDF or semantic HTML result is claimed. Final printed and PDF page fields in the decision-occurrence ledger remain pending until reader integration and final pagination.

## Canon actually consulted

The following page images were visually reread during this chapter review. Index generation revalidates each image hash and the hash of its original document. These sources establish India-standard Bengali academic style and adjacent logic, quantifier, relation, equivalence-class, equality, mapping, proof and finite/infinite-set language. They do not independently determine OpenLogic’s formal results; the frozen source and displayed definitions remain the mathematical authority.

| Passage | Page and role | Directly useful evidence | Page-image SHA-256 |
|---|---|---|---|
| `BN-IN-P008` | Tripura mathematics workbook, PDF/printed p. 153 | গাণিতিক যুক্তি, উক্তি, যৌগিক উক্তি, সংযোজক and negation prose | `6a78b10f84652623f444a8bac6a47d65a673c1a5f17b9a8bedc244fbb2d24a03` |
| `BN-IN-P009` | University philosophy scan, PDF p. 1 / printed pp. 110–111 | বচন, বচনাপেক্ষক, সার্বিক পরিমাণন and variable language | `2aa0305e562e80fb943a633e56440c27c7112e64c730e5d6fbd4dbb60289c35b` |
| `BN-IN-P010` | University philosophy scan, PDF p. 2 / printed pp. 112–113 | অস্তিত্বমূলক পরিমাণন, পরিসর and quantified negation | `e0aa05aae6b6cc5d15766cff6b5c3b34b5377c2fdf9c5de9cd9ca43be835312f` |
| `BN-IN-P013` | University mathematics, PDF p. 365 / printed p. 360 | সম্পর্ক, প্রতিবিম্ব, প্রতিসাম্য and পরিযায়িতা roots | `f39f21f21052c188341ecdbbe2cb546540553986d65b85dd0ff409a450d8f96d` |
| `BN-IN-P015` | University mathematics, PDF p. 367 / printed p. 362 | তুল্যতা শ্রেণী, representatives and congruence example | `fb23f76e1dcd489a4df95cc4d0b5bd5d6b165ba7b7c26f032bcad928f359c218` |
| `BN-IN-P016` | University mathematics, PDF p. 368 / printed p. 363 | equality of equivalence classes, বিভাজন and proof flow | `9cede4af079bee09ea5a9cb3186ccb3eeb8803c7c8bccae89b717768ed7d617a` |
| `BN-IN-P020` | West Bengal mathematics, PDF p. 227 / printed p. 48 | সমান চিহ্ন, উভয় পক্ষ and equality-operation prose | `ce52122e599ab1e77d530449dd436ea3d07d3a769f3ea7a53df61783e4faf009` |
| `BN-IN-P023` | University mathematics, PDF p. 371 / printed p. 366 | mapping, domain/codomain, bijection and identity-map language | `adcd9898538fe4d9015062edc664142f460e0e9e27aa4952b15eec36b413f0f2` |
| `BN-IN-P025` | University mathematics, PDF p. 373 / printed p. 368 | Bengali proof flow, theorem structure and uniqueness language | `8ee57cf1055fa586c9c95fc4f5dd67e0e806f49ddec21f22967ef1f4bd374556` |
| `BN-IN-P027` | University mathematics, PDF p. 324 / printed p. 319 | সসীম সেট, অসীম সেট, empty-set distinctions and examples | `74f9f4ec28833932ff66e625febe150affa52896a5e202179255c8cd52e8658e` |
| `BN-IN-P028` | University mathematics, PDF p. 325 / printed p. 320 | finite cardinality, set-size examples and empty-set cardinality | `0e2aee7c091db5be3edfd99b16db531fefb078d88d099343e773684d5da639bb` |

Existing decisions `BN-IN-T033`, `BN-IN-T040`, `BN-IN-T049`, `BN-IN-T063`, `BN-IN-T069`, `BN-IN-T081` and `BN-IN-T090` continue to govern completeness, countability, representative independence, denumerability, soundness/consistency, compactness and syntactic proof vocabulary. New decisions `BN-IN-T091` through `BN-IN-T095` record the chapter-specific register: complete consistent theories and decidability; Henkin expansion and saturation; term models, the Truth Lemma and quotient construction; finite satisfiability and compactness applications; and the Löwenheim–Skolem/Skolem-paradox vocabulary. The checked pages directly support component roots and academic style; the full model-theoretic compounds remain explicitly provisional where they are not directly attested.

## Unit-by-unit comparison and reverse paraphrase

The reverse paraphrases below were made from the Bengali targets and checked against the frozen English units. They sample every unit and each major semantic function. The segment index supplies complete block-level coverage.

| Unit | Blocks (translated) | Sample | Reverse paraphrase and judgment |
|---|---:|---|---|
| `OLP-0126` | 13 (1) | `B001–B013` | The driver names the Completeness chapter and imports introduction, outline, complete consistent sets, Henkin expansions, Lindenbaum’s lemma, model construction, identity, the theorem, two compactness treatments and Löwenheim–Skolem in source order. All file identities, imports and tag guards are unchanged. |
| `OLP-0127` | 6 (5) | `B002–B006` | Soundness gives derivability only when there is semantic consequence; completeness supplies the converse. The proof must build a model from consistency and cannot merely inspect finitely many formulas. The Bengali preserves the historical theorem, the difference between the weak and strong forms and the later extensions to compactness and countable models. |
| `OLP-0128` | 12 (11) | `B002–B012` | The outline extends a consistent set first to a saturated set and then to a complete consistent set. It constructs a term model, or a valuation in the propositional branch, so that a sentence is true exactly when it belongs to the completed set. Identity requires quotienting the term model. Each step, counterfactual explanation and tag-dependent branch is retained. |
| `OLP-0129` | 22 (21) | `B002–B022` | A sentence set is complete when it contains each sentence or its negation. For a complete consistent set, derivability is equivalent to membership and the expected connective membership conditions follow. A complete axiomatizable theory is decidable by searching for a proof of a sentence or its negation. The Bengali keeps semantic completeness distinct from proof-system completeness and retains every biconditional. |
| `OLP-0130` | 19 (18) | `B002–B019` | A Henkin expansion adds fresh constants so that every existential member has a witness, or every false universal has a counterexample in the alternate configuration. The stagewise construction preserves consistency and yields saturation; complete, consistent, saturated sets then contain quantified sentences exactly when they contain the required closed-term instances. `BN-SRC-073` restores the missing `x_n` argument, and `BN-SRC-074` assigns the existential explanation to `prvEx`. |
| `OLP-0131` | 9 (8) | `B002–B009` | Lindenbaum’s lemma enumerates all sentences and adds either each sentence or its negation while preserving consistency. Earlier stages remain subsets of later ones. Every finite subset of the union lies in a consistent stage, so the union is consistent, and the enumeration makes it complete. `BN-SRC-075` handles the empty finite subset before selecting a greatest stage index. |
| `OLP-0132` | 26 (21) | `B002–B026` | The term model uses closed terms as its domain, interprets constants and functions by term formation and predicates by membership in the complete set. Every domain element is named by a closed term, which turns quantifier satisfaction into quantification over closed terms. The Truth Lemma proves by formula induction that truth in the model is equivalent to membership. `BN-SRC-076` and `BN-SRC-077` restore closed-term scope; `BN-SRC-078` restores `B(x)` in the universal case. |
| `OLP-0133` | 17 (17) | `B001–B017` | With identity, provable equality on closed terms is an equivalence relation compatible with functions and predicates. The construction factors the term model into equivalence classes, proves independence from representatives and recovers the value and Truth Lemmas in the quotient. `BN-SRC-079` removes a duplicate argument comma, `BN-SRC-080` restores the alternative representative `t'`, and `BN-SRC-081` restores closed-term scope. |
| `OLP-0134` | 12 (11) | `B002–B012` | Every consistent premise set has a model: extend it to a saturated complete consistent set and use the term model, quotienting by provable identity when required. Hence semantic consequence and derivability coincide; validity and theoremhood coincide; consistency and satisfiability coincide. The proof directions and all FOL/PL and identity branches are retained. |
| `OLP-0135` | 14 (13) | `B002–B014` | Compactness says that a sentence set is satisfiable exactly when every finite subset is. Its consequence form extracts a finite premise subset. Applications produce a model with an infinitesimal element, a nonstandard model of arithmetic and the contrast that first-order logic can force infinitude but cannot characterize finitude. `BN-SRC-082` defines the finite-subfamily argument when the selected `Delta` part is empty. |
| `OLP-0136` | 21 (20) | `B002–B021` | The direct proof replaces consistency with finite satisfiability throughout the complete-set, Henkin, Lindenbaum and Truth Lemma construction. A complete finitely satisfiable set has the same connective membership behavior, the FOL branch supplies saturation and closed-term instances, and the constructed interpretation satisfies the original set. Every exercise and configuration branch is retained. |
| `OLP-0137` | 7 (7) | `B001–B007` | The Löwenheim–Skolem theorem follows because the completeness construction has no more domain elements than the language has closed terms. A consistent theory has a finite or countably infinite model; without identity, the term domain gives a countably infinite model. The Skolem-paradox example preserves the distinction between an externally countable model and sets that the model internally regards as uncountable. |

## Source findings resolved in this chapter

| Finding | Unit | Target action | Exact validation |
|---|---|---|---|
| `BN-SRC-073` | `OLP-0130` | Restored the bound argument in `A_n(x_n)`. | Exact one-for-one formula transformation asserted. |
| `BN-SRC-074` | `OLP-0130` | Changed the existential explanatory branch from `prvAll` to `prvEx`. | Exact source/target tag contexts asserted. |
| `BN-SRC-075` | `OLP-0131` | Discharged the empty finite-subset case before taking a largest index. | Frozen maximum claim and corrected case split asserted. |
| `BN-SRC-076` | `OLP-0132` | Restricted the term-model value lemma to closed terms. | Governing proof scope and target qualification asserted. |
| `BN-SRC-077` | `OLP-0132` | Restricted both quantified Truth Lemma cases to closed terms. | Both frozen overbroad clauses and both corrected cases asserted. |
| `BN-SRC-078` | `OLP-0132` | Replaced the stray universal `A(x)` with the governing `B(x)`. | Exact one-for-one formula transformation asserted. |
| `BN-SRC-079` | `OLP-0133` | Removed the duplicate comma in the function-term argument list. | Exact displayed-formula transformation asserted. |
| `BN-SRC-080` | `OLP-0133` | Used `R(t')` for the alternative representative. | Exact one-for-one formula transformation asserted. |
| `BN-SRC-081` | `OLP-0133` | Restricted the factored value lemma to closed terms. | Cited unfactored lemma and target qualification asserted. |
| `BN-SRC-082` | `OLP-0135` | Chose `n=1` when the finite `Delta` subfamily is empty and took a maximum only otherwise. | Frozen maximum claim and corrected case split asserted. |

## Variety, script, register and notation assessment

One `bn-Beng-IN` edition remains appropriate. It uses Bengali script and a normalized India-standard academic register, with the checked Tripura, West Bengal and university pages supplying regional evidence. Recorded alternatives remain reviewable rather than generating parallel builds. Technical names such as `হেনকিন`, `লিন্ডেনবাউম`, `লোয়েনহাইম--স্কোলেম`, and provisional compounds such as `সত্যতা-সহায়ক উপপাদ্য` and `সসীমভাবে পরিতৃপ্তিযোগ্য` are governed by explicit definitions and occurrence records.

Formal notation remains source-identical except for the four documented formula repairs and the one documented tag repair. Latin metavariables, Arabic indices, logical symbols and OpenLogic macros are retained because they belong to the formal system, not to a competing Bengali-script or numeral edition. No parallel script, numeral, notation or register build is justified by the present canon. A Bangladesh-standard Bengali edition would require its own canon-backed regional terminology review; it may share build infrastructure but should not inherit this edition’s choices silently.

## Semantic conclusions and remaining gates

The translation keeps proof-theoretic consistency distinct from semantic satisfiability and preserves the direction in which completeness supplies a model. It distinguishes completeness of a sentence set from completeness of a proof system, keeps saturation as a named-witness condition, restricts assignment-free term values and quantifier instances to closed terms, and preserves the representative-independence work needed for identity. The compactness applications retain the finite-subset quantifiers and the Löwenheim–Skolem example retains the internal/external model distinction.

The remaining gates for these units are reader integration, a mutex-guarded TeX build, visual PDF inspection, semantic-HTML verification and pagination backfill in the occurrence ledger. Those gates remain separate from this completed source-draft semantic review.
