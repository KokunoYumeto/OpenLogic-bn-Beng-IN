# Semantic review: Computability — coding and diagonal arguments

This review covers OLP-0219 through OLP-0223: Primes, Sequences, Trees, Other Recursions and Non-Primitive Recursive Functions. I reread every Bengali block against its frozen English block, audited the displayed mathematics and protected controls, and reverse-paraphrased the number-theoretic coding and diagonal arguments. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; index generation revalidates every cited page-image and original-file hash.

## Scope and method

- The five units contain 7 + 21 + 6 + 4 + 8 aligned source/target blocks, for 46 aligned blocks in total. All 46 contain Bengali translation and are marked `translated_semantically_reviewed` in the segment index.
- Source-to-target replay passes for every unit: aligned block counts, protected controls, environment order, OpenLogic semantic-token multisets, mathematical fragments and Unicode NFC all agree after the single documented prose repair is removed for comparison.
- I consulted BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023 and BN-IN-P025 for number, logic, quantification, relation, function, mapping and proof language. Existing decisions BN-IN-T019, BN-IN-T031, BN-IN-T043, BN-IN-T044 and BN-IN-T157 govern sequence, tree, coding, diagonalization and notation language; BN-IN-T164 through BN-IN-T170 record this batch’s specialized terminology.
- BN-SRC-141 corrects one reversed dividend/divisor description beside the affected paragraph. The frozen source remains unchanged and the checker asserts the exact Bengali repair.

## Unit review

### OLP-0219 — Primes

The section defines x dividing y by a bounded existential witness to x times z equals y, then defines primality through nontriviality and bounded checking of every divisor. The prime-enumerating function starts with two and advances through the least larger prime. Euclid’s factorial bound turns that next-prime search into bounded minimization, so both next-prime and the enumeration are primitive recursive. The parenthetical proof preserves the product of all primes at most x, the remainder-one argument for p plus one, and the factorial upper bound. Reverse paraphrase: arithmetic already shown primitive recursive, together with bounded quantification and minimization, suffices to decide divisibility and primality and to compute the prime at any index.

The source’s explanation of x not dividing y says that the remainder is obtained when x is divided by y. This reverses the relation just defined and the later witness equation. BN-SRC-141 changes only that Bengali prose to the remainder when y is divided by x; all symbols and displayed formulas remain unchanged.

### OLP-0220 — Sequences

Finite natural-number sequences are encoded by consecutive prime powers whose exponents are each one more than the corresponding entry. Adding one distinguishes trailing zeros, and zero is selected as the empty-sequence code. Unique prime factorization gives injectivity. The length function finds the last consecutive prime divisor; append multiplies by the next prime power; element extraction searches for the first nondividing higher power and returns zero outside the sequence. Compact tuple and concatenation notation are then introduced.

The helper concatenation recursion appends the first n elements of its second input. A numerical sequence bound follows from the maximum prime factor and exponent; the alternate bounded-search specification preserves both length and each element of the two input sequences. The iterated concatenation, tail and subsequence exercises remain intact. Reverse paraphrase: every elementary operation on finite sequences reduces to primitive-recursive arithmetic on their unique prime-power codes.

### OLP-0221 — Trees

A tree is coded recursively as a sequence whose first entry counts immediate subtrees and whose following entries are their codes, with optional node labels afterward. The two worked code shapes preserve the single labeled node and the labeled binary-root example. `ISubtrees` extracts the immediate-subtree portion. The helper recursion accumulates the root and successively generated immediate subtrees; the tree code bounds its depth, so running to that bound lists every subtree code. Reverse paraphrase: because a tree is a finite nested sequence, previously established sequence operations implement a primitive-recursive traversal. The final exercise still asks for a repetition-free variant.

### OLP-0222 — Other Recursions

The first scheme advances two functions simultaneously from their respective base values and shared prior outputs. The course-of-values scheme supplies the entire sequence of earlier h-values to the next computation and thereby permits access to any earlier value selected by k. The remainder exercise and the final parameter-changing scheme are preserved, including the warning that reduction to ordinary primitive recursion requires a careful unwinding. Reverse paraphrase: pairing and sequence coding store the extra state needed to simulate these richer-looking recursions with the ordinary primitive-recursion constructor.

### OLP-0223 — Non-Primitive Recursive Functions

The section effectively enumerates all unary primitive recursive functions and defines their evaluation function g. The diagonal h at x is the x-th listed function evaluated at x plus one, so h differs from each listed function at its own index; h and g are computable but cannot be primitive recursive. The fast-growing sequence retains successor at level zero, x-fold iteration at the next level, the stated values of the first levels and the Ackermann--Péter diagonal.

The notation codes for zero, successor, projection, composition and recursion are preserved exactly as finite sequence codes. Invalid codes receive the constant-zero function, producing an explicit enumeration with unavoidable repetitions. The last discussion explains how an evaluator unpacks a code and computes the represented function; the tagged digression distinguishes an appeal to the Church--Turing thesis from a direct Turing-machine construction and previews simulation by recursive functions. Reverse paraphrase: finite syntactic descriptions can be enumerated and evaluated, but diagonalizing over that enumeration constructs a computable function outside the primitive-recursive class.

## Technical claim audit

- All file identifiers, labels, cross-references, tag blocks, environments, tuple and sequence macros, prime indices, exponent bounds, recursion equations and notation codes are preserved.
- Every occurrence of a translated `\text{...}` or `\mbox{...}` caption retains its nested mathematics, and the public checker compares those mathematical fragments independently of the caption language.
- BN-SRC-141 is recognized from its paired correction markers and by an exact assertion that the Bengali sentence uses y as dividend and x as divisor. No mathematical parity exception is needed because the defect occurs only in prose.
- No TeX build was attempted. Reader rendering, glyph inspection, semantic HTML validation and final printed-page locators remain pending while the shared TeX mutex is reserved elsewhere.

## Terminology and edition scope

BN-IN-T164 through BN-IN-T170 cover divisibility and prime arithmetic, finite-sequence operations, coded-tree vocabulary, simultaneous and course-of-values recursion, the effective diagonal argument, the Ackermann--Péter name and the Church--Turing/Turing-machine register. The specialized compounds remain provisional and invite expert correction. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set.
