# PREDICTIONS t178: the t27 tension: is the field's area coefficient a fact or a choice?

Registered 2026-11-27, committed before t178_regulator.py is written or run.

Tension (§306, §314). The meeting count gives η = (√3/10) ln 3 per cell area (cell 0.87 l_P). t27's field entanglement gave 0.295 R² per degree of freedom on Srednicki's radial lattice, × 118 degrees of freedom, which would put the lattice spacing at 3.3 l_P. §316 removed the ×118 (the record's entropy does not depend on the number of fields). What remains: does the per-field area coefficient itself carry a reason, or is it set by the lattice chosen?

Reasoning [S]. A number that changes when an arbitrary choice changes has no sufficient reason to be the record's η. Known in the continuum: the area coefficient of entanglement entropy depends on the cutoff, while the log coefficient (−1/90 for a scalar) is universal.

Method. Srednicki's radial chain as in t153 (same code path, exact diagonalisation to L1 = 3000 plus the perturbative tail), with two discretisations of r²(∂φ)² that agree in the continuum: A, the t27/t153 weights (j + ½)²; B, weights j(j + 1). Sizes n = 10, 12, 14, 16, 20, 24, 28, 32, N = 6n. Fit S = s R² + c ln R + c₀ + d/R², R = n + ½.

P1 [M]: the area coefficients differ: |s_B/s_A − 1| > 5%.
P2 [M]: the log coefficients agree with each other within 15% and each lies within 15% of −1/90.
Consequence fixed now: if P1–P2 pass, the field route's area coefficient is a property of the regulator, not of the record; t27's 0.295 has no sufficient reason to fix η, and the tension is resolved in favour of the meeting count (with §316). If P1 fails, the tension stands.
Gate: physics; public.

## Scoring (2026-11-27), run 1 (t178_run1_A.log, t178_run1_B.log)
- P1 FAIL: s_A = 0.2954314 and s_B = 0.2954314 (identical to 1e-7): the two weightings differ only by ¼ per bond, which vanishes relative to j² where the area term is set; the radial spacing is the only cutoff in this chain, and both keep it. The variation registered was too weak to change the regulator.
- P2 PASS: log coefficients −0.010818 (A) and −0.010930 (B), within 1% of each other and within 2.6% and 1.6% of −1/90.
Verdict as fixed in advance: P1 fails, so the tension stands as stated in §306: t27's 0.295 per degree of freedom is not shown to be a regulator artefact by this test. Reported: the area coefficient here is set by the radial spacing alone; a real change of regulator (a longer-range derivative, a different angular cutoff) is needed to test non-universality, and that has to be registered separately.
