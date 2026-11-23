# Pre-registration (2026-11-22, 16:10): the tower along light rays, measured on real geodesics (record §81)
Method: from a vertex x0, shoot the null geodesic with direction k = u + n (u the static observer, n a unit spatial direction set by angles a, b) and four neighbours k +- eps s_i (s_1, s_2 the screen directions); RK4, step 0.01, eps = 1e-4; separation vectors by central differences; Gram matrix G_ij = g(dX_i, dX_j)/lambda^2 at lambda = 0.1..1.0 (10 values). Area deficit 1 - sqrt(det G) and shape (eigenvalue gap of G) are fit by c1 lambda + c2 lambda^2 + c3 lambda^3 + c4 lambda^4. [M] From the Jacobi equation, J = lambda I - (lambda^3/6) T + O(lambda^4), T the tidal matrix on the screen: area deficit = (lambda^2/6) tr T + ..., shape = (2/3) lambda^2 w + ..., where tr T = R_ab k^a k^b (Ricci: Einstein's equations) and w = half the eigenvalue gap of T (Weyl: the free gravitational field). Order 1 must vanish (rays are geodesics, free).
Direct values: tr T and w from the Riemann tensor at the vertex (finite differences).
SANITY RUN (cone_sanity.py; seen; vertex r = 4, theta = 1.2, phi = 0.5, a = 0.9, b = 0.4): Schwarzschild direct R_kk 0, w 0.02876; cone R_kk -0.00001, w 0.02866; RN (Q^2 = 0.5) direct 0.00240, 0.02517; cone 0.00238, 0.02509. Order-1 coefficients 2e-7 to 7e-6.
FULL RUN on new vertices and directions (seed 20261122): 6 cases per metric, r in [3.5, 7] (de Sitter: r in [1, 5]), theta in [0.5, 2.6], a in [0.2, 2.9], b in [0, 6.2].
C0 [control] flat space: |R_kk est| and |w est| below 1e-5.
C1 [identity] order 1: |c1| below 1e-4 for area and shape, every case, every metric.
C2 [real] Schwarzschild: |R_kk est| below 3% of w direct; w est within 3% of w direct.
C3 [real] Reissner-Nordstrom (M = 1, Q^2 = 0.5): R_kk est within 5% of R_kk direct (nonzero); w est within 3% of w direct.
C4 [real] de Sitter (L = 10): |R_kk est| and |w est| below 1e-4 although |R_ab| ~ 0.03 (conformally flat and Einstein: light sees neither).

## Results (cone_run.log): all pass
C0 flat max 8.1e-8. C1 order 1 below 1e-4 in every case. C2 Schwarzschild: |R_kk est| at most 0.2% of w; w within 2.1%. C3 Reissner-Nordstrom: R_kk within 2.6% (values 0.00014-0.00238), w within 0.8%. C4 de Sitter max 1.4e-7.
