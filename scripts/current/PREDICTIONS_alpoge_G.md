# Pre-registered before running alpoge_G.py (2026-11-20). Label: math (numerical consistency check), not a test of the proof.
Quantity from the reconstruction (Allahyar 2026, eq. 1): G(x) = S(x) - x log x + (1 + gamma) x, S(x) = sum_{n<=x} Lambda(n)(x/n - 1).
From its Mellin transform (eq. 3-4): G(x) = log(2 pi) + sum_rho x^rho / (rho(1 - rho)) + O(1/x).
Under RH, |G(x) - log 2pi| <= sqrt(x) * sum_rho 1/|rho|^2 = 0.0461 sqrt(x) (sum over nontrivial zeros, known constant 0.046191...).
G1: for 200 log-spaced x in [1e2, 1e7], |G(x) - log 2pi| / sqrt(x) <= 0.047 at every x.
G2: the maximum of that ratio is above 0.02 (the zeros' term is really there, not just a small constant).
G3: the reconstruction's Arithmetic input 1.1 with A*eps -> 0: G(x) <= x^(1/2) on every sampled x >= 1e3 (much stronger than needed).
N1 (null, Cramer random primes, n prime with probability 1/ln n, seed 20261120): the ratio exceeds 0.047 somewhere in [1e2, 1e7].

# Scored after run (2026-11-20)
G1 PASS: max |G - log 2pi|/sqrt x = 0.0183 (at x = 5,607,170), below the RH bound 0.0461.
G2 FAIL as stated: max 0.0183 < 0.02. The zeros' term is present (G grows from 1.7 at 1e2 to 8.3 at 1e6, beyond log 2pi = 1.84), but the phases never align enough to approach the full bound in this range.
G3 PASS: max G/sqrt x for x >= 1e3 is 0.064; G <= sqrt x everywhere sampled.
N1 PASS but weak: Cramer model ratio 1234.8; its main term is not matched to x log x, so this mostly shows the drift a wrong prime density gives, not a fair fluctuation null.
