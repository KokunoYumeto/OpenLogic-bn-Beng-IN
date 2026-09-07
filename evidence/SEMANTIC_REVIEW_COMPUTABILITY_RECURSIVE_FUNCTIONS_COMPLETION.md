# Semantic review: Computability — Recursive Functions completion

This review covers OLP-0224 through OLP-0227: Partial Recursive Functions, The Normal Form Theorem, The Halting Problem and General Recursive Functions. I reread every Bengali block against its frozen English block, audited the displayed mathematics and protected controls, and reverse-paraphrased the definitions and diagonal proof. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; index generation revalidates every cited page-image and original-file hash.

## Scope and method

- The four units contain 12 + 4 + 5 + 4 aligned source/target blocks, for 25 aligned blocks in total. All 25 contain Bengali translation and are marked `translated_semantically_reviewed` in the segment index.
- Source-to-target replay passes for every unit: aligned block counts, protected controls, environment order, OpenLogic semantic-token multisets, mathematical fragments and Unicode NFC all agree.
- I consulted BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023 and BN-IN-P025 for number, logic, quantification, relation, function, mapping and proof language. Existing decisions BN-IN-T039, BN-IN-T154, BN-IN-T155 and BN-IN-T168 govern partiality, minimization, recursive classes and diagonalization; BN-IN-T171 through BN-IN-T175 record this batch’s specialized terminology.
- No source defect in these four units was sufficiently established to justify an editorial repair. The frozen source and every mathematical expression are retained.

## Unit review

### OLP-0224 — Partial Recursive Functions

The opening diagonal argument applies to any effectively enumerable class, so an exhaustive class of computable functions cannot consist only of total functions. Allowing partial functions makes an effective enumeration possible. The translation preserves the two required changes to primitive recursion: composition and recursion admit undefined subterms, and unbounded search is added.

Definedness, undefinedness and `\simeq` retain their exact clauses. A composite is defined only when every inner value and the resulting outer application are defined. Unbounded search returns the least input at which the function is zero only after all earlier computations have returned; otherwise it is undefined. The relation form using the characteristic function, the distinction from total minimization, the closure definition of partial recursive functions and the total recursive subclass are all retained. Reverse paraphrase: partiality turns failure to halt into an allowed semantic outcome, and unbounded minimization then supplies the operation needed for the full partial-recursive class.

### OLP-0225 — The Normal Form Theorem

Kleene’s theorem is preserved as a representation by one primitive-recursive relation `T`, one primitive-recursive decoding function `U`, and one unbounded search. The explanation keeps the roles separate: an index names a program or definition, a number records a terminating computation, `T` checks that record from the index and input, and `U` extracts its result. Every partial recursive function has at least one index and in fact infinitely many. Reverse paraphrase: arbitrary partial-recursive definitions can be normalized so that all potentially nonterminating behavior occurs in a single search for a valid computation record.

### OLP-0226 — The Halting Problem

The general problem asks whether the computation named by a specification halts on a given input. In the partial-recursive setting the normal-form index supplies that specification, and the second displayed case definition records whether the indexed computation is defined. The translation retains the distinction between the introductory computability claim and the theorem that the resulting halting function is not partial recursive.

The diagonal proof preserves both cases. Assuming the halting function partial recursive makes `d` partial recursive; `d` is defined exactly when the self-indexed computation is undefined (or the supplied number is not an index), and undefined exactly when that computation is defined. Giving `d` its own index forces either value of the halting function to contradict the corresponding definedness clause. Reverse paraphrase: a total procedure that predicts indexed termination can be fed its own index to construct a computation whose behavior reverses that prediction.

### OLP-0227 — General Recursive Functions

A regular total function has a zero for every parameter tuple, so unbounded search applied to it always returns a value. General recursive functions close the initial functions under composition, primitive recursion and this restricted search. The translation preserves totality and the apparent difference from the earlier definition, which permits partial intermediate functions provided that the final function is total. It also retains the historical warning that “general” is a misleading name and the final equality of the two classes. Reverse paraphrase: restricting minimization to searches guaranteed to succeed changes the presentation but not the resulting class of total recursive functions.

## Technical claim audit

- All file identifiers, labels, cross-references, tag blocks, environments, enumerated cases, definedness macros, minimization terms, normal-form equations and diagonal expressions are preserved.
- Every translated `\text{...}` caption retains its nested mathematics, and the checker compares those mathematical fragments independently of the caption language.
- The stepwise parity audit repaired three draft-only transcription mismatches before indexing: a prose zero had been typeset as an extra math fragment, one computation-code symbol had been omitted, and one index symbol had been repeated. The final targets have exact mathematical-fragment parity.
- No TeX build was attempted. Reader rendering, glyph inspection, semantic HTML validation and final printed-page locators remain pending while the shared TeX mutex is reserved elsewhere.

## Terminology and edition scope

BN-IN-T171 through BN-IN-T175 cover partial-function definedness, unbounded search and recursive subclasses, Kleene normal form and indices, the halting problem, and regular/general recursive functions. The specialized compounds remain provisional and invite expert correction. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set.
