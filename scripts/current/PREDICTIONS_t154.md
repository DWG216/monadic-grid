# PREDICTIONS t154: the log term on a black-hole horizon

Registered 2026-11-26, before t154_schwarzschild_log.py was written or run.

Question. t153 reproduced the flat-sphere log term (−1/90 = −4a for a scalar). On a Ricci-flat horizon the local coefficient is instead Sen's per-field C = 4(c − a): for a minimally coupled scalar 2/90 = +1/45 multiplying ln(r_s), positive. Compute it on a record lattice around a Schwarzschild horizon.

Engine. Massless minimally coupled scalar outside a Schwarzschild black hole (radius r_s), partial waves l, χ = rφ. Exact reduction (derived here): L = ½∫dr [χ̇²/f − fχ′² − (l(l+1)/r² + r_s/r³)χ²], f = 1 − r_s/r. The record's lattice is uniform in proper radial distance ρ (dr = √f dρ), spacing ε, sites ρ_i = iε, Dirichlet at the horizon (ρ = 0) and at a wall r = 4r_s. Discrete: masses ε/√f_i, springs √f_{i+1/2}/ε, potential ε√f_i W_i. The Hartle–Hawking state restricted to the outside is thermal at T = 1/(4πr_s) in Killing time, so the horizon's entanglement entropy is Σ_l (2l + 1) Σ_modes s(ω/T), s(x) = x/(eˣ − 1) − ln(1 − e⁻ˣ). With the wall at a fixed multiple of r_s, every term except the cutoff ε scales with r_s, so S = c₂L² + c_log ln L + c₀ + c₋₂/L² + … with L = r_s/ε.
Sizes: L = 8, 10, 12, 14, 16, 20, 24, 28, 32, 40; l summed until the next term is below 1e-14.

S1 [convergence]: at L = 20, S changes by less than 1e-6 when the l cutoff is tightened to 1e-16.
S2 [box]: c_log changes by less than 10% when the wall moves from 4r_s to 6r_s (radii L ≤ 32 for the second run).
P1 [M]: c_log = +1/45 = +0.02222 within 15%.
P2 [M]: the sign is opposite to t153's flat sphere (−0.0111): the horizon's curvature flips it.
Consequence fixed in advance: P1 passes → the grid's log term on a black hole is computed on its own lattice for the scalar; the photon (−26/90 with edge modes) remains the next item (t155).
Prior work: 't Hooft's brick wall (1985); Solodukhin's review of entanglement entropy of black holes (Living Rev. Rel. 2011) for the conical-singularity log term; Sen 2012 for C_local.
