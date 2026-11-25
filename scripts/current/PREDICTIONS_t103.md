# t103 Deriving 2/9: two candidate rules, tested across sectors (pre-registered 2026-11-25, before any t103 code is written or run)

t98 found the charged-lepton chord phase on 2/9 to 0.9 sigma, read as "two hands over nine points". A derivation must say why a phase in radians takes this value and what it does in other sectors. Two candidate rules that use only the grid's quantities, each with a consequence elsewhere:
Rule R1 (self-consistent record) [I]: the chord's phase per step equals its balance divided by the three steps: delta = Q/3. For leptons Q = 2/3 gives 2/9.
Rule R2 (the grain's tower) [I]: the phase is 2/9 at the colourless level and is divided by the colour dimension per level of the bifundamental (down-type quarks: 2/9 / 2 = 1/9; up-type: 1/18), the halving pattern seen post hoc in t98.
Data: chord fits of t98 (up: Q = 0.889, delta = 0.050 +- 0.002; down: Q = 0.741, delta = 0.102 +- 0.015; neutrinos: Q = 0.524, delta = 0.365, no error given).
P1 [M on data] R1: |delta - Q/3| within 3 sigma for up and down quarks.
P2 [M on data] R2: |delta_d - 1/9| and |delta_u - 1/18| each within 3 sigma.
Note: R2 was suggested by t98's post hoc; its test here is the same data, so a pass is weak; a fail removes it.
Verdict: if both fail, 2/9 remains a lepton-sector reading without a derivation, and the next attempt must come from a dynamical principle (the chord as the eigenvalues of a circulant mass matrix with the grain's phase), not from numerology.

## Scoring (2026-11-25)
Run 1 (t103_run1.log).
- P1 FAIL: delta = Q/3 misses badly for quarks (up: 0.050 vs 0.296, -107 sigma; down: 0.102 vs 0.247, -9.5 sigma). R1 is removed: 2/9 = Q/3 for leptons is not a rule.
- P2 PASS (weak, as stated): the halving pattern sits within 3 sigma (down -0.6, up -2.2). Same data that suggested it; not evidence on its own.
Verdict: no derivation of 2/9 yet. R2 survives as a pattern to test with better light-quark masses (FLAG lattice averages). The derivation must come from a dynamical principle: the chord as the eigenvalues of a circulant mass matrix built from the grain, with its phase fixed by the counting phase's action.
