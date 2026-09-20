# Semantic review: Lambda Calculus introduction

Review date: 2026-09-20

Locale: `bn-Beng-IN`

Units: OLP-0341--OLP-0352

Scope: 77 aligned source/target blocks across the Lambda Calculus part driver, Introduction chapter driver, overview, introductory syntax and reduction, Church--Rosser, currying, lambda definability, both computability directions, basic primitive-recursive lambda definitions, and composition closure. Of these, 58 blocks contain reviewed Bengali translation and 19 are unchanged structural or formal blocks.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of lambda notation, abstraction and application, inductive term formation, alpha-equivalence, capture-avoiding substitution, beta-contraction and reduction, normal forms, the Church--Rosser joining property, currying, Church numerals, lambda definability, the two computability implications, the normal-form proof plan, initial primitive-recursive functions, and composition. Every source/target pair passes block-count, audited-mathematics, control-sequence, environment, semantic-token, and Unicode NFC checks. This is a source and semantic review by the primary translation model; no independent human review, TeX-engine result, or PDF result is claimed. The part and chapter editorial notes about provenance, redundancy, and needed revision are retained in Bengali.

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
| OLP-0347 | Currying | 5 | 5 | Unary simulation of multiargument functions, function-valued functions, and nested substitution |
| OLP-0348 | Lambda-definable arithmetical functions | 7 | 7 | Church numerals, iteration, partial-function representation, and the equivalence theorem |
| OLP-0349 | Lambda-definable implies computable | 4 | 4 | Reduction-tree search, Church's thesis, and recursive syntax/reduction encodings |
| OLP-0350 | Computable implies lambda-definable | 4 | 4 | Kleene normal form, closure proof plan, and conventional arity notation |
| OLP-0351 | Basic primitive-recursive functions | 5 | 5 | Lambda definitions of zero, successor, and projections |
| OLP-0352 | Composition | 3 | 3 | Componentwise construction proving closure under composition |

## Source review outcome

Four source-level notation defects were corrected with adjacent Bengali notes and exact validator transformations.

1. **BN-SRC-267 (OLP-0347):** the last line of the general currying derivation substituted into an undefined `P`, although `N` is the body fixed throughout. The target restores `N`.
2. **BN-SRC-268 (OLP-0348):** the definition called `f(x_0, ..., x_{k-1})` an `n`-ary function. The target restores `k`-ary, matching every variable and input index.
3. **BN-SRC-269 (OLP-0348):** the undefined branch placed a comma between `F` and its first Church-numeral argument. The target restores application spacing, so both branches concern the same applied term.
4. **BN-SRC-270 (OLP-0349):** the first search term omitted braces around both arguments of the one-argument `\num` macro, leaving each subscript outside the numeral overline. The target writes `\num{m_0}` and `\num{m_{n-1}}`, matching the correctly braced repetition later in the proof.

OLP-0344 contains the ordinary prose typo `From example`; the Bengali rendering uses the intended `যেমন` (“for example”). This does not alter a formal object or technical claim and is therefore not entered as a source-correction record. The remaining terms, reductions, theorem claims, and proof plans in OLP-0341--OLP-0352 are internally consistent.

## Reverse-paraphrase checks

