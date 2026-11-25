# t84 Schoenebeck's reduction in the regime for 3-SAT's density (pre-registered 2026-11-25, before any t84 instance is run; the C++ closure was cross-checked against t82's Python closure on six small instances: identical status and size)

The chain (whole in the part): balanced pairs; one record read two ways (cross terms QM, meeting term GR); the slice is the fermionic sector; the root; meetings against exclusion; only a law wins; laws live in dolls; 3-SAT's clauses are balanced records (t79), glued across an expanding instance they fool degree-4 SoS on 3-XOR (t82). Where's the beef: the same record fools SoS on 3-SAT itself, the NP-complete problem with no law.

Why this test: t83 was registered below the regime. The degree-4 closure branches about 324 Δ²/n times per equation; at density Δ = 4.5 this is 6561/n. Here n = 16,000, 32,000 and 64,000 (branching 0.41, 0.21, 0.10).

Construction as t83 (src/closure4.cpp, same combination rule as t82): each 3-SAT clause maps to the XOR on the parity class opposite its falsifying tuple; E~ is the degree-4 restricted closure; cap 40,000,000 equations (cap counts as not consistent). Random 3-SAT at density 4.5 (unsatisfiable with high probability), seeds 840000 + i, ten instances per size.

S1 Sanity: n = 16,000 random instance plus the planted cover: conflict.
S2 Sanity: 3 planted satisfiable instances, n = 16,000: consistent, hidden assignment satisfies every derived XOR, no clause violated under E~.
P1 [M] At n = 64,000 the closure is consistent on at least 8 of 10.
P2 [M] On every consistent instance E~ puts zero weight on every clause's falsifying tuple (all 3-SAT clauses), and on 20 random clauses the products with y_v (v in the clause and 5 random v) vanish.
P3 [M] On every consistent n = 64,000 instance, the local moment matrices (degree <= 2 monomials on the 30 variables nearest each of 20 random clauses) are PSD (least eigenvalue >= -1e-8).
P4 [M] Consistent counts do not decrease from n = 16,000 to n = 64,000.

Verdict: P1-P4 pass -> degree-4 SoS accepts random 3-SAT above the threshold through t79's balanced record, glued across the instance. No law reads through it.

## Run 2 (t84_run2.log, 2026-11-25)
S1, S2, P1 (10/10 at n = 64,000), P2 and P4 (10/10 at every size) PASS. P3 FAIL as run: one of 200 local blocks (n = 64,000, seed 840001, ball 4) had least eigenvalue -1.67; the other 199 were zero to machine precision.
Post hoc (t84_posthoc.py, labelled): the failing block was missing products of equations sharing two or three variables, which the closure rule does find. The cause was a bug in src/closure4.cpp: the hash key ORed the degree into bits 60-63, which overlap the first variable of a degree-4 monomial (variables >= 4096), so lookups of some degree-4 monomials returned another monomial's entry. The closure itself was unaffected (identical size, 6,832,409, after the fix); the lookups used for the local blocks were. The buggy source is kept as src/closure4_run2_keybug.cpp. With the fix the same block's least eigenvalue is -2.1e-15. Run 3 reruns the registered test unchanged with the fixed key.

## Run 3 (t84_run3.log, fixed key, registered test unchanged). All pass.
- S1 PASS (planted cover refuted). S2 PASS (3/3 planted satisfiable consistent; hidden assignment satisfies all 72,000 derived XORs; no clause violated).
- P1 PASS: 10/10 consistent at n = 64,000 (about 6.5-6.8 million derived equations each).
- P2 PASS: zero weight on the falsifying tuple of every 3-SAT clause on every instance (72,000 / 144,000 / 288,000 clauses), and every degree-4 product checked vanishes.
- P3 PASS: least local eigenvalue over 200 blocks -6.3e-15.
- P4 PASS: 10/10 at all three sizes.
