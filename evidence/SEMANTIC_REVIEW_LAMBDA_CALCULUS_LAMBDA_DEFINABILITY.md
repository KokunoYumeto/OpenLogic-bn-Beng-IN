# Semantic review: Lambda Calculus Lambda Definability

Review date: 2026-09-21

Locale: `bn-Beng-IN`

Units: OLP-0373--OLP-0378

Scope: 58 aligned source/target blocks covering the Lambda Definability chapter driver, its introduction, Church-numeral arithmetic, ordered pairs and predecessor, truth values and relations, and primitive-recursive functions. Fifty-six blocks contain reviewed Bengali translation and two are unchanged structural or formal blocks.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of Church-numeral representation, reduction-based computation, uniqueness of normal forms, many-place partial lambda definability, arithmetic, pair-state predecessor and subtraction, selector encodings of truth, lambda-definable relations, Boolean operations, and closure of lambda definability under composition and primitive recursion. Every source/target pair passes block-count, audited-mathematics, protected-control, environment, semantic-token, and Unicode NFC checks. This is a source and semantic review by the primary translation model; no independent human review, TeX-engine result, or PDF result is claimed.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index generation revalidates each source file hash before accepting the unit.

## Unit coverage

| Unit | File or role | Blocks | Translated | Review focus |
|---|---|---:|---:|---|
| OLP-0373 | Lambda Definability chapter driver | 4 | 2 | Bengali chapter title, experimental editorial note, nine active imports, and the commented lists import |
| OLP-0374 | Introduction | 9 | 9 | Church numerals, computation by reduction, normal-form uniqueness, partial lambda definability, constant and identity functions |
| OLP-0375 | Arithmetical functions | 14 | 14 | Successor, two additions, multiplication, eta simplification, alternate multiplication, exponentiation, predecessor, and subtraction |
| OLP-0376 | Pairs and predecessor | 6 | 6 | Pair encoding, constructor, projections, pair-state predecessor, and truncated subtraction |
| OLP-0377 | Truth values and relations | 8 | 8 | Selector encoding, relation definability, zero test, negation, conjunction, and disjunction exercise |
| OLP-0378 | Primitive recursive functions | 17 | 17 | Basic representers, closure under composition, pair-state primitive recursion, induction, and final reduction |

## Canon and terminology

The drafting reused exact passages already consulted from the India-standard corpus: BN-IN-P005 for natural-number language; BN-IN-P008 and BN-IN-P009 for mathematical reasoning, variables, binding, and university logic register; BN-IN-P012 for ordered-pair language; BN-IN-P018 and BN-IN-P023 for functions, identity, mappings, domain, and codomain; BN-IN-P019 for variables, constants, sums, and products; and BN-IN-P025 for proof and uniqueness register. Index generation revalidated the original and page-image hashes for every attributed passage.

The text applies established decisions T017 for ordered pairs, T034 and T057 for arithmetic and successor vocabulary, T043/T061/T062 for truth functions, truth values and the principal Boolean operations, T115 for projections, T150 for primitive recursion, T158 for exponentiation and truncated subtraction, T286 for lambda calculus and lambda definability, T289 for reduction and normal form, T290 for Church--Rosser uniqueness, T292 for Church numerals and iteration, T293 for lambda definability and computability, and T295/T296 for the basic primitive-recursive functions, composition closure and pair-state construction. New provisional decision T310 records `নির্বাচক` and `নির্বাচকরূপে সত্যমানের উপস্থাপন`; the displayed first-or-second-argument behavior governs the meaning, while the checked canon supports only the surrounding logic and function register. The introduction was also compared directly with the earlier translated OLP-0348 treatment of Church numerals and partial lambda definability; the shared definitions use the same Bengali technical register while the additional explanatory material is translated in full.

## Source review outcome

Six source-level defects are corrected with adjacent Bengali notes and exact checker transformations.

