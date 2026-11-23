# Pre-registered before running mirror_pair.py (2026-11-14). Labels: M1 math; P1-P4, N1-N2 numerical tests of a known construction.
Build: the self-mirrored, paired operator in two parts.
(a) Mirror (frequency side). The dilation operator D = (xp+px)/2 has eigenfunctions |x|^(s-1). The Fourier transform (time <-> frequency)
    maps |x|^(s-1) to chi(s) |k|^(-s), chi(s) = pi^(-s/2)Gamma(s/2) / (pi^(-(1-s)/2)Gamma((1-s)/2)) (Tate). Grid reading: the mirror
    sends s to 1-s and keeps the weight equal on both sides only on the critical line.
(b) Pairing (primes). Spectral staircase F_X(T) = theta(T)/pi + S_X(T), S_X(T) = -(1/pi) sum_{n<=X} w(n) Lambda(n) sin(T ln n)/(sqrt(n) ln n),
    taper w(n) = 1 - ln n / ln X. Smooth part theta/pi = the hyperbola xp = E (Berry-Keating); prime powers = the periodic orbits of length ln p^k.
    F is odd in T, so the spectrum comes in +-gamma pairs; H = A^2 then has each gamma^2 twice (the two modes; positivity automatic).
    Ideal: at the n-th true zero gamma_n, F(gamma_n) = n - 3/2. Residual r_n = F(gamma_n) - (n - 3/2), in units of mean spacing.
Zeros: computed independently from the Riemann-Siegel Z function (own code), t in [10, 400].
M1: |chi(1/2 + it)| = 1 to 1e-10 at t = 14, 100, 400; at sigma = 0.6, t = 100, |ln|chi|| > 0.1.
P1: smooth only (X = 1): RMS residual in [0.15, 0.40].
P2: X = 100: RMS at least 40% below smooth only.
P3: X = 1000 beats X = 100.
P4: fraction of zeros with |r_n| < 0.5 (count assigned correctly): X = 1000 >= 0.99 and above smooth only.
N1 (fake primes): Lambda weights placed at ln of random integers in [2, 1000] (seed 20261114): RMS >= 0.9 x smooth only (no help).
N2 (sign flipped): -S_X with X = 1000: RMS above smooth only.
Interpretation fixed: if all pass, the mirror fixes the line and the prime pairing places the zeros on it to within a fraction of a spacing,
from primes alone. This does NOT prove RH: the construction assumes the zeros are counted on the line; a zero off the line would show up
as a residual that no finite X removes. What it tests is that the paired, mirrored operator reproduces the actual spectrum.

# Scored after run (2026-11-14)
M1 PASS: |chi(1/2+it)| - 1 = 0 (machine precision) at t = 14, 100, 400; ln|chi(0.6+100i)| = 0.277.
P1 PASS: smooth-only RMS 0.230.
P2 PASS: X = 100 RMS 0.044 (81% below smooth). (X = 10: 0.114.)
P3 PASS: X = 1000 RMS 0.028.
P4 PASS: fraction |r| < 0.5: smooth 0.985 (3 of 201 misassigned), X = 10, 100, 1000 all 1.000.
N1 PASS: fake primes RMS 0.330 (1.44 x smooth: worse, not better).
N2 PASS: sign flipped RMS 0.434.
Caveats: zeros from first-order Riemann-Siegel (first zero 14.1372 vs 14.1347); 201 zeros up to t = 400. Known construction (Tate; Berry-Keating;
Selberg-type truncated S(T)). Does not prove RH (see interpretation).
