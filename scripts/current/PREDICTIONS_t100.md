# t100 The Higgs mass from gravity's meeting (pre-registered 2026-11-25, before any t100 code is written or run)

Bridge under test [S]: the zero/infinity rule: a coupling with no structure fixing it is 0. The Higgs quartic lambda has no structure at the grid's top scale, gravity's meeting M* = 2.435e18 GeV (t85), so lambda(M*) = 0. Running down predicts m_h.
Scope of this run: Standard Model running only (two-loop gauge, top Yukawa, quartic). The grid's extra states below M* (light lepton-like doublets 1e3-1e9 GeV, triplets 6e11-7e13 GeV, E6 fields above M3 = 4.5e13 GeV) are left out; they are the next correction.
Inputs at mu = M_t (Buttazzo et al. 2013, matched): g' = 0.35830, g2 = 0.64779, g3 = 1.1666, y_t = 0.93690 + 0.00556 (M_t - 173.34), lambda(M_t) = 0.12604 + 0.00206 (m_h - 125.15) - 0.00004 (M_t - 173.34). M_t = 172.57 +- 0.29 GeV (PDG 2024), measured m_h = 125.20 +- 0.11 GeV.
S1 Sanity: with the measured m_h and M_t = 173.34 the code gives lambda(M_Pl = 1.22e19) between -0.020 and -0.008 (Buttazzo et al.: about -0.014) and lambda crossing zero between 1e9 and 1e12 GeV.
P1 [M on data] lambda(M*) = 0 with M_t = 172.57 predicts m_h within 2 GeV of 125.20 (2 GeV covers M_t, alpha_s and the matching's theory error). Expected by the writer: fail (near 129 GeV), as known for the SM.
Information: the predicted m_h at M_t = 172.57 +- 0.29 (two-sigma band), and the M_t for which lambda(M*) = 0 gives 125.20.
Verdict: P1 pass -> the Higgs mass follows from the zero/infinity rule at gravity's meeting with SM running. P1 fail -> the grid's own states between the electroweak scale and M* must be included (they enter beta_lambda); that is the next test, not a refutation of the rule.
