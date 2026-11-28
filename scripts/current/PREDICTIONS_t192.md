# PREDICTIONS t192: the counts hold at every scale

Registered 2026-11-28, committed before t192_scales.py is written or run.

If n is structure (§331–§335: leptons' hands share a multiplet, n = 1; quarks' n = 1 + open thirds of the right hand), it carries no scale: the meeting shares 2/3, 3/4, 8/9 should hold wherever the masses are read, not only at M_Z.

Data: Huang and Zhou, arXiv:2009.04851, Table 2 (quarks) and Table 3 (charged leptons), full SM rows at M_Z, M_h, M_t, 10⁵, 10⁸, 10¹² GeV, as printed. Read before this file; no Q computed from rows other than M_Z (t189). Method as t189 (10⁵ Monte Carlo draws, Gaussian errors).
Disclosure: QCD running is the same for every flavour at leading order, so the quark Q's drift only through Yukawa and electroweak running; the test is of that drift. Koide's 2/3 is known to hold for pole lepton masses; how far running masses move it was not looked up.

P1 [M]: Q_d within 2σ of 3/4 at all six scales.
P2 [M]: Q_u within 2σ of 8/9 at all six scales.
P3 [M]: charged-lepton Q within 0.003 of 2/3 at all six scales (threshold fixed now: flavour-dependent running enters at about α/π ≈ 0.0023).
Consequence fixed now: all pass → the counts are scale-free, as structure requires. A drift outside the bounds → the count holds at one scale only, and that scale (the cut, or where masses are set) has to be named and derived.
Gate: statement about nature; public.

## Scoring (2026-11-28), run 1 (t192_run1.log)
- P1 PASS: Q_d stays within 2σ of 3/4 from M_Z to 10¹² GeV (0.7483 to 0.7388; worst z = −1.63), drifting down.
- P2 FAIL: Q_u drifts up through 8/9: 0.8876 at M_Z (−0.9σ), 0.8899 at 10⁵ GeV (+0.7σ), 0.8926 at 10¹² GeV (+2.34σ).
- P3 PASS: charged leptons sit at 2/3 + 0.0012 at every scale, steady to 3e-5.
Verdict as fixed in advance: the counts hold over the low scales, but Q_u is not scale-free at the 2σ level; the up count holds at one band of scales and that scale must be named and derived. Post hoc, labelled: Q_u crosses 8/9 between M_t and 10⁵ GeV, and Q_d's drift is in the opposite direction, so both cannot be exact at one high scale; the leptons' running shift (+0.0012) is flavour-dependent QED/electroweak running, steady across scales.
