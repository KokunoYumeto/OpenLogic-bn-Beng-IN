# Semantic review: Second-order Logic Metatheory

Review date: 2026-09-19

Locale: `bn-Beng-IN`

Units: OLP-0330--OLP-0335

Scope: 46 aligned source/target blocks across the Metatheory chapter driver, introduction, second-order arithmetic, undecidability and non-axiomatizability, compactness, and Löwenheim--Skolem sections. Of these, 35 blocks contain reviewed Bengali translation and 11 are unchanged structural or formal blocks.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of effective validity enumeration, second-order induction, categoricity, arithmetic definability, reduction from true arithmetic, finite satisfiability, and both Löwenheim--Skolem directions. Every source/target pair passes block-count, audited-mathematics, control-sequence, environment, semantic-token, and Unicode NFC checks. This is a source and semantic review by the primary translation model; no independent human review, TeX-engine result, or PDF result is claimed.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index and correction-ledger generation revalidate the per-file source hashes before accepting these units.

## Unit coverage

| Unit | File or role | Blocks | Translated | Review focus |
|---|---|---:|---:|---|
| OLP-0330 | Metatheory chapter driver | 7 | 1 | Chapter identity and five imported sections |
| OLP-0331 | Introduction | 4 | 3 | Effective axiomatizability, compactness, and model-size contrasts |
| OLP-0332 | Second-order arithmetic | 15 | 14 | Induction, standard-domain theorem, categoricity, and definability |
| OLP-0333 | Undecidability and non-axiomatizability | 6 | 5 | First-order reduction and true-arithmetic contradiction |
| OLP-0334 | Compactness | 7 | 6 | Finite satisfiability and the infinite-domain counterexample |
| OLP-0335 | Löwenheim--Skolem | 7 | 6 | Failure of the downward and upward model-size theorems |

## Source-level corrections carried into the Bengali draft

The following four corrections are marked next to the affected target passages and recorded in `SOURCE_CORRECTIONS.jsonl`. Correction-note material is excluded from source parity and terminology occurrence counts.

* **BN-SRC-255 (OLP-0332):** the recursive clause in the displayed definition of addition now uses the universally quantified variable `w` in both places. The frozen formula quantifies `w` but writes free `x` in both occurrences, contrary to the immediately preceding prose.
* **BN-SRC-256 (OLP-0333):** the satisfaction expression for `P` implying `A` closes its second macro argument before math mode. The frozen source closes math mode first and therefore leaves malformed TeX.
* **BN-SRC-257 (OLP-0334):** the non-compactness theorem uses the unique label `thm:sol-not-compact`. The frozen source repeats `thm:sol-undecidable`, already used by the preceding theorem.
* **BN-SRC-258 (OLP-0334):** the finite-satisfiability proof selects its maximum lower-bound sentence from the finite fragment `Gamma_0`, and it takes `k=1` if that fragment contains no lower-bound sentence. The frozen source twice names the full set `Gamma`, which contains every larger requirement, and omits the empty-index case.

## Reverse-paraphrase checks

1. **Metatheoretic comparison:** a sound and complete first-order proof system makes first-order validities computably enumerable even though first-order logic is undecidable. Full second-order validities are not computably enumerable, so there is no sound and complete proof system for them. Compactness and both Löwenheim--Skolem directions also fail because full second-order logic can constrain domain size.
2. **Second-order induction and standardness:** second-order Peano arithmetic replaces the first-order induction schema with one sentence quantifying over every subset of the domain. Applying it to the set of numeral values proves that every domain element is a numeral value; the remaining arithmetic axioms then make every model isomorphic to the standard natural-number structure.
3. **Arithmetic definability:** the successor axioms plus second-order induction suffice to define order as membership in every successor-closed set containing the lower endpoint. Addition is defined by a function starting at the first addend and advancing by successor until the second addend; BN-SRC-255 makes the quantified iteration variable agree with this recursion. The stated exercise leaves multiplication to the reader, as in the source.
4. **Undecidability and non-axiomatizability:** first-order validity reduces immediately to second-order validity, establishing undecidability. For the stronger result, the nine second-order Peano axioms are conjoined, arithmetic symbols are replaced by second-order variables, and all replacements are universally quantified. A complete proof system would then computably enumerate the true first-order arithmetic sentences, yielding a definition of true arithmetic contrary to Tarski's theorem.
5. **Compactness failure:** the set containing not-`Inf` together with a sentence demanding at least `n` elements for every positive `n` has no model. Every finite fragment has a finite model whose size meets its largest lower-bound requirement; the corrected proof also covers a fragment with no such requirement. This establishes finite satisfiability without satisfiability.
6. **Löwenheim--Skolem failure:** not-`Count` has infinite nonenumerable models but no enumerable model, refuting the downward direction. `Count` together with `Inf` has a denumerable model but no nonenumerable model, refuting the upward direction. The two examples preserve the distinctions among enumerable, denumerable, and nonenumerable domains.

## Terminology and authority scope

BN-IN-T275 records the second-order metatheory and effective-proof register; BN-IN-T276 covers second-order Peano arithmetic and induction; BN-IN-T277 covers arithmetic definability; BN-IN-T278 covers undecidability and non-axiomatizability; BN-IN-T279 covers compactness failure and finite fragments; and BN-IN-T280 covers both Löwenheim--Skolem directions and model-size vocabulary. Earlier decisions continue to govern validity, derivability, compactness, finite satisfiability, second-order semantics, arithmetic, definability, domain size, and enumerability. The linked canon pages support the surrounding India-standard Bengali logic, number, relation, function, proof, and cardinality prose. They do not directly attest every complete second-order metatheoretic compound, so the new choices remain provisional, definition-governed, and open to expert correction.

## Validation state

The per-unit checker passes all 334 translated target units. The cumulative index contains 3,903 aligned blocks: 3,303 translated and semantically reviewed, and 600 unchanged structural or formal blocks. This batch contributes 46 blocks, of which 35 are translated. The cumulative 299-unit semantic reader remains the current published reader tranche; reader rebuilding is deferred while source translation continues. The next source gate is the 334-unit public checkpoint with anonymous immutable-archive readback.
