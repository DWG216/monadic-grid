# PREDICTIONS t178b: the field's area coefficient under a real change of regulator

Registered 2026-11-27, committed before t178b_cubic.py is written or run.

Why. t178 changed only the radial weights of Srednicki's chain, which keeps the same cutoff; the area coefficient did not move. A real change of regulator: a cubic lattice (spacing 1 in all three directions, nearest-neighbour derivatives) with a planar entangling surface, against the spherical chain (radial spacing 1, angular directions continuous), whose per-area coefficient is 0.2954/(4π) = 0.02351.

Method. Free massless scalar on the cubic lattice; half-space A = {x ≤ 0}. By translation invariance along the surface, S/Area = ∫ over the transverse Brillouin zone d²k/(2π)² S₁(M²(k)), with M²(k) = 4 sin²(k_y/2) + 4 sin²(k_z/2) and S₁(M²) the entropy of half of a 1D harmonic chain with mass² M² (correlation-matrix method, chain of 2N = 1600 sites, cut in the middle). Quadrature: Gauss–Legendre, 64 × 64 nodes on [0, π]² (×4 by symmetry). Convergence check with N = 400 → 800 and 64 → 96 nodes.

S1 [sanity]: S/Area changes by less than 1% between the two resolutions.
P1 [M]: |s_cubic / 0.02351 − 1| > 5%: the area coefficient depends on the regulator.
Consequence fixed now: if P1 passes, the field's area coefficient is a property of the lattice chosen, not of the record, and t27's 0.295 per degree of freedom has no sufficient reason to fix η; with §316 the tension resolves in favour of the meeting count. If P1 fails, the tension stands.
Gate: physics; public.
