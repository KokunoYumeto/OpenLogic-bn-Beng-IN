# Semantic review: Incompleteness and Provability

Review date: 2026-09-19

Locale: `bn-Beng-IN`

Units: OLP-0312--OLP-0321

Scope: 105 aligned source/target blocks across the chapter driver, historical introduction, fixed-point lemma, first incompleteness theorem, Rosser theorem, comparison with Gödel's paper, derivability conditions for Peano arithmetic, second incompleteness theorem, Löb theorem and Tarski undefinability theorem. Of these, 85 blocks contain reviewed Bengali translation and 20 are unchanged structural or formal blocks.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of theorem hypotheses, object-language and metalanguage predicates, diagonal constructions, proof-code arguments, derivability conditions, fixed points, reflection, definability and truth. Every source/target pair passes block-count, audited-mathematics, control-sequence, environment, semantic-token and Unicode NFC checks. This is a source and semantic review by the primary translation model; no independent human review, TeX-engine result or PDF result is claimed.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index and correction-ledger generation revalidate the per-file source hashes before accepting these units.

## Unit coverage

| Unit | File or role | Blocks | Review focus |
|---|---|---:|---|
| OLP-0312 | Incompleteness and Provability chapter driver | 11 | Chapter identity and nine imported sections |
| OLP-0313 | Introduction | 9 | Hilbert's program, two incompleteness results, liar comparison and fixed-point statement |
| OLP-0314 | Fixed-point lemma | 13 | Quotation, diagonalization, represented diagonal function, proof and truth-definition exercise |
| OLP-0315 | First incompleteness theorem | 15 | Proof coding, Gödel sentence, consistency, omega-consistency and incompleteness |
| OLP-0316 | Rosser theorem | 9 | Modified provability, smaller-refutation comparison, two consistency arguments and inseparability |
| OLP-0317 | Gödel's original paper | 3 | Historical proof sequence, primitive recursion, beta lemma and the role of Q |
| OLP-0318 | Derivability conditions for PA | 5 | Induction schema, computable axioms, represented proof relation and P1--P4 |
| OLP-0319 | Second incompleteness theorem | 13 | Consistency statement, formalized Gödel argument, P1--P3 proof and Hilbert's program |
| OLP-0320 | Löb theorem | 11 | Provability fixed point, reflection, formal proof, second-incompleteness corollary and exercise |
| OLP-0321 | Tarski undefinability theorem | 16 | Definability, true arithmetic, halting relation, diagonal contradiction and truth predicates |

## Source-level corrections carried into the Bengali draft

The following nine corrections are marked next to the affected target passages and recorded in `SOURCE_CORRECTIONS.jsonl`. Correction-note material is excluded from source parity and terminology occurrence counts.

* **BN-SRC-244 (OLP-0318):** the definition of `OProv` uses the representing object-language formula `OPrf`, rather than the metalanguage proof relation `Prf`.
* **BN-SRC-245 (OLP-0319):** the informal second-incompleteness argument retains the defined object-language predicate `OProv`, rather than switching to undefined `Prov`.
* **BN-SRC-246 (OLP-0319):** the second P2 instance takes the Gödel number of `!G`, restoring the formula marker omitted in the frozen source.
* **BN-SRC-247 (OLP-0319):** the generalized theorem requires an `axiomatizable` theory, matching the effective hypothesis used to obtain the provability predicate.
* **BN-SRC-248 (OLP-0319):** the generalized consistency statement is indexed by the fixed theory `\Th{T}`, rather than raw `T`.
* **BN-SRC-249 (OLP-0320):** all six proof-relation occurrences in the closing exercise use the theory macro `\Th{T}` introduced by the exercise.
* **BN-SRC-250 (OLP-0316):** the first Rosser-predicate occurrence uses the same bracketed `\Th{T}` index as its definition and every later occurrence.
* **BN-SRC-251 (OLP-0316):** the first contradiction argument takes the assumed derivation from the fixed theory `\Th{T}`, rather than raw `T`.
* **BN-SRC-252 (OLP-0320):** Gödel-sentence unprovability is stated under the consistency premise required by the paragraph's own contradiction argument.

