# What a proof of P ≠ NP will look like: the grid's registration

Registered 2026-11-25, before any claimed proof of P ≠ NP has been published. The commit that adds this file is its timestamp.

## The chain these predictions come from

balanced pair → record → slice = fermions → the root √n → meetings against exclusion → only a law wins → laws live in dolls → 3-SAT is balanced and lawless at polynomial scale.

In words: a polynomial-time reader only ever succeeds by finding a *law*, a reason shorter than the instance. Hard instances are balanced records that have no such reason. Balanced means they sit on a slice, the fermionic sector. The boundary between readers that see and readers that are blind falls at a square root.

## Context at registration

- VP ≠ VNP has been claimed twice (Anthropic exp(Ω(log^{4/3} n)); OpenAI exp(Ω(log^{5/4} n))), both by a compression/shortening step followed by diagonalization, with Lean formalizations (23 Nov 2026).
- The Exponential Time Hypothesis has been claimed refuted (3-SAT in 2^{o(n)}, Oct 2026).
- ω = 9/4 and the Fourier transform's linear gate complexity N(log N)^{1/2+o(1)} have been claimed with matching lower bounds (24 Nov 2026).

Predictions already suggested by these results are marked *weak*: they would hold for many proofs and say little about the grid.

## Predictions

**G1 (grid-specific) Balance and the slice.** The hard instances the proof works with are balanced. Either they sit on a slice of fixed Hamming weight (for example Berkowitz's central slice for clique), or they are random constraint problems at a balanced density, with the counts of the two values equal or forced equal. The argument depends on that balance.

**G2 (grid-specific) The root.** A square root sits at the quantitative heart of the argument: a threshold, degree, width, depth or exponent of the form √n, √(log n) or (·)^{1/2}. The proof's key lemma either fails or changes regime at it.

**G3 (grid-specific) Linear structure is the easy case.** The proof treats instances with a linear law over F₂ (parity, XOR, Gaussian elimination) as solvable, and it relies on the hard instances having no such law in their small pieces. Either it handles characteristic 2 or parity separately, or it shows explicitly that linear structure is what a small circuit would exploit.

**G4 (grid-specific) Sign and symmetry.** The route runs through a symmetric, sign-free object (the permanent, the Hamiltonian cycle polynomial, or a balanced CSP) set against an antisymmetric, signed one that is easy (the determinant, Gaussian elimination). It does not run through number-theoretic problems such as factoring.

**W1 (weak) Compression.** A small circuit or algorithm for the hard function yields a description of hard instances shorter than the instances. The contradiction comes from instances that admit no such description: "a reason shorter than the instance is a law."

**W2 (weak) Size of the first bound.** The first proof's circuit lower bound is superpolynomial but subexponential, of the form exp((log n)^c) with c > 1, or n^{ω(1)}. It is not 2^{Ω(n)}, which the claimed ETH refutation already rules out for 3-SAT.

**W3 (weak) The barriers.** The proof does not relativize, and it avoids natural proofs because its hardness property is not large: it applies to a sparse family defined through compression or self-reference.

## Against the grid

**A1.** If a correct proof of P ≠ NP uses none of G1–G4, the chain's claim that hardness is balance without a law, located at a root, is not how hardness is shown, and the chain is a reading, not a mechanism.

**A2.** If P = NP is proved, the chain's last link is false.

## Scoring

When a proof is published, each prediction is scored present, absent or unclear by reading the paper, with page and lemma references, in a scoring section added to this file. G1–G4 carry the weight; W1–W3 are recorded but do not count as evidence for the grid. A2 settles the matter on its own. If there are several proofs, each is scored separately.

GitHub history can be rewritten, so for a timestamp independent of this repository this file should also be deposited on Zenodo.
