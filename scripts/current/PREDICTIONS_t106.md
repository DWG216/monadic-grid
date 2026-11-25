# t106 The scalar content above the meeting, its vacuum, and radiative breaking (pre-registered 2026-11-25, before any t106 code is written or run)

Step 1 [M]: which scalar content the grid needs. The meeting's breaking SU(3)_L x SU(3)_R -> SU(2)_L x U(1)_Y (dimension 16 -> 4) must use vevs that leave SU(2)_L unbroken, i.e. in the SU(2)_L-singlet row of a lepton bifundamental (components H_3r). Count the unbroken generators (16 minus the rank of the gauge-boson mass matrix):
 P1a: one bifundamental, vevs anywhere in its row 3 (generic): unbroken dimension 7 (an extra SU(2) survives): not the Standard Model.
 P1b: two bifundamentals, H1_33 = V1, H2_32 = V2 (generic V1, V2): unbroken dimension 4: the Standard Model's SU(2)_L x U(1)_Y.
 [S] So the minimal content is two lepton bifundamentals: two Higgs 27s (n_h = 2), fixed by the breaking, not chosen.
Step 2 [M]: with two bifundamentals (36 real fields), the top coupling y on H1 only (stated assumption), every quartic zero at M* = 2.435e18 GeV, run all quartic invariants down to M3 = 4.98e13 GeV with t105's engine (basis: all independent real quartic invariants built from Tr(X_ij) Tr(X_kl) and Tr(X_ij X_kl), X_ij = H_i^dag H_j; closure residual reported), n_h = 2 in the gauge running.
 P2: the potential at M3 is bounded below: the minimum of V over the unit sphere (20,000 random directions, each refined locally) is positive.
Step 3 [M, testing an I reading]: radiative breaking. For t105's single bifundamental, the Coleman-Weinberg scale mu_CW is where 4 lambda_eff + beta_eff = 0 along the most negative direction (lambda_eff = lambda1 + lambda2 along one column).
 P3: mu_CW lies within a factor 10 of M*.
 Consequence fixed now: if P3 passes, radiative breaking of the lepton bifundamental happens at gravity's meeting, which would break SU(3)_L x SU(3)_R there, contradicting the coupling meeting at M3; the reading then holds only for E6's own breaking direction, not for this field. If P3 fails, the reading is removed.
Matching to the light doublet (the m_h number) needs the light doublet's direction among the two bifundamentals' doublets, which the potential's mass terms (the hierarchy problem) decide; it is not attempted here.

## Scoring (2026-11-25)
Run 1 timed out at the session limit after step 1 (t106_run1_timeout.log). The stability search was then vectorised (same 20,000 random directions and 40 local refinements, with an analytic gradient; the slow version is kept as t106_scalar_content_slow.py). Run 2 (t106_run2.log):
- P1a PASS: one bifundamental with vevs in its SU(2)_L-singlet row leaves 7 generators unbroken (an extra SU(2)).
- P1b PASS: two bifundamentals (H1_33, H2_32) leave exactly 4: SU(2)_L x U(1)_Y. The minimal content is two Higgs 27s, fixed by the breaking.
- Engine: 20 independent real quartic invariants; closure residuals 6e-14 (gauge), 2e-14 (Yukawa).
- P2 FAIL: with all 20 quartics zero at M*, the potential at M3 is unbounded below (minimum on the unit sphere -0.014). Kept.
- P3 PASS: the single bifundamental's Coleman-Weinberg scale is 1.9e18 GeV = 0.78 M*.
Verdict, with the consequence fixed in advance: radiative breaking of the lepton bifundamentals would happen at gravity's meeting, breaking SU(3)_L x SU(3)_R there and contradicting the coupling meeting at M3. So the zero/infinity rule cannot be applied to every scalar quartic of the 27s at M*: with the grid's minimal content it gives no stable vacuum (t105, t106). What survives is the rule for the light Higgs's own quartic (t100, t101: 116-128 GeV). Open: the rule's correct object above the meeting, and the E6-breaking scalars' portals, which enter the vacuum.
