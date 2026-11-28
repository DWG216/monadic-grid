# PREDICTIONS t195: the counts against the 2024 world averages

Registered 2026-11-28, committed before t195_pdg2024.py is written or run.

The tests so far used inputs with errors of 5–17% on the light quarks. The 2024 averages are far tighter (1σ, as rescaled in arXiv:2510.01312): m_c(m_c) = 1.2730(28) GeV, m_b(m_b) = 4.183(4) GeV, m_s(2 GeV) = 93.5(5) MeV, m_d(2 GeV) = 4.70(4) MeV, m_u(2 GeV) = 2.16(4) MeV, M_t (pole) = 172.4(7) GeV. These were read before this file; no Q or mass has been computed from them.

Running: each mass is carried to the reading scale by Huang–Zhou's own ratio (their output at that scale over their input), which depends on the input only weakly. Allowances for the running, fixed now: 1.0% on the predicted charm mass (α_s in the pole-to-MS-bar and charm running), 0.5% on m_b relative to m_s and m_d (the b threshold).
Reading scales: up at μ = v (§339, interpolated as t194); down at M_Z (down does not run, t192–t193).

Disclosure: t194's post hoc pointer gave m_c(m_c) ≈ 1.245(12) from the older inputs; the up and top inputs barely change here, so U1 is expected near that value and roughly 1.5σ below the average. D1 has not been estimated.

U1 [M]: with Q_u = 8/9 at v, m_t(v) and m_u(v) predict m_c(v); carried to m_c(m_c) it lies within 2σ (prediction and allowance combined with the average's error) of 1.2730 GeV.
D1 [M]: Q_d at M_Z from the 2024 inputs lies within 2σ of 3/4.
Consequence fixed now: both pass → the counts survive data a factor of ten tighter. U1 fails → 8/9 at v is excluded as the up count's reading. D1 fails → the down count 3/4 is excluded, and with it the charge count n = 2 for down quarks.
Gate: statement about nature; public.
