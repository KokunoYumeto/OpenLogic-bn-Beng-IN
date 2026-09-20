+# Semantic review: Lambda Calculus Lambda Definability opening

Review date: 2026-09-21

Locale: `bn-Beng-IN`

Units: OLP-0373--OLP-0375

Scope: 27 aligned source/target blocks covering the Lambda Definability chapter driver, its introduction, and Church-numeral arithmetical functions. Twenty-five blocks contain reviewed Bengali translation and two are unchanged structural or formal blocks.

The Bengali text was read against the frozen English blocks in source order and reverse-paraphrased at the level of Church-numeral representation, reduction-based computation, uniqueness of normal forms, many-place partial lambda definability, constant and identity functions, successor, addition, multiplication, exponentiation, and the need for pairs in predecessor and subtraction. Every source/target pair passes block-count, audited-mathematics, protected-control, environment, semantic-token, and Unicode NFC checks. This is a source and semantic review by the primary translation model; no independent human review, TeX-engine result, or PDF result is claimed.

## Frozen-source identity

The controlling source is OpenLogic revision `9620cc73f9c8e0ad003c514a5d3748f29611c4c0`. Its 722-unit manifest has SHA-256 `5a6fef5c16c15a5b2f90f874c268512cfd6ed2e846bdfa850a67304a4c05a155`. Index generation revalidates each source file hash before accepting the unit.

## Unit coverage

| Unit | File or role | Blocks | Translated | Review focus |
|---|---|---:|---:|---|
| OLP-0373 | Lambda Definability chapter driver | 4 | 2 | Bengali chapter title, experimental editorial note, nine active imports, and the commented lists import |
| OLP-0374 | Introduction | 9 | 9 | Church numerals, computation by reduction, normal-form uniqueness, partial lambda definability, constant and identity functions |
| OLP-0375 | Arithmetical functions | 14 | 14 | Successor, two additions, multiplication, eta simplification, alternate multiplication, exponentiation, predecessor, and subtraction |

## Canon and terminology

The drafting reused exact passages already consulted from the India-standard corpus: BN-IN-P005 for natural-number language; BN-IN-P008 and BN-IN-P009 for mathematical reasoning, variables, binding, and university logic register; BN-IN-P018 and BN-IN-P023 for functions, identity, mappings, domain, and codomain; BN-IN-P019 for variables, constants, sums, and products; and BN-IN-P025 for proof and uniqueness register. Index generation revalidated the original and page-image hashes for every attributed passage.

No new terminology decision was needed. The text applies established decisions T286 for lambda calculus and lambda definability, T289 for reduction and normal form, T290 for Church--Rosser uniqueness, T292 for Church numerals and iteration, T293 for lambda definability and computability, T034 and T057 for arithmetic and successor vocabulary, and T158 for exponentiation as a numerical function. The introduction was also compared directly with the earlier translated OLP-0348 treatment of Church numerals and partial lambda definability; the shared definitions use the same Bengali technical register while the additional explanatory material is translated in full.

## Source review outcome

Two source-level defects are corrected with adjacent Bengali notes and exact checker transformations.

1. **BN-SRC-305 (OLP-0374):** the frozen constant-function example names the function `c_k` but then gives its defining equation as `c(n)=k`. The target restores `c_k(n)=k`, matching both the introduced function name and the representing term `C_k`.
2. **BN-SRC-306 (OLP-0375):** the frozen alternate multiplication term is `a (Add a) 0`. It leaves the bound variable `b` unused and iterates addition of `a` exactly `a` times, yielding `a^2` rather than `ab`. The target uses `a (Add b) 0`, so Church numeral `a` iterates addition of `b` from zero and computes the product.

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

## QA disposition

The strict checker reports 4, 9, and 14 source blocks for OLP-0373, OLP-0374, and OLP-0375 respectively, with matching target counts. It validates the two exact audited transformations, every mathematical token outside those repairs, all protected controls, environments, semantic tokens, and NFC normalization. The segment index records every translated block with the actual canon passages consulted and leaves the two unchanged blocks unattributed. No TeX engine was invoked for this source-only checkpoint. The 374-unit public source checkpoint has been anonymously verified from its immutable archive and raw translation URLs.
