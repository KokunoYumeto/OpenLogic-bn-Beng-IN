# Semantic review: Turing Machine Computations — completion

This review covers OLP-0258 through OLP-0263: Unary Representation of Numbers, Halting States, Disciplined Machines, Combining Machines, Variants of Turing Machines, and the Church--Turing Thesis. I reread every Bengali block against its frozen English block, traced the arithmetic-machine diagrams, checked the staged transition construction case by case, tested the tape-variant simulations against the formal machine convention, and reverse-paraphrased every definition, proposition and explanatory claim. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; index generation revalidates every cited page-image and original-file hash.

## Scope and method

- The six units contain 19 + 10 + 10 + 13 + 7 + 5 aligned source/target blocks, for 64 aligned blocks in total. Fifty-five contain Bengali translation and are marked `translated_semantically_reviewed`; nine are diagram-only or other structural/formal blocks and are marked `unchanged_structural_or_formal`.
- Source-to-target replay passes for every unit: aligned block counts, protected controls, environment order, OpenLogic semantic-token multisets, mathematical fragments and Unicode NFC all agree after the six documented source repairs are normalized for comparison.
- I consulted BN-IN-P001, BN-IN-P005 through BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P019, BN-IN-P023 and BN-IN-P025 for number, set, relation, function, sequence, logic, proof and complexity language. BN-IN-T170 governs the established Church--Turing thesis wording; BN-IN-T201 through BN-IN-T216 govern the chapter's machine and computation register, with T209 through T216 added for this batch.
- BN-SRC-169 through BN-SRC-174 disclose and repair six frozen-source defects beside their affected passages. No frozen English byte is changed.

## Unit review

### OLP-0258 — Unary representation of numbers

The representation keeps zero as the empty stroke block and a positive natural number as that many consecutive strokes. A machine computes a total numerical function when every valid unary input halts with exactly the corresponding unary output. For a partial function, a defined value requires that same successful behavior, while an undefined value may diverge, halt without a defined output, or halt with a defined output that is not a unary numeral of the required form. Reverse paraphrase: unary inputs and outputs connect the tape model to ordinary number functions without requiring the machine to behave numerically outside a partial function's domain.

The addition machine scans the first stroke block in `q_0`, erases its separator blank while entering `q_1`, and scans the second block until it halts, leaving one contiguous block of `n+m` strokes. Both doubling constructions preserve the intended distinction: one invokes a previously built doubler for a single input block, while the disciplined construction marks, traverses and restores tape regions so that the final doubled output is contiguous. The mover construction shifts a stroke block across the tape using a temporary marker. All six exercises retain their specified arithmetic operations and machine-combination tasks.

BN-SRC-169 repairs the addition diagram's stroke transition from an erroneous edge into `q_1` to a `q_0` self-loop, making the separator blank the unique transition into `q_1`. BN-SRC-173 adds the absent-output case required by the output convention repaired in BN-SRC-168.

### OLP-0259 — Halting states

The two parity examples preserve their machine behavior while replacing implicit halting by designated halt states. One machine enters an accepting halt state on even input and otherwise continues; the second uses separate accepting and rejecting halt states so that both parity outcomes terminate with an explicit decision. The Bengali consistently distinguishes acceptance from rejection and uses `বর্জন-দশা` for the latter. Reverse paraphrase: named terminal states expose whether a run accepts or rejects, but any such convention can be simulated by the original partial-transition model and therefore adds no computing power.

### OLP-0260 — Disciplined machines

The four discipline conditions remain distinct: the machine preserves the end marker, halts only in a designated state, halts while scanning the first input square, and leaves output in the required canonical tape form. The normalization argument retains the claim that every ordinary machine can be converted to this form without changing the partial function it computes. The disciplined addition machine performs the same block-joining addition and then returns the head to square 1 before halting. Reverse paraphrase: standard entry, exit, tape and head conventions make machines easier to connect while preserving their computed functions.

BN-SRC-170 repairs the repeated addition diagram's `q_0` stroke edge to the required self-loop. The proposition and both exercises preserve their construction claims and scope.

