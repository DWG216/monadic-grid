# t83 Schoenebeck's reduction run directly: SoS accepts random 3-SAT through the balanced record (pre-registered 2026-11-24, before any t83 code is written or run)

The chain (whole in the part): sufficient reason gives monads as balanced pairs; one record, read two ways (cross terms QM, meeting term GR); the slice is the fermionic sector; the cross term reads from the root, the meeting term pays against exclusion; only a law beats the meetings, and laws live in dolls; 3-SAT's clauses are balanced records (t79) and the record glued across an expanding instance fools degree-4 SoS on 3-XOR (t82). Where's the beef: here the same record fools SoS on 3-SAT itself, the NP-complete problem with no law.

Construction (Schoenebeck 2008, in our terms): for a 3-SAT clause on variables a, b, c with falsifying tuple f, take the XOR constraint whose parity class is the one opposite to f. The 3-SAT clause allows 7 tuples; the opposite parity class is 4 of them, so the XOR is a strengthening. Build E~ from the degree-4 restricted closure of the derived XOR system (t82's construction). Then the probability E~ gives the falsifying tuple is (1/8)(1 + s_f s) = 0 when the record holds (singletons and pairs 0, triple = s).

Instances, seed 83: random 3-SAT, density m = 4.5 n (above the satisfiability threshold 4.267, so unsatisfiable with high probability; no polynomial certificate of that is known, which is the point), n = 2000, 4000, 8000, ten each. Literal signs uniform.

S1 Sanity: the planted odd even cover of t82, written as 3-SAT clauses through the same map, makes the closure inconsistent.
S2 Sanity: for 3 planted satisfiable 3-SAT instances (n = 2000, density 4.5, clauses drawn satisfied by a hidden assignment, XOR parity chosen to contain the hidden tuple) the closure is consistent and the hidden assignment satisfies every derived XOR.
P1 [M] At n = 8000 the degree-4 closure of the derived XOR system is consistent on at least 8 of 10 instances.
P2 [M] On every consistent instance, for every 3-SAT clause: E~[1{x_abc = f}] = 0 exactly, and for 20 random clauses per instance E~[y_v 1{x_abc = f}] = 0 for every v in the clause and for 5 random v outside it (the degree-4 constraint products).
P3 [M] On every consistent n = 8000 instance, the local moment matrix (degree <= 2 monomials, 30 nearest variables) is PSD at 20 random clauses (least eigenvalue >= -1e-8).
P4 [M] The number of consistent instances does not decrease from n = 2000 to n = 8000.

Verdict: P1-P4 pass -> degree-4 SoS accepts random unsatisfiable-with-high-probability 3-SAT at scale, through a pseudo-distribution that is t79's balanced record on every clause. No law reads through it.

## Scoring (2026-11-25)
- S1 PASS (t83_run1_timeout.log, t83_run2.log): the planted cover is refuted.
- S2 not completed: on the first planted satisfiable instance (n = 2000, density 4.5) the degree-4 closure grew past 0.9 GB in four minutes; run 1 hit the 590 s session limit, run 2 was stopped by hand. P1-P4 not reached. Kept.
Why (analysis after the run, labelled): a degree-4 equation meets another sharing two variables about 324 Δ² / n times on average (about 9Δ²n/2 degree-4 equations, 6 pairs each, n²/2 pairs). At Δ = 4.5 that is 6561 / n: above 1 for n below about 6600, so the closure percolates at the registered sizes. At Δ = 1 (t82) it is 324 / n, already 0.3 at n = 1000, which is why t82 sat in the regime. The test was registered below the regime for 3-SAT's density; t84 goes where the branching is below 1/2.
