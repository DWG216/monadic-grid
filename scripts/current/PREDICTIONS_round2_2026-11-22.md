# Pre-registration (2026-11-22, 02:05): five tests (proposals 1-5)
## 1. Is the four-solution result a law for every mirror step?
System for a sequence with s(n+1) = t s(n) - Q s(n-1), unknowns a = s(-1), b = s(0), c = s(1):
  Q = -1 (mirror, det -1): a = b^2 + a^2, c = c^2 + b^2, t b = c^2 - a^2.
  Q = +1 (contrast, det +1): a = b^2 - a^2, c = c^2 - b^2, t b = c^2 - a^2.
(These are the doubling formulas s(2n-1) = s(n)^2 + Q... at n = 0, 1 and t s(2n) = s(n+1)^2 - s(n-1)^2.) Solved by multistart Newton in C^3 (4000 starts, seed 20261122).
1a [M] Q = -1, t = 1, 2, 3, 4: exactly 4 solutions, all real: 0, the two pure modes lambda^n/(lambda-mu) and -mu^n/(lambda-mu), and their sum (the integer sequence 1, 0, 1 at n = -1, 0, 1); the mirror condition a = c keeps exactly {0, integer sequence}.
1b [M] Q = +1: t = 3 has 4 solutions, all real; t = 1 (|t| < 2, rotation) has 4 solutions of which exactly 2 are real (the pure modes are complex). The integer sequence there is (-1, 0, 1): it is selected by a = -c (antisymmetric), not by a = c.
## 2. Golden Artin from first principles (derived before running the new range)
Heuristic (Hooley-type, our derivation): clock = lcm(ord phi, ord -1/phi). Split p: the 2-part fails only if p = 1 mod 4 and phi is a square (prob 1/4); 5-part fails if p = 1 mod 5 and phi is a 5th power (prob 1/10 within split); other odd l: (1 - 1/(l(l-1))). Inert p: phi has norm -1, so the 2-part never fails, l = 5 never divides p + 1, other odd l: (1 - 1/(l(l-1))).
Predicted densities: inert = prod over odd l != 5 of (1 - 1/(l(l-1))) = 0.7873; split = 0.75 * 0.9 * 0.7873 = 0.5314; all = 0.6593.
2a [real] For primes in [2*10^6, 10^7): split share within 0.005 of 0.5314, inert within 0.005 of 0.7873, all within 0.005 of 0.6593.
## 3. Can the zeros hear the primes through an operator?
Build the Jacobi (tridiagonal) matrix whose eigenvalues are our 201 zeros (uniform weights, Lanczos). Detrend its diagonal a_k against position (cubic fit in a_k), then form P(x) = |sum_k d_k e^(i a_k x)|^2 for x in [0.5, 2.2].
3a [real, exploratory] at x = ln 2, ln 3, ln 5, ln 7, P exceeds the 95th percentile of 200 nulls (zeros rebuilt from shuffled spacings) for at least 3 of the 4.
## 4. Weil positivity on our zeros
Explicit formula (Guinand-Weil): sum over zeros h(gamma) = h(i/2) + h(-i/2) - g(0) ln pi + (1/2pi) int h(r) Re psi(1/4 + i r/2) dr - sum_n Lambda(n)/sqrt n [g(ln n) + g(-ln n)].
4a [M, implementation check] Gaussian h(r) = exp(-r^2/25): the two sides agree to 1e-6.
4b [real] For 7 smooth bumps f_i (centres -1.5..1.5, half-width 0.5), the arithmetic-side matrix Q_ij (h_ij = F_i(r) F_j(-r)) matches the zero-side Gram matrix sum_gamma F_i(gamma) conj F_j(gamma) to relative error < 1e-3, and its smallest eigenvalue is >= -1e-6 x its largest.
4c [null] the same arithmetic side with fake prime powers (random integers, seed 20261122) gives a negative eigenvalue below -1e-3 x the largest.
## 5. A queen monad: does one strong oscillator entrain a body, and does gating matter?
Body: 50 oscillators, rates 1 + 0.03 normal (seed 20261122), no coupling among themselves, same concave state as §59 (b = 3). Leader: rate 1, kicks every body member by eps_L once per its cycle: GATED at its zero, UNGATED at a fresh random phase. eps_L in {0.005, 0.01, 0.02, 0.04, 0.08}; 600 cycles; a member is entrained if it fires exactly as many times as the leader in the last 200 cycles.
5a [real] GATED: entrained fraction increases with eps_L and reaches >= 0.9 at eps_L = 0.08.
5b [real] UNGATED: entrained fraction <= 0.3 at every eps_L.
5c [real] GATED needs less coupling: it passes 0.5 at a smaller eps_L than UNGATED (UNGATED may never pass it).

## Results
1a PASS, 1b PASS: Q = -1 (t = 1..4): 4 solutions, all real, = {0, two pure modes, their sum}; a = c keeps exactly {0, (1,0,1)}. Q = +1: t = 3 four real; t = 1 four solutions, two real; the integer sequence (-1,0,1) is kept by a = -c, not a = c. (A bug in my check of the pure modes, t^2 + 4Q instead of t^2 - 4Q, was fixed before scoring; the solution counts were unaffected.)
2a PASS: primes in [2e6, 1e7) (515,646): split 0.5318 (pred 0.5314), inert 0.7880 (0.7873), all 0.6600 (0.6593); every difference < 0.001. Caveat: the formula was derived after seeing the 66% measurement below 2e6; this range is new data.
3a FAIL: the uniform-weight Jacobi matrix's detrended diagonal shows none of ln 2, 3, 5, 7 above the shuffled-spacing null (percentiles 0.11, 0.49, 0.68, 0.35). Post hoc diagnostic: the same detector on the raw zeros puts all four at the 100th percentile. The naive operator scrambles the prime information that the spectrum carries.
4a FAIL (narrow): Gaussian check agrees to 1.9e-6, not 1e-6 (our zeros come from first-order Riemann-Siegel).
4b FAIL as run: relative mismatch 2.5e-2 and a negative eigenvalue (-5.2e-3 of the largest). Diagnosis: the missing zeros above t = 400 contribute ~5e-15 (t4_tail.py), so not truncation; the cause is a rounding step in the correlation (grid shift) plus zero precision ~1e-6. Post hoc (interpolated correlations, wider grid, t4_weil_posthoc.py): max |A - Z| = 5.5e-6; the prime-side matrix is positive definite (min/max +9.65e-3), its 7 eigenvalues match the zero-side Gram matrix to < 1%.
4c PASS: fake primes give min/max = -0.73.
5a FAIL: gated entrainment saturates at 0.50 (eps 0.04 and 0.08), because half the body runs faster than the leader and excitatory kicks cannot slow an oscillator (a design flaw I should have seen). 5b PASS: ungated <= 0.10 at every eps. 5c borderline: gated reaches 0.50 at eps = 0.04; ungated never exceeds 0.10.
Post hoc (leader rate 1.08, faster than nearly all members): gated 0.02, 0.02, 0.38, 0.88, 1.00; ungated 0.02, 0.00, 0.04, 0.08, 0.08.