1. **Purpose and expressive notation:** Church introduced the calculus as a basis for constructive logic, after which it was shown equivalent in computability strength to Turing-computable and partial recursive functions. Lambda notation names a function directly by the expression defining it. Renaming the dummy variable does not change the function, and external parameters remain available.
2. **Abstraction and application:** lambda abstraction turns an expression with a designated variable into a function-denoting expression. Application supplies an argument. Combining them permits the applied expression to replace the abstracted variable, as in the displayed example reducing the application of the add-three abstraction to `2 + 3`.
3. **Untyped and typed calculi:** in the untyped calculus every object denotes a function, abstraction forms functions, and any term may be applied to any other. The typed calculus restricts such applications, aligns more readily with classical set-theoretic interpretation, and has materially different properties. The historical LISP reference remains a programming-language example rather than a claim of identity with the calculus.
4. **Inductive syntax:** variables and constants are terms; application of two terms and abstraction of a term over a variable produce terms. Removing constants yields the pure calculus. Lowercase object letters and uppercase term metavariables remain distinct. Application associates to the left, abstraction receives the widest scope, and multi-variable abstraction abbreviates nested single-variable abstractions.
5. **Alpha-equivalence and variable status:** alpha-equivalence changes only names of bound variables. The translation preserves the source convention that “same term” includes equality up to such renaming. A variable inside the scope of its governing lambda is bound; the other occurrences are free, exactly as classified in the final example.
6. **Capture-avoiding substitution:** `\Subst{M}{N}{x}` replaces `x` by `N` in `M` only after renaming bound variables of `M` that would capture free variables of `N`. The first displayed substitution keeps `w` harmless. The three alternative notations are retained with the source warning that their slash direction varies.
7. **Beta-reduction:** replacing a redex `(\lambd[x][M])N` by its contractum `\Subst{M}{N}{x}` is beta-contraction. One-step reduction and its reflexive-transitive closure remain distinct. A beta-normal term admits no further contraction. The examples respectively terminate at `y`, grow indefinitely, reproduce themselves unchanged, and reduce along two different first steps to the common term `zv`.
8. **Church--Rosser and normal forms:** if one term reduces to `N_1` and `N_2`, both descendants reduce to some common `P`. If both descendants are normal, neither can take a genuine further step, so each is identical to `P` and the normal form is unique. Common-reduct beta-equivalence is therefore an equivalence relation containing every directed reduction pair, and the source's least-relation qualification is retained.
9. **Currying:** the informal addition example turns each fixed `x` into a unary add-`x` function and then makes `g(x)` return that function. The formal example `\lambd[x][\lambd[y][x]]` accepts two successive inputs and discards the second. The general nested abstraction applies `n` arguments by successive capture-avoiding substitutions into the original body `N`; BN-SRC-267 removes the stray `P` that broke this invariant.
10. **Church numerals and partial representation:** `\num{n}` applies its first input `n` times to its second input and is already normal. A term lambda-defines a `k`-ary partial function exactly when its application to the `k` Church numerals reduces to the numeral of the output on defined inputs and has no normal form on undefined inputs. BN-SRC-268 and BN-SRC-269 make the arity and applied term identical in both branches.
11. **Lambda definability implies computability:** the informal procedure explores every finite reduction path level by level and returns when it reaches a numeral. The rigorous account replaces the appeal to Church's thesis by primitive-recursive codes for subterms, substitutions, one-step reductions, finite reduction sequences, and numerals, followed by a partial recursive search. BN-SRC-270 ensures the initial indexed inputs are full Church numerals.
12. **Computability implies lambda definability:** Kleene's normal-form theorem reduces the task to lambda-defining all primitive-recursive functions and closing the class under the required compositions and unbounded search. Primitive-recursive definability itself reduces to the initial functions plus closure under composition, primitive recursion, and unbounded search. Writing `M(x,y,z)` is explicitly a readability convention; untyped lambda terms have no intrinsic arity.
13. **Initial functions:** zero is the abstraction returning its second argument, hence Church zero. The successor term applies the iterated function once more after the `n` applications supplied by a Church numeral. The nested abstraction for `\fn{Proj}^n_i` returns exactly its `i`th input.
14. **Composition:** if `H` and the `G_i` lambda-define `h` and the component functions `g_i`, the displayed term applies each `G_i` to the same `l` inputs and feeds the `k` results to `H`. It therefore lambda-defines the ordinary componentwise composition without adding a new operation to the calculus.

## Terminology and authority scope

BN-IN-T286 records the core lambda-calculus, notation, term, and definability register; BN-IN-T287 covers abstraction, application, placeholder variables, and the typed/untyped distinction; BN-IN-T288 covers the pure syntax, compound term forms, notation, alpha-equivalence, and bound/free variables; BN-IN-T289 covers capture avoidance, redex/contractum, beta-contraction, reduction, and normality; and BN-IN-T290 covers Church--Rosser, common reducts, normal-form uniqueness, beta-equivalence, and the least equivalence relation.

BN-IN-T291 records currying and function-valued functions; BN-IN-T292 records Church numerals and iteration; BN-IN-T293 records the lambda-definability/computability equivalence, Church's thesis, and reduction-tree search; BN-IN-T294 records the Kleene-normal-form proof route, conventional arity notation, and the three closure operations; and BN-IN-T295 records the basic primitive-recursive lambda definitions and composition closure. Existing T057, T099, T150, T154, T157, T173, T177, T198, and T242 continue to govern successor, substitution, primitive recursion, unbounded search, notation, normal forms, partial computability, beta-equivalence, and free-for-substitution vocabulary.

The checked India-standard pages directly support numbers, variables/constants, algebraic expressions, functions, mappings, and university proof and uniqueness prose. They do not directly attest the complete lambda-specific compounds. Those choices are definition-governed, explicitly provisional, and open to expert correction.

## Validation state

The per-unit checker recognizes all 351 translated target units and passes the twelve reviewed units individually. After state export, the cumulative index contains 4,026 aligned blocks: 3,398 translated and semantically reviewed, and 628 unchanged structural or formal blocks. OLP-0347--OLP-0352 contributes 28 translated blocks. The cumulative 299-unit semantic reader remains the current published reader tranche; reader rebuilding is deferred while source translation continues. The next source gate is the 351-unit public checkpoint with anonymous immutable-archive readback.
