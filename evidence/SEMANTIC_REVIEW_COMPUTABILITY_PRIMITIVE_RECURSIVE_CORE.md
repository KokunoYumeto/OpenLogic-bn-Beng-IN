# Semantic review: Computability — primitive-recursive core

This review covers OLP-0213 through OLP-0218: Primitive Recursion Functions, Primitive Recursion Notations, Primitive Recursive Functions are Computable, Examples of Primitive Recursive Functions, Primitive Recursive Relations and Bounded Minimization. I reread every Bengali block against its frozen English block, checked the displayed mathematics and protected controls, and reverse-paraphrased the definitions and arguments. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; index generation also revalidates the hashes of every cited page image and original file.

## Scope and method

- The six units contain 15 + 5 + 4 + 21 + 12 + 6 aligned source/target blocks, for 63 aligned blocks in total. All 63 contain Bengali translation and are marked `translated_semantically_reviewed` in the segment index.
- Source-to-target replay passes for every unit: block counts agree, protected controls and environment order agree, OpenLogic semantic-token multisets agree, audited mathematical fragments agree and every target is Unicode NFC.
- I consulted the established India-standard witnesses BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023 and BN-IN-P025 for number, logic, quantification, relation, function, mapping and proof language. Specialized computability terms are documented in decisions BN-IN-T150 through BN-IN-T163.
- Two frozen-source defects are corrected visibly and recorded as BN-SRC-139 and BN-SRC-140. Both repairs are narrow, mechanically asserted and leave the frozen source untouched.

## Unit review

### OLP-0213 — Primitive Recursion Functions

The section restates the two constructors precisely: primitive recursion from a k-place base function and a k+2-place step function, and composition from one k-place outer function and k many n-place inner functions. It adds zero, successor and projections as starting functions and defines the primitive recursive class as the least class closed under both constructors. The stage description preserves S-zero and the union over all natural stages. The addition proof retains the projection used for the base case and the composition that turns the unary successor into the required three-place step function. Multiplication remains an exercise. The final worked example preserves the dummy argument and the successive compositions used to show that the power-of-two recursion is primitive recursive. Reverse paraphrase: every claimed member is obtained by a finite construction from the three basic function families using only composition and primitive recursion.

### OLP-0214 — Primitive Recursion Notations

The section assigns formal terms to construction trees. `Comp` records the arities and the notation for the outer and inner functions; `Rec` records the base and step notation. The full notation for addition retains the projection, successor, composition and recursion indices, and the multiplication notation remains the exercise. Reverse paraphrase: the notation gives each finite primitive-recursive construction a systematic syntactic code, which later supports enumeration.

### OLP-0215 — Primitive Recursive Functions are Computable

The argument expands the primitive recursion equations at zero, one, two, three and four, then states the general successive procedure through the requested y. It separately preserves closure of computability under composition. Since zero, successor and projection are computable, structural induction over the defining construction proves that every primitive recursive function is computable. Reverse paraphrase: each recursion stage calls computable functions only finitely many times, and every construction tree starts from computable leaves.

### OLP-0216 — Examples of Primitive Recursive Functions

The opening examples retain identity and constant functions and show how constants enter later compositions. Exponentiation preserves its informal recursion and the arity-correct base and step functions. Predecessor preserves the dummy-argument repair; factorial preserves its two-place auxiliary recursion. Truncated subtraction, absolute difference, maximum and the minimum exercise remain distinct. The iterated exponentiation and integer-division problems are retained, including the stipulated value at division by zero. The closure proposition preserves inclusive finite sums and products and the displayed recursion for finite sums. Reverse paraphrase: familiar arithmetic operations are built from the primitive-recursive constructors, while the explicit projections and dummy arguments make the informal recurrences formally well-typed.

### OLP-0217 — Primitive Recursive Relations

The definition identifies a primitive recursive relation through its zero-one characteristic function and retains the `IsZero` recursion. Equality is recovered from absolute difference. The next displayed formula is x less than or equal to y and is defined by zero-testing truncated subtraction; the frozen prose calls it less-than. BN-SRC-139 therefore translates the mathematically defined relation as the less-than-or-equal relation (`অনধিক সম্বন্ধ`) and records the discrepancy beside the passage.

The Boolean-closure proof preserves the characteristic functions for negation, conjunction, disjunction and implication. Bounded universal quantification is implemented as iterated minimum with the true empty case, and bounded existential quantification as iterated maximum or by duality; the conversion from a non-strict bound to a strict successor bound is retained. The conditional function and the proposition on definitions by cases preserve the priority order among the relations and the default branch. Reverse paraphrase: zero-one characteristic functions turn logical operations and bounded quantifiers into already established primitive-recursive arithmetic operations.

### OLP-0218 — Bounded Minimization

The section distinguishes unbounded least-number search from search below an independently supplied bound. It defines the result as the least witness below y, returning y when there is none. The proof preserves the zero-bound case and the three successor-bound cases: an earlier witness persists, y becomes the first witness, or y+1 records continued failure. In the third source case, the left-hand side unexpectedly changes the fixed parameter vector from x to z. BN-SRC-140 restores the x-vector used throughout the definition and records the repair beside the list. The final recurrence and the equivalence between an earlier witness and a result unequal to y are unchanged in meaning; the closing exercise instead asks for a zero default. Reverse paraphrase: a bounded search can remember the least witness through primitive recursion because each new bound requires only one decidable test.

## Technical claim audit

- All file identifiers, labels, references, problem and proposition boundaries, list structures, macros, indices, arities and displayed numerical or algebraic expressions are preserved except for the two documented source repairs.
- BN-SRC-139 is checked by an exact target-prose assertion requiring the less-than-or-equal name for the formula `x \leq y`; BN-SRC-140 is checked by an exact mathematical transformation requiring `m_R(\vec{x},y+1)=y+1` in the third case.
- The math-part comparison now treats `\mbox{...}` like the existing `\text`, `\textrm` and `\emph` text-bearing wrappers. This lets Bengali case captions vary linguistically while the nested mathematical fragments remain subject to parity checking.
- No TeX build was attempted. Reader rendering, glyph inspection, semantic HTML validation and printed-page locators remain outside this source-draft checkpoint while the shared TeX mutex is reserved elsewhere.

## Terminology and edition scope

BN-IN-T157 through BN-IN-T163 add the construction-notation, arithmetic-operation, finite sum/product, integer-division, primitive-recursive-relation, Boolean-operation, bounded-quantification, conditional-function, definition-by-cases and bounded-minimization vocabulary used here. These decisions are provisional and invite expert correction. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set.
