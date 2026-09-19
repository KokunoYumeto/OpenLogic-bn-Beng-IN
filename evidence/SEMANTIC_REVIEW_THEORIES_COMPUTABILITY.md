# Semantic review: Theories and Computability

Review date: 2026-09-19

Locale: `bn-Beng-IN`

Units: OLP-0301--OLP-0311

Scope: 88 aligned source/target blocks across the chapter driver, theory introduction, c.e.-completeness of Q, omega-consistent and consistent extensions, effective axiomatization, complete theories, first incompleteness, computable inseparability, consistency with Q and interpretability. Of these, 66 blocks contain reviewed Bengali translation and 22 are unchanged structural or formal blocks.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of definitions, theorem hypotheses, reductions, proof searches, diagonal arguments, corollaries and language-signature claims. Every source/target pair passes block-count, audited-mathematics, control-sequence, environment, semantic-token and Unicode NFC checks. This is a source and semantic review by the primary translation model; no independent human review, TeX-engine result or PDF result is claimed.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index and correction-ledger generation revalidate the per-file source hashes before accepting these units.

## Unit coverage

| Unit | File or role | Blocks | Review focus |
|---|---|---:|---|
| OLP-0301 | Theories and Computability chapter driver | 13 | Chapter identity, editorial note and ten imported sections |
| OLP-0302 | Introduction | 5 | Theory closure, Robinson Q, formula coding and computability questions |
| OLP-0303 | Q is c.e.-complete | 6 | Proof enumeration, Kleene T representation, soundness and many-one reduction |
| OLP-0304 | Omega-consistent extensions | 6 | Omega-consistency definition, historical role and modified halting reduction |
| OLP-0305 | Consistent extensions | 11 | No-universal-relation diagonal, representability and true arithmetic |
| OLP-0306 | Computably axiomatizable theories | 6 | Computable axiom sets, positive proof recognition and c.e. deductive closure |
| OLP-0307 | Complete theories are decidable | 7 | Parallel proof search, consistency and complement enumeration |
| OLP-0308 | First incompleteness | 6 | Complete/consistent/effectively axiomatized tradeoff and historical comparison |
| OLP-0309 | Computable inseparability | 6 | Provable/refutable sets, separators and universal-relation contradiction |
| OLP-0310 | Theories consistent with Q | 11 | Deduction-theorem separator and arithmetic first-order-logic corollary |
| OLP-0311 | Interpretability | 11 | Interpretations, ZFC, signature thresholds and Presburger arithmetic |

## Source-level corrections carried into the Bengali draft

The following ten corrections are marked next to the affected target passages and recorded in `SOURCE_CORRECTIONS.jsonl`. Correction-note material is excluded from source parity and terminology occurrence counts.

* **BN-SRC-234 (OLP-0303):** the converse reduction proof no longer calls the represented false-case negation a false formula; it uses standard-model soundness to derive the contradiction between the representing instance and its negation.
* **BN-SRC-235 (OLP-0303):** the reduction outputs a sentence built with the object-language representing formula `!A_T`, rather than placing the meta-level Kleene relation `T` inside the sentence.
* **BN-SRC-236 (OLP-0305):** the meta-relation is evaluated at the natural number `n`; only the representing formula takes the object-language numeral `\num n`.
* **BN-SRC-237 (OLP-0305):** true arithmetic is defined with satisfaction in the standard arithmetic structure `N`, rather than putting the carrier set `\Nat` in the model slot.
* **BN-SRC-238 (OLP-0306):** unbounded derivation search is described as recognizing positive theorem membership; it is not claimed to decide nonmembership.
* **BN-SRC-239 (OLP-0307):** both parallel proof searches start from the computable axiom set `A`, the effective presentation supplied by the hypothesis.
* **BN-SRC-240 (OLP-0308):** the proof invokes the preceding lemma with the required `axiomatizable` hypothesis, rather than changing it to `axiomatized`.
* **BN-SRC-241 (OLP-0309):** the meta-relation uses number arguments and the universal relation receives the Gödel code `\Gn{!D_S(u)}` of the open representing formula.
* **BN-SRC-242 (OLP-0311):** the first ZFC corollary excludes consistent decidable extensions; an inconsistent extension remains a decidable counterexample to the unqualified frozen claim.
* **BN-SRC-243 (OLP-0311):** the Presburger claim locates truth in the standard model, because a formal language alone does not determine truth.

## Reverse-paraphrase checks

1. **Theory and effective theorem sets:** a theory is a sentence set closed under entailment. The chapter treats theorems through their codes, so computability applies to membership in that coded set rather than to an informal proof practice.
2. **c.e.-completeness of Q:** proofs from Q can be enumerated, making its theorem set c.e. Kleene’s primitive-recursive computation predicate is represented by `!A_T`; the standard-model soundness argument supplies the converse, and the resulting computable map sends each index to the code of an object-language existential sentence.
3. **Omega-consistency and ordinary consistency:** omega-consistency forbids proving an existential sentence while refuting every numeral instance. The first extension theorem uses that stronger condition; the next theorem replaces it with ordinary consistency by a universal-relation diagonal argument.
4. **No universal computable relation:** if a binary computable relation contained every unary computable relation as a fixed-index section, the diagonal relation `S(y)` equivalent to `not R(y,y)` would equal one of those sections and contradict itself at its own index. The representation proof preserves the distinction between natural-number arguments and numeral terms.
5. **Effective axiomatization and decidability:** a computable axiom set makes the deductive closure c.e. because proof search recognizes members. If the theory is also complete, parallel searches for a sentence and its negation terminate; consistency makes the result unambiguous. The repaired proof searches from the effective axiom set in both branches.
6. **First incompleteness:** no extension of Q is simultaneously complete, consistent and computably axiomatizable. The historical note keeps Gödel’s original omega-consistency condition distinct from the later consistency strengthening, and the three examples show that dropping any one property permits the other two.
7. **Computable inseparability and relative consistency:** the Q-theorems and Q-refutable sentences admit no computable separator. If a decidable theory were consistent with Q, the finite conjunction of Q’s axioms and the deduction theorem would construct exactly such a separator, so even the first-order consequence set of the empty theory in the arithmetic language is undecidable.
8. **Interpretability and signatures:** an interpretation defines one language’s domain, relations and functions in another. A theory consistent with the interpreted Q is undecidable; when it proves interpreted Q, every consistent extension is undecidable. The ZFC, binary-relation, two-unary-function and Presburger consequences retain their stated signature boundaries, with truth evaluated in the standard model.

## Terminology and authority scope

Decisions BN-IN-T251 through BN-IN-T259 record the chapter-level computability register, the consistency contrast, universal computable relations, effective axiomatization, complete theories, first incompleteness, computable inseparability, consistency with Q and interpretability/Presburger vocabulary. Earlier decisions continue to govern theory, decidability, many-one reduction, c.e.-completeness, representability, Robinson Q and omega-consistency. The linked canon pages support the surrounding India-standard Bengali number, statement, quantification, relation, function, variable, mapping and proof register. They do not directly attest every specialized compound or theorem name, so these choices remain provisional, definition-governed and open to expert correction.

## Validation state

The full checker passes all 310 translated target units. The cumulative index contains 3,678 aligned blocks: 3,124 translated and semantically reviewed, and 554 unchanged structural or formal blocks. This batch contributes 88 blocks, of which 66 are translated. The cumulative 299-unit semantic reader remains the current published reader tranche; reader rebuilding is intentionally deferred while source translation continues. The next source gate is the 310-unit public checkpoint with anonymous immutable-archive readback.
