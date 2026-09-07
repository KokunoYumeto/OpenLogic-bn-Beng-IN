# Semantic review: Computability Theory — reductions and completeness

This review covers OLP-0241 through OLP-0246: Computably Enumerable Sets are Closed under Union and Intersection, Computably Enumerable Sets not Closed under Complement, Reducibility, Properties of Reducibility, Complete Computably Enumerable Sets and An Example of Reducibility. I reread every Bengali block against its frozen English block, checked every reduction direction and domain/range construction, audited the displayed mathematics and protected controls, and reverse-paraphrased the definitions and proofs. Canon passage use is recorded per translated block in `SEGMENT_CANON_USE.jsonl`; index generation revalidates every cited page-image and original-file hash.

## Scope and method

- The six units contain 11 + 8 + 7 + 12 + 9 + 9 aligned source/target blocks, for 56 aligned blocks in total. Of these, 55 contain Bengali translation and are marked `translated_semantically_reviewed`; OLP-0241-B001 is a formal-only block preserved byte for byte and marked `unchanged_structural_or_formal`.
- Source-to-target replay passes for every unit: aligned block counts, protected controls, environment order, OpenLogic semantic-token multisets, mathematical fragments and Unicode NFC all agree after the five documented source repairs are normalized for comparison.
- I consulted BN-IN-P005, BN-IN-P008, BN-IN-P009, BN-IN-P010, BN-IN-P013, BN-IN-P018, BN-IN-P023 and BN-IN-P025 for number, set, pair, relation, function, composition and proof language. Existing decisions BN-IN-T040, BN-IN-T044, BN-IN-T168, BN-IN-T171, BN-IN-T173, BN-IN-T179 and BN-IN-T184 through BN-IN-T187 govern enumeration, computability, complement, coding and halting terminology; BN-IN-T188 through BN-IN-T193 record this batch’s closure, reduction, completeness and oracle register.
- BN-SRC-150 through BN-SRC-154 disclose and repair five frozen-source defects beside their affected arguments. No frozen English byte is changed.

## Unit review

### OLP-0241 — C.E. closure under union and intersection

The theorem keeps union and intersection distinct across three proof styles. The domain proof searches one enumeration for a union and a coded pair of enumeration positions for an intersection. The range proof alternates the two enumerators for a union and emits matching values, with a fixed common element as the fallback, for a nonempty intersection. The final proof uses simultaneous definedness for an intersection and a certified parallel search for a union. Reverse paraphrase: positive evidence from either process recognizes a union, while positive evidence from both processes recognizes an intersection.

### OLP-0242 — Complements of c.e. sets

The theorem says that a set is computable exactly when it and its complement are both c.e. In the reverse direction, the Bengali proof searches the two partial-domain computations in parallel; exactly one side must eventually halt, so the resulting search is total and identifies membership. The corollary correctly infers that the complement of the noncomputable c.e. halting set cannot be c.e. Reverse paraphrase: simultaneous positive enumerability of membership and nonmembership yields a terminating yes/no procedure.

The frozen formal proof tests `T(e,x,h(x))` for membership in `A`, although `d` was assigned to `A` and `e` to its complement. BN-SRC-150 restores `d` in the membership test. The following frozen explanation instead names `e` and an unintroduced `f`, then assigns the `e` branch to `A`; BN-SRC-151 restores the declared pair `d,e` and the `d` membership branch.

### OLP-0243 — Many-one reducibility

The motivation correctly treats a reduction as a computable transformation that turns one membership question into another and distinguishes this from efficiency-bounded complexity reductions. The formal biconditional, direction `A \leq_m B`, symmetric equivalence and injective one-one strengthening are retained. The diagonal map `x \mapsto \langle x,x\rangle` transfers any decision for the paired halting set to the self-halting set. Reverse paraphrase: deciding the transformed `B` instance decides the original `A` instance with the same yes/no polarity.

BN-SRC-152 repairs the frozen equivalent description of `K_0`, which reverses the pair to `\langle x,e\rangle` while retaining the condition `x\in W_e`; the Bengali formula consistently uses index-input order `\langle e,x\rangle`.

### OLP-0244 — Properties of reducibility

Composition proves transitivity. Pulling a partial domain back through a reduction proves downward preservation of c.e. status; complement reduction plus the complement criterion, or direct characteristic-function composition, proves downward preservation of computability. The problems retain the complement and characteristic-function identities. The digression correctly distinguishes a one-query polarity-preserving many-one reduction from an oracle procedure allowed to ask questions about the target, and retains the Karp/Cook polynomial-time analogues. Reverse paraphrase: any effective solution to the harder target problem supplies an effective solution to the source problem.

BN-SRC-153 changes the frozen problem’s type `f\colon A\to B` to the defining type `f\colon\mathbb N\to\mathbb N`; the characteristic-function identity must be evaluated on every natural input, including nonmembers of `A`.

### OLP-0245 — Complete c.e. sets

The definition retains both requirements: the set itself is c.e., and every c.e. set many-one reduces to it. A fixed index maps any c.e. domain into `K_0`; the previously proved reductions `K_0 \leq_m K_1` and `K_0 \leq_m K`, combined with transitivity, establish completeness of all three halting sets. The final digression preserves the historical Friedberg-Muchnik result that intermediate c.e. sets also exist. Reverse paraphrase: a c.e.-complete set is a universal positive-evidence decision problem under computable instance transformation.

The frozen final proof sentence gives `K \leq_m K_0`, a direction that supports the already established hardness of `K_0` rather than the claimed completeness of `K`. BN-SRC-154 restores the required direction `K_0 \leq_m K`.

### OLP-0246 — Reduction to `K_1`

The set `K_1` contains exactly the program indices defined on input zero and is c.e. by its existential computation predicate. The oracle explanation builds a program that ignores its received input and instead runs a fixed coded computation. The formal construction uses the universal partial computable function and the s-m-n theorem to produce that program index uniformly from the original index-input pair, then packages the two arguments through the pairing projections. Reverse paraphrase: a general halting instance is transformed effectively into a zero-input halting instance without changing whether the simulated computation terminates.

## Technical claim audit

- All file identifiers, labels, cross-references, tag blocks, environments, minimization searches, domain/range equations, characteristic functions, reduction biconditionals, pairing projections and s-m-n expressions are preserved except the three exact mathematical substitutions documented by BN-SRC-150, BN-SRC-152 and BN-SRC-153.
- The checker accepts only the audited fragment-counter differences: `e` to `d` in the membership test and explanation, `f` to the declared `e` in that explanation, `\langle x,e\rangle` to `\langle e,x\rangle`, and `f\colon A\to B` to `f\colon\mathbb N\to\mathbb N`. It separately asserts the prose direction repair BN-SRC-154.
- All five correction notes share the target file hash recorded in the correction ledger and are stripped before structural comparison. Every translated block cites the canon pages actually consulted.
- No TeX build was attempted. Reader rendering, glyph inspection, semantic HTML validation and final printed-page locators remain pending while the shared TeX mutex is reserved elsewhere.

## Terminology and edition scope

BN-IN-T188 through BN-IN-T193 cover c.e. closure, the complement criterion, many-one and one-one reduction, Turing/Karp/Cook reduction, c.e. completeness and the `K_1` oracle construction. The specialized compounds remain provisional and invite expert correction. The edition remains one India-standard Bengali-script (`bn-Beng-IN`) set.
