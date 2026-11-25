# t89 Dirac neutrino masses from the grid's own cut (roadmap item 2) (pre-registered 2026-11-25, before any t89 code is written or run)

Ground: the forces come from cutting E6 to SU(3)_C x SU(3)_L x SU(3)_R (t66); the 27 is three bifundamentals, quarks (3,3bar,1) + (3bar,1,3) and leptons (1,3,3bar). The lepton bifundamental holds L, e^c, nu^c and the extra lepton doublets and singlet together.
Bridge under test [I]: t65 used the SO(10) relation m_D = up-quark masses. On the grid's cut the neutrino's Dirac mass and the charged lepton's mass come from the same lepton bifundamental coupling (1,3,3bar)^3 to the Higgs, not from the quark multiplets. So the grid's own bridge is m_D,i = m_l,i (charged lepton masses, generation by generation, up to the ratio of two vevs, taken as 1).
Masses: m_e = 0.51099895 MeV, m_mu = 105.6583755 MeV, m_tau = 1776.969 MeV (grid); light neutrinos (section 125): m1 = 0.365 meV, m2 = sqrt(m1^2 + 7.50e-5 eV^2), m3 = 59.16 meV - m1 - m2. Seesaw, diagonal (as t65): M_Ri = m_Di^2 / m_i.
Leptogenesis check (as section 158): Davidson-Ibarra eps_1 <= (3/(16 pi)) M_R1 m3 / v^2, v = 174 GeV; eta_B ~ 9.6e-3 eps_1 kappa with kappa <= 0.1 (strong washout); observed 6.1e-10.

S1 Sanity: with m_D = up-quark pole masses (2.16 MeV, 1.27 GeV, 172.57 GeV) the t65 values are reproduced (M_R1 about 1.3e7 GeV, M_R3 about 5.9e14 GeV).
P1 [M] With m_D = charged-lepton masses: M_R1, M_R2, M_R3 computed and reported; expected M_R3 between 1e10 and 1e11 GeV.
P2 [M] Consistency with t71: M_R3 (lepton bridge) is below the meeting scale M3 = 4.48e13 GeV, so v_psi ~ M3 can supply it with a coupling <= 1.
P3 [M] Thermal N1 leptogenesis with the lepton bridge: the Davidson-Ibarra maximum eta_B is below 6.1e-10 (expected: it fails, worse than SO(10)).
P4 [M] The heaviest right-handed neutrino with the lepton bridge passes the Davidson-Ibarra requirement on its own (M_R3 >= the M needed for eta_B = 6.1e-10 at kappa = 0.1), so an asymmetry is available from N3 if N1 and N2 washout is avoided (information for the next step: flavoured or N3-dominated leptogenesis).

Verdict: P1-P2 pass -> the grid's own cut replaces the SO(10) bridge; P3 records that thermal N1 leptogenesis is out either way; P4 says where the asymmetry must come from.

## Scoring (2026-11-25)
Run 1 (t89_run1.log). All pass.
- S1 PASS: SO(10) bridge reproduces t65 (1.28e7, 1.86e11, 5.94e14 GeV).
- P1 PASS: lepton bridge M_R = 7.2e5, 1.3e9, 6.3e10 GeV.
- P2 PASS: M_R3 = 6.3e10 GeV is three orders below the meeting scale 4.5e13 GeV.
- P3 PASS: thermal N1 leptogenesis gives at most eta_B = 6.8e-14 (needs 6.1e-10): out, as registered.
- P4 PASS: N3 at 6.3e10 GeV is ten times the 6.4e9 GeV Davidson-Ibarra needs at kappa = 0.1.
Verdict: the grid's own cut puts the Dirac masses at the charged-lepton masses. The heaviest right-handed neutrino, 6.3e10 GeV, is where the asymmetry can come from; the next step is N3-dominated, flavoured leptogenesis with the lighter N1 and N2 washout computed.
