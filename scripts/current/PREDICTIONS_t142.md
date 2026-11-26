# t142 E6 broken by a holonomy of order three (pre-registered 2026-11-25, before any t142 code is written or run)

Question: the scalar route cannot break E6 at the Planck scale cleanly (t131). In heterotic models E6 is broken instead by a Wilson line, a discrete holonomy g = exp(2πi H) on a space whose loops carry a Z₃; no adjoint scalar and no potential are needed. The grid's grain is a clock of three. Which subgroups can a holonomy of order three leave?
Method [M, exact]: E6's 72 roots in the trinification basis (the roots of SU(3)_C × SU(3)_L × SU(3)_R plus ±(u_a, u_b, u_c), u the SU(3) fundamental weights); simple roots from a generic chamber; every Cartan element H = Σ c_i ω_i^∨ / 3 with c ∈ {0, 1, 2}⁶, c ≠ 0 (728 elements); the unbroken group's roots are those with α(H) ∈ Z; its number of U(1) factors is 6 minus the rank of those roots.
P1 [M] Among the 728, every unbroken group with no U(1) factor (semisimple rank 6) has exactly 18 roots: SU(3)³ is the only group a holonomy of order three leaves without a U(1).
P2 [M] At least one of the 728 leaves SU(3)³ (18 roots, rank 6).
P3 [M] The centre of SU(3)_C, H = ((2, −1, −1)/3, 0, 0), leaves exactly the 18 roots of SU(3)³, and acts on the 27 with one phase per block: (3, 3̄, 1), (1, 3, 3̄) and (3̄, 1, 3) carry three different cube roots of unity.
Consequence fixed now: if P1–P3 pass, the cut E6 to SU(3)³ is forced for a clock of three: a Z₃ holonomy of the grain breaks E6 at the scale where the grain is resolved, gravity's meeting, with no scalar potential, and the three cube roots label the 27's three blocks.

## Scoring (2026-11-25, t142_run1.log): all pass
Checks: 72 roots of one length, 6 simple roots, Cartan determinant 3 (E6).
Unbroken groups over the 728 order-three elements, (roots, semisimple rank): (18, 6) × 80; (22, 5) × 432; (24, 4) × 90; (30, 5) × 72 (SU(6) × U(1)); (40, 5) × 54 (SO(10) × U(1)).
- P1 PASS: the only unbroken group with no U(1) factor has 18 roots: SU(3)³.
- P2 PASS: 80 of the 728 leave SU(3)³.
- P3 PASS: the centre of SU(3)_C leaves exactly SU(3)³ and gives the 27's blocks the phases 2/3, 0, 1/3: the three cube roots, one per block.
Verdict, as fixed in advance: a Z₃ holonomy of the grain breaks E6 exactly to SU(3)³ when it leaves no extra U(1); every other outcome of a clock of three carries a U(1). The cut needs no scalar potential, and the three blocks of the 27 are labelled by the three cube roots.
