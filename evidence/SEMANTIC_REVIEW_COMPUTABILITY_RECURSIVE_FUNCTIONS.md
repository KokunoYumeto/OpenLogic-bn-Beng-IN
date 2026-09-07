# Semantic review: Computability — Recursive Functions opening

This review covers OLP-0208 through OLP-0212, the Computability part driver, the Recursive Functions chapter driver, the introduction, Primitive Recursion and Composition. I reread every Bengali block against its frozen English block, checked every displayed formula and source control, and reverse-paraphrased the computational claims. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; the indexed passage images and original files are hash-verified during index generation.

## Scope and method

- OLP-0208 is the Computability part driver; OLP-0209 is the Recursive Functions chapter driver; OLP-0210 through OLP-0212 are the first three reader units.
- The five units contain 5 + 21 + 4 + 7 + 7 aligned source/target blocks respectively, for 44 aligned blocks in total. Structural driver blocks and displayed formal material remain unchanged; translated prose is marked `translated_semantically_reviewed` in the segment index.
- Every unit passes source-to-target replay. Source and target block counts agree; protected controls, environment order, OpenLogic semantic-token multisets, mathematical fragments and Unicode NFC agree. No source-correction record is introduced in this opening batch.
- The Bengali register follows the established India-standard choices: গণনসাধ্যতা for computability, গণনসাধ্য for computable, অপেক্ষক for function, পুনরাবৃত্ত for recursive, আদিম পুনরাবৃত্তি for primitive recursion, মিশ্রণ for composition and অভিক্ষেপ for projection. Formal macros, indices, arities and displayed calculations are retained.

## Unit review

### OLP-0208 — Computability part driver

The part title identifies computability and preserves the two chapter imports, the source editorial attribution to Jeremy Avigad and the end hook. Reverse paraphrase: the part remains the same two-chapter computational sequence, with the source's note that motivation, examples and exercises can be expanded.

### OLP-0209 — Recursive Functions chapter driver

The chapter title identifies recursive functions and retains all seventeen section imports in their frozen order. The editorial note preserves Avigad's authorship, Richard Zach's revision, the presence of exercises and the independent use of the chapter for arithmetization of syntax. Reverse paraphrase: the driver exposes exactly the same chapter boundary and pedagogical purpose.

### OLP-0210 — Introduction

The introduction motivates a mathematical model of computation through numerical functions on natural numbers. It explains why addition, multiplication and exponentiation suggest recursive definitions, then identifies primitive recursion as the central simple pattern. The second paragraph reduces computable sets and relations to characteristic functions and retains the divisibility example. The closing paragraph distinguishes primitive recursive functions from the broader class obtained by unbounded search, defines the relation between partial and general recursive functions, and lists Turing machines and lambda calculus as simulable models. Reverse paraphrase: the section moves from numerical computation to a function-based account of computability and then previews the later extensions.

### OLP-0211 — Primitive Recursion

The section explains base and successor clauses for a one-place function, computes the example $h(x)=2^x$, and states uniqueness of the recursively specified function. It then defines addition and multiplication by fixing one argument, works through $\Add(2,3)$ and $\Mult(2,3)$, and gives the general $f/g$ schema for $h(x_0,\dots,x_{k-1},y)$. Reverse paraphrase: primitive recursion uses the initial value at zero and only the immediately preceding value at the successor step; the final schema correctly separates the fixed parameters, the recursion index and the prior output.

### OLP-0212 — Composition

The section generalizes one-place composition to a $k$-place outer function and $n$-place inner functions. It introduces projection functions to ignore, repeat or reorder arguments, then handles the apparent arity restriction through a worked three-place example with an auxiliary $l$. Reverse paraphrase: composition remains closed for computable functions, and projections supply the wiring needed to express ordinary argument manipulation without changing the formal arities.

## Technical claim audit

- All imports, part/chapter identifiers, section identifiers and end hooks are preserved.
- The primitive-recursion displays retain every index, successor, multiplication, addition, projection-free $f/g$ schema and intermediate numerical value.
- The composition displays retain the exact $k$- and $n$-place formulas, every `\Proj` index, the reordered arguments and the auxiliary $l$ definition.
- No source formula was silently corrected. The public checker compares normalized mathematical fragments and protected controls; all five units pass those checks.

## Terminology and edition scope

Decisions BN-IN-T150 onward record the computability, recursive-function, primitive-recursion, composition, projection and arity register. The checked number, logic, relation, mapping and proof witnesses support the component Bengali roots; specialized computability compounds remain provisional and open to expert review. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set.

## Remaining release boundary

This is source evidence, not a reader release. No TeX attempt was made because the shared global TeX mutex is reserved by the Persian reader lane. PDF rendering, glyph inspection, semantic HTML checks, printed-page locators and release-level archive readback remain pending under that policy.
