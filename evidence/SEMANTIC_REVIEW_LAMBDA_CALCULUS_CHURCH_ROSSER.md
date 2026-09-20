# Semantic review: Lambda Calculus Church--Rosser foundations

Review date: 2026-09-20

Locale: `bn-Beng-IN`

Units: OLP-0367--OLP-0369

Scope: 33 aligned source/target blocks across the Church--Rosser chapter driver, the definitions-and-properties section, and the parallel-beta-reduction section. Of these, 29 blocks contain reviewed Bengali translation and four are unchanged structural or formal blocks.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of the Church--Rosser joining property, the computational interpretation of normal forms, uniqueness of a normal form, the transitive-closure grid proof, the four inductive parallel-beta-reduction rules, simultaneous contraction and later-created redexes, reflexivity, beta-complete development, compatibility with substitution, the continuation lemma, and the resulting Church--Rosser theorem. Every source/target pair passes block-count, audited-mathematics, protected-control, environment, semantic-token, and Unicode NFC checks. This is a source and semantic review by the primary translation model; no independent human review, TeX-engine result, or PDF result is claimed.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index generation revalidates the per-file source hashes before accepting these units.

## Unit coverage

| Unit | File or role | Blocks | Translated | Review focus |
|---|---|---:|---:|---|
| OLP-0367 | Church--Rosser chapter driver | 3 | 1 | Bengali chapter identity and all five imports in frozen-source order |
| OLP-0368 | Definitions and properties | 12 | 11 | Joining property, computation interpretation, unique normal forms, algebra example, and transitive-closure grid |
| OLP-0369 | Parallel beta reduction | 18 | 17 | Four inductive rules, later-created redexes, reflexivity, complete development, substitution compatibility, continuation, and Church--Rosser |

## Source review outcome

Three source-level defects are corrected with adjacent Bengali notes and exact validator transformations.

1. **BN-SRC-292 (OLP-0368):** the frozen grid proof writes two reduction chains but never identifies their endpoints as the arbitrary terms `P` and `Q` used at the end. The target begins from arbitrary `M \xred P` and `M \xred Q` and marks `P_m=P` and `Q_n=Q`, so the completed grid proves the required Church--Rosser conclusion for the transitive closure.
2. **BN-SRC-293 (OLP-0369):** the abstraction rule in the inductive definition assumes ordinary `N \xrightarrow{\beta} N'` even though the conclusion defines parallel beta reduction and both later induction proofs invoke this rule from `N \bredpar N'`. The target restores the parallel premise.
3. **BN-SRC-294 (OLP-0369):** the abstraction case of substitution compatibility drops the prime from the replacement on the right, writing `\Subst{N'}{R}{y}` where the lemma and induction hypothesis require `\Subst{N'}{R'}{y}`. The target restores `R'`.

The frozen prose also contains ordinary editorial slips such as “states is,” “height is,” “prove the it,” and the nonstandard plural “redices.” The Bengali text renders the intended prose idiomatically. The editorial warning that recursive functions on lambda terms have not yet been introduced is retained rather than silently resolved.

## Reverse-paraphrase checks

