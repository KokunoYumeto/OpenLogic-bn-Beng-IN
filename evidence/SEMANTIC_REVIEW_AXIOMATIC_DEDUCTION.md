# Axiomatic Deduction semantic review (OLP-0112–OLP-0125)

Date: 2026-09-05
Locale: `bn-Beng-IN`
Frozen source revision: `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`
Source manifest SHA-256: `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`

## Scope and result

This review covers the complete reader-reachable Axiomatic Deduction chapter, fourteen source units from `axiomatic-deduction.tex` through `identity.tex`. The detached source unit `axiomatic-deduction/provability.tex` is not imported by this chapter driver and is outside this checkpoint. The reviewed units contain 149 source blocks: 122 contain Bengali linguistic translation and 27 are unchanged structural or formal blocks. Every block has an exact source and target span in `SEGMENT_CANON_USE.jsonl`; canon pages are attributed only to translated blocks.

The chapter passed a consolidated source-to-target replay after translation and repair. All fourteen source and target block counts agree. Correction-stripped mathematical fragments, protected controls, environment order, OpenLogic semantic tokens and Unicode NFC agree under the exact transformations for `BN-SRC-058` through `BN-SRC-069`. Every finding is marked beside the repaired target passage, asserted by the checker and recorded in `SOURCE_CORRECTIONS.jsonl`.

This is a source-draft review. These units have not been added to the 18-unit public reader, and no new PDF or semantic HTML result is claimed. Final printed and PDF page fields in the decision-occurrence ledger remain pending until reader integration and final pagination.

## Canon actually consulted

The following page images were visually reread during this chapter review. Index generation revalidates each image hash and the hash of its original document. These sources establish India-standard Bengali academic style and adjacent logic, quantifier, relation, equality and proof language. They do not independently determine OpenLogic’s formal results; the frozen source and displayed definitions remain the mathematical authority.

| Passage | Page and role | Directly useful evidence | Page-image SHA-256 |
|---|---|---|---|
| `BN-IN-P008` | Tripura mathematics workbook, PDF/printed p. 153 | গাণিতিক যুক্তি, উক্তি, যৌগিক উক্তি, সংযোজক and negation prose | `6a78b10f84652623f444a8bac6a47d65a673c1a5f17b9a8bedc244fbb2d24a03` |
| `BN-IN-P009` | University philosophy scan, PDF p. 1 / printed pp. 110–111 | বচন, বচনাপেক্ষক, সার্বিক পরিমাণন and variable language | `2aa0305e562e80fb943a633e56440c27c7112e64c730e5d6fbd4dbb60289c35b` |
| `BN-IN-P010` | University philosophy scan, PDF p. 2 / printed pp. 112–113 | অস্তিত্বমূলক পরিমাণন, পরিসর and quantified negation | `e0aa05aae6b6cc5d15766cff6b5c3b34b5377c2fdf9c5de9cd9ca43be835312f` |
| `BN-IN-P013` | University mathematics, PDF p. 365 / printed p. 360 | সম্পর্ক, প্রতিবিম্ব, প্রতিসাম্য and পরিযায়িতা roots | `f39f21f21052c188341ecdbbe2cb546540553986d65b85dd0ff409a450d8f96d` |
| `BN-IN-P020` | West Bengal mathematics, PDF p. 227 / printed p. 48 | সমান চিহ্ন, উভয় পক্ষ and equality-operation prose | `ce52122e599ab1e77d530449dd436ea3d07d3a769f3ea7a53df61783e4faf009` |
| `BN-IN-P025` | University mathematics, PDF p. 373 / printed p. 368 | Bengali proof flow, theorem/proof structure and uniqueness language | `8ee57cf1055fa586c9c95fc4f5dd67e0e806f49ddec21f22967ef1f4bd374556` |

Existing decisions `BN-IN-T068` through `BN-IN-T070`, `BN-IN-T081`, `BN-IN-T083` through `BN-IN-T085` govern derivation systems, soundness, axiomatic derivations, provability, quantifier metatheory and identity. New decision `BN-IN-T090` records `নিঃসরণ উপপাদ্য`, `অনুমিতি নিঃসরণ`, `স্বতঃসিদ্ধের রূপ` and the ordered operation `নিষ্পাদনগুলি পরপর বসানো`. The unqualified theorem name is syntactic because both sides use `Proves`; `BN-IN-T067` continues to reserve `অর্থগত নিঃসরণ উপপাদ্য` for the entailment theorem.

## Unit-by-unit comparison and reverse paraphrase

The reverse paraphrases below were made from the Bengali targets and checked against the frozen English units. They sample every unit and each major semantic function. The segment index supplies complete block-level coverage.

