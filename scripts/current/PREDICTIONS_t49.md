# t49 full-coupling check of the t48 coil prediction (pre-registered 2026-11-23, before run)
Model: p.204 winding, one circuit (12 passes per wire, the 18 repeats not modelled). Torus R=40 mm, tube a=15 mm,
36 slots; each pass wraps once round the tube while advancing 15 slots; grey on radius a, brown on a+0.6 mm; wire radius 0.2 mm.
PEEC: partial inductance matrix of all 24 passes (Neumann), potential coefficients of 26 node cells (1/r), C = P^-1, lossless.
Drive: Va = 1 at grey node 0, Vb = i (quadrature) at grey node 12-s; brown wire floating. r1 = P(1)/P(0), r2 = P(2)/P(0).
S1 sanity: L and C matrices symmetric (rel 1e-12); L positive definite; C positive definite.
S2 sanity: lossless, so P_A + P_B = 0 (|sum| < 1e-9 |P_A|) at every scanned frequency.
Q1 (the t48 prediction): there is a frequency with |r1 + 2| < 0.1 and |r2 - 4| < 0.4.
Q2 (uniform chain): at that frequency |r2 - r1^2| < 0.2 |r1|^2.
Q3 (t48 placement): that frequency is within 1.06 +- 0.10 of the coil's first self-resonance f_sr (grey wire, far end open, first zero of Im Z_in), used as f_c.
Unsettling: Q1 fails = the nearest-neighbour bridge does not hold for this coil.
Control (reported, no threshold): plain toroid, each pass advancing 3 slots (12 passes = one turn), same test.
