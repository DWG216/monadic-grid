# Pre-registration (2026-11-22, 02:40)
## A. The operator rebuilt with arithmetic weights (§60 test 3 failed with uniform weights)
Jacobi matrix whose eigenvalues are our 201 zeros, with spectral weights w_n proportional to 1/|zeta'(rho_n)|^2 (= 1/|Z'(gamma_n)|^2 from Riemann-Siegel; the weights of 1/zeta, i.e. of the Mobius ledger). Same detector as §60: detrended diagonal d_k, P(x) = |sum_k d_k e^(i a_k x)|^2 at x = ln 2, 3, 5, 7. Null: the same weights randomly permuted among the zeros (200 draws, seed 20261122).
A1 [real] P exceeds the null's 95th percentile at >= 3 of the 4 prime frequencies.
A2 [built-in positive control, not a test] weights w_n = |sum_{n<=50} Lambda(n) n^(-1/2 - i gamma)|^2 (primes put in by hand) pass the same detector.
A3 [real] negative control: weights from a polynomial over fake prime powers (random integers, seed 20261122) do NOT pass at ln 2, 3, 5, 7 (<= 1 of 4).
## B. Two worlds and switching (proposal 7)
60 pulse-coupled oscillators (state x = ln(1 + (e^3 - 1) phase)/3), rates 1 + 0.005 normal; two worlds of 30, started synchronised at phases 0 and 0.5; kicks eps = 0.004 go only to members of the kicker's current world (gated at firing, cascades absorbed). Each member requests a switch with probability s per cycle, s in {0.01, 0.05, 0.2}. The switch executes:
  OWN: at the member's own next firing (its zero);
  TARGET: at the target world's next firing (the collective's zero), receiving that firing's kick;
  ANY: at the moment of the request (random phase).
400 cycles, seeds 20261122 + k (k = 0, 1, 2). A switcher is locked when within 0.02 of its world's circular mean phase for 3 consecutive cycles.
B1 [real] at s = 0.01 both worlds stay coherent (mean within-world r > 0.9 over the last 200 cycles) under all three rules.
B2 [real] median time to lock after a switch: TARGET < ANY; OWN within 20% of ANY (joining at the collective's gate helps; one's own gate alone does not).
B3 [real] at s = 0.2, mean within-world r: TARGET > ANY.

## Results
A1 FAIL: 1/|zeta'|^2 weights: percentiles 0.575, 0.10, 0.755, 0.79 (0 of 4 above the 95th).
A2 FAIL (positive control): primes put into the weights by hand also give 0 of 4 (0.305, 0.61, 0.245, 0.90). So the detector (Fourier of the detrended Jacobi diagonal at positions a_k) is blind to spectral frequencies. This also voids the §60 reading of test 3 ("the naive operator scrambles the primes"): that test could not have passed whatever the weights.
A3 PASS (trivially, given A2): fake-prime weights 0 of 4.
B1 PASS: within-world r > 0.9 for every rule and rate (0.94-0.997).
B2 FAIL: median lock times (cycles, from the moment the switch executes): s = 0.01: OWN 4.06, TARGET 3.19, ANY 3.12; s = 0.05: 3.66, 2.78, 2.61; s = 0.2: 3.17, 2.82, 2.50. ANY is fastest; TARGET is not faster than ANY; OWN is 27-40% slower than ANY. (Gated rules also wait before executing, which these times do not even count.)
B3 FAIL: at s = 0.2, r: TARGET 0.9907 < ANY 0.9969.
Reading: in pulse-coupled worlds the world's own firing absorbs a newcomer wherever it arrives; waiting for a gate adds delay and buys nothing. The "re-link only at the gate" reading of birth and death is not supported by this model.
