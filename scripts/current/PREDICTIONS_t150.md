# PREDICTIONS t150: horizon microstates as balanced records

Registered 2026-11-26, before t150_horizon_count.py was written or run.

Reading [I]. A horizon is a region's record at capacity. Each horizon cell carries one of d states; the record is balanced (net zero in every conserved charge). The count of balanced configurations of n cells is the microstate number, n ∝ A.
Choice fixed in advance [I]: d = 16, the SO(10) spinor (one generation), whose weights are (±1/2)⁵ with an even number of minus signs; balance = total weight zero in all r = 5 Cartan directions. (Lead, post hoc, §286: t27's grain with N = 118 Standard Model degrees of freedom gives ln d = cN/(4π) = 2.770, ln 16 = 2.773. Not a test.)

Engine. Exact count: N0(n) = 2^(−n) Σ_t C(n, t) c(t)^5, c(t) = Σ_k (−1)^k C(t, k) C(n − t, n/2 − k), n even (big integers). Check against brute force for n ≤ 6.

S1 [sanity]: formula equals brute force for n = 2, 4, 6.
P1 [M]: ln N0(n) = n ln 16 − (5/2) ln n + const + o(1): the fitted log coefficient over n = 200…2000 is −2.50 within 0.02.
P2 [I, expected to disagree, registered anyway]: the grid's microcanonical log correction is then −(r/2) ln A = −2.5 ln A. Compare Sen (arXiv:1205.0971): for Schwarzschild in D = 4 the microcanonical coefficient of ln A is (C_local − 1)/2 with C_local = (2n_S − 26n_V + 7n_F + 424)/90. With Standard Model fields (n_S = 4, n_V = 12; n_F = 24 if Dirac, 48 if Majorana, with ν_R) it is positive, between about +1.1 and +2.0. Pass if |−2.5 − Sen| < 0.5.
Consequence fixed in advance: if P2 fails, the bare balanced count is not the black hole's microstate count; the Euclidean one-loop part (the massless fields' fluctuations around the horizon) must be added to the grain's count, or the cells carry more structure than the 16. Recorded as an open obstacle, stated in any letter.
