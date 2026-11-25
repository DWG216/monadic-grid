# t107 Strong CP from the hand swap (pre-registered 2026-11-25, before any t107 code is written or run)
[S] The hand swap (Frobenius φ→1−φ, the S4 element outside 2T) exchanges the hands: SU(3)_L ↔ SU(3)_R. Under it θ_QCD → −θ_QCD and the quark Yukawas go to their adjoints, so at the meeting θ_QCD = 0 and M_u = M_u†, M_d = M_d†. Hermitian matrices have real determinants, so θ̄ = θ + arg det(M_u M_d) = 0 at tree level, while the CKM phase survives (it lives in the off-diagonals). Condition: the vacuum carries no relative vev phase (open, tied to the scalar vacuum, t106).
P1 [M, algebra on data] With M_u = diag(m_u, m_c, m_t), M_d = V diag(m_d, m_s, m_b) V† (V = PDG 2024 CKM with δ = 1.144): |arg det(M_u M_d)| < 1e-12 and the Jarlskog invariant J = Im(V_us V_cb V_ub* V_cs*) matches 3.08e-5 within 5%. Sanity, holds by construction.
P2 [M] 1000 random Hermitian pairs (log-uniform eigenvalues): |θ̄| < 1e-12 in all, and |J| > 1e-8 in at least 99%: CP violation in mixing survives θ̄ = 0 generically.
P3 [M] One-loop SM matrix RGE of (Y_u, Y_d) from M3 = 4.98e13 GeV down to M_Z, starting Hermitian (P1's matrices scaled to the meeting): |θ̄(M_Z)| < 1e-10 (the nEDM bound). Expected pass: d ln det Y/dt is a real trace at one loop.
P4 [future data] θ̄ contributes nothing to the neutron EDM: n2EDM and successors see |d_n| consistent with zero down to 1e-28 e·cm from θ; there is no QCD axion (ADMX, MADMAX, IAXO find none in the QCD band).

## Scoring (2026-11-25), run 1 (t107_run1.log)
- P1 PASS: θ̄ = −6e-16, J = 3.11e-5 (1% from 3.08e-5).
- P2 FAIL as registered: worst |θ̄| = 4.5e-8 > 1e-12 in double precision; |J| > 1e-8 in 100%. Post hoc (t107_posthoc.py, labelled): the worst pairs have condition number up to 1.6e9 and Hermiticity error 4e-15, so the determinant's phase carries rounding of that size; computed from the real eigenvalues, θ̄ = 0 exactly in all 1000 pairs. The fail is the threshold's, kept.
- P3 PASS: running from M3 to M_Z leaves θ̄ = 2e-16 though Y_d is no longer Hermitian (0.5%); J at M_Z 2.4e-5 (the toy starting sizes are not refit).
- P4 registered for future data: no θ-induced neutron EDM, no QCD axion.
Verdict: the hand swap fixes θ̄ = 0 at the meeting and the SM running keeps it; CP violation lives in the mixing. Condition still open: no relative phase in the scalar vacuum.
