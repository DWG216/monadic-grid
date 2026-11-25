# t92 The matter excess: does the grid supply a near-degenerate right-handed pair? (pre-registered 2026-11-25, before any t92 code is written or run)

From t90: with m_D = charged-lepton masses, hierarchical thermal leptogenesis fails (max eta_B 8e-15). The two remaining routes are resonance (a near-degenerate pair, |M_j/M_i - 1| small enough that the self-energy is enhanced) and non-thermal production.
Bridge under test [S]: a near-degeneracy needs a reason; if no point of the grid's parameter space (Majorana phases, the only freedom left) brings two right-handed masses within 10%, resonance is closed and the excess must be non-thermal.
Computation (t90's construction, same mixing, m1 = 0.365 meV): scan alpha21, alpha31 on a 400 x 400 grid; record the minimum over the plane of min_i (M_(i+1)/M_i - 1).
S1 Sanity: t90's median masses are reproduced at a scan point (order 1e5, 1e8-1e9, 1e12 GeV).
P1 [M] The minimum ratio over the whole plane exceeds 10 (no pair within an order of magnitude): resonance is closed.
Information: the minimum ratio and where it occurs.
Verdict: P1 pass -> the grid offers no reason for a degenerate pair; the matter excess must come from a non-thermal route (next: inflaton or E6-breaking decays).
