# t105 The Higgs mass from the full scalar sector above the meeting (pre-registered 2026-11-25, before any t105 code is written or run)

Rule [S] (t100): every quartic coupling is zero at gravity's meeting M* = 2.435e18 GeV; no parameter is adjusted.
Above the meeting (M3 = 4.98e13 GeV, meeting B of t101): gauge SU(3)_C x SU(3)_L x SU(3)_R with one coupling g, b = -5 + n_h (t71), n_h = 0..3 reported. Scalar: the lepton bifundamental H ~ (1, 3, 3bar) (18 real fields), potential lambda1 [Tr H^dag H]^2 + lambda2 Tr(H^dag H H^dag H). Fermions with a Yukawa: the third generation's quark bifundamentals Q ~ (3, 3bar, 1) and Q^c ~ (3bar, 1, 3); the 27^3 coupling y Q Q^c H (unique invariant). Other fermions enter only through b.
Engine [M]: one-loop beta functions from the general formula (Machacek-Vaughn) evaluated numerically on explicit component tensors (real scalar basis, Weyl fermions), projected onto (lambda1, lambda2) and y.
Matching at M3 [I, stated]: one bifundamental carries both the breaking vev (component H_33) and the light doublet (components H_i1, i = 1, 2); then the light doublet's quartic at tree level is lambda_SM = (lambda1 + lambda2) - lambda1^2 / (lambda1 + lambda2) (heavy radial mode integrated out; lambda2 does not mix the two columns), and y_t = y. If lambda1 + lambda2 <= 0 at M3 the vacuum is unstable and the case fails.
Below M3: t101's Standard Model two-loop running with meeting B's exotics; m_h from the matched lambda(M_t) by inverting Buttazzo et al.'s matching (as t100).
Procedure: g and y run up from M3 (values from the low-energy running at M3) to M*; lambda1, lambda2 run down from zero at M* to M3; match; run the SM down.

S1 Sanity [M]: the same engine applied to the Standard Model (Higgs doublet, SU(2) x U(1), top Yukawa with Q and t^c, colour) reproduces the one-loop beta functions of lambda (24 lambda^2 - 6 y^4 + 12 lambda y^2 - 3 lambda (g'^2 + 3 g^2) + 3/8 (2 g^4 + (g^2 + g'^2)^2)) and y_t (y (9/2 y^2 - 8 g3^2 - 9/4 g^2 - 17/12 g'^2)) to 1e-9 at random coupling values.
S2 Sanity [M]: the engine's gauge term for the bifundamental along the single-component direction reproduces t102's c = 17/3 when projected (the direction-based number is a special case of the full tensor).
P1 [M on data] m_h within 1.0 GeV of 125.20 for every n_h = 0..3.
Information: lambda1, lambda2 at M3; lambda_SM(M3); m_h for each n_h.
Verdict: P1 pass -> the Higgs mass follows from the grid with no free parameter, to 1 GeV. Fail -> report the number; the matching assumption (one bifundamental carrying both vev and doublet) is the first bridge to revisit.

## Scoring (2026-11-25)
Run 1 (t105_run1.log, script t105_scalar_sector_run1.py): S1 FAILED (max relative error 21): a bug in the pairing helper (the third index pairing was permuted wrongly), which also corrupted the quartic basis; run 1 is invalid and kept. Run 2 fixes that one line; thresholds unchanged.
Run 2 (t105_run2.log):
- S1 PASS: the engine reproduces the Standard Model's one-loop beta functions for lambda and y_t to 4e-14.
- S2 PASS: the engine's gauge term along one component is t102's 17/3. Closure: beta stays in the span of the two invariants (residual 8e-16).
- Engine output (per 16 pi^2): beta1 = 52 l1^2 + 48 l1 l2 + 12 l2^2 + 31/6 g^4 - 32 g^2 l1 + 12 y^2 l1; beta2 = 24 l2^2 + 24 l1 l2 + g^4/2 - 6 y^4 - 32 g^2 l2 + 12 y^2 l2; beta_y = y (6 y^2 - 16 g^2).
- P1 FAIL: from zero at M*, the gauge term drives lambda1 negative going down: at M3, lambda1 = -0.043 to -0.050, lambda2 = +0.009; lambda1 + lambda2 < 0, so the potential is unbounded along a single column and the registered matching has no stable vacuum. No m_h.
Post hoc (t105_posthoc.log, labelled): lambda1 + lambda2 turns negative immediately below M*.
Verdict as registered: with one bifundamental carrying both the breaking vev and the light doublet, the zero-at-M* rule gives no stable vacuum at the meeting. The first bridge to revisit is that matching (registered as such): the grid's other scalars (the 27's quark-bifundamental scalars, the psi-breaking field, a second bifundamental) enter beta1 and the vacuum. [I] A quartic that turns negative just below gravity's meeting is the signature of radiative (Coleman-Weinberg) breaking at that scale, which is where t85 put E6's breaking: noted as a reading, not a result.
