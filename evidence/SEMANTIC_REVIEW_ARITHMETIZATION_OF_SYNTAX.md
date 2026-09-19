# Semantic review: Arithmetization of Syntax

Review date: 2026-09-09

Locale: `bn-Beng-IN`

Units: OLP-0280--OLP-0288
Scope: 116 aligned source/target blocks across the chapter driver, introduction, coding of symbols, terms and formulas, substitution, and the LK, natural-deduction and axiomatic proof-coding sections.

This review records the semantic pass completed before reader integration. The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of definitions, recursive clauses, bounds, proof-object layouts and exercises. Every source/target pair passed the checked structural policy: block counts, audited mathematical fragments, control sequences, environments, semantic tokens and Unicode NFC. The nine target files remain draft source files; TeX/PDF rendering and final reader pagination are pending because the shared TeX mutex is reserved by another workflow.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index and correction-ledger generation revalidated the per-file source hashes before accepting these units.

## Unit coverage

| Unit | File or role | Blocks | Review focus |
|---|---|---:|---|
| OLP-0280 | Arithmetization of Syntax chapter driver | 11 | Chapter identity, provenance note, eight imported sections |
| OLP-0281 | Introduction | 6 | Gödel numbering, computable syntactic properties, arithmetized substitution, incompleteness role |
| OLP-0282 | Coding Symbols | 7 | Fixed symbol codes, concatenation and numeral coding |
| OLP-0283 | Coding Terms | 12 | Term and closed-term codes, formation sequences, primitive-recursive search bounds |
| OLP-0284 | Coding Formulas | 12 | Formula codes, predicate arity, free occurrence and sentence recognition |
| OLP-0285 | Substitution | 7 | Recursive symbol, term and formula substitution and the capture-avoidance test |
| OLP-0286 | Proofs in LK | 21 | Derivation tuples, end sequents, last rules, correctness and the proof relation |
| OLP-0287 | Proofs in Natural Deduction | 27 | Derivation trees, discharge labels, open assumptions, subtree sequences and correctness |
| OLP-0288 | Proofs in Axiomatic Deduction | 13 | Justified sequences, axiom schemas, MP/QR, nested conditionals and the deduction theorem |

## Source-level corrections carried into the Bengali draft

The following thirteen corrections are documented in `SOURCE_CORRECTIONS.jsonl` and marked adjacent to the affected target passages. Correction-note material is excluded from source parity and terminology occurrence counts.

* **BN-SRC-205 (OLP-0284):** the predicate-code condition now requires `\len{z}=n`, so the number of coded arguments equals the predicate arity.
* **BN-SRC-206 (OLP-0284):** the proof no longer claims that the whole formation-sequence code is below the formula code. It bounds the subformula codes and derives a primitive-recursive bound for the combined sequence code.
* **BN-SRC-207 (OLP-0284):** the `FreeOcc` implication lies inside both bounded quantifier scopes in the definition of `Sent`.
* **BN-SRC-208 (OLP-0286):** the expanded LK example drops the unmatched right parenthesis after the initial sequent code.
* **BN-SRC-209 (OLP-0286):** the end-sequent helper is consistently named `\fn{EndSequent}`.
* **BN-SRC-210 (OLP-0286):** the final initial-sequent alternative calls the defined `\fn{InitSeq}`, and its explanation refers to the running derivation code `$p$`.
* **BN-SRC-211 (OLP-0286):** the derivation test consistently uses `$p$` and closes the final `\fn{Correct}` application.
* **BN-SRC-212 (OLP-0286):** the unique succedent formula has Gödel number `$y$`; `$x$` remains the derivation code.
* **BN-SRC-213 (OLP-0287):** immediate subderivations occupy slots `$(d')_{j+1}$`, after the count stored in slot zero.
* **BN-SRC-214 (OLP-0287):** the incomplete subsequence sentence explicitly names `\fn{SubtreeSeq}(d)` as the controlling sequence.
* **BN-SRC-215 (OLP-0288):** the previous-line index in the `\fn{QR}_1` condition is bound by `\bexists{j<i}`.
* **BN-SRC-216 (OLP-0288):** the nonoccurrence wording is repaired and the code bound consistently refers to the constant `$c$`.
* **BN-SRC-217 (OLP-0288):** the recursive nested-conditional definition calls its defined helper `\fn{hCond}` rather than the undefined three-argument `\fn{Cond}`.

## Reverse-paraphrase checks