### OLP-0261 — Combining machines

The staged construction first renames states so that the two state sets are disjoint, takes their union and a shared tape alphabet, and follows the first machine while its transition is defined. Exactly when the first machine would halt, control passes to the second machine's initial state without moving or rewriting the scanned square; transitions of the second machine then govern the rest of the run. The qualification about head position is retained, so the second stage begins with the tape and scan position produced by the first stage. Reverse paraphrase: disciplined exit conventions make sequential machine composition a finite relabeling-and-dispatch construction.

The worked machine first adds `n` and `m`, then doubles the resulting block, producing `2(n+m)`. Its three displayed versions preserve the same addition phase and the combined diagram preserves every state and transition of its components. The composition proposition retains the order of partial functions and its definedness conditions, and the exercise retains the requested construction.

BN-SRC-171 restricts the first branch of the piecewise transition definition to defined transitions, removing its overlap with the handoff branch. BN-SRC-172 repairs all three repeated addition diagrams so their `q_0` stroke edges are self-loops.

### OLP-0262 — Variants of Turing machines

The section retains the extensional equivalence of the listed presentation choices: larger alphabets, separate write and move actions, stay-put moves, different tape geometries, multiple tapes, nondeterminism, alternate halting conventions and alternate number encodings. The even/odd-square simulation of a two-way tape on a one-way tape preserves adjacency and shows how one tape layout represents both sides of the origin. The binary/unary discussion keeps the distinction between computability, which is unchanged by an effective encoding, and resource measures, which may change substantially.

For the left-boundary convention, BN-SRC-174 makes the simulation invariant explicit: a distinct marker is reserved permanently and exclusively for square 0, is never overwritten, is never written elsewhere, and has its left-moving transitions deleted. Reverse paraphrase: each variant can simulate the others by a finite effective translation, so they compute the same partial functions even when their running-time behavior differs.

### OLP-0263 — Church--Turing thesis

The section retains the thesis in its intended extensional form: a function is effectively computable exactly when it is computable by a Turing machine. It also preserves the thesis's two methodological uses. A high-level pseudocode procedure may establish Turing computability without spelling out a transition table, provided each step is effective; conversely, a proof that no Turing machine computes a function establishes that no effective procedure computes it. The halting-problem application remains attached to the second use. Reverse paraphrase: the thesis connects the formal machine class to the informal notion of effective procedure, licensing ordinary algorithms as positive witnesses and machine impossibility proofs as general negative results.

## Technical claim audit

- All file identifiers, imports, labels, cross-references, captions, environments, transition labels, function signatures and mathematical expressions are preserved except the four audited diagram endpoints and the added definedness condition documented by BN-SRC-169 through BN-SRC-172.
- The checker transforms exactly one diagram edge in OLP-0258, one in OLP-0260 and three in OLP-0261 before mathematical comparison. It separately asserts the repaired piecewise condition, absent-output case and permanent-boundary-marker invariant.
- The addition diagrams now agree with the prose algorithm: strokes keep control in `q_0`, and only the separator blank enters `q_1`. The combined-machine cases are disjoint and exhaustive over transitions belonging to the two component state sets.
- The reserved-marker repair closes the square-0 overwrite case left open by the frozen variant argument; it preserves the stated one-way-tape model and does not strengthen unrelated machines.
- All six correction notes share the target file hashes recorded in the correction ledger and are stripped before structural comparison. Every translated block cites the canon pages actually consulted.
- No TeX build was attempted because the shared TeX mutex is reserved elsewhere. Reader rendering, glyph inspection, semantic HTML validation and final printed-page locators remain pending.

## Terminology and edition scope

BN-IN-T209 through BN-IN-T216 cover unary representation and partial computation, arithmetic machines and tape blocks, designated accepting and rejecting halt states, disciplined-machine conditions, staged combination, machine variants and nondeterminism, tape simulations and number encodings, and effective procedure plus the Church--Turing thesis. Specialized compounds remain provisional and invite expert correction. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set. OLP-0264, the Undecidability chapter driver, is the next untranslated source unit.
