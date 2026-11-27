# PREDICTIONS t178b: the field's area coefficient under a real change of regulator

Registered 2026-11-27, committed before t178b_cubic.py is written or run.

Why. t178 changed only the radial weights of Srednicki's chain, which keeps the same cutoff; the area coefficient did not move. A real change of regulator: a cubic lattice (spacing 1 in all three directions, nearest-neighbour derivatives) with a planar entangling surface, against the spherical chain (radial spacing 1, angular directions continuous), whose per-area coefficient is 0.2954/(4π) = 0.02351.

Method. Free massless scalar on the cubic lattice; half-space A = {x ≤ 0}. By translation invariance along the surface, S/Area = ∫ over the transverse Brillouin zone d²k/(2π)² S₁(M²(k)), with M²(k) = 4 sin²(k_y/2) + 4 sin²(k_z/2) and S₁(M²) the entropy of half of a 1D harmonic chain with mass² M² (correlation-matrix method, chain of 2N = 1600 sites, cut in the middle). Quadrature: Gauss–Legendre, 64 × 64 nodes on [0, π]² (×4 by symmetry). Convergence check with N = 400 → 800 and 64 → 96 nodes.

S1 [sanity]: S/Area changes by less than 1% between the two resolutions.
P1 [M]: |s_cubic / 0.02351 − 1| > 5%: the area coefficient depends on the regulator.
Consequence fixed now: if P1 passes, the field's area coefficient is a property of the lattice chosen, not of the record, and t27's 0.295 per degree of freedom has no sufficient reason to fix η; with §316 the tension resolves in favour of the meeting count. If P1 fails, the tension stands.
Gate: physics; public.

Amendment before any code was run (2026-11-27): the resolutions above are too costly here (each mass needs an 800 × 1600 projection). Changed to: chain 2N = 800 sites, 64 × 64 nodes for the result; convergence check against 2N = 400 sites and 48 × 48 nodes (S1 tolerance unchanged, 1%). P1 unchanged.

## Scoring (2026-11-27), run 1 (t178b_run1.log)
- S1 PASS: converged to 1e-5 (chain length) and 4e-7 (nodes).
- P1 FAIL: cubic lattice 0.024262 per unit area against the spherical chain's 0.023510: they differ, and the difference is resolved far beyond the numerical error, but by 3.2%, under the registered 5%.
Verdict as fixed in advance: the tension stands. Reported: the field's area coefficient does depend on the regulator (3.2% here), but weakly: for one field it is about 0.024 per unit area for either lattice, about one eighth of the meeting count's 0.19 per cell area. So the two counts are not the same quantity at the same grain. Reading [I, not tested]: with species removed (§316) the field's own entanglement is a separate, smaller contribution; if η is the sum, the cell moves from 0.87 to about 0.93 l_P. Not adopted: it needs a reason from the ground before it is registered.
