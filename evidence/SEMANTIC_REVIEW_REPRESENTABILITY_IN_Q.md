# Semantic review: Representability in Q

Review date: 2026-09-17

Locale: `bn-Beng-IN`

Units: OLP-0289--OLP-0300
Scope: 165 aligned source/target blocks across the chapter driver, introduction, computability direction, beta coding, elimination of primitive recursion, basic representable functions, closure proofs, relation representation, undecidability and Sigma-1 completeness. Of these, 150 blocks contain reviewed Bengali translation and 15 are unchanged structural or formal blocks.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of definitions, theorem hypotheses, algorithms, induction steps, quantifier scopes and exercises. Every source/target pair passes block-count, audited-mathematics, control-sequence, environment, semantic-token and Unicode NFC checks. This is a source and semantic review; no TeX engine or PDF result is claimed.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index and correction-ledger generation revalidated the per-file source hashes before accepting these units.

## Unit coverage

| Unit | File or role | Blocks | Review focus |
|---|---|---:|---|
| OLP-0289 | Representability in Q chapter driver | 13 | Chapter identity, provenance note and eleven imported sections |
| OLP-0290 | Introduction | 10 | Robinson Q, theory-relative representation, computability characterization and roadmap |
| OLP-0291 | Representable implies computable | 9 | Search procedure, uniqueness, consistency and numeral embedding |
| OLP-0292 | Beta function | 12 | Finite-sequence coding, coprimality, congruence, Sunzi theorem and decoding |
| OLP-0293 | Primitive recursion | 5 | Beta-coded computation histories and elimination by composition plus regular minimization |
| OLP-0294 | Basic representable functions | 29 | Zero, successor, projections, addition, multiplication and characteristic functions |
| OLP-0295 | Closure under composition | 11 | Witness formulas, uniqueness and general finite composition |
| OLP-0296 | Closure under regular minimization | 29 | Least-zero witness, bounded clauses and induction inside Q |
| OLP-0297 | Computable implies representable | 5 | Closure characterization and the consistency scope of the generalization |
| OLP-0298 | Representing relations | 8 | Relation formulas, characteristic functions and complements |
| OLP-0299 | Undecidability | 6 | Theorem-set characteristic function and omega-consistency consequence |
| OLP-0300 | Sigma-1 completeness | 28 | Bounded formulas, closed arithmetic, Delta-0 induction and Sigma-1 witnesses |

## Source-level corrections carried into the Bengali draft

The following sixteen corrections are documented in `SOURCE_CORRECTIONS.jsonl` and marked next to the affected target passages. Correction-note material is excluded from source parity and terminology occurrence counts.

* **BN-SRC-218 (OLP-0291):** the representing formula is consistently `!A_f`, rather than switching to `!A` in the lemma introduction.
* **BN-SRC-219 (OLP-0291):** the computed value `(s)_1` is embedded as the object-language numeral `\num{(s)_1}`.
* **BN-SRC-220 (OLP-0293):** the primitive-recursion signature is `h(\vec x,y)`, matching the governing equations.
* **BN-SRC-221 (OLP-0293):** the open parenthesis around the minimization condition is closed after the bounded recursion clause.
* **BN-SRC-222 (OLP-0295):** the composition formula binds `y_0` through `y_{k-1}` in balanced, complete existential scopes.
* **BN-SRC-223 (OLP-0295):** the exercise now cites the two distinct guiding propositions `prop:rep1` and `prop:rep2`.
* **BN-SRC-224 (OLP-0296):** the successor-addition induction uses Q5, the induction hypothesis and transitivity in a noncircular order.
* **BN-SRC-225 (OLP-0297):** the general representation characterization includes consistency, excluding the trivial inconsistent-theory counterexample.
* **BN-SRC-226 (OLP-0300):** the file identifier uses the importing chapter code `req`.
* **BN-SRC-227 (OLP-0300):** the second closed term is proved equal to `\num m`, its fixed value.
* **BN-SRC-228 (OLP-0300):** the less-than witness keeps the addend order required by Q8 without assuming commutativity in Q.
* **BN-SRC-229 (OLP-0300):** both successor-equals-zero contradictions cite Q2 rather than Q3.
* **BN-SRC-230 (OLP-0300):** the zero-bound universal expansion is described as an empty conjunction, equivalent to truth.
* **BN-SRC-231 (OLP-0300):** the bounded existential macro receives the complete braced formula scope.
* **BN-SRC-232 (OLP-0300):** the existential formula uses the edition’s well-formed two-argument `\lexists` invocation.
* **BN-SRC-233 (OLP-0294):** the fallback word in the cases display is placed in `\text{...}` rather than being parsed as a product of variables.

