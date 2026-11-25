# t79 Tracing the law back: in every characterized algorithm the law is a polymorphism, and 3-SAT's clauses carry a balanced record no law can break (pre-registered 2026-11-24, before any code is written or run)

Step (§186): show that a law used inside an algorithm traces back to a polymorphism of the solution set.

Where this is already a theorem [M, others]: for each algorithm family whose power has been characterized, the law it uses is a family of polymorphisms. Arc consistency: totally symmetric polymorphisms of all arities; the basic LP (BLP): symmetric polymorphisms of all arities; the affine integer relaxation (AIP): alternating polymorphisms of all odd arities; BLP+AIP: block-symmetric polymorphisms (Brakensiek, Guruswami, Wrochna, Zivny), and it solves every tractable Boolean CSP; local consistency (bounded width): weak near-unanimity polymorphisms of almost all arities (Barto, Kozik).

What we add [M, proved below, checked by computation]: why the strongest of these, BLP+AIP, is blind on 3-SAT, in our terms. Each 3-SAT clause carries a balanced local record:
- Fractional balance (BLP): the four satisfying tuples of one parity class (the class not containing the falsifying tuple), weight 1/4 each, give every variable marginal 1/2. Every clause, every instance: all marginals 1/2 everywhere, globally consistent.
- Integer balance (AIP): marginal 1 for every variable is reached in every clause with integer weights: tuple 111 alone for any clause it satisfies; for the all-negative clause, 110 + 101 + 011 - 100 - 010 - 001 + 000.
So both halves accept every 3-SAT instance, satisfiable or not. For 3-XOR the same affine record fails: for weights on a parity class with sum 1, the three marginals add to b mod 2, so integer marginals reduce mod 2 to a solution; an unsatisfiable system has no AIP solution. The minority law is the arithmetic of the marginals.

Computation, seed 79: random 3-SAT with n = 10, m = 80 (checked unsatisfiable by brute force), 10 instances; random 3-XOR with n = 10, m = 20 (checked unsatisfiable), 10 instances.
S1 Sanity: the BLP is solved by linear programming (scipy) and its value agrees with the explicit all-1/2 record on one 3-SAT instance (both feasible).
P1 [M] BLP accepts all 10 unsatisfiable 3-SAT instances, and the explicit balanced record satisfies every BLP constraint exactly.
P2 [M] The explicit integer record (all marginals 1) satisfies every AIP constraint exactly on all 10 unsatisfiable 3-SAT instances.
P3 [M] BLP alone also accepts all 10 unsatisfiable 3-XOR instances (balance fools the LP), but AIP rejects them: the mod-2 reduction of the marginal system is inconsistent in all 10 (Gaussian elimination over F2).

Verdict: P1-P3 pass -> in the strongest single algorithm known to solve every tractable Boolean CSP, the law at work traces back to a polymorphism (the minority law is the AIP's marginal arithmetic), and 3-SAT is blind to it because every clause carries a balanced record, zero-sum to the algorithm, with no law to break the balance.

## Scoring (2026-11-24)
Run 1 (t79_run1.log, script t79_balanced_record.py). All pass.
- S1 PASS: the LP is feasible and the explicit all-1/2 record satisfies every BLP constraint.
- P1 PASS: BLP accepts 10/10 unsatisfiable 3-SAT instances; the balanced record checks exactly on all 10.
- P2 PASS: the integer record (all marginals 1) satisfies every AIP constraint exactly on all 10.
- P3 PASS: BLP accepts 10/10 unsatisfiable 3-XOR instances; the mod-2 marginal system is inconsistent on all 10, so AIP rejects them.
Scope note (after the run): the integer record answers the plain AIP. The combined BLP+AIP first restricts AIP to the support of a relative-interior BLP solution; that the record's tuples lie in that support was not checked here and is the next check.
