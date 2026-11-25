# t82 Sum of squares in the expanding regime (pre-registered 2026-11-24, before any t82 code is written or run)

The chain (whole in the part): sufficient reason gives monads as balanced pairs; the reconciliation reads one record two ways, cross terms (QM) and meeting term (GR); on the fermionic sector a clique is an object over a reference; the cross term reads it from the root, the meeting term against exclusion; only a law beats the meetings, and laws live in dolls; every characterized algorithm reads through a law; 3-SAT's clauses are balanced records (t79), and SoS's fooling functional is that record glued across the instance (t81). Where's the beef: the ground of the grid, balance, is what blinds the strongest algorithm.

Why this test: t81 was registered at n = 60, below the regime where Grigoriev's construction lives (small random instances hold dense subsystems that low-degree derivations refute; t81 post hoc: refuting degree 3 up to n = 120, 4 at n = 240). Here we go to n in the thousands with a sparse closure.

Instances, seed 82: random 3-XOR, m = n clauses (density 1.0, above the satisfiability threshold 0.918), kept only if Gaussian elimination over F2 refutes; n = 1000, 2000, 4000; 10 instances each. Restricted closure at degree d = 4 (combine derivable equations while the degree stays <= 4), sparse: equations indexed by variable, a cap of 5,000,000 derived equations (hitting the cap counts as not consistent).

S1 Sanity: a planted odd even cover of degree-4 reach (y1y2y3 = 1, y1y2y4 = 1, y3y5y6 = 1, y4y5y6 = -1) added to a random n = 1000 instance is refuted by the closure.
S2 Sanity: on 3 planted satisfiable instances (n = 1000, m = n, signs from a hidden assignment) the closure is consistent.
P1 [M] At n = 4000 the degree-4 closure is consistent on at least 8 of 10 instances.
P2 [M] The number of consistent instances does not decrease from n = 1000 to n = 4000.
P3 [M] On every consistent n = 4000 instance, for 20 random clauses: the local moment matrix over monomials of degree <= 2 on the ~30 variables nearest the clause (breadth-first over the clause graph) is positive semidefinite (least eigenvalue >= -1e-8). A principal submatrix of the global moment matrix: PSD is necessary for the global one.
P4 [M] On every consistent n = 4000 instance, E~ restricted to every clause is the uniform distribution on its parity class (t79's record): singletons 0, pairs inside the clause 0, the clause monomial = its sign.
P5 [M] Gaussian elimination refutes every instance kept (by construction; reported).

Verdict: P1-P4 pass -> at scale, degree-4 SoS accepts unsatisfiable random 3-XOR through t79's balanced record glued across the instance; only the minority law (elimination, the polymorphism of XOR) breaks it.

## Scoring (2026-11-24)
Run 1 (t82_run1.log). All pass.
- S1 PASS: the planted odd even cover is refuted. S2 PASS: 3/3 planted satisfiable instances consistent.
- P1 PASS: 10/10 consistent at n = 4000 (about 23,000 derived equations each, under a second).
- P2 PASS: 10/10 at n = 1000, 2000 and 4000.
- P3 PASS: least local eigenvalue over 200 local moment matrices (466 x 466) -9.5e-15 (zero to machine precision: the record's linear relations).
- P4 PASS: every clause of every n = 4000 instance carries t79's record (no singleton or in-clause pair derivable; clause monomial = its sign).
- P5 PASS: elimination refutes all 30.
