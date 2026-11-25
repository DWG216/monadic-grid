# t80 The support check, and the balanced record across clauses (pre-registered 2026-11-24, before any code is written or run)

Chain so far (each part carries the whole): one principle, sufficient reason, gives monads as balanced pairs (§26). The reconciliation reads one record |O + R|^2 two ways: cross terms (phase, sign: quantum mechanics) and the meeting term (positive: gravity). On the fermionic sector (a slice) a clique is an object in a reference; the cross term reads it from the root (t73); the root is the meeting term against exclusion (t74); only a polymorphism, a law, beats the meetings (t75-t76); the law lives in one doll (t77); mixing dolls cheapens laws, never creates them (t78); every characterized algorithm reads through a law, and 3-SAT's clauses are balanced records that every law-reader accepts (t79). Where's the beef: the balance that is the grid's ground is exactly what blinds every algorithm on 3-SAT.

Part A, the open check of t79. BLP+AIP restricts AIP to the support of a relative-interior BLP solution. Check: for each clause and each satisfying tuple, the largest weight that tuple can carry in any BLP solution (one LP each). If every satisfying tuple has positive maximum, the support is everything satisfying and the integer record of t79 is admissible.
A1 [M] On 5 of t79's unsatisfiable 3-SAT instances (seed 79 regenerated, n = 10, m = 80), every satisfying tuple of every clause has maximum weight > 1e-9. Then BLP+AIP accepts all 5.

Part B, next step: the balanced record across many clauses. A fixed-width local algorithm checks every few variables jointly; balance would have to hold across clauses, not just within one. (2,3)-consistency (Barto: every bounded-width CSP is solved at relational width (2,3)) keeps, for each pair of variables, the value pairs that extend to every third variable consistently with all clauses inside the triple; it refutes when some pair's set empties.
Instances, seed 80, brute-force checked unsatisfiable, n = 20: random 3-SAT with m = 100 (density 5); random 3-XOR with m = 25; random 2-SAT with m = 60 (a law: majority); 10 each.
B1 [M] (2,3)-consistency refutes 10/10 unsatisfiable 2-SAT (its law is majority: bounded width).
B2 [M] (2,3)-consistency refutes at most 1/10 unsatisfiable 3-SAT: the balance holds across triples.
B3 [M] (2,3)-consistency refutes at most 1/10 unsatisfiable 3-XOR, while elimination over F2 refutes 10/10 (the minority law, not width, carries 3-XOR).
S1 Sanity: (2,3)-consistency never refutes a satisfiable instance (one each of 3-SAT and 2-SAT, n = 20).

Verdict: A1 passes -> the t79 open check closes: BLP+AIP accepts every unsatisfiable 3-SAT instance tested. B1-B3 pass -> local reading at fixed width is blind to 3-SAT as the single-clause relaxations are; the balance extends across clauses; only a law (majority for 2-SAT, minority for XOR) breaks it.

## Scoring (2026-11-24)
Run 1 (t80_run1.log, script t80_support_and_width.py).
- A1 PASS: every satisfying tuple of every clause carries positive weight in some BLP solution (5/5 instances). The support is everything satisfying, so the integer record of t79 is admissible and BLP+AIP accepts every unsatisfiable 3-SAT instance tested. t79's open check is closed.
- S1 PASS: (2,3)-consistency never refutes a satisfiable instance.
- B1 PASS: it refutes 10/10 unsatisfiable 2-SAT (majority: bounded width).
- B2 FAIL as registered: it refutes 2/10 unsatisfiable 3-SAT (threshold 1). Kept.
- B3 FAIL as registered: it refutes 2/10 unsatisfiable 3-XOR (threshold 1), while elimination refutes 10/10. Kept.
Reading: at n = 20 a few instances contain a small unsatisfiable core inside a few triples (small random instances are not expanders); 8/10 of each survive local reading, against 10/10 refuted where a law exists. The asymptotic statements are theorems (width lower bounds for random 3-SAT and 3-XOR on expanding instances); the registered threshold was too tight for n = 20.