| Unit | Blocks (translated) | Sample | Reverse paraphrase and judgment |
|---|---:|---|---|
| `OLP-0112` | 16 (2) | `B001–B002` | The driver selects Axiomatic Deduction for propositional or first-order logic, explains the `prfAxD` switch and imports all thirteen chapter sections in source order. All structural imports and tag guards are unchanged. |
| `OLP-0113` | 9 (8) | `B002–B009` | An axiomatic derivation is a finite formula sequence in which each line is a premise, an axiom instance or follows from earlier lines by a rule. Modus ponens derives `A` from earlier `B` and `B conditional A`. Derivability means that a derivation from `Gamma` ends in the formula; a theorem is derivable without premises. The Bengali keeps a sequence rather than recasting the object as a tree. |
| `OLP-0114` | 5 (4) | `B002–B005` | The propositional system contains the displayed schemas for conjunction, disjunction, conditional, negation, truth, falsity and double-negation elimination. Its sole inference rule is modus ponens. Every schema variable, grouping, label and premise order agrees with the source. |
| `OLP-0115` | 5 (4) | `B002–B005` | Universal instantiation and existential generalization are admitted when the term is free for the quantified variable. The two QR directions move from a conditional containing a fresh constant to the corresponding universal or existential conditional. The constant-exclusion conditions and both formula orientations are retained. |
| `OLP-0116` | 9 (8) | `B002–B009` | The worked examples first derive `D conditional D`, then derive `A conditional C` from `A conditional B` and `B conditional C`. The exploratory dead ends, each axiom instance, line justification and final seven-line construction remain explicit. The general proposition concatenates two premise derivations before appending the same chain. |
| `OLP-0117` | 4 (3) | `B002–B004` | From the two universal conjunct premises, instantiate each at the fresh constant, combine the instances by the conjunction axiom and modus ponens, then use QR to infer the universal conjunction. All intermediate formulas and the freshness-dependent last step are preserved. |
| `OLP-0118` | 19 (18) | `B002–B019` | Derivability, theoremhood and consistency are syntactic notions. Reflexivity, monotonicity and transitivity manipulate premise sets and derivation sequences; inconsistency is equivalent to deriving every formula; compactness extracts the finitely many premises actually used. `BN-SRC-058` restores `!B_i`; `BN-SRC-059` lets the compactness proof cover both modus ponens and the FOL QR rule; `BN-SRC-070` lets a repeated formula inherit any of the three licensed justification types. |
| `OLP-0119` | 16 (15) | `B002–B016` | Meta-level modus ponens follows by a three-line derivation and transitivity. The deduction theorem says `Gamma` plus `A` proves `B` exactly when `Gamma` proves `A conditional B`. The difficult direction proceeds by derivation length, treating premise/axiom lines and modus-ponens conclusions separately. All five later derivability facts and tag-dependent problems are retained. `BN-SRC-060` closes one malformed exercise formula. |
| `OLP-0120` | 8 (7) | `B002–B008` | The first-order deduction theorem needs an extra induction case for QR. When the last line is `C conditional forall x D(x)`, freshness survives moving `A` into the antecedent; the aligned argument derives `A conditional (C conditional forall x D(x))`. The existential QR form remains an exercise. `BN-SRC-061` balances the curried conditional, and `BN-SRC-062` restores the required `A conditional B` summary. |
| `OLP-0121` | 15 (14) | `B002–B015` | Deriving `A` is equivalent to becoming inconsistent after adding `not A`; derivability from a premise set is equivalent to inconsistency after adjoining the negated conclusion. Explicit `A` and `not A` yield inconsistency, and the tagged classical result gives derivability of a formula or its negation. Each direction, premise-set change and exercise is preserved. |
| `OLP-0122` | 10 (9) | `B002–B010` | The expected conjunction, disjunction and conditional provability equivalences are established from the axiom schemas and meta-level modus ponens. `BN-SRC-063` changes the second conjunction projection citation to `ax:land2`; `BN-SRC-064` identifies `not A conditional (A conditional false)` as `ax:lnot2`. No displayed formula changes. |
| `OLP-0123` | 8 (7) | `B002–B008` | Strong generalization turns a derivation of `A(c)` into one of `forall x A(x)` when the constant is absent from the premise set and open formula. It then supplies the universal and existential provability facts. `BN-SRC-065` keeps configurable `ltrue`; `BN-SRC-071` uses the truth axiom plus modus ponens for the last step; `BN-SRC-072` restores the closed-term scope imposed by the two quantified axioms. |
| `OLP-0124` | 15 (14) | `B002–B015` | Every axiom instance is semantically valid, and derivability entails semantic consequence. The induction handles zero inference-supported steps, modus ponens and the FOL QR case; the latter modifies a structure’s interpretation of the fresh constant and transfers satisfaction through substitution. Weak soundness and consistency follow. `BN-SRC-067` names the induction measure actually used, while `BN-SRC-068` and `BN-SRC-069` restore three omitted formula prefixes. |
| `OLP-0125` | 10 (9) | `B002–B010` | Identity adds reflexivity and substitutability axiom schemas for closed terms while leaving the derivation definition unchanged. The schemas are valid, every closed term proves self-identity, and two modus-ponens applications transport `A(t_1)` across `t_1=t_2`. `BN-SRC-066` keeps both propositions within the closed-term range licensed by the displayed schemas. |

