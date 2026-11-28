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

## Scoring (2026-11-28), run 1 (t190_run1.log)
Correction to the text above: the halving pattern was registered in §216 (t103), not §218.
- Amplitudes (t189's law, reported): c_d = 1.578(13) against √(5/2) = 1.581; c_u = 1.8236(23) against √(10/3) = 1.8257.
- P1 PASS: δ_d = 0.0999 ± 0.0060 against 1/9 (z = −1.87).
- P2 FAIL: δ_u = 0.0518 ± 0.0008 against 1/18 = 0.0556 (z = −4.6). The tighter data sharpen t99's −2.2σ into a clear miss.
- P3 FAIL: from n and the heaviest mass, m_s 57.6 MeV (z = +1.0) and m_c 657 MeV (z = +2.1) come close, m_d 1.68 MeV misses (z = −5.2); m_u (unscored) 0.012 MeV against 1.23.
Verdict as fixed in advance: the phase does not halve by sector. The amplitude law c² = n + 1/n stands from t189; the phase is a second number per sector, still open. The light masses are set by the phase, so they stay open with it.
