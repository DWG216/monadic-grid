# t81 Sum of squares: the balanced record extends to a pseudo-distribution (pre-registered 2026-11-24, before any code is written or run)

The chain (whole in the part): sufficient reason gives monads as balanced pairs; the reconciliation reads one record two ways, cross terms and meeting term; on the fermionic sector a clique is an object over a reference; the cross term reads it from the root, the meeting term against exclusion; only a law beats the meetings, and laws live in dolls; every characterized algorithm reads through a law, and 3-SAT's clauses are balanced records it accepts (t79, t80). Where's the beef: the grid's ground, balance, is what blinds the strongest algorithms.

Step: sum of squares (SoS) is the strongest algorithm family not characterized by polymorphisms. At degree d it accepts an instance when a pseudo-expectation exists: a linear functional on polynomials of degree <= d with E~[1] = 1, every constraint holding, and the moment matrix positive semidefinite. Grigoriev's construction for 3-XOR, in our terms: in +-1 variables y = (-1)^x a clause is y_a y_b y_c = s. Put E~[y_S] = the sign s_S when the monomial y_S is derivable from the clauses by combining equations whose degrees stay <= d (the restricted closure), and 0 otherwise.

Its restriction to one clause has E~[y_a] = E~[y_b] = E~[y_c] = 0, pairwise 0, and E~[y_a y_b y_c] = s: the uniform distribution on the clause's parity class, exactly t79's balanced record. Every 3-SAT clause's satisfying set contains the parity class opposite its falsifying tuple, so the same functional satisfies the 3-SAT clauses built that way (Schoenebeck's reduction).

Instances, seed 81: random 3-XOR, n = 60 variables, m = 70 clauses, kept only if unsatisfiable (Gaussian elimination over F2); 10 instances. SoS degree d = 4 (moment matrix over multilinear monomials of degree <= 2: 1 + 60 + 1770 = 1831 rows).

S1 Sanity: on a 4-clause hand example with a degree-2 derivation, the closure finds it with the right sign.
P1 [M] The restricted closure up to degree 4 is consistent (no monomial with both signs, no derivation of the constant -1) on at least 8 of 10 instances.
P2 [M] On every consistent instance the moment matrix is positive semidefinite (least eigenvalue >= -1e-8) and every constraint y_C y_S = s_C y_S with deg <= 4 holds under E~.
P3 [M] On every consistent instance E~ restricted to every clause is the uniform distribution on its parity class (t79's record).
P4 [M] Gaussian elimination refutes all 10.

Verdict: P1-P4 pass -> degree-4 SoS accepts unsatisfiable 3-XOR through a pseudo-distribution that is t79's balanced record on every clause, glued consistently; only the minority law (elimination) breaks it. For 3-SAT the same record fools SoS through Schoenebeck's reduction (theorem: degree linear in n on random instances).

## Scoring (2026-11-24)
Run 1 (t81_run1.log, script t81_sos_balanced.py).
- S1 PASS: the closure derives y0 y3 = -1 from the hand example.
- P1 FAIL as registered: the degree-4 closure is inconsistent on all 10 instances (n = 60, m = 70). P2 and P3 could not be scored (no consistent instance). P4: all 10 refuted by elimination (by construction).
Post hoc (t81_posthoc.py, after the run, not scored): the least closure degree that derives a contradiction, m = 1.2 n, four instances each: 3 at n = 30, 60 and 120; 4 at n = 240. At these sizes random 3-XOR still contains small dense subsystems, so low-degree derivations refute it; the refuting degree begins to rise at n = 240. Grigoriev's theorem (degree linear in n) holds on expanding instances, which these sizes do not yet reach. The test was registered below the regime where the construction lives.
