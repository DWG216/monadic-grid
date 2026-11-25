# t95 The matter excess, non-thermally: is the grid's CP asymmetry large enough? (pre-registered 2026-11-25, before any t95 code is written or run)

From t90-t92: thermal and resonant leptogenesis fail with the grid's Dirac masses. Non-thermal route: right-handed neutrinos produced by decays of a heavy state at reheating temperature T_R below the lightest N (no washout), each decay giving lepton asymmetry eps_i.
Requirement [M, standard]: n_B/s = eta_B/7.04 = 8.7e-11; n_(B-L)/s = (79/28) n_B/s = 2.45e-10; with at most n_N/s = (3/2) T_R / m_phi (two N per decay of a scalar of mass m_phi, T_R << m_phi), the asymmetry needs |eps_i| >= 2.45e-10 / ((3/2) T_R/m_phi).
Test [M]: with t90's construction (run 4 code), the maximum over the Majorana-phase plane (400 x 400) of |eps_i| = |sum_alpha eps_i,alpha| for i = 1, 2, 3 (ordered by mass).
S1 Sanity: t90's maximum eta (8.2e-15) is reproduced by the same code on the t90 seed (identity of the imported function).
P1 [M] At least one N_i has max |eps_i| >= 1e-6 (so that T_R/m_phi >= 1.6e-4 suffices, a mild requirement).
P2 [M] Washout-free window: T_R below the lightest N mass (about 1e5 GeV) leaves a range of m_phi that satisfies P1's requirement with m_phi > 2 M_i (kinematics) for the N_i that reaches it.
Verdict: P1-P2 pass -> the matter excess can be non-thermal with the grid's own CP phases; what produces the heavy state (inflaton or the psi-breaking field) is the next step.
