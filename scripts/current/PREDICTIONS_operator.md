# Pre-registration (2026-11-22, 05:25): the operator from the primes (record §75)
Object [M]: on test functions g(u) of the scale u = ln x, the generator of scaling D = -i d/du (on the frequency side: multiplication by r), with the Weil form as inner product: <g1, g2> = sum over zeros of h1 h2-bar, computed WITHOUT the zeros from the explicit formula (pole term, Gamma term, primes). D^2 in a basis of Gaussians phi_c (centres c, width s = 1.5): Gram G, form H (h times r^2), Ritz values = sqrt of the eigenvalues of H relative to G (directions with G-eigenvalue below 1e-7 of the largest dropped).
SANITY RUN (t15_sanity.py; window A, centres 9..46; seen): G is positive (min/max -3e-16); 9 directions kept; Ritz values 14.135, 21.022, 25.011, 30.425, 32.935, 37.586, 40.919, 43.327, 48.009 (published zeros 14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, 40.9187, 43.3271, 48.0052). Random "fake primes" kept G positive, so the null below is on the Ritz values.
TEST on window B (centres 47..80.5 step 1.5; not computed before freezing). Reference: published zeros (from memory, 6 decimals) 48.005151, 49.773832, 52.970321, 56.446248, 59.347044, 60.831779, 65.112544, 67.079811, 69.546402, 72.067158, 75.704691, 77.144840, 79.337375.
T1 [real] every published zero in [50, 77] (11 of them) has a Ritz value within 0.01.
T2 [real] the number of kept directions is 12, 13 or 14 (the zeros the window sees: the primes count them).
T3 [real] G from the primes is positive: min eigenvalue >= -1e-10 of the max (Weil positivity; equivalent to RH for the full family).
T4 [null] fake primes (random integers, seed 20261122): fewer than 6 of the 11 zeros matched within 0.01.
C1 [control] the same forms computed from our own zeros (Riemann-Siegel, lower precision) give Ritz values within 0.02 of the prime side.

## Results (t15_operator.log)
Correction: there are 9 published zeros in [50, 77], not 11 (77.14 lies outside); the rule is unchanged.
T1 PASS: all 9 matched; Ritz values 48.0052, 49.7738, 52.9703, 56.4462, 59.3470, 60.8318, 65.1125, 67.0798, 69.5464, 72.0672, 75.7047, 77.1448, 79.3374 agree with the published zeros to the 4 decimals printed (also 43.327 and 82.9148 at the window's edges).
T2 FAIL: 15 directions kept, not 12-14: the window also sees one zero beyond each end (43.33 and 82.91).
T3 PASS: min/max eigenvalue of G = -1.4e-16.
T4 PASS: fake primes match 0 of the zeros (23 directions kept, evenly spread Ritz values: no arithmetic).
C1 PASS: prime side vs our own zeros: 0.0024.
