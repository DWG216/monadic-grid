# Pre-registration: resonance as phase-locking (2026-11-21)
Tiers: [built] built into the model, [real] numerical test.
R1 [real] Sine circle map th -> th + W - (K/2pi) sin(2 pi th). Fraction of W in [0,1) that is mode-locked (rotation number rational with q <= 60 and plateau): K = 1 (critical) > 0.90; K = 0.5 between 0.1 and 0.6; K = 0.1 < 0.1.
R2 [real] At K = 1 plateau width ordering: w(0/1) > w(1/2) > w(1/3) > w(2/5) > w(3/8); golden W* (rotation number 1/phi^2 ... the golden irrational 0.381966) is not locked at any K < 1, and its plateau-free point sits between the Fibonacci-ratio tongues 3/8 < 0.38197 < 2/5.
R3 [real] Kuramoto, N oscillators, Lorentzian frequencies width g = 0.5 (Kc = 1). Order parameter r at K = 1.0: decreases with N (finite-size rounding); r at K = 2.0 near the infinite-N value sqrt(1 - Kc/K) = 0.707 (within 0.1 for N = 2000); r below Kc (K = 0.5) scales roughly as 1/sqrt(N). Transition sharp only as N -> infinity.
R4 [built] Bosonic pull: a test oscillator of detuning D locks iff |D| <= K r; so lock probability rises with r.
Null R3: coupling with random signs (frustrated): r stays ~ 1/sqrt(N) at K = 2.
