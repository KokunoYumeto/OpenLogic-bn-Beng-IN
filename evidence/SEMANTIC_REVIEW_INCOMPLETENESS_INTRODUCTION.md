# Semantic review: Incompleteness introduction

Review date: 2026-09-09

Locale: `bn-Beng-IN`

Units: OLP-0274--OLP-0279
Scope: 92 aligned source/target blocks across the Incompleteness part driver, Introduction chapter driver, and the four Introduction sections.

This review records the semantic pass completed before reader integration. The Bengali text was read against the frozen English blocks in source order, then paraphrased back into English at the level of definitions, theorem hypotheses, proof direction and exercise request. Source and target alignment passed for every block: block counts, formula fragments, control sequences, environments, semantic tokens and Unicode NFC all match the checked policy. The six target files are currently draft source files; TeX/PDF rendering and final reader pagination remain pending.

## Unit coverage

| Unit | File or role | Blocks | Review focus |
|---|---|---:|---|
| OLP-0274 | Incompleteness part driver | 8 | Part identity, provenance note, five imported chapters |
| OLP-0275 | Introduction chapter driver | 6 | Chapter identity and four imported sections |
| OLP-0276 | Historical background | 19 | Logic and foundations history, Hilbert programme, Gödel context |
| OLP-0277 | Definitions | 32 | Theories, standard model, Q, PA, induction schemas, decidability and axiomatizability |
| OLP-0278 | Overview | 9 | First/second incompleteness roadmap, Gödel sentence, arithmetization and provability predicate |
| OLP-0279 | Undecidability | 18 | Diagonal set, representation contradiction, complete axiomatizable theories and Presburger contrast |

## Source-level corrections carried into the Bengali draft

The following seven corrections are documented in `SOURCE_CORRECTIONS.jsonl` and marked adjacent to the affected target passages. Their correction notes are excluded from source formula parity.

* **BN-SRC-198 (OLP-0276):** the transition after the numbered historical aims now says “another aim,” avoiding a false “second aim” label.
* **BN-SRC-199 (OLP-0276):** the historical summary attaches effective axiomatization, consistency and sufficient strength to the relevant Gödel results and states the second-theorem conclusion with the correct scope.
* **BN-SRC-200 (OLP-0277):** the relation-representability definition explicitly says that representation is in the given theory, matching the theory-relative proof clauses.
* **BN-SRC-204 (OLP-0277):** the final induction-schema exercise restores the second `$!B$` in the mismatch alternative.
* **BN-SRC-201 (OLP-0278):** the roadmap describes recursive functions as a later logical dependency, so it does not contradict the physical import order of the chapters.
* **BN-SRC-202 (OLP-0278):** both audited provability-predicate occurrences use the object-language `\OProv[\Gamma]`, rather than the metalanguage `\Prov[\Gamma]`.
* **BN-SRC-203 (OLP-0279):** both diagonal occurrences retain the family subscript, `$!A_n(\num{n})$`, so the set definition refers to the enumerated n-th formula.

## Reverse-paraphrase checks

1. **Historical background:** the Bengali passage presents the historical aims and then narrows the incompleteness claims to the theories whose effectiveness, consistency and strength are established later. It does not turn the historical summary into a universal claim about every axiomatic system.
2. **Definitions:** “theory” remains closure under entailment; the standard model and true arithmetic remain semantic constructions; Q and PA remain axiomatic presentations; the induction-schema exercise still asks the reader to recover the quantified formula and distinguish the matching and nonmatching cases.
3. **Overview:** the first theorem is stated for a consistent, axiomatizable theory representing the relevant computable functions and decidable relations. “Independent” still means that neither a sentence nor its negation is provable. The Gödel sentence construction and the object-language provability predicate remain separate levels of description.
4. **Undecidability:** the enumerated family `A_0,A_1,\ldots` is used to define the diagonal set, the representation assumption supplies the index `d`, and the two cases yield the contradiction. The later complete-plus-axiomatizable decidability result and the Presburger counterexample retain their distinct roles.

## Terminology register

The five new terminology decisions BN-IN-T229, BN-IN-T230, BN-IN-T231, BN-IN-T232 and BN-IN-T233 cover the historical, theory, arithmetic, decidability and Gödel-sentence vocabulary used by these units. They are provisional India-standard Bengali decisions, linked to the checked canon passages and included in the regenerated decision log. Exact target occurrences and source block hashes are recorded there; correction-note prose is excluded from occurrence counts.

## Remaining validation

The source checker and draft alignment checks pass. The next release gate is the durable 278-unit verifier, followed by the public commit and anonymous archive readback. A TeX build, PDF render and reader visual review have not yet been run for this batch and are intentionally recorded as pending rather than inferred from source alignment.
