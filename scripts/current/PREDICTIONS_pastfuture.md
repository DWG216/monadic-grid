# Pre-registration (2026-11-22, 16:30): the other hand as the reverse strand, on light cones (record §83)
Method as §81 (cone_lib), with the past cone along the same ray: velocity -k, screen (s1, -s2) so that each cone's screen is right-handed relative to its own direction of travel; screen basis rotated by a fixed 0.6 rad (the sanity run showed the Schwarzschild ellipse aligned with the unrotated basis, a degenerate angle).
[M, expectation] Tidal matrix T is quadratic in k, so order 2 is the same for past and future (time-even); in each cone's own right-handed screen the ellipse's axis angle is reflected (theta_past = -theta_future mod pi): conjugate complex shear. Order 3 involves the derivative of curvature along the ray, odd in the direction: its coefficient flips sign.
SANITY RUN (pf_sanity.py; seen; one Schwarzschild case): shape c2 future 0.019109, past 0.019291; c3 -0.005069, +0.004941.
FULL RUN (seed 20261122): 4 Schwarzschild and 4 Reissner-Nordstrom (Q^2 = 0.5) cases, r in [3.5, 7], theta in [0.5, 2.6], a in [0.2, 2.9], b in [0, 6.2].
P1 [real] order 2 time-even: shape c2 (past) within 3% of shape c2 (future), every case; RN area c2 within 5%.
P2 [real] conjugate shear: theta_future + theta_past = 0 mod pi within 0.02 rad at lambda = 0.3, every case.
P3 [real] order 3 time-odd: for every case with |shape c3 (future)| > 1e-3, opposite sign and |c3 future + c3 past| < 15% of |c3 future|.
P4 [real] matter is time-symmetric: RN area c2 past and future both positive and within 5% (same as P1's area part).
Reading fixed in advance: P1-P3 passing means the reverse strand carries the same curvature with the opposite orientation (conjugate shear, the other hand) and the opposite odd part; the balanced pair (future + past) cancels the odd orders and keeps the even ones.

## Results (pf_run.log)
P1 FAIL as registered: shape c2 past vs future within 0.1-2.1% in 7 of 8 cases; the eighth (RN, r = 5.43, shape c2 0.00077) differs by 3.2%. RN area c2 within 0.4-2.8% in 3 of 4; the fourth (area c2 0.000013/0.000014) by 7%. Both misses are at the smallest coefficients, where differences of 2e-5 (shape) and 1e-6 (area) are at the fit's noise level (labelled reading, no rerun).
P2 PASS, but weak: theta_future + theta_past = 0 mod pi to 1e-4 in every case; post hoc it is forced by spherical symmetry (the ellipse's axis is always the screen projection of the radial direction), so the test had no way to fail here. A non-symmetric spacetime (Kerr) is needed for a real test.
P3 PASS: order-3 coefficients opposite in all 8 cases (e.g. -0.00587/+0.00583, +0.00158/-0.00157), sums within 15%.
P4 FAIL as registered (same RN case as P1); in the other three cases matter's area term is the same in both cones within 2.8%, both positive.
