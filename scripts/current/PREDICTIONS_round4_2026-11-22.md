# Pre-registration (2026-11-22, 02:55), under the new rules
## A. Do the zeros' Mobius weights carry the primes? (basis-free spectral sum)
Quantity: S(u) = sum over our 201 zeros of 2 Re[ taper * w_n * e^(i gamma_n u) ], taper 1 - gamma/400; detector: jump J(n) = S(ln n + 0.012) - S(ln n - 0.012) for n = 2..30.
Explicit formula: with w = 1/rho, S(u) ~ e^(-u/2)(e^u - psi(e^u)) (jumps -ln p / sqrt n at prime powers); with w = 1/(rho zeta'(rho)), S(u) ~ e^(-u/2)(M(e^u) + 2) (jumps mu(n)/sqrt n at squarefree n).
SANITY RUN (done before this file was frozen; t8_sanity.py): control w = 1/rho gives negative jumps at 100% of prime powers <= 30 (ratio 4.55 to other n); a weight-permutation null does NOT break it (0.94, 3.34) because 1/rho is smooth, so the control's null is shuffled spacings, which does break it (0.38, 0.86).
M1 [control, already seen in the sanity run] w = 1/rho: all prime-power jumps negative, ratio > 3.
M2 [real] w = 1/(rho zeta'(rho)): sign(J(n)) = mu(n) for >= 15 of the 18 squarefree n in 2..30, and median |J| at squarefree n / at the 11 non-squarefree n > 2.
M3 [real] null A, weights permuted among the zeros (200 draws, seed 20261122): the M2 sign count exceeds the null's 95th percentile.
M4 [real] null B, zero spacings shuffled with weights kept by index (200 draws, seed 20261123): the M2 sign count exceeds the null's 95th percentile.
M5 [exploratory] over squarefree n, corr(|J(n)|, 1/sqrt n) > 0.5.
## B. Making a world vs joining one (from §59 and §61)
60 pulse oscillators (b = 3), rates 1 + 0.005 normal, eps = 0.003 (the §59 post-hoc coupling).
F (formation, from random phases, 20 seeds): gated kicks form a world (all within 0.01) in >= 18/20 within 300 cycles; random-phase kicks in <= 2/20.
J (joining): a world of 59 formed with gated kicks; one newcomer enters at a random phase (40 trials); its own kicks are either gated or at random phases. Median cycles to lock (within 0.02 of the world's mean phase for 3 cycles): the two newcomer types within 20% of each other.
SANITY RUN for B before freezing: done below in t9 (formation reproduces §59 at N = 60; a newcomer does lock in both modes).
AMENDMENT after the B sanity run (before the full run): every joining time came out at 3.00 cycles, the metric's floor. The lock metric is changed to: the time at which the newcomer comes within 0.02 of the world's mean phase and stays there for 3 cycles, sampled every 0.05 cycle. Prediction J unchanged (the two newcomer types within 20%).

## Results
M1 pass (control, as in the sanity run). M2 PASS: 18/18 squarefree signs correct; |J| ratio squarefree / non-squarefree = 77.0; J(n) sqrt(n) = 0.83-0.93 times mu(n) for every n <= 30, non-squarefree |J sqrt n| <= 0.04. M3 pass (null 95th 16, real 18). M4 pass (null 95th 15, real 18). M5 pass: corr 0.999.
Note: the sign-count nulls are high (95th 15-16 of 18), so the decisive evidence is the magnitude pattern. Post hoc (labelled): under null A the ratio's 95th percentile is 2.80 (real 77.0) and the correlation's is 0.424 (real 0.999).
F PASS: gated 20/20 formed (median 8.0 cycles), random-phase 0/20 in 300 cycles. J PASS: newcomer with gated kicks and with random-phase kicks both lock in 40/40, median 1.00 cycle each (absorbed at the world's first firing).