1. **Chapter driver and introduction:** the Bengali driver imports the introduction and seven technical sections in the frozen order. The introduction assigns natural numbers to symbols and then to terms, formulas and derivations; it uses those codes to turn syntactic tests and transformations into number-theoretic relations and functions. Substitution remains the motivating example, and arithmetized syntax remains the bridge needed for statements about formal theories to speak about their own proofs.
2. **Symbols and codes:** each primitive symbol receives its fixed code. A string code is built by the stated prime-power convention, concatenation remains an arithmetic operation on string codes, and the numeral construction produces the syntactic numeral corresponding to a natural number. Symbol codes are kept distinct from Gödel numbers of complete terms and formulas.
3. **Terms and formulas:** a well-formed object is recognized by a finite formation sequence whose entries obey the relevant formation clauses. The search is finite because the component codes and sequence length admit primitive-recursive bounds; the review does not rely on the false claim corrected by BN-SRC-206. Predicate codes require exactly the declared number of arguments. `FreeOcc` still identifies an occurrence outside a binding quantifier, and `Sent` still means a formula with no free variable occurrence.
4. **Substitution:** the recursive function copies unaffected symbols, replaces the selected variable where licensed, recurses through compound terms and connectives, and treats quantifiers with the stated capture-avoidance conditions. The “free for” relation remains a syntactic test preventing a formerly free variable occurrence from becoming bound.
5. **LK proof coding:** an LK derivation is represented as a tuple containing immediate subderivations, an end sequent and a last-rule code. `Correct(p)` checks the final inference from the child end sequents, `Deriv(p)` checks every coded subtree, and `\Prf[\Gamma](x,y)` additionally verifies that the left side of the final sequent belongs to `\Gamma` and its right side is the singleton sentence coded by `$y$`.
6. **Natural-deduction proof coding:** a derivation tree records its immediate subderivations, end formula, discharge label and last rule. The subtree sequence lets the definitions inspect every node. Open assumptions are precisely the labelled assumptions not discharged on the path governed by an inference, and the quantified rules retain their eigenvariable conditions. The corrected `j+1` indexing covers all direct children without treating the stored child count as a derivation.
7. **Axiomatic proof coding:** an axiomatic derivation is a finite sequence whose line is a premise, an axiom-schema instance, a modus-ponens consequence of earlier lines or a quantified-rule consequence satisfying its nonoccurrence condition. The recursive conditional constructor converts a finite premise sequence into a right-associated conditional with the target sentence as consequent. The deduction theorem then connects a proof from those premises with a proof of that nested conditional from the empty premise set.

## Terminology and authority scope

Decisions BN-IN-T234, BN-IN-T235, BN-IN-T236, BN-IN-T237, BN-IN-T238, BN-IN-T239, BN-IN-T240, BN-IN-T241 and BN-IN-T242 record the chapter vocabulary for Gödel numbering, formation sequences, primitive recursion, proof-object fields, discharge, subderivations, axiomatic rules, nested conditionals and substitution. The linked canon pages were read for India-standard Bengali mathematical, logic, sequence, relation, function, variable and proof prose. They support the surrounding register and some component words; they do not directly establish every OpenLogic-specific compound. Formal correctness therefore rests on the frozen-source comparison, the displayed definitions and the explicit BN-SRC-205--BN-SRC-217 audits. All nine decisions remain provisional and open to expert correction.

## OLP-0281-B006 translation correction

The 2026-09-17 semantic re-review found that the former phrase `গুরুত্বপূর্ণ ও অনায়াসসাধ্য অন্তর্দৃষ্টি` reversed the source wording “non-trivial insight”: `অনায়াসসাধ্য` means easy or not hard to accomplish. The corrected phrase is `অ-তুচ্ছ অন্তর্দৃষ্টি`, which preserves the explicit non-trivial polarity and drops the unsupported added claim of importance. The government Accessible Dictionary entry was consulted only to confirm the rejected easy/effortless sense; the selected replacement follows the frozen source and a transparent Bengali composition. Previously inspected canon passages BN-IN-P005 and BN-IN-P018 do not attest this advanced phrase and are not represented as support for it.

The exact old and new file/span hashes, manager-audit hashes, dictionary URL, rejected interpretation, rationale and high editorial confidence are recorded in `TRANSLATION_CORRECTION_OLP_0281_2026-09-17.json`. Regenerating the segment index rebound OLP-0281-B006 to target file SHA-256 `779aa58c4e2adb1115bca57eb407643130530383bcd753b1b88b8ab3103573df` and target-span SHA-256 `7346700caf6b397aa991104cf68607095dc32577e4ad7256b87a0a560ecc9ce9`. The corrected unit passes the same block, mathematics, control-sequence, environment, semantic-token and Unicode checks as the rest of the draft.

## Validation state

The full source checker passes all 299 current target units, including these 116 blocks and the corrected OLP-0281 binding. The 287-unit public checkpoint remains the prior immutable baseline until the 299-unit source transaction and anonymous archive readback complete. TeX compilation and PDF rendering remain outside this review; semantic HTML/EPUB integration is tracked independently.
