# PREDICTIONS t190: one integer per sector, both numbers of the chord

Registered 2026-11-28, committed before t190_sector_index.py is written or run.

Each sector's generation chord has two numbers: amplitude c and phase δ, with √m_k = A(1 + c cos(δ + 2πk/3)). t189 found c² = n + 1/n (n = 1, 2, 3 for leptons, down, up). The record (§209, §218) already flagged a phase pattern by sector, δ = 2/9, 1/9, 1/18, i.e. δ_n = (2/9)·2^(1−n), found post hoc on the t99 data (down −0.6σ, up −2.2σ). If one integer n fixes both numbers, each quark sector's two mass ratios follow from n alone.

Disclosure: both patterns were found on older data. The Huang–Zhou masses (arXiv:2009.04851, Table 2, full SM, μ = M_Z) were used for Q in t189; their phases have not been computed. Data, method and Monte Carlo as in t189 (10⁵ draws, Gaussian errors, phase convention and fold as in t98's chord()).

Search for a ground reason for n, reported before testing: none found. Colour, electric charge, hypercharge, isospin and the E6 and trinification state counts were each tried as a count giving 1, 2, 3; none does without an added rule. One reading [I], not tested here: c²/2 = (n + 1/n)/2 = cosh(ln n), the oscillating-to-constant power ratio of the chord, equal (n = 1) when the two hands balance and the hands' arithmetic mean at rapidity ln n otherwise.

P1 [M]: δ_d lies within 2σ of 1/9.
P2 [M]: δ_u lies within 2σ of 1/18.
P3 [M]: with c² = n + 1/n and δ_n = (2/9)·2^(1−n), the heaviest mass alone predicts the other two in each quark sector; m_s, m_d, m_c each within 2σ of the data (m_u is reported, not scored: its value is the small remainder of a near-cancellation).
Consequence fixed now: P1–P3 pass → one integer per sector fixes the chord; the quark mass ratios reduce to n and the open problem is n alone. Any fail → the phase law is not the halving, and the chord needs a second number per sector.
Gate: statement about nature; public.
