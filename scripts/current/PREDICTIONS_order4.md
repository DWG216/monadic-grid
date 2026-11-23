# Pre-registration (2026-11-22, 16:45): order 4 predicted from the curvature (record §85)
[M] Jacobi equation J'' = -T(lambda) J, J(0) = 0, J'(0) = I, with T(lambda) = T0 + T1 lambda + T2 lambda^2/2 + ... in a parallel-transported screen frame. Series solution: J/lambda = I - T0 lambda^2/6 - T1 lambda^3/12 + (T0^2/120 - T2/40) lambda^4, so
M(lambda) = J^T J / lambda^2 = I + A lambda^2 + B lambda^3 + C lambda^4 + ..., A = -T0/3, B = -T1/6, C = (2/45) T0^2 - T2/20.
Predicted side: T(lambda) from the Riemann tensor along the central ray in a parallel-transported frame (9 points, lambda 0..0.4, quartic fit): no cone. Measured side: the cone's Gram matrix (§81-§84), each entry fit with powers 2..7 on lambda 0.05..1.2.
SANITY RUN (o4_sanity.py; seen; Kerr, r = 4.5): A, B, C agree to 4e-6, 1e-4, 2.5e-3; C without the T0^2 term misses by 0.12. T0^2 part was proportional to the identity.
FULL RUN (seed 20261122): 4 Kerr (a = 0.9), 3 Schwarzschild, 3 Reissner-Nordstrom (Q^2 = 0.5); r in [3.5, 7], theta in [0.5, 2.6], a in [0.2, 2.9], b in [0, 6.2].
O1 [real] relative difference measured vs predicted: A below 1e-3, B below 1e-2, C below 2%, every case.
O2 [real] the meeting term is needed: dropping (2/45) T0^2 makes the C difference at least 5 times larger, every case.
O3 [M + real] in vacuum T0 is trace-free, so T0^2 = w^2 I: the order-4 meeting of the hands is pure area (shear feeding focusing, the sigma^2 term of Raychaudhuri), with no shape part. Check: anisotropy of the T0^2 part (eigenvalue gap / mean) below 1e-3 for Kerr and Schwarzschild; above 1e-2 for Reissner-Nordstrom (T0 has trace there).

## Results (o4_run.log)
O1 PASS: A to 9e-7..9e-5, B to 3e-5..1.7e-3, C to 3.5e-4..1.9e-2 (all below 2%), in all 10 cases.
O2 FAIL as registered: in all 7 vacuum cases dropping T0^2 worsens the C difference by 10-800 times (e.g. 5.0e-3 -> 2.1e-1; 1.2e-2 -> 10); in the 3 Reissner-Nordstrom cases the T0^2 term is 0-3% of C and dropping it changes the difference by factors 1.0, 1.1, 3.3. The prediction should have been conditioned on the term's share; recorded as failed.
O3 PASS: anisotropy of the T0^2 part below 2e-5 in all 7 vacuum cases (pure area), 0.13-0.19 in Reissner-Nordstrom.
Exploratory: the T0^2 share of C ranges from 0.02 to 1.00 in vacuum (it dominates where the second derivative of curvature along the ray is small).