## Source findings resolved in this chapter

| Finding | Unit | Target action | Exact validation |
|---|---|---|---|
| `BN-SRC-058` | `OLP-0118` | Restored `!` on the final `B_i` occurrence. | Exact one-for-one formula transformation asserted. |
| `BN-SRC-059` | `OLP-0118` | Replaced the modus-ponens-only compactness claim with all permitted inference rules and preserved finite support/freshness. | Frozen and corrected prose asserted. |
| `BN-SRC-060` | `OLP-0119` | Added the missing outer right parenthesis. | Exact one-for-one formula transformation asserted. |
| `BN-SRC-061` | `OLP-0120` | Added the missing outer right parenthesis in the quantified theorem formula. | Exact one-for-one align-fragment transformation asserted. |
| `BN-SRC-062` | `OLP-0120` | Restored `Gamma proves A conditional B` after the display. | Exact one-for-one formula and prose transformation asserted. |
| `BN-SRC-063` | `OLP-0122` | Changed the second projection reference from `ax:land1` to `ax:land2`. | Exact control-command multiset transformation asserted. |
| `BN-SRC-064` | `OLP-0122` | Changed the negation reference from `ax:lnot1` to `ax:lnot2`. | Exact control-command multiset transformation asserted. |
| `BN-SRC-065` | `OLP-0123` | Replaced raw `top` with configurable `ltrue`. | Exact one-for-one formula transformation asserted. |
| `BN-SRC-066` | `OLP-0125` | Restricted both identity consequences to closed terms. | Governing source clause and both target qualifications asserted. |
| `BN-SRC-067` | `OLP-0124` | Changed the induction measure to inference-justified step count. | Frozen opening and corrected target measure asserted. |
| `BN-SRC-068` | `OLP-0124` | Restored `!` in two universal formulas. | Exact two-occurrence formula transformation asserted. |
| `BN-SRC-069` | `OLP-0124` | Restored `!` in satisfaction of `B(c)`. | Exact one-for-one formula transformation asserted. |
| `BN-SRC-070` | `OLP-0118` | Replaced “same rule” with the same axiom, premise or inference justification basis. | Frozen and corrected prose asserted against the three-category derivation definition. |
| `BN-SRC-071` | `OLP-0123` | Replaced the wrong final deduction-theorem attribution with the truth axiom and modus ponens. | Frozen and corrected inference prose asserted. |
| `BN-SRC-072` | `OLP-0123` | Restricted both elementary quantified consequences to a closed term. | Governing axiom scope and shared target qualification asserted. |

## Variety, script, register and notation assessment

One `bn-Beng-IN` edition remains appropriate. It uses Bengali script and a normalized India-standard academic register, with the checked Tripura, West Bengal and university pages supplying regional evidence. Recorded alternatives remain reviewable rather than generating parallel builds: `প্রকৃত/যথার্থ উপসেট`, `নঞর্থকরণ/না-ক্রিয়া`, `সংকোচন/সঙ্কোচন`, and technical loans such as `ডিডাকশন উপপাদ্য` versus the selected `নিঃসরণ উপপাদ্য` stay in the decision evidence.

Formal notation remains source-identical except for the twelve documented repairs. Latin metavariables, Arabic line numbers, logical symbols and OpenLogic macros are retained because they belong to the formal system, not to a competing Bengali-script or numeral edition. No parallel script, numeral, notation or register build is justified by the present canon. A Bangladesh-standard Bengali edition would require its own canon-backed regional terminology review; it may share build infrastructure but should not inherit this edition’s choices silently.

## Semantic conclusions and remaining gates

The translation keeps axiom instances distinct from inference-rule applications, premise membership distinct from theoremhood, and derivability distinct from semantic entailment. It preserves the syntactic deduction theorem’s direction and keeps its name distinct from the semantic deduction theorem. Quantifier-rule freshness, finite support in compactness, the soundness induction measure and the closed-term scope of identity axioms are explicit.

The remaining gates for these units are reader integration, a mutex-guarded TeX build, visual PDF inspection, semantic-HTML verification and pagination backfill in the occurrence ledger. Those gates remain separate from this completed source-draft semantic review.
