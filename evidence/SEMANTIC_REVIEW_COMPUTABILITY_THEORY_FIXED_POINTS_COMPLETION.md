# Semantic review: Computability Theory — fixed points and chapter completion

This review covers OLP-0247 through OLP-0251: Totality is Undecidable, Rice's Theorem, The Fixed-Point Theorem, Applying the Fixed-Point Theorem and Defining Functions using Self-Reference. I reread every Bengali block against its frozen English block, audited every partial-function equality and fixed-point construction, checked the displayed mathematics and protected controls, and reverse-paraphrased the definitions and proofs. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; index generation revalidates every cited page-image and original-file hash.

## Scope and method

- The five units contain 6 + 14 + 17 + 6 + 4 aligned source/target blocks, for 47 aligned blocks in total. All 47 contain Bengali translation and are marked `translated_semantically_reviewed`.
- Source-to-target replay passes for every unit: aligned block counts, protected controls, environment order, OpenLogic semantic-token multisets, mathematical fragments and Unicode NFC all agree after the seven documented source repairs are normalized for comparison. The Rice corollary's legacy nested math inside a set-builder text caption is parsed by a dedicated checker path on both source and target.
- I consulted BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023 and BN-IN-P025 for number, set, relation, function, composition and proof language. Existing decisions BN-IN-T168, BN-IN-T171, BN-IN-T173, BN-IN-T179 through BN-IN-T182, BN-IN-T184 through BN-IN-T187 and BN-IN-T190 govern computability, partial equality, halting and reductions; BN-IN-T194 through BN-IN-T200 record this batch’s totality, Rice, fixed-point and recursive-definition register.
- BN-SRC-155 through BN-SRC-161 disclose and repair seven frozen-source defects beside their affected arguments. No frozen English byte is changed.

## Unit review

### OLP-0247 — Undecidability of totality

The set `Tot` contains exactly the indices of total unary computable functions. The reduction transforms an index `x` into a program that returns zero on every input if the self-computation at `x` halts and is undefined on every input otherwise. Thus membership in the self-halting set is equivalent to totality of the transformed program. The closing note keeps the stronger claim that `Tot` is not c.e. and locates that result higher in the arithmetical hierarchy without relying on it. Reverse paraphrase: a totality decider would decide whether a program halts on itself by asking whether a uniformly specialized constant-or-nowhere-defined program is total.

BN-SRC-155 changes ordinary equality to `\simeq` in the specialized case definition, because both sides are undefined when `x` is outside the self-halting set.

### OLP-0248 — Rice's theorem

The theorem retains its extensional scope: a decidable set of program indices that depends only on the partial function computed must be trivial. The syntax/behavior explanation correctly leaves decidable syntactic questions about program text outside the theorem and includes semantic questions about halting, any output and even output parity. The proof chooses the nowhere-defined function outside the nontrivial class and one function inside it, then uses a self-halting computation to switch uniformly between them. The s-m-n specialization makes the switch an effective index transformation, reducing the self-halting set to the purported index set. Reverse paraphrase: any effective nontrivial classifier of computed behavior would distinguish a nowhere-defined function from a selected member, and that distinction would reveal self-halting.

BN-SRC-156 restores partial equality in the specialized-function equation. BN-SRC-157 repairs the fourth corollary item so strict increase is required when `y<y'` and both compared values are defined; the frozen prose gives the first definedness clause outside the conditional and introduces only the second with “if.”

### OLP-0249 — The fixed-point theorem

The opening halting argument preserves its named-computation notation and contradiction. The equivalence lemma retains both standard forms: a partial computable binary function has an index that can receive its own index as its first argument, and a total computable transformation of indices has an extensional program fixed point. The main proof builds `diag` by s-m-n specialization, indexes the function that applies `g` to the diagonalized index, and diagonalizes that index itself. Each line of the concluding calculation preserves simultaneous definedness. Reverse paraphrase: an effective program transformer can be fed a program whose code already contains the transformation of its own code, yielding the required extensional self-reference.

The self-printing-program explanation retains the quoted-string substitution, repeated-print variant and replacement of the print skeleton by arbitrary `g`. The tagged lambda section preserves the distinct Curry and Turing fixed-point combinators and their beta-reduction strengths. BN-SRC-158 replaces four ordinary equalities in the two directions of the equivalence lemma with `\simeq`, matching the partial-function statements they prove.

### OLP-0250 — Applying the fixed-point theorem

The first example retains a program whose output adds its own index to the input. The main theorem rules out a partial computable selector that uniformly returns a characteristic-function index whenever a c.e. domain happens to be computable. Its fixed point produces either the singleton `{0}` or the empty set and forces the selected program to disagree at input zero. The Bengali proof also covers the candidate selector being undefined at the fixed index: the resulting domain is empty and computable, while the required selector output is absent. Reverse paraphrase: a uniform effective extractor can be made to select a decider whose zero answer determines a computable set constructed specifically to require the opposite zero answer.

BN-SRC-159 restores the proof's candidate class from total computable functions to the partial computable functions prohibited by the theorem. BN-SRC-160 supplies the omitted case in which `f(e)` itself is undefined before the proof discusses the behavior of the indexed program.

### OLP-0251 — Defining functions by self-reference

The general schema uses the fixed-point theorem to turn a computable case distinction with a recursive indexed call into a partial computable self-referential function. The Euclidean greatest-common-divisor example keeps the argument order of the remainder and recursive call. The fixed-point result establishes partial computability, while descent and induction establish totality. The closing comparison correctly distinguishes ordinary recursive self-definition from the stronger ability to define behavior through an index of the implementing algorithm. Reverse paraphrase: the fixed-point theorem validates recursive equations as partial computations, and a separate termination argument proves that a particular recursion is total.

BN-SRC-161 restores `\simeq` in the fixed-point equation after the general schema, where both sides may be undefined.

## Technical claim audit

- All file identifiers, labels, cross-references, tag blocks, verbatim programs, environments, totality and index-set definitions, universal-function applications, s-m-n specializations, diagonal equations, lambda terms and recursive gcd expressions are preserved except the exact equality substitutions documented by BN-SRC-155, BN-SRC-156, BN-SRC-158 and BN-SRC-161.
- The checker accepts only the audited fragment-counter differences for those partial equalities. It separately asserts the strict-increase repair BN-SRC-157 and the partial-selector scope and missing-case repairs BN-SRC-159 and BN-SRC-160.
- All seven correction notes share the target file hash recorded in the correction ledger and are stripped before structural comparison. Every translated block cites the canon pages actually consulted.
- No TeX build was attempted. Reader rendering, glyph inspection, semantic HTML validation and final printed-page locators remain pending while the shared TeX mutex is reserved elsewhere.

## Terminology and edition scope

BN-IN-T194 through BN-IN-T200 cover totality and `Tot`, Rice's theorem and index invariance, program syntax versus behavior, the fixed-point theorem and diagonal specialization, Curry and Turing combinators, characteristic-function index extraction, and recursive self-definition. The specialized compounds remain provisional and invite expert correction. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set. With OLP-0251, every source unit in the Computability Theory chapter is translated and semantically reviewed.
