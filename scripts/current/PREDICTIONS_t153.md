# PREDICTIONS t153: the scalar's −1/90 on the record lattice

Registered 2026-11-26, before t153_log_term.py was written or run.

Question. t152 rests on the record's field entanglement carrying the trace-anomaly log term. For a free massless scalar and a sphere of radius R, the entanglement entropy is S = c₂R² + c_log ln R + c₀ + …, with c_log = −4a = −1/90 (a = 1/360; Solodukhin 2008, Casini and Huerta 2010; on this lattice Lohmayer, Neuberger, Schwimmer and Theisen 2010). Reproduce it on t27's lattice (Srednicki's radial chain).

Engine. Radial chain of N sites, partial waves l, S(n) = Σ_l (2l + 1) S_l(n), R = n + 1/2, N = 6n (outer wall at a fixed ratio, so the setup scales with R).
Partial-wave sum: exact N-site diagonalisation for l ≤ 1500; for larger l the correlations are local to the cut (mass term l/j beats the hopping), so S_l is computed on a window of sites around n, the window size fixed by a convergence check (S_l with window w and 2w agree to 1e-14 at the switch point), on a geometric grid of l up to 2×10⁶ and summed by Euler–Maclaurin; beyond that a fitted power-law tail. Numerical settings may be tightened by convergence checks; the fit and criteria below are fixed now.
Radii: n = 10, 12, 14, 16, 20, 24, 28, 32, 40.

S1 [sanity]: the area coefficient c₂ within 2% of t27's 0.295.
S2 [convergence]: S(n) changes by less than 1e-6 between the base settings and doubled settings (exact-l cutoff, window, grid density) at n = 20.
P1 [M]: fit S(n) = c₂R² + c_log ln R + c₀ + c₋₂/R² over all radii: c_log = −0.01111 within 10%.
P2 [M]: the same within 15% when the 1/R² term is dropped or when the three smallest radii are removed (stability of the fit).
Consequence fixed in advance: P1 and P2 pass → the record's lattice carries the anomaly log term, and t152's field part is computed here, not only cited.
