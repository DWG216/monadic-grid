# t102 Refining the Higgs mass: the gauge term above the meeting from the trinification structure (pre-registered 2026-11-25, before any t102 code is written or run)

Why: t101 ran the Higgs quartic above the meeting with the Standard Model's gauge term (coefficient c = 1.71 g^4 with the unification relation). A labelled sensitivity check after t101 (t101_sensitivity.log) showed m_h moves by several GeV as c changes (1.71 -> 126.7, 2.5 -> 125.1, 3.0 -> 124.1, 4.33 -> 121.2 GeV). So c must be computed, not assumed. Above the meeting the light doublet sits in the lepton bifundamental Phi ~ (3, 3bar) of SU(3)_L x SU(3)_R with one coupling g; c is fixed by that structure with no free parameter.
Method [M]: one-loop gauge contribution to the quartic along the vev direction, beta_lambda,gauge = (3/2) sum_V m_V^4 / |phi|^4 (per 16 pi^2), with the vector masses from |D Phi|^2 for Phi = phi e1 e1^T (the neutral component), D Phi = d Phi - i g T_L Phi + i g Phi T_R.
S1 Sanity: the same code for the Standard Model doublet under SU(2) x U(1) gives 3/8 (2 g^4 + (g^2 + g'^2)^2) exactly, and with g'^2 = (3/5) g^2 gives c = 1.71.
P1 [M] c for the bifundamental is computed and reported (no threshold: it is a number).
P2 [M on data] Meeting (B) of t101 (two doublet pairs at 1 TeV), with this c above the meeting (n_h = 0..3), gives m_h within 1.0 GeV of 125.20 for every n_h.
Verdict: P2 pass -> the Higgs mass follows from lambda(M*) = 0 and the grid's content to within 1 GeV with no parameter adjusted. P2 fail -> report the value and the remaining gap (Yukawa structure above the meeting is next).

## Scoring (2026-11-25)
Run 1 (t102_run1.log).
- S1 PASS: the code reproduces 3/8 (2 g^4 + (g^2 + g'^2)^2) exactly and c = 1.71 in the unified normalisation.
- P1: for the light doublet in (3, 3bar) of SU(3)_L x SU(3)_R with one coupling, c = 17/3 = 5.67 (the left and right bosons both couple to the neutral component, and their cross term adds).
- P2 FAIL: with c = 5.67 above the meeting, m_h = 116.2-118.1 GeV over n_h = 0..3, 7-9 GeV low. Kept.
Verdict: t101's agreement within 1.5 GeV used the Standard Model form of the gauge term above the meeting; the bifundamental's own gauge term overshoots in the other direction. The Higgs mass is sensitive at the several-GeV level to how the light doublet sits in the scalar sector above the meeting: the full multiplet has two quartic invariants and tree-level matching at M3 that this direction-based running leaves out. Correction: t101's selection of the TeV meeting is downgraded from a result to an indication; the real refinement is the full trinification scalar running (two quartic invariants, the top Yukawa in 27^3 form) with tree-level matching at M3, all quartics zero at M*.
