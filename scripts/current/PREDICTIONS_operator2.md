# Pre-registration (2026-11-22, 05:30): more about the operator (record §77)
SANITY RUN (t16_sanity.py; seen): for the golden L-function L(s, chi_5) (chi_5 = the quadratic character mod 5, the Euler factors of Q(sqrt 5)), the operator built from primes weighted by chi_5(n), conductor term ln(5/pi), no pole term, window 3-25, returns 6.6485, 9.8314, 11.9588, 16.0338, 17.5670, 19.5407, 22.2274, 24.5885, matching our direct computation of L(1/2 + it, chi_5) (Hurwitz zeta by Euler-Maclaurin) to 4 decimals.
G1 [real] golden window B (centres 28..55.5 step 1.5; not computed): every directly computed zero of L(s, chi_5) in [30, 53] has a Ritz value within 0.001; the form is positive (min/max >= -1e-10).
G2 [null] the same window with the zeta primes (no character) but the chi_5 conductor term: fewer than half of those zeros matched within 0.01.
X1 [real] how many primes: zeta, window 47-80, the 9 published zeros in [50, 77]; prime powers cut at X. Expectation [M]: the test functions on the scale side are Gaussians of width ~1/1.06 in u, so prime powers beyond about e^4 ~ 55 contribute below 1e-4. Prediction: with X = 100 all 9 are within 0.01; with X = 10 fewer than 9 are; with no primes at most 2 are.
A1 [real] the pole term: zeta, window 9-46; dropping it moves no Ritz value by more than 1e-4 (the two ends 0 and 1 are far from tones at these heights).
D1 [exploratory] the eigenvector for the zero 59.347 as a function of frequency r: it should be 1 at that zero and 0 at the other zeros in the window.

## Results (t16_operator2.log): all pass
G1 PASS: 12 zeros of L(s, chi_5) in [30, 53] matched within 0.00017 (33.0004/33.0005, 34.7288, 35.8686, 38.1292, 39.5606, 41.8424, 44.0313, 45.4273, 46.4927, 48.3457, 51.0877/51.0878, 52.1257/52.1259); positivity min/max 9e-9. G2 PASS: without the character 0 of 12.
X1 PASS: no primes 0/9 (max distance 0.56); primes to 10: 0/9 (0.70); to 30: 9/9 (0.0075); to 100: 9/9 (1e-5); 300 and beyond: below 1e-5.
A1 PASS: dropping the pole term shifts nothing (2e-14).
D1: the eigenvector for 59.347 is 1.000 there and at most 0.002 at the 14 other zeros in view.