## Reverse-paraphrase checks

1. **Chapter claim and definition:** the chapter fixes Robinson Q and defines a function as represented when one formula proves the correct numeral value and refutes every incorrect value. The two directions of the main theorem remain distinct: effective proof search extracts a represented value, while the converse constructs formulas from the closure scheme for computable functions.
2. **Search from representation:** enumerating Q-proofs eventually finds the representing instance for the true output. Consistency and the refutation clauses prevent two different outputs. The repaired numeral constructor keeps the searched natural value inside the arithmetic language.
3. **Beta coding:** a single number can encode any prescribed finite sequence so that `\beta(d,i)=a_i` at each required position. The proof first constructs pairwise coprime moduli and then applies Sunzi’s theorem. The resulting beta function uses only the allowed basic functions, composition and regular minimization.
4. **Eliminating primitive recursion:** a beta-coded sequence records the successive values of a primitive recursion. Regular minimization finds a code satisfying the initial and step clauses, so the final entry defines the same function without primitive recursion. The corrected signature and closing delimiter preserve the full condition.
5. **Basic functions and composition:** Q represents zero, successor, projections, addition, multiplication and equality’s characteristic function. Composition introduces one witness for each intermediate result; the nested formula asserts each component representation and the outer representation. The repaired quantifier scopes bind every witness exactly once.
6. **Regular minimization:** the representing formula asserts that the chosen value is a zero and that every smaller candidate is nonzero. Q’s arithmetic axioms and a finite induction over the standard numeral prove the positive and negative representation clauses. The reordered equality chain no longer assumes its conclusion.
7. **Characterization and relations:** closure under the basic functions, composition and regular minimization yields every general recursive, hence computable, function. Together with the first direction this identifies Q-representable functions with computable functions. Relations pass through their zero-one characteristic functions and complements with the stated truth-value convention.
8. **Undecidability:** if theoremhood for a consistent axiomatized extension of Q were decidable, its characteristic function would be representable, producing the standard diagonal contradiction. The omega-consistency exercise remains a stronger numeral-by-numeral condition and is not conflated with ordinary consistency.
9. **Bounded and Sigma-1 completeness:** true and false closed atomic statements are decided in Q. Bounded quantifiers expand over the finitely many standard numerals denoted by their closed bounds, supporting induction over Delta-0 formula complexity. A true Sigma-1 sentence has a standard witness; substituting its numeral reduces the proof to Delta-0 completeness before existential introduction.

## Terminology and authority scope

Decisions BN-IN-T243 through BN-IN-T250 record representability, beta coding, coprimality and congruence, closure operations, the bounded arithmetical hierarchy, omega-consistency, Robinson-Q proof vocabulary and Sigma-1 completeness. The linked canon pages support the surrounding India-standard Bengali number, relation, function, sequence, logic and proof register. They do not directly attest every specialized compound or theorem name. Those decisions therefore remain provisional, definition-governed and open to expert correction.

## Validation state

The full checker passes all 299 translated target units. The cumulative index contains 3,590 aligned blocks: 3,058 translated and semantically reviewed, and 532 unchanged structural or formal blocks. This batch contributes 165 blocks, of which 150 are translated. The next gates are the parameterized checkpoint verifier, publication, anonymous immutable-archive readback, and independent semantic HTML/EPUB validation.