1. **BN-SRC-305 (OLP-0374):** the frozen constant-function example names the function `c_k` but then gives its defining equation as `c(n)=k`. The target restores `c_k(n)=k`, matching both the introduced function name and the representing term `C_k`.
2. **BN-SRC-306 (OLP-0375):** the frozen alternate multiplication term is `a (Add a) 0`. It leaves the bound variable `b` unused and iterates addition of `a` exactly `a` times, yielding `a^2` rather than `ab`. The target uses `a (Add b) 0`, so Church numeral `a` iterates addition of `b` from zero and computes the product.
3. **BN-SRC-307 (OLP-0376):** the frozen predecessor explanation writes its initial state and zero-case result as the raw pair `(0,0)`, although raw natural numbers are not pure lambda terms and the displayed definition uses Church numeral terms. The target uses the pair of Church-zero terms in both explanatory occurrences.
4. **BN-SRC-308 (OLP-0377):** the frozen relation definition declares `R` as a subset of `Nat^n`, but every input and truth condition uses the `k`-tuple `n_1,...,n_k`. The target declares `R` as a subset of `Nat^k`.
5. **BN-SRC-309 (OLP-0378):** the frozen composition lemma gives `k` component functions `g_0,...,g_{k-1}` but lists representers through the extra `G_k`, then concludes that undefined uppercase `H` is lambda definable instead of the composed function `h`. The target ends the list at `G_{k-1}` and concludes that `h` is lambda definable; uppercase `H` remains the representing term in the proof.
6. **BN-SRC-310 (OLP-0378):** the frozen primitive-recursion successor clause applies `h` with `n+2` arguments and the following prose says that `h` is iterated, although `g` is the declared step function and the later state transformer applies its representer `G`. The target restores `g` in the clause and describes iteration of the `g`-based state transformer.

The frozen files use several chapter-component identifiers—`rep`, `ldf`, and later `dfl`—inside the same physical chapter. No cross-reference in the reviewed scope establishes a unique intended normalization, so all three protected identifiers are preserved here rather than silently changed. The inconsistent spelling `lambda-definablity` occurs only in a source comment and is likewise preserved because it has no rendered or referential effect.

## Reverse-paraphrase checks

