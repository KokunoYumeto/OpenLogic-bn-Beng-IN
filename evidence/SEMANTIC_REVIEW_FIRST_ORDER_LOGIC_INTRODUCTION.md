# First-order Logic introduction semantic review (OLP-0138–OLP-0148)

Date: 2026-09-05
Locale: `bn-Beng-IN`
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`
Source manifest SHA-256: `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`

## Scope and result

This review covers the First-order Logic part driver and the complete introductory chapter: eleven source units from `first-order-logic.tex` through `soundness-completeness.tex`. The reviewed units contain 81 source blocks: 48 contain Bengali linguistic translation and 33 are unchanged structural or formal blocks. Every block has an exact source and target span in `SEGMENT_CANON_USE.jsonl`; canon pages are attributed only to translated blocks.

The batch passed a consolidated source-to-target replay after translation and repair. All eleven source and target block counts agree. Correction-stripped mathematical fragments, protected controls, environment order, OpenLogic semantic tokens and Unicode NFC agree under the exact transformations for `BN-SRC-083` through `BN-SRC-087`. Every finding is marked beside the repaired target passage, asserted by the checker and recorded in `SOURCE_CORRECTIONS.jsonl` with controlling frozen-source evidence.

The semantic reread also replaced `সঙ্গত পরিমাণসূচক` and `সঙ্গত সংঘটন` with `সংশ্লিষ্ট পরিমাণসূচক` and `অনুরূপ সংঘটন`. The earlier wording collided with the edition’s fixed root for logical consistency; the revised terms distinguish a matching quantifier from a corresponding syntactic occurrence. Decision `BN-IN-T097` records the distinction and alternatives.

This is a source-draft review. These units have not been added to the verified 18-unit reader, and no new PDF or semantic HTML result is claimed. Final printed and PDF page fields in the decision-occurrence ledger remain pending until reader integration and final pagination.

## Canon actually consulted

The following page images were visually reread during this chapter review. Index generation revalidates each image hash and the hash of its original document. These sources establish India-standard Bengali academic style and adjacent logic, quantifier, relation, variable, mapping, proof and finite/infinite-set language. They do not independently determine OpenLogic’s formal definitions or results; the frozen source and displayed definitions remain the mathematical authority.

| Passage | Page and role | Directly useful evidence | Page-image SHA-256 |
|---|---|---|---|
| `BN-IN-P008` | Tripura mathematics workbook, PDF/printed p. 153 | গাণিতিক যুক্তি, উক্তি, সংযোজক and negation prose | `6a78b10f84652623f444a8bac6a47d65a673c1a5f17b9a8bedc244fbb2d24a03` |
| `BN-IN-P009` | University philosophy scan, PDF p. 1 / printed pp. 110–111 | বচন, বচনাপেক্ষক, সার্বিক পরিমাণন and variable language | `2aa0305e562e80fb943a633e56440c27c7112e64c730e5d6fbd4dbb60289c35b` |
| `BN-IN-P010` | University philosophy scan, PDF p. 2 / printed pp. 112–113 | অস্তিত্বমূলক পরিমাণন, পরিসর and quantified negation | `e0aa05aae6b6cc5d15766cff6b5c3b34b5377c2fdf9c5de9cd9ca43be835312f` |
| `BN-IN-P013` | NSOU university mathematics, PDF p. 365 / printed p. 360 | সম্পর্ক, প্রতিবিম্ব and পরিযায়িতা roots | `f39f21f21052c188341ecdbbe2cb546540553986d65b85dd0ff409a450d8f96d` |
| `BN-IN-P019` | West Bengal school mathematics, PDF p. 189 / printed p. 10 | চল, ধ্রুবক and mathematical-expression prose | `c55d1f090e29adaf5053e21ad875b0c0e01c5d94f24afba0f9b6fad04da80c00` |
| `BN-IN-P020` | West Bengal school mathematics, PDF p. 227 / printed p. 48 | equality-operation and উভয় পক্ষ prose | `ce52122e599ab1e77d530449dd436ea3d07d3a769f3ea7a53df61783e4faf009` |
| `BN-IN-P023` | NSOU university mathematics, PDF p. 371 / printed p. 366 | mapping, domain/codomain, bijection and identity-map language | `adcd9898538fe4d9015062edc664142f460e0e9e27aa4952b15eec36b413f0f2` |
| `BN-IN-P025` | NSOU university mathematics, PDF p. 373 / printed p. 368 | Bengali proof flow, theorem structure and uniqueness language | `8ee57cf1055fa586c9c95fc4f5dd67e0e806f49ddec21f22967ef1f4bd374556` |
| `BN-IN-P027` | NSOU university mathematics, PDF p. 324 / printed p. 319 | সসীম সেট, অসীম সেট and empty-set distinctions | `74f9f4ec28833932ff66e625febe150affa52896a5e202179255c8cd52e8658e` |
| `BN-IN-P028` | NSOU university mathematics, PDF p. 325 / printed p. 320 | finite cardinality, set-size examples and empty-set cardinality | `0e2aee7c091db5be3edfd99b16db531fefb078d88d099343e773684d5da639bb` |

Existing decisions for first-order logic, proof systems, semantics, countability and model theory continue to govern this chapter. New decisions `BN-IN-T096` through `BN-IN-T100` record formal-language and expression vocabulary; terms, formulas, sentences and variable occurrences; structures, domains, interpretations, assignments and satisfaction; substitution and instantiation; and models, theories, axiomatic characterization and expressibility. The checked pages directly support several component roots and the academic register; every unattested full compound remains explicitly provisional, carries plausible alternatives and is open to expert correction.

## Unit-by-unit comparison and reverse paraphrase

The reverse paraphrases below were made from the Bengali targets and checked against the frozen English units. They sample every unit and each major semantic function. The segment index supplies complete block-level coverage.

| Unit | Blocks (translated) | Sample | Reverse paraphrase and judgment |
|---|---:|---|---|
| `OLP-0138` | 15 (3) | `B001–B015` | The part driver names First-order Logic, explains how FOL-tagged source material is reused for propositional logic, preserves every proof-system tag guard and imports introduction, syntax, semantics, models, proof systems, completeness and later material in source order. |
| `OLP-0139` | 11 (1) | `B001–B011` | The chapter driver names the introduction and imports all nine sections in exact source order, followed by the chapter hook. No section is duplicated or omitted. |
| `OLP-0140` | 6 (5) | `B002–B006` | First-order logic is presented as a formal language of terms, formulas and sentences. Structures and satisfaction make cases and truth-in-a-case precise; derivation systems manipulate symbols, and a metalogical proof must connect derivability with entailment. The ants-and-insects example retains two premises and one conclusion. `BN-SRC-083` and `BN-SRC-084` balance five malformed quantified formulas without changing their logical content. |
| `OLP-0141` | 4 (3) | `B002–B004` | The vocabulary divides into nonlogical symbols used to designate objects or predicate of them and logical connectives and quantifiers. The discussion asks which strings count as sentences, how to prove claims about all of them and how substitution should treat bound variables. Every example and nesting question is retained. |
| `OLP-0142` | 11 (9) | `B002–B011` | Formulas are introduced before sentences so free and bound variables can be defined. The simplified language has one predicate, one constant, infinitely many variables and selected connectives. Atomic formulas form the base; negation, conjunction and existential quantification form new formulas; nothing else qualifies. Structural induction follows those exact constructors. |
| `OLP-0143` | 7 (6) | `B002–B007` | A structure supplies a nonempty domain, the object denoted by the constant and the extension of the predicate. Satisfaction is defined recursively, then relativized to a total variable assignment. Existential satisfaction uses an assignment modified only at the quantified variable. The example domain and extensions yield the stated truth values. `BN-SRC-085` restores predicates as the symbols with arity, and `BN-SRC-086` restores assignment values 0, 1 and 2 to the declared domain. |
| `OLP-0144` | 6 (4) | `B002–B006` | A quantifier binds occurrences of its variable within its scope. Formula occurrences without a matching quantifier are free; a sentence is exactly a formula with no free variable occurrences. The four recursive cases for atomic formulas, negation, conjunction and existential quantification preserve the correspondence of token occurrences. |
| `OLP-0145` | 5 (4) | `B002–B005` | Satisfaction of a sentence is independent of variable assignments because sentences have no free occurrences. Validity quantifies over every structure, entailment over every structure satisfying the premises, and satisfiability requires one structure satisfying all members simultaneously. The Bengali keeps these three quantifier patterns distinct. |
| `OLP-0146` | 4 (3) | `B002–B004` | Universal instantiation motivates a precise, binding-sensitive substitution operation. An admissible term instance must preserve the relation between syntactic substitution and satisfaction under an assignment modified to the term’s value. `BN-SRC-087` restores the missing argument of the opening quantified atom. |
| `OLP-0147` | 5 (4) | `B002–B005` | A model of a sentence set satisfies every member. Model theory studies models of theories and sentences true in structures; the axiomatic method characterizes classes through sentence sets. The preorder example encodes reflexivity and transitivity. The final paragraph distinguishes what first-order languages can say about exact finite sizes and infinitude from what they cannot characterize about finitude or nonenumerability. |
| `OLP-0148` | 7 (6) | `B002–B007` | Derivation systems define syntactic derivability. Soundness is the direction from derivability to entailment; completeness is the converse. Together they identify consistent sets with satisfiable sets having models and yield compactness and Löwenheim–Skolem consequences. The historical conclusion retains the applications to logic, computer science and linguistics. |

## Source findings resolved in this chapter

| Finding | Unit | Target action | Exact validation |
|---|---|---|---|
| `BN-SRC-083` | `OLP-0140` | Closed the universal premise before the comma and removed the surplus closing bracket after the existential conclusion. | Exact one-for-one entailment-formula counter transformation asserted. |
| `BN-SRC-084` | `OLP-0140` | Closed two universal premises at their own scopes and removed two surplus brackets from existential conclusions. | Exact multiplicity-aware four-formula counter transformation asserted. |
| `BN-SRC-085` | `OLP-0143` | Replaced constants with predicates as the symbols that may have more than one place. | Exact prose assertion and one-token constant-to-predicate transformation asserted. |
| `BN-SRC-086` | `OLP-0143` | Replaced the out-of-domain value 3 with the declared domain member 0. | Exact one-numeral counter transformation plus declared-domain prose context asserted. |
| `BN-SRC-087` | `OLP-0146` | Placed `v_0` inside the predicate atom as its argument. | Exact one-for-one malformed-to-well-formed formula transformation asserted. |

## Variety, script, register, notation and numeral assessment

One `bn-Beng-IN` edition remains appropriate for the current scope. It uses Bengali script and normalized modern India-standard university Bengali orthography. The Tripura and West Bengal school pages provide regional and explanatory witnesses; NSOU and the university philosophy scan anchor higher-education mathematical and logical prose. Directly witnessed variants remain recorded as alternatives rather than being mixed without notice.

Formal notation preserves the frozen source’s formula order, left-to-right mathematical direction, Latin metavariables, Arabic indices, logical symbols, labels and OpenLogic macros except for the five documented source repairs. Ordinary Bengali prose may use Bengali digits where idiomatic, while mathematical expressions and identifiers retain source Arabic numerals. The current evidence does not justify separate script, orthographic, numeral, notation or regional editions. No variant has been introduced. If later evidence supports another edition, its locale and name will be coordinated with the OpenLogic Internationalization Manager before creation.

## Retrospective expert-review index

The regenerated `TRANSLATION_DECISION_LOG.md` covers all 100 current substantive decisions across the entire 147-unit draft, not only this chapter. Every record includes the source concept, chosen Bengali, rationale, plausible alternatives, confidence, a clear expert-review-welcome flag, representative exact frozen-source wording, every matching target occurrence mapped to stable unit and source/target line spans, and pending final reader-page fields. `TRANSLATION_DECISION_OCCURRENCES.csv` is the exhaustive occurrence view; `TRANSLATION_DECISION_INDEX.json` is the machine-readable companion. Absence of external expert response is never a production hold: uncertain terms remain reversible, provisional and open to correction.

## Semantic conclusions and remaining gates

The translation preserves the distinction among expression, formula and sentence; between free and bound variable occurrences; and among structures, assignments and satisfaction. It keeps the quantifier patterns for validity, entailment and satisfiability separate, states the syntactic and semantic sides of soundness and completeness in the correct directions, and retains the model-theoretic limits on expressing finitude and nonenumerability.

The remaining gates for these units are reader integration, a mutex-guarded TeX build, visual PDF inspection, semantic-HTML verification and pagination backfill in the occurrence ledger. Those gates remain separate from this completed source-draft semantic review.
