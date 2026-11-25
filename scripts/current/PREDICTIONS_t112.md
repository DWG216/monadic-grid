# t112 The light doublet's direction and b/τ (pre-registered 2026-11-25, before any t112 code is written or run)
Setting. One fermion 27 = (L, Q_L, Q_R) per generation, third generation only. The E6 cubic norm in the trinification basis (Freudenthal/Albert form) N = det L + det Q_L + det Q_R − tr(Q_L L Q_R). With Higgs 27s H1, H2 and couplings Y1, Y2, every fermion mass depends on one 3×3 matrix W = Y1⟨H1⟩ + Y2⟨H2⟩ in the L slot: quark masses from the tr term (the block W itself), lepton masses from det (ε_ijk ε^abc W^k_c). Heavy entries (t106 breaking): W_33 = Y1 v1, W_32 = Y2 v2, ratio t = Y2 v2/(Y1 v1). Light entries: the neutral components of the doublets; the two down-type (Y = −1/2) columns carry κ2 and κ3, direction x = κ3/κ2. Charges are computed from the unbroken generators, not assumed. Masses: lightest singular values of the charge −1/3 and charge −1 blocks of the 27×27 Hessian.
[S] Grid rule R1 (hand swap): the light doublets live in the block the hand swap maps to itself, rows and columns 1–2 (the bidoublet). Column 3 is the hand-swap image of the SU(2)_L-singlet row, so x = 0.
[S] Grid rule R2 (balanced pair) for comparison: x = 1.
Target: y_b/y_τ at M* = 0.597 (t109, meeting B), with a ±10% band for the approximations in t109's running: 0.537–0.657.
S1 [sanity] t = 0, x = 0: m_b/m_τ = 1 (the single-coupling E6 relation).
S2 [sanity] heavy masses: the charge −1/3 block has one singular value of order Y1·sqrt(v1² + ...) (the exotic D) and one light; the charge −1 block has its light value separated from the heavy ones by > 1e6 at κ/v = 1e-10.
P1 [M] R1 at t = 1 gives m_b/m_τ in 0.537–0.657.
P2 [M] R1's ratio is independent of t over t ∈ [0.1, 10] to 1%, or, if not, there is a t in [0.1, 10] where it hits 0.597; report t*.
P3 [M] R2 at t = 1 gives m_b/m_τ in 0.537–0.657.
Information: m_b/m_τ over the (x, t) plane, and the contours where it equals 0.597.

## Scoring (2026-11-25), run 1 (t112_run1.log)
Charges computed from the unbroken generators: the neutral down-type doublet entries are L[1,2] and L[1,3] (1-based), the up-type L[2,1], as assumed.
- S1 PASS: t = 0, x = 0 gives m_b/m_τ = 1. S2 PASS: heavy and light singular values separated by 2e10.
- P1 FAIL: R1 (x = 0) at t = 1 gives m_b/m_τ = 1.0000, not 0.537–0.657.
- P2 PASS: R1's ratio is 1 to 2e-5 for all t in [0.1, 10].
- P3 FAIL: R2 (x = 1) at t = 1 sits on the degenerate line x = t, where the light lepton direction is the heavy one and m_τ → 0 (ratio 3.8e5).
- Information: m_b/m_τ = 1 over the whole (x, t) grid except the line x = t. With an up-type vev 50 κ, still 1.
Verdict: the E6 cubic norm gives m_b = m_τ for every direction of the light doublet and every heavy vev ratio. The doublet's direction cannot carry b/τ: the earlier statement (§223–227) that b/τ, the Veltman balance and the vacuum phase reduce to the doublet direction is corrected for b/τ. The R1 direction (the hand-swap bidoublet) stands as the grid's direction; it fixes nothing in b/τ.
Found during this test, labelled post hoc for t109 (t109_posthoc.py): above M3 the trinification gauge terms of the quark and lepton couplings are equal, so the ratio does not run from gauge terms there. Corrected: y_b/y_τ = 0.69 at M3 and 0.68 at M* (both meetings). The gap to 1 is a factor 1.47, which must come from structure beyond one 27³ coupling (a second Yukawa structure such as the 351', vector-like mixing, or thresholds at the meeting).
