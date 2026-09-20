# Semantic review: Lambda Calculus introduction

Review date: 2026-09-20

Locale: `bn-Beng-IN`

Units: OLP-0341--OLP-0346

Scope: 49 aligned source/target blocks across the Lambda Calculus part driver, Introduction chapter driver, overview, introductory syntax, reduction, and Church--Rosser sections. Of these, 30 blocks contain reviewed Bengali translation and 19 are unchanged structural or formal blocks.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of lambda notation, abstraction and application, inductive term formation, alpha-equivalence, capture-avoiding substitution, beta-contraction and reduction, normal forms, and the Church--Rosser joining property. Every source/target pair passes block-count, audited-mathematics, control-sequence, environment, semantic-token, and Unicode NFC checks. This is a source and semantic review by the primary translation model; no independent human review, TeX-engine result, or PDF result is claimed. The part and chapter editorial notes about provenance, redundancy, and needed revision are retained in Bengali.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index generation revalidates the per-file source hashes before accepting these units.

## Unit coverage

| Unit | File or role | Blocks | Translated | Review focus |
|---|---|---:|---:|---|
| OLP-0341 | Lambda Calculus part driver | 7 | 2 | Part identity, editorial provenance, and four chapter imports |
| OLP-0342 | Introduction chapter driver | 16 | 2 | Chapter identity, editorial integration note, and thirteen section imports |
| OLP-0343 | Overview | 8 | 8 | Historical purpose, computability equivalence, notation, abstraction/application, and typed/untyped distinction |
| OLP-0344 | Introductory syntax | 7 | 7 | Inductive term formation, pure calculus, notation, alpha-equivalence, and bound/free variables |
| OLP-0345 | Reduction of lambda terms | 6 | 6 | Capture-avoiding substitution, beta-contraction, reduction relations, normality, and four examples |
| OLP-0346 | Church--Rosser property | 5 | 5 | Common reduct, uniqueness of normal form, beta-equivalence, and the least equivalence relation |

## Source review outcome

No source-level mathematical correction was required in these six units. Every displayed term, substitution, reduction path, theorem hypothesis, and conclusion is internally consistent. OLP-0344 contains the ordinary prose typo `From example`; the Bengali rendering uses the intended `যেমন` (“for example”). This does not alter a formal object or technical claim and is therefore not entered as a source-correction record.

## Reverse-paraphrase checks

1. **Purpose and expressive notation:** Church introduced the calculus as a basis for constructive logic, after which it was shown equivalent in computability strength to Turing-computable and partial recursive functions. Lambda notation names a function directly by the expression defining it. Renaming the dummy variable does not change the function, and external parameters remain available.
2. **Abstraction and application:** lambda abstraction turns an expression with a designated variable into a function-denoting expression. Application supplies an argument. Combining them permits the applied expression to replace the abstracted variable, as in the displayed example reducing the application of the add-three abstraction to `2 + 3`.
3. **Untyped and typed calculi:** in the untyped calculus every object denotes a function, abstraction forms functions, and any term may be applied to any other. The typed calculus restricts such applications, aligns more readily with classical set-theoretic interpretation, and has materially different properties. The historical LISP reference remains a programming-language example rather than a claim of identity with the calculus.
4. **Inductive syntax:** variables and constants are terms; application of two terms and abstraction of a term over a variable produce terms. Removing constants yields the pure calculus. Lowercase object letters and uppercase term metavariables remain distinct. Application associates to the left, abstraction receives the widest scope, and multi-variable abstraction abbreviates nested single-variable abstractions.
5. **Alpha-equivalence and variable status:** alpha-equivalence changes only names of bound variables. The translation preserves the source convention that “same term” includes equality up to such renaming. A variable inside the scope of its governing lambda is bound; the other occurrences are free, exactly as classified in the final example.
6. **Capture-avoiding substitution:** `\Subst{M}{N}{x}` replaces `x` by `N` in `M` only after renaming bound variables of `M` that would capture free variables of `N`. The first displayed substitution keeps `w` harmless. The three alternative notations are retained with the source warning that their slash direction varies.
7. **Beta-reduction:** replacing a redex `(\lambd[x][M])N` by its contractum `\Subst{M}{N}{x}` is beta-contraction. One-step reduction and its reflexive-transitive closure remain distinct. A beta-normal term admits no further contraction. The examples respectively terminate at `y`, grow indefinitely, reproduce themselves unchanged, and reduce along two different first steps to the common term `zv`.
8. **Church--Rosser and normal forms:** if one term reduces to `N_1` and `N_2`, both descendants reduce to some common `P`. If both descendants are normal, neither can take a genuine further step, so each is identical to `P` and the normal form is unique. Common-reduct beta-equivalence is therefore an equivalence relation containing every directed reduction pair, and the source's least-relation qualification is retained.

## Terminology and authority scope

BN-IN-T286 records the core lambda-calculus, notation, term, and definability register; BN-IN-T287 covers abstraction, application, placeholder variables, and the typed/untyped distinction; BN-IN-T288 covers the pure syntax, compound term forms, notation, alpha-equivalence, and bound/free variables; BN-IN-T289 covers capture avoidance, redex/contractum, beta-contraction, reduction, and normality; and BN-IN-T290 covers Church--Rosser, common reducts, normal-form uniqueness, beta-equivalence, and the least equivalence relation. Existing T058, T097, T099, T173, T198, and T242 continue to govern free/bound variables, substitution, normal form, beta-equivalence, and free-for-substitution vocabulary.

The checked India-standard pages directly support variables/constants, algebraic expressions, functions, mappings, injectivity, and university proof and uniqueness prose. They do not directly attest the complete lambda-specific compounds. Those choices are definition-governed, explicitly provisional, and open to expert correction.

## Validation state

The per-unit checker recognizes all 345 translated target units and passes the six new units individually. After state export, the cumulative index contains 3,998 aligned blocks: 3,370 translated and semantically reviewed, and 628 unchanged structural or formal blocks. This batch contributes 49 blocks, of which 30 are translated. The cumulative 299-unit semantic reader remains the current published reader tranche; reader rebuilding is deferred while source translation continues. The next source gate is the 345-unit public checkpoint with anonymous immutable-archive readback.
