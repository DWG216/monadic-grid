# t68 Where E6 breaks, and the coloured triplets, against proton decay (pre-registered 2026-11-23, before run)

Bridge under test [I]: the cut of t66 sets the trinification scale M3 (about 1e13-1e14 GeV), and the equal couplings there come from the counting phases permuting the three SU(3) arms, not from unbroken E6. So E6 itself may break higher. Super-Kamiokande: tau/B(p -> e+ pi0) > 2.4e34 yr.

Lifetime estimate used throughout (order of magnitude): tau = M^4 / (c^2 m_p^5), c the product of couplings at the two vertices (c = alpha for gauge bosons, c = lambda_qq * lambda_ql for scalars), m_p = 0.938 GeV.

S1 Sanity: with alpha^-1 = 40 the estimate gives a lower bound on a GUT X-boson mass between 1e15 and 1e16.5 GeV (the usual minimal-SU(5) range).
G1 [M] Every boson of su(3)^3 (24) has colour triality 0, so none turns a quark into a lepton; every boson in the 27 + 27bar of the 78 (54) has colour triality non-zero. Thresholds: exact counts 24/0 and 0/54.
G2 [M] The Dynkin index of the 27 is the same for SU(3)_C, SU(3)_L and SU(3)_R (expected 3 each), so for any content made of whole 27s the one-loop coefficients b_C = b_L = b_R. The couplings stay equal from M3 up to wherever E6 breaks, so M_E6 is not tied to M3.
G3 [M, information] The Super-K bound on the E6 bosons with alpha^-1 = 42.4 (t66 G7) is recorded: M_E6 >= (tau alpha^2 m_p^5)^(1/4). Expected 1e15-1e16.5 GeV; passes if below the Planck mass 1.22e19.
G4 [M] The E6 cubic invariant (triples of 27 weights summing to zero) has 45 terms. Under the Standard Model it contains both a diquark term (three colour-charged fields) and a leptoquark term (one colour-charged field with a lepton) involving the colour triplets D. Expected: both present, so D-type triplets can mediate proton decay; the risk is real.
G5 [M] The colour-triplet scalars in a Higgs 27 couple with Yukawas tied to the first-generation masses. With lambda_qq * lambda_ql = y_u y_d (m_u = 2.16 MeV, m_d = 4.67 MeV, v = 246 GeV, y = sqrt2 m / v) the Super-K bound needs M_T >= M_T,min. Passes if M_T,min < 1e13 GeV (they may sit at the cut). Also reported with y_u y_e (m_e = 0.511 MeV).

Controls:
C1 The end-node grading (so(10) + u(1), t66 C2) contains colour-triplet bosons in its fixed algebra (expected > 0): cutting there would put leptoquark bosons at the cut and be excluded.
C2 With order-one Yukawas the same G5 bound is above 1e13 GeV: the bound is not trivially met.

Verdict rule: G1, G2, G4 and G5 pass -> proton decay does not exclude the cut; E6 must break above the G3 bound and the triplet scalars sit above the G5 bound. G5 fails -> the triplets cannot sit at the cut and the bridge must be revised.

## Scoring (2026-11-23)
Run 1 (t68_run1.log). All pass.
- S1 PASS: alpha^-1 = 40 gives M >= 4.8e15 GeV, the usual minimal-SU(5) range.
- G1 PASS: the 24 bosons of su(3)^3 carry no colour triplet; all 54 bosons of the 27 + 27bar do. Only E6's own bosons can turn quarks into leptons.
- G2 PASS: the 27 has Dynkin index 3 for each of SU(3)_C, SU(3)_L, SU(3)_R. The couplings stay equal above M3 for any content made of whole 27s, so E6 is free to break higher.
- G3 PASS: the E6 bosons must be above 4.6e15 GeV (alpha^-1 = 42.4).
- G4 PASS: the cubic invariant has 45 terms: 6 colourless, 27 with two coloured fields, 12 with three. 12 diquark-type and 21 leptoquark-type terms involve the charge-1/3 triplets. The risk is real.
- G5 PASS: with first-generation Yukawas the triplet scalars need only M_T >= 5.5e11 GeV (y_u y_d) or 1.8e11 GeV (y_u y_e), below the cut at 1e13. They may sit at the cut.
- C1 PASS: the end-node grading (so(10) + u(1)) has 30 colour-triplet bosons in its fixed algebra; a cut there would put leptoquark bosons at 1e13 GeV and be excluded. C2 PASS: order-one Yukawas would need 3.0e16 GeV.
Note: the D test in the script also admits the Y = +1/3 antitriplets (d^c-like), which mix with D^c; the counts include them.
Verdict: proton decay does not exclude the cut. It requires E6 to break above about 5e15 GeV, which the Z3 permutation allows, and the triplet scalars to have Yukawas of first-generation size. Prediction for Hyper-K: p -> e+ pi0 from E6 bosons at a lifetime set by M_E6, not by the cut; the scale of M_E6 is not yet derived (open).
