# Pre-registration (2026-11-22, 03:10), under the rules: positive control first, sanity run first
Question (from §60 test 3, §61 A): can an operator's entries carry the prime/Mobius information the zeros carry (§62)?
Operator: the Jacobi (tridiagonal) matrix J with our 201 zeros as eigenvalues and e1-spectral weights w (Lanczos).

SANITY RUN (t10_sanity.py, done before freezing; seed 1, 50 null draws):
- entries-only spectral function <f, exp(iuJ) e1> by Chebyshev recurrence on the entries a, b (no diagonalisation) equals the eigen sum to 6e-10;
- OLD detector (Fourier of the detrended diagonal at positions a_k, §60/§61) against a huge planted modulation w = 1 + 0.9 cos(gamma ln 2): 62nd percentile of its null, i.e. blind;
- NEW detector (peak of Re <e1, exp(iuJ) e1> at u = ln 2 over the median of |.| in a +-0.5 window) on the same plant: 34.7 vs null 95th 8.15;
- J built from |c| (c = taper/(rho zeta'(rho))) plus a readout vector f carrying the phases reproduces §62's jumps to 6e-9 (18/18 signs). This is an identity [M], so it is not a test below.

## P. Positive controls (200 null draws: weights permuted among the zeros, seed 20261122)
P1 OLD detector, planted w = 1 + 0.9 cos(gamma ln 2): below its null's 95th percentile (we expect it blind; if it passes, the §61 withdrawal is reopened).
P2 NEW detector, same plant: peak at ln 2 above its null's 95th percentile.
P3 NEW detector, w = |sum_{n<=50} Lambda(n) n^(-1/2 - i gamma)|^2 (primes planted; |.|^2 puts frequencies at ln(m/n)): peaks at ln 2, ln 3, ln(3/2) all above the null's 95th.
P4 NEW detector, negative control: same polynomial over fake prime powers x_m uniform in [2, 50] (non-integers, seed 20261122): peak at ln 2 NOT above the null's 95th.
Only if P2-P4 pass do R1-R3 count.

## R. Real (Mobius weights, from zeta alone)
c_n = taper / (rho_n zeta'(rho_n)) as in §62; jumps J(n) = S(ln n + 0.012) - S(ln n - 0.012), n = 2..30; 18 squarefree, 11 not.
R1 [real] Magnitudes only: J built from w = |c| and read with e1 alone, S(u) = 2 Re <e1, exp(iuJ) e1>. A positive spectral measure cannot carry signs, so we predict the Mobius signs are NOT recovered: sign count at squarefree n not above the null's 95th (null: |c| permuted among the zeros).
R2 [real] Same operator, read through the phase vector f (f = Q (conj(c) sqrt(sum|c| / |c|))): sign count above the null's 95th and ratio squarefree / non-squarefree |J| > 2 (an identity [M]; recorded as the reference).
R3 [exploratory, no pass/fail] Locality: keep only the top-left K x K block of J and the first K components of f, K = 25, 50, 100, 150, 175, 201. How many of the 18 signs, and how close the jumps (median |J_K / J_full| at squarefree n), as K grows? Expectation [argument]: resolving frequency u needs Chebyshev degree ~ u r (r ~ 192, the spectrum's half-width), more than the block can supply until K is near N, so we expect few signs until K is close to 201.

## Results (t10_operator.py, 200 null draws; log t10_operator.log)
P1 as predicted: old detector blind to the huge plant (71st percentile). The §61 withdrawal stands; the detector is retired.
P2 PASS: new detector, planted ln 2: 34.70 vs null 95th 8.84.
P3 FAIL (positive control): primes planted via |sum Lambda(n) n^(-1/2-i gamma)|^2: ln 2 6.85 vs 8.55; ln 3 8.99 vs 10.29; ln 3/2 0.04 vs 2.58.
P4 PASS: fake primes at ln 2: 4.48 vs 6.18 (not above).
Because P3 failed, R1-R3 do NOT count as tests. Recorded as exploratory:
R1 magnitudes only (J from |c|, read with e1): 8/18 signs (null 95th 12), ratio 1.07: no Mobius signs.
R2 with the phase vector: 18/18 (null 95th 14), ratio 77.0, equal to §62 to 5.6e-9 (identity).
R3 locality, top-left K x K block: K = 25: 10/18 (median |J_K/J| 0.51); 50: 15/18 (0.47); 100: 18/18 (0.56); 150: 18/18 (0.90); 175: 18/18 (0.95); 201: 18/18 (1.00). Our expectation (few signs until K near 201) was wrong: all signs are readable from half the rows.
POST HOC (t10_posthoc.py, labelled): the zeros with uniform weights already dip at ln 2 (-0.151) and ln 3 (-0.199); the primes are in the zeros' positions, so a weight-permutation null keeps them, and the P3 plant (187 frequencies ln(n/m) within ln 2 +- 0.5) cannot rise above it. A sparse plant 1 + 2^-s + 3^-s gives peaks 18.6 (ln 2), 4.3 (ln 3), 9.1 (ln 3/2) without a null: candidate positive control for a next round, not counted here.