1. **Chapter driver:** the chapter is titled the Church--Rosser property and imports definitions and properties, parallel beta reduction, beta reduction, parallel beta-eta reduction, and beta-eta reduction in exactly the frozen-source order.
2. **Church--Rosser property:** a relation on terms has the property when any two one-step descendants `P` and `Q` of the same term `M` themselves reduce to some common term `N`. The Bengali definition preserves both premises, the existential common reduct, and both outgoing conclusions.
3. **Computation interpretation:** normal-form terms play the role of values and the reduction relation supplies calculation rules. Different available calculation paths therefore retain a single value when the joining property holds; the text does not claim that every term necessarily has a normal form.
4. **Elementary-algebra example:** `4 \times (1+2)+3` can first reduce the parenthesized sum or first use distributivity. The two displayed descendants both continue to `12+3`, and the later final result remains `15`.
5. **Unique normal form:** if `M` reduces to normal forms `P` and `Q`, Church--Rosser supplies a common descendant `N`. Because neither normal form admits a nontrivial further reduction, both paths to `N` are trivial, so `P`, `Q`, and `N` are identical. The Bengali prose preserves the conditional “if any” status of a final result.
6. **Transitive-closure grid:** from arbitrary finite chains ending at `P=P_m` and `Q=Q_n`, the proof builds an `(m+1)` by `(n+1)` grid. Each interior `N_{i,j}` joins its upper and left predecessors under the original relation. The bottom and right boundary chains meet at `N_{m,n}`, which makes `P` and `Q` join under the smallest transitive relation. BN-SRC-292 supplies the endpoint identifications needed for this argument.
7. **Parallel-beta rules:** variables reduce to themselves; abstraction propagates a parallel reduction of its body; application propagates parallel reductions in both components; and a beta redex simultaneously reduces its body and argument before capture-avoiding substitution. BN-SRC-293 keeps all four clauses inside the relation being inductively defined.
8. **Original versus newly created redexes:** one parallel step may contract any number of redexes already present in the original term, but it cannot also contract a redex created by that same step. Thus `(\lambd[f][fx])(\lambd[y][y])` can become itself or `(\lambd[y][y])x`, but needs a second parallel step to reach `x`.
9. **Reflexivity:** every term is parallel-beta-related to itself. The proof is left as an exercise and the following problem asks the reader to supply it; the target preserves both the theorem and that pedagogical division.
10. **Beta-complete development:** `\bcd{M}` recursively preserves variables, develops abstraction bodies, develops both sides of a non-redex application, and develops then substitutes both parts of a beta redex. Unlike an arbitrary parallel reduction, complete development contracts every original redex. The example consequently yields `(\lambd[y][y])x`, not the unchanged source term.
11. **Substitution compatibility:** if both `M` and replacement `R` reduce in parallel, then substituting `R` for `y` in `M` reduces in parallel to the corresponding substitution of `R'` in `M'`. The abstraction case uses the parallel abstraction rule and the induction hypothesis; BN-SRC-294 restores the required primed replacement. The application and redex cases retain the nested substitutions and their variable order.
12. **Continuation lemma:** every one-step parallel reduct `M'` of `M` can reduce in parallel to the complete development `\bcd{M}`. The induction distinguishes a non-abstraction head from an abstraction head in the application case, and uses substitution compatibility in the redex case. Each displayed target of the case analysis remains the appropriate clause of the complete-development definition.
13. **Church--Rosser theorem:** any two parallel reducts of the same term both continue to that term's complete development by the continuation lemma. This supplies their common reduct immediately and proves that parallel beta reduction has the Church--Rosser property.

## Terminology and authority scope

BN-IN-T290 continues to govern `চার্চ--রসার ধর্ম`, the common-reduct wording, and uniqueness of normal form. BN-IN-T306 continues to govern beta reduction, redexes, normality, and trivial reduction. BN-IN-T308 records `সমান্তরাল $\beta$-হ্রাস` for parallel beta reduction, simultaneous redex contraction, `$\beta$-পূর্ণ বিকাশ` for beta-complete development, complete parallel reduction, and later-created redexes.

The checked India-standard pages directly support variables, relations, functions, algebraic expressions, reduction language, and university proof and uniqueness prose. They do not directly attest every Church--Rosser-specific compound. Those choices are definition-governed, explicitly provisional, and open to expert correction. No unlisted dictionary or expert consultation is claimed.

## Validation state

The per-unit checker recognizes all 368 translated target units and passes OLP-0367--OLP-0369 individually. The cumulative index contains 4,236 aligned blocks: 3,591 translated and semantically reviewed, and 645 unchanged structural or formal blocks. This review contributes 33 blocks, 29 translated and four unchanged. Evidence has 301 source-correction records, three render-equivalent source normalizations, and 308 translation decisions, 289 of them provisional, with 24,303 indexed target-line occurrences and 293 decisions tied to representative exact source wording. The cumulative 299-unit semantic reader remains the current published reader tranche; reader rebuilding is deferred while source translation continues. The 365-unit source checkpoint remains the latest anonymously verified public source checkpoint pending publication and readback of this three-unit batch.
