# Pre-registration (2026-11-22, 16:40): Kerr (no spherical symmetry) and order 4 (record §84)
Method as §83 with a general orthonormal frame (static observer, Gram-Schmidt in the full metric). Kerr M = 1, a = 0.9 (Boyer-Lindquist). Affine distances 0.05..1.2 (24 values); area and shape fit with powers 1..6; ellipse axis angle (in each cone's right-handed screen, rotated 0.6 rad) fit linearly on lambda <= 0.4.
[M, expectation] G/lambda^2 = I - (lambda^2/3) T - (lambda^3/6) T' + lambda^4 [T^2/36 + c T''] + ..., with T even, T' odd, T'' and T^2 even under reversing the ray. So: order 2 even, order 3 odd, order 4 even (it carries the shear-squared term T^2, where the two hands meet: Psi_0 times its conjugate). In each cone's right-handed screen the order-2 angle reflects (intercepts sum to 0 mod pi) while the order-3 rotation keeps its sign (equal slopes).
SANITY RUN (kerr_sanity.py; seen; one case r = 4.5, theta = 1.0): Kerr vacuum (R_kk 2e-8), shape c2 0.012893 both cones, w est 0.01934 = direct 0.01934; c3 -0.002377/+0.002376; c4 +0.000142/+0.000143; angle intercepts 2.6025 / 0.5391 (sum 0 mod pi; intercept 0.06 from the screen rotation, so not forced); slopes -0.0403 / -0.0428.
FULL RUN (seed 20261122): 6 Kerr cases (r in [3.5, 7], theta in [0.5, 2.6], a in [0.2, 2.9], b in [0, 6.2]) and 4 Schwarzschild cases (order 4 only).
K1 [real] Kerr vacuum: |6 x area c2| below 3% of direct w; 1.5 x shape c2 within 3% of direct w (future cone).
K2 [real] conjugate shear without symmetry: |theta0_future + theta0_past| mod pi below 0.02 in every case; and in at least 4 of 6 cases theta0_past is more than 0.03 from the screen rotation 0.6 (the test is not forced).
K3 [real] equal rotation: where |slope_future| > 0.01, same sign and difference below 20%.
K4 [real] order 3 odd: shape c3 opposite sign, |sum| below 15% of |c3 future| (cases with |c3| > 1e-3).
K5 [real] order 4 even: shape c4 future and past within 10% (cases with |c4| > 5e-5), Kerr and Schwarzschild.

## Results (kerr_run.log); post hoc (kerr_posthoc.py, labelled; verdicts unchanged)
K1 PASS: Kerr area term at most 3.8e-7; w estimate equals the direct value to 4-5 digits in all 6 cases.
K2 PASS: angle intercepts sum to 0 mod pi within 1e-4 in all 6 cases, and the intercept is 0.054-0.436 rad from the screen rotation in all 6 (not forced).
K3 FAIL as registered: slopes have the same sign in all 6 cases, but two differ by 25% and 34% (linear fit). Post hoc: a quadratic fit gives equal slopes to 3-4 digits in all 6 (e.g. -0.0202/-0.0201, -0.0398/-0.0398); the linear fit was biased by the lambda^2 term, which has opposite sign in the two cones in 5 of 6 cases (as the mirror predicts for an even-order term).
K4 PASS: order 3 opposite in all 6 Kerr cases (e.g. -0.00595/+0.00596).
K5 FAIL as registered: order-4 shape coefficients agree within 10% in 9 of the 10 cases with |c4| > 5e-5; the tenth (Schwarzschild r = 5.43, c4 7.4e-5/8.2e-5) differs by 11%. Post hoc: over six fit choices the future and past ranges overlap in all 10 cases; the miss is within the fit's spread.