## Reverse-paraphrase checks

1. **Hilbert, incompleteness and self-reference:** completeness requires every sentence or its negation to be derivable. The first theorem blocks a sufficiently strong, consistent, effectively axiomatized complete theory; the second blocks an adequate such theory from proving its own consistency. The liar and Quine examples motivate self-reference without treating informal truth as an arithmetic predicate.
2. **Fixed-point construction:** diagonalizing a one-free-variable formula substitutes the standard numeral naming that formula into its free variable. Because the diagonal function is computable, a representing formula in Q replaces a nonexistent object-language function symbol. The two proof directions use representation to show that the resulting sentence is equivalent in Q to the original property applied to its own numeral.
3. **First incompleteness:** `Prf` is the computable metalanguage relation on proof and formula codes; `OPrf` represents it in arithmetic; `OProv` existentially closes the proof-code variable. The fixed point says of itself that it is not T-provable. Consistency excludes its proof, omega-consistency excludes a proof of its negation, and the two exclusions yield incompleteness.
4. **Rosser strengthening:** Rosser provability requires a proof whose code has no smaller refutation code. If the Rosser sentence were provable, consistency excludes all smaller refutations and the fixed point yields its negation. If its negation were provable with code n, any assumed proof code must lie above n, providing the smaller refutation required to prove the Rosser sentence. Thus ordinary consistency suffices.
5. **Gödel-paper comparison:** the historical outline proceeds from the formal system through primitive-recursive coding and the proof relation, representability, the first theorem, arithmetical form and finally the second theorem. The beta lemma supplies finite-sequence coding; the modern presentation isolates Q as sufficient even though the original paper did not.
6. **Derivability conditions:** PA adds every induction-schema instance to Q and has a computable, though not finite, axiom set. P1 internalizes theoremhood, P2 internalizes modus ponens and P3 internalizes provability of provability. Their object-language formula is built from `OPrf`; the metalanguage relation is not inserted into an arithmetic sentence.
7. **Second incompleteness:** the consistency sentence denies provability of a contradiction. Formalizing the Gödel-sentence argument inside PA and applying P1--P3 yields consistency implies the Gödel sentence. If PA proved its consistency statement it would therefore prove the Gödel sentence, contradicting the established metatheoretic result under consistency.
8. **Löb and reflection:** an instance of reflection has the form provability of A implies A. Löb's theorem says that a qualifying theory derives such an instance only when it already derives A. The fixed-point proof moves from the sentence D equivalent to provability of D implies A through P1--P3 to D, its provability and finally A. The short consistency corollary substitutes falsity.
9. **Tarski undefinability:** a relation is definable when an arithmetic formula tracks it in the standard structure. Computable relations, including the halting relation, are definable, but the set of all true arithmetic sentences is not: a putative truth-defining formula and the fixed-point lemma produce a sentence equivalent to its own failure under that definition. The final linguistic argument retains the distinction between an object language and the metalanguage used to state its truth conditions.

## Terminology and authority scope

Decisions BN-IN-T260 through BN-IN-T267 record the fixed-point and diagonalization register, Gödel coding and numerals, first incompleteness and omega-consistency, Rosser provability and refutation, PA derivability conditions, second incompleteness and consistency statements, Löb reflection, and Tarski definability and truth vocabulary. Earlier decisions continue to govern theory, proof, soundness, consistency, computability, representability, Peano arithmetic and true arithmetic. The linked canon pages support the surrounding India-standard Bengali number, statement, quantification, relation, function, variable, mapping and proof register. They do not directly attest every named theorem or specialized metamathematical compound, so these choices remain provisional, definition-governed and open to expert correction.

## Validation state

The full checker passes all 320 translated target units. The cumulative index contains 3,783 aligned blocks: 3,209 translated and semantically reviewed, and 574 unchanged structural or formal blocks. This batch contributes 105 blocks, of which 85 are translated. The cumulative 299-unit semantic reader remains the current published reader tranche; reader rebuilding is deferred while source translation continues. The next source gate is the 320-unit public checkpoint with anonymous immutable-archive readback.
