# t71 Do posts 30, 62 and 64 agree with each other? (pre-registered 2026-11-24, before any code is written or run)

Three posted claims, each tested alone so far:
- Post 30 / t65: Z'_psi sits near 1e14-1e15 GeV, set by the seesaw (M_R3 = m_t^2 / m3; high-scale 1.28e14 GeV, pole 5.94e14 GeV).
- Post 62 / t68: E6 bosons above 4.6e15 GeV (alpha^-1 = 42.4); colour-triplet scalars above 5.5e11 GeV.
- Post 64 / t70: the couplings meet at M3 = 3.7e13-5.6e13 GeV, alpha^-1 = 37.1-39.3, with light doublets and triplets at M_D.

Bridge under test [I]: the meeting scale M3 is the scale where SU(3)^3 breaks (t67), and every mass that comes from that breaking is at most of order M3. The ground (the cut, the counting phases) is not on trial.

Hand estimates made while writing this file (recorded so they are not mistaken for blind predictions): G1 near 4.6e15, G2 near 7e13 against M3 up to 5.6e13, G3 non-empty.

S1 Sanity: the t68 lifetime formula with alpha^-1 = 42.4 reproduces M_E6 >= 4.64e15 GeV; t70's best meeting is reproduced (M3 = 4.48e13 GeV, alpha^-1 = 38.8).

G1 [M] E6 bound with the alpha actually reached. Above M3 the three couplings run together with b = -11 + (2/3)*3*3 (three Weyl 27s, Dynkin index 3 each, t68 G2) + (1/3)*3*n_h (n_h = 0..3 Higgs 27s), i.e. b = -5 + n_h [arithmetic slip "-11 + 2" corrected before any code ran], from alpha^-1(M3) of the best t70 meeting, up to the scale where the Super-K bound is met. Pass if the bound stays within a factor 1.1 of 4.64e15 GeV for every n_h and below the Planck mass 1.22e19 GeV.

G2 [M] Z'_psi against M3. U(1)_psi is in the Cartan of E6, which is the Cartan of SU(3)^3 (rank 6 each), and it commutes with colour, so Z'_psi is one of the SU(3)_L x SU(3)_R bosons. The vev that gives the Majorana mass (v_psi >= M_R3, couplings <= 1, t65 D1) therefore breaks SU(3)^3, and the heaviest broken boson has mass at least g(M3) * M_R3, g = sqrt(4 pi alpha(M3)). Pass if g * M_R3 (high-scale masses, since the seesaw acts at M_R) <= 3 * M3_max (threshold allowance, fixed now). Pole masses reported as information. Fail -> post 30's 1e14-1e15 GeV and post 64's 4.5e13 GeV cannot both stand as written.
G2a [M] Check that U(1)_psi lies in the span of the SU(3)_L x SU(3)_R Cartan: on the 27 weights, the psi charges (16: +1, 10: -2, 1: +4 in units of 1/(2 sqrt 6) up to normalisation) are reproduced by a combination of the four Cartan generators of SU(3)_L and SU(3)_R, residual < 1e-9.

G3 [M] Triplets between the bounds. Under unbroken SU(3)^3 the triplets D share multiplets with the quarks, so their mass comes from the breaking: M_D <= M3 / g. With t68: M_D >= 5.5e11 GeV. Pass if at least one two-loop meeting of t70 has 5.5e11 <= M_D <= M3/g. Reported: the count, and the doublet windows (n_H = 2, 3) restricted to these meetings.

Controls:
C1 A Z' that is not in the Cartan (a random direction orthogonal to all six Cartan generators does not exist: rank 6). Instead: the hypercharge-like combination of only SU(3)_C generators does not reproduce the psi charges (residual > 0.1).
C2 With the pole masses, G2's ratio is reported; expected larger than with high-scale masses.

Verdict rule: all pass -> the three posts agree. G2 fails -> the bridge "Z'_psi mass = seesaw scale" (t65 D4) and the bridge "M3 = breaking scale" (t67) cannot both hold; record which wording changes. G3 fails -> the t70 meetings need triplets above the breaking scale and the meeting bridge is revised.

## Scoring (2026-11-24)
Run 1 (t71_run1.log, script as first written): G2a FAIL from a script error, kept on record. It tried only the two end-node coweights of the Dynkin diagram, and those need not commute with the colour arm fixed in t66. Run 2 (t71_run2.log, script t71_consistency.py) searches the whole Weyl orbit (27 elements) for the copies that commute with SU(3)_C and the weak root. That is what G2a asks; no threshold changed.
- S1 PASS: 4.64e15 GeV at alpha^-1 = 42.4; the best t70 meeting is reproduced (4.48e13 GeV, alpha^-1 = 38.76).
- G1 PASS: with alpha run above M3 (b = -5 to -2), the E6 bound is 4.64e15 to 4.77e15 GeV (ratio 1.00 to 1.03).
- G2a PASS (run 2): three copies of U(1)_psi commute with SU(3)_C x SU(2)_L (the standard one and its two relabellings that swap d^c with D^c and L with H). All three lie in the Cartan of SU(3)_L x SU(3)_R (residual 0). C1 PASS: none can be built from colour alone (residual 0.46 to 0.67).
- G2 PASS: g M_R3 = 7.3e13 GeV against M3 up to 5.6e13 GeV, a ratio of 1.3 (allowance 3). C2: pole masses give 3.4e14 GeV, a ratio of 6.0; this would fail.
- G3 PASS: 577 of the 1203 two-loop meetings have the triplets between 5.5e11 GeV and M3/g. The other 626 have triplets above the breaking scale and are now excluded. The doublet windows are unchanged: n_H = 2 at 1.0e3 to 7.5e6 GeV, n_H = 3 at 4.2e5 to 1.3e9 GeV. Triplets sit at 5.6e11 to 7.5e13 GeV.
Verdict: posts 30, 62 and 64 agree, with one refinement to post 30. Z'_psi is one of the SU(3)_L x SU(3)_R bosons broken at the meeting, so its mass is near 1e14 GeV (about 7e13 GeV, from the high-scale masses). The 1e15 GeV end of post 30's range is disfavoured. Correction-map entry: t65 D4 (Z'_psi = g_psi |Q| v_psi with pole masses) is superseded by "Z'_psi is broken at M3".
