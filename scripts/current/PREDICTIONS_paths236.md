# Pre-registration (2026-11-22, 16:00): googly paths 2, 3 and 6 (record §80)
SANITY RUN (g_sanity.py, seed 1, one point each; seen): max |R_ab k^a k^b| over null k: Schwarzschild 3.5e-8, Reissner-Nordstrom (Q^2 = 0.1) 7.8e-4, de Sitter (L = 10) 3.0e-8 with |R_ab| = 0.48, FRW dust 1.3; flat-space Z.W 5e-16; a coboundary changed the contour field by 3e-14 (field size 0.15). Both outcomes occur, so the tests can discriminate.
Full run: seed 20261122, 20 points per metric (r in [3, 8], theta in [0.4, 2.7]; FRW t in [0.8, 1.5]), 12 null directions each.

## Path 2: the veil. Ambitwistor space = pairs (Z, W), Z = (i x pi, pi), W = (lam, -i x^T lam).
A1 [identity] for random complex x, lam, pi: Z.W = 0 (below 1e-12), and (Z, W) is unchanged along the null line x + t lam pi^T (below 1e-12).
A2 [identity] given (Z, W) with Z.W = 0, the points x solving omega = i x pi and nu = -i x^T lam form a line whose direction has det = 0 (a null line); given Z.W != 0 there is no solution (least-squares residual above 1e-3 of the data).

## Path 3: the tower along a ray. [M] R_ab k^a k^b = 0 for every null k iff R_ab = f g_ab; with the Bianchi identity in four dimensions, f is constant: Einstein's equations with a cosmological constant are a condition on light rays alone (second order along the ray: focusing, Raychaudhuri). The cosmological constant is invisible to it.
T1 [positive control] Schwarzschild (M = 1): max |R_kk| below 1e-5 at all 20 points.
T2 [positive control] de Sitter (L = 10): max |R_kk| below 1e-5 although max |R_ab| is above 0.01 (light does not see Lambda).
T3 [null] Reissner-Nordstrom (Q^2 = 0.1, electromagnetic energy): max |R_kk| above 1e-4 at every point; FRW dust: above 0.1.

## Path 6: the collective. A twistor field depends only on the gluing data up to coboundaries (agreement on the overlap).
G1 [identity] f = 1/((a.Z)^3 (b.Z)^3) on the overlap U0 = {a.Z != 0} and U1 = {b.Z != 0}; adding h0 = (c.Z)^2/(a.Z)^8 (holomorphic on U0) and h1 = (d.Z)^3/(b.Z)^9 (holomorphic on U1) changes the field by less than 1e-9 of its size, at 20 random points.
G2 [null] adding eps/((a.Z)^2 (b.Z)^4) (poles in both patches, not a coboundary), eps = 0.1: the field changes by more than 1e-3 of its size.

## Results (paths236.log); post hoc diagnosis (paths236_posthoc.py, labelled; not upgraded)
A1 FAIL as registered: Z.W = 0 holds (2.8e-15), but (Z, W) changed along the line (23) because the registered direction lam pi^T lacked the spinor epsilon. Post hoc: with direction (eps lam)(eps pi)^T the change is 2.1e-15. Design error, not a counterexample.
A2 PASS: Z.W = 0 gives a null line of points (rank 3, det of direction 0); Z.W != 0 gives none.
T1 PASS: Schwarzschild max |R_kk| 3.5e-7.
T2 PASS: de Sitter max |R_kk| 2.5e-6 while |R_ab| >= 0.09: light does not see Lambda.
T3 FAIL as registered: Reissner-Nordstrom min |R_kk| 6.6e-5, below the 1e-4 threshold (FRW dust min 0.60 passed). Post hoc: RN tracks Q^2/r^4 (2.5e-3 at r = 3 to 4.8e-5 at r = 8) and exceeds Schwarzschild at the same points by 5,700-23,000 times; the threshold was set too high for r up to 8.
G1 FAIL as registered: coboundary changed the field by 7.0e-8 of its size (threshold 1e-9). Post hoc: the coboundary's own integral is 4e-15 of the integral of its absolute value (roundoff on large terms near poles of order 8 and 9); the residual is numerical.
G2 PASS: a non-coboundary change of 0.1 changes the field by at least 2.2e-2.
