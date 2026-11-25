# t88 The parity doll on 3-SAT: small reasons carry no F2 law (pre-registered 2026-11-25, before any t88 code is written or run)

The chain (whole in the part): balanced pairs; one record read two ways (cross terms QM, meeting term GR); the slice is the fermionic sector; the root; meetings against exclusion; only a law wins; laws live in dolls; 3-SAT's clauses are balanced records that fool every reader up to sum of squares (t79-t84). Where's the beef: the next rung, resolution over parities (Res(+)), has XOR's law built in. Its lines are disjunctions of F2-linear equations; it beats 3-XOR at once. The grid's claim: the law lives in its doll, and 3-SAT puts nothing in that doll at small scale, so a reader carrying the F2 law finds nothing to read until it holds a constant fraction of the instance. Target sentence: a reason shorter than the instance is a law; here, in the F2 doll, no reason shorter than the instance is an F2 law.

Measured quantity (exact): for a set S of clauses on variables V, S carries an F2 law if its satisfying assignments lie in a proper affine subspace of F2^V (some nonzero c and b with c.x = b on every solution). Computed exactly in C++ (src/f2law.cpp): randomized DPLL samples solutions until their affine span is full (no law) or stalls; each remaining complement direction is then decided by DPLL with that parity constraint negated (unit propagation on clauses and on the parity); a law is reported only when such a call is unsatisfiable.

Subsets: grown from a random clause by adding a random clause that shares a variable with the current set (connected), sizes s = 5, 10, 20, 30; 200 subsets per (instance family, n, s), seed 88.
Families: random 3-SAT at density 4.5 (above threshold) and random 3-XOR (each XOR clause written as its 4 forbidding 3-SAT clauses) at density 1.0, n = 100, 200, 400, 800.

S1 Sanity: the 4 clauses (x v y v z), (x v y v -z), (x v -y v z), (x v -y v -z) carry the law x = 1; a single clause carries none.
C1 Control (identity): for every 3-XOR subset the number of independent laws equals the rank of its XOR system (checked on s = 5 and 10 at n = 100: law found in every subset whose XOR system is non-empty, i.e. every subset).
P1 [M] 3-SAT, n = 800: at most 5% of subsets carry an F2 law, for every s up to 30.
P2 [M] 3-SAT, s = 30: the fraction carrying a law does not increase from n = 100 to n = 800.
P3 [M] 3-XOR, every n and s: 100% of subsets carry a law (the law is present at every scale).

Verdict: P1-P3 pass -> in the F2 doll, 3-XOR shows its law in every small piece, 3-SAT in almost none, and fewer as n grows: a parity reader working on pieces finds a law only at a scale that grows with the instance. This is the local condition the Res(+) rung needs, not the Res(+) lower bound itself.
