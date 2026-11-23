# Pre-registered before running nearmiss.py (2026-11-09 ~01:10 ET). Label: math (calculation).
Object: for each prime p < 2,000,000, the quotient q_p = U_{p-e}/p (mod p) for golden phi (Fibonacci), silver 1+sqrt2 (Pell),
2+sqrt3, and the ordinary base-2 Fermat quotient (control). q_p = 0 is an exact Wieferich-type hit; small |q_p| is a near miss.
Randomness hypothesis: |q_p|/p (folded to [0, 1/2]) is uniform.
N1: all four distributions are uniform (Kolmogorov-Smirnov p-value > 0.01). Prediction: yes, golden included.
N2: near misses |q_p| <= k for k = 10 and k = 1000: observed counts match the expected sum of (2k+1)/p within Poisson noise
    (|z| < 3) for every case. Prediction: yes.
N3 (decisive for the "golden has no floor" idea): golden shows NO significant deficit of near misses relative to expectation
    (one-sided Poisson p > 0.01 at both k). If it does show a deficit while silver/sqrt3/base-2 do not, that is the first evidence of
    structure; otherwise golden's empty record is consistent with chance.

# Scored after run (2026-11-09)
N1 PASS: KS p = 0.883 golden, 0.715 silver, 0.932 2+sqrt3, 0.856 base 2. All uniform.
N2 PASS: all |z| < 3. k=10: golden 32 vs 31.1, silver 23, 2+sqrt3 18, base 2 35 (expected 31.1 each).
   k=1000: 1271, 1273, 1286, 1283 vs 1288.3.
N3 PASS: golden shows no deficit (P = 0.61 at k=10, 0.32 at k=1000). Golden quotients look exactly random.
Note: 2+sqrt3 has a k=10 deficit (P = 0.008), but with 8 tests this is within multiple-comparison noise (Bonferroni 0.00125).
Exact hits below 2e6: golden 0, silver 3 (13, 31, 1546463), 2+sqrt3 1 (103), base 2 2 (1093, 3511): consistent with ~2 expected each.
Conclusion: no evidence that the golden case is structurally different. "Golden has no finite floor" gets no support from the data.