1. **Chapter structure:** the driver labels the chapter Lambda Definability, retains the warning that the material is experimental, and preserves all nine active section imports plus the commented-out lists import.
2. **Abstract syntax versus numbers:** lambda-calculus syntax denotes functions and their application without privileging natural numbers. Application and abstraction apply to arbitrary functions, which is why the later numerical interpretation requires an explicit encoding.
3. **Church numerals:** for each natural number `n`, `num(n)` is `lambda f x. f^n(x)`. The examples preserve zero as `lambda f x.x` and three as three nested applications of `f`.
4. **Computation:** applying a term `F` to a Church numeral and reducing to `num(m)` reads `m` as output. The Bengali text preserves the biconditional `f(n)=m` exactly when `F num(n)` reduces to `num(m)`.
5. **Uniqueness:** Church--Rosser gives uniqueness only when a normal form exists. The target does not claim termination; it says that if `F num(n)` reduces to a normal-form numeral, no distinct normal-form term can also be its result.
6. **Partial definability:** a term lambda-defines a many-place partial function when defined inputs reduce to the corresponding Church numeral and undefined inputs have no normal form. The target preserves all `k` arguments and the undefined branch.
7. **Simple examples:** `C_k = lambda x.num(k)` ignores its input and represents the constant function `c_k`; `lambda x.x` represents identity. BN-SRC-305 keeps the function name consistent in its defining equation.
8. **Successor:** `Succ` applies the encoded iterator once more, changing `f^n(x)` to `f(f^n(x))`. The full reduction at zero still ends at `num(1)`, and the alternate successor is retained as an exercise.
9. **Addition:** the first term composes `n` iterations with `m` iterations to obtain `f^(n+m)(x)`. The second iterates the successor operation `n` times from `m`, again yielding `num(n+m)`.
10. **Multiplication:** `Mult` iterates the function “apply `f` `m` times” a further `n` times, producing `n*m` applications and the numeral `num(nm)`. The editorial eta-reduced form remains explicitly conditional on first explaining eta reduction.
11. **Alternate multiplication:** after BN-SRC-306, `a (Add b) 0` starts at zero and adds `b` a total of `a` times. Both bound operands now participate, and the exercise genuinely asks for a proof of multiplication.
12. **Exponentiation:** `Exp = lambda b e. e b` treats the encoded exponent as an iterator over the base. The expanded alternative iterates multiplication by `b` from one, preserving the same base/exponent order.
13. **Boundary to the next construction:** predecessor and subtraction are not claimed to follow from the simple iterators already given. The section ends by identifying an encoding of ordered pairs as the needed next device.
14. **Pair encoding:** the pair of `M` and `N` is the function `lambda f.fMN`. The constructor returns this encoding, while `Fst` and `Snd` pass it selectors that return the first and second components respectively.
15. **Predecessor state:** the predecessor iterator starts at the pair of Church zeroes and maps a state `p` to the pair consisting of its second component and that component's successor. After zero steps it remains `(0,0)`; after positive `n` steps it is `(n-1,n)`, so `Fst` returns the predecessor. BN-SRC-307 keeps every state component inside the pure lambda calculus.
16. **Truncated subtraction:** `Sub a b` applies `Pred` to `a` exactly `b` times. Because predecessor stays at zero, this is truncated rather than integer subtraction.
17. **Truth as selection:** `true` returns its first argument and `false` its second. T310's Bengali selector term is governed directly by these reductions, not by an assumed external Boolean type.
18. **Relations:** a `k`-place relation is lambda definable when its representing term reduces on `k` Church numerals to `true` exactly when the relation holds and to `false` otherwise. BN-SRC-308 makes the declared arity agree with both branches.
19. **Zero test:** `IsZero` begins at `true` and uses a step that always returns `false`. Church numeral zero performs no step, while every positive numeral performs at least one, giving exactly the intended characteristic relation.
20. **Boolean operations:** `Not x` swaps the two selector results. `And x y` asks `x` to choose between `y` and `false`, so it returns true exactly when both encoded truth values are true. The caveat that arbitrary lambda terms need not yield encoded truth values is retained, as is the exercise to define inclusive and exclusive disjunction.
21. **Basic primitive-recursive functions:** the displayed terms represent zero, successor and each projection. The target preserves the distinction between the numerical functions and their uppercase or `fn`-marked representing lambda terms.
22. **Composition closure:** if `F` represents `f` and `G_0,...,G_{k-1}` represent the component functions, the displayed `H` feeds every component result into `F`. BN-SRC-309 aligns the representer range and the lowercase function named in the conclusion without changing uppercase `H` in the construction.
23. **Primitive-recursion equation:** the base value is `f(x_1,...,x_n)` and the successor value applies the `n+2`-place step function `g` to the parameters, current index and prior `h` value. BN-SRC-310 restores that declared invariant.
24. **Pair-state transformer:** for one parameter `x`, `D` maps a state pair to the successor of its first component paired with `G x` applied to the old index and old result. Iterating `D` with Church numeral `y` from `(0,Fx)` therefore computes the recursion while carrying its index explicitly.
25. **Induction and final extraction:** the proof establishes `D_n^m(0,F n)` reduces to `(m,h(n,m))` by the zero and successor cases, then applies `Snd` to obtain `h(n,m)`. Every occurrence of `g(n,m,h(n,m))=h(n,m+1)` remains aligned with the corrected recursion equation.

## QA disposition

The strict checker reports 4, 9, 14, 6, 8, and 17 source blocks for OLP-0373 through OLP-0378 respectively, with matching target counts. It validates all six exact audited repairs, every mathematical token outside those repairs, all protected controls, environments, semantic tokens, and NFC normalization. The segment index records every translated block with the actual canon passages consulted and leaves the two unchanged blocks unattributed. The multiline tuple derivation and dotted `\lambd[p].` notation in OLP-0378 are preserved from the frozen source; no unsupported normalization is claimed. No TeX engine was invoked for this source-only checkpoint. The 377-unit public source checkpoint has been anonymously verified from its immutable archive and raw translation URLs.
