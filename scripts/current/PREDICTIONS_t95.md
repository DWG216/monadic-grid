# t95 The matter excess, non-thermally: is the grid's CP asymmetry large enough? (pre-registered 2026-11-25, before any t95 code is written or run)

From t90-t92: thermal and resonant leptogenesis fail with the grid's Dirac masses. Non-thermal route: right-handed neutrinos produced by decays of a heavy state at reheating temperature T_R below the lightest N (no washout), each decay giving lepton asymmetry eps_i.
Requirement [M, standard]: n_B/s = eta_B/7.04 = 8.7e-11; n_(B-L)/s = (79/28) n_B/s = 2.45e-10; with at most n_N/s = (3/2) T_R / m_phi (two N per decay of a scalar of mass m_phi, T_R << m_phi), the asymmetry needs |eps_i| >= 2.45e-10 / ((3/2) T_R/m_phi).
Test [M]: with t90's construction (run 4 code), the maximum over the Majorana-phase plane (400 x 400) of |eps_i| = |sum_alpha eps_i,alpha| for i = 1, 2, 3 (ordered by mass).
S1 Sanity: t90's maximum eta (8.2e-15) is reproduced by the same code on the t90 seed (identity of the imported function).
P1 [M] At least one N_i has max |eps_i| >= 1e-6 (so that T_R/m_phi >= 1.6e-4 suffices, a mild requirement).
P2 [M] Washout-free window: T_R below the lightest N mass (about 1e5 GeV) leaves a range of m_phi that satisfies P1's requirement with m_phi > 2 M_i (kinematics) for the N_i that reaches it.
Verdict: P1-P2 pass -> the matter excess can be non-thermal with the grid's own CP phases; what produces the heavy state (inflaton or the psi-breaking field) is the next step.

## Scoring (2026-11-25)
Run 1 (t95_run1.log). S1 PASS (t90's maximum reproduced).
- P1 FAIL: the largest CP asymmetry anywhere on the Majorana-phase plane is 3.2e-10 (N2, M = 4.0e8 GeV); N1 reaches 1.0e-11 and N3 1.5e-11. N2 would need T_R/m_phi >= 0.52, which is not a non-thermal regime (T_R << m_phi is the premise).
- P2 FAIL (no N_i qualifies).
Verdict as registered: with m_D = charged-lepton masses, no decay of right-handed neutrinos, thermal, resonant or non-thermal, makes the matter excess: the CP asymmetries are small because the Dirac masses are small (m_tau / v ~ 1e-2). Correction map: either the Dirac bridge m_D = m_l (t89) or the source of the excess must change. Recorded for the next step: the excess from the 27's exotics or the E6/psi sector, or a Dirac bridge with a top-sized entry.
