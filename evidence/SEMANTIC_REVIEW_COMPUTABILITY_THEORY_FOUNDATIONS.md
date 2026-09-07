# Semantic review: Computability Theory foundations

This review covers OLP-0228 through OLP-0233: the Computability Theory chapter driver, Introduction, Coding Computations, The Normal Form Theorem, The s-m-n Theorem and The Universal Partial Computable Function. I reread every Bengali block against its frozen English block, audited the displayed mathematics and protected controls, and reverse-paraphrased the definitions and proofs. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; index generation revalidates every cited page-image and original-file hash.

## Scope and method

- The six units contain 26 + 6 + 4 + 11 + 4 + 4 aligned source/target blocks, for 55 aligned blocks in total. Thirty-one blocks contain Bengali translation and are marked `translated_semantically_reviewed`; the chapter driver’s twenty-three unchanged section imports and its end hook account for the other twenty-four formal blocks.
- Source-to-target replay passes for every unit: aligned block counts, protected controls, environment order, OpenLogic semantic-token multisets, mathematical fragments and Unicode NFC all agree after the two documented source repairs are normalized for comparison.
- I consulted BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023 and BN-IN-P025 for number, logic, quantification, relation, function, mapping and proof language. Existing decisions BN-IN-T043, BN-IN-T154, BN-IN-T171 through BN-IN-T173 and BN-IN-T180 govern sequence coding, minimization, partiality and normal form; BN-IN-T176 through BN-IN-T180 record this batch’s field and computation vocabulary.
- BN-SRC-142 and BN-SRC-143 disclose and repair two frozen-source defects beside the affected explanations. No frozen English byte is changed.

## Unit review

### OLP-0228 — Computability Theory chapter driver

The chapter identity and editorial warning are translated. All twenty-three section imports remain byte-identical and in source order, followed by the unchanged chapter-end hook. Reverse paraphrase: this chapter develops computability independently of a chosen machine model and remains marked for later expansion because it has no exercises.

### OLP-0229 — Introduction

The introduction distinguishes partial computable functions from total computable functions and defines computable relations through their characteristic functions. Definedness, undefinedness and equality of partial terms retain the same clauses as the preceding chapter. A universal partial computable function supplies indexed enumerations at arbitrary arities. The minimization convention still requires all earlier values to be defined before the first zero.

The final comparison preserves both proof methods: an explicit Turing-machine or partial-recursive construction, and an algorithm plus Church’s thesis. The middle course demands enough operational detail to recover a rigorous construction in principle. Reverse paraphrase: the theory may reason model-independently once universal indexing and minimization are available, while concrete computability proofs still need a defensible bridge to a formal model.

### OLP-0230 — Coding Computations

Four capabilities are preserved: systematic descriptions of programs, full records of individual computations, decidable verification of proposed records, and extraction of the final value. Numerical indices computably recover instructions, while a single number can encode a full trace. The relation saying that a number codes an indexed computation and the function extracting its output are both stated to be primitive recursive. Reverse paraphrase: finite descriptions and traces can be arithmetized strongly enough that later theorems depend only on their codes, not on the original machine formalism.

### OLP-0231 — The Normal Form Theorem

The opening search/check/extract procedure and Kleene theorem preserve the primitive-recursive relation `T`, decoder `U`, and one unbounded minimization. The proof sketch keeps the two coding tasks separate and states that both the validity test and output extraction are primitive recursive. The explanation accurately weakens what most applications need to computability of `T` and `U` plus totality of `U`.

The fixed enumeration and defining equation for the indexed functions are retained. The final theorem and padding argument show that every partial computable function has infinitely many indices: a description may perform a harmless extra computation before running the same program. Reverse paraphrase: every partial computation can be located by searching finite certified traces, and redundant descriptions make its index highly nonunique.

### OLP-0232 — The s-m-n Theorem

The displayed equation fixes the first `m` inputs of an `(m+n)`-ary indexed program and returns an index for the resulting `n`-ary function. The Turing-machine gloss prepends those fixed inputs and runs the original indexed machine. Reverse paraphrase: program text can be transformed effectively so that some data is compiled into it while the remaining arguments stay live.

The frozen explanation changes the program index from `e` to an unintroduced `x` in both the returned-program expression and the Turing-machine description. BN-SRC-142 restores `e` in both places, matching the theorem statement; the checker admits exactly those two mathematical substitutions and asserts their values.

### OLP-0233 — The Universal Partial Computable Function

Normal form defines a binary partial computable evaluator whose rows include every unary partial computable function. The explanation retains joint, uniform computation from index and input, and it explains how sequence coding extends universality to higher arities. Reverse paraphrase: a single partial evaluator simulates every indexed program, so its first argument selects a member of an effective enumeration.

The final example starts with a three-place partial recursive function and composes it with three sequence projections. The source calls the result a unary recursive function, although no totality premise is present. BN-SRC-143 corrects only that prose classification to unary partial recursive function; the displayed formula is unchanged.

## Technical claim audit

- All file identifiers, chapter imports, labels, cross-references, tag blocks, environments, enumerations, definedness macros, minimization terms, T/U equations and indexed-function expressions are preserved except the two precisely documented `x`-to-`e` substitutions in BN-SRC-142.
- BN-SRC-142 is accepted only when the source-only and target-only mathematical-fragment counters contain exactly the two audited index changes. BN-SRC-143 is asserted against the premise and exact repaired Bengali classification.
- The driver’s unchanged imports are recorded as `unchanged_structural_or_formal` without canon attribution; every linguistically translated block cites the canon pages actually consulted.
- No TeX build was attempted. Reader rendering, glyph inspection, semantic HTML validation and final printed-page locators remain pending while the shared TeX mutex is reserved elsewhere.

## Terminology and edition scope

BN-IN-T176 through BN-IN-T180 cover computability/recursion theory, partial and total computability classes, computation records and sequences, program specialization, and the universal partial computable function. The specialized compounds remain provisional and invite expert correction. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set.
