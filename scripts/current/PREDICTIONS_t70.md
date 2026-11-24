# t70 The coupling meeting at two loops (pre-registered 2026-11-24, before any code)

Bridge under test [I]: as t67 (§166). t67 used one-loop running; this repeats its scan with two-loop gauge running and the top Yukawa, to see whether the meeting survives.

Method: d(alpha_i^-1)/dt = -b_i/(2 pi) - sum_j b_ij alpha_j/(8 pi^2) + c_i y_t^2/(32 pi^3), t = ln mu, alpha_1 GUT-normalised, from M_Z with t67's inputs (59.0, 29.6, 8.47) and y_t(M_Z) = 0.99, run at one loop with dy_t/dt = y_t/(16 pi^2) (9/2 y_t^2 - 8 g3^2 - 9/4 g2^2 - 17/20 g1^2). Standard Model b_ij = [[199/50, 27/10, 44/5], [9/10, 35/6, 12], [11/10, 9/2, -26]], c = (17/10, 3/2, 2). Each extra Weyl multiplet F adds Delta b_ij = 2 S2_i(F) C2_j(F) + delta_ij (10/3) C2(G_i) S2_i(F) above its mass (U(1): S2 = (3/5) Y^2 dim, C2 = (3/5) Y^2, C2(G) = 0). Same thresholds, scan grid and meeting criterion (spread < 0.5) as t67, and the same reading for the doublet pairs that are not light (they sit with the triplets).

S1 Sanity (method): with b_ij and c set to zero the code reproduces t67: 1108 meetings, M3 4.1e13-6.1e13 GeV.
S2 Sanity: the two-loop SM coefficients above reproduce the SM numbers when the extras' formula is applied to one SM generation's fermions (check of the Delta b_ij formula: three generations give the fermion part of b_33 = 76 and of b_12 = 9/5).
G1 [M] A meeting still exists at two loops, only for n_H = 2 or 3 light doublet pairs, and every meeting has M_H < M_D.
G2 [M] Every two-loop meeting has M3 between 1e13 and 1e17 GeV and alpha^-1 between 30 and 45.
G3 [M] Every two-loop meeting has M_H <= 2e8 GeV.
G4 [information] Shift of the best point and of the n_H = 2 window of M_H against t67. Expected: M3 moves by less than a factor 3.
Controls: C1 Standard Model alone at two loops does not meet (spread > 0.5). C2 all extras at one common mass do not meet.

Verdict rule: G1 fails -> the t67 meeting was a one-loop artefact and goes in the correction map. G1-G3 pass -> the meeting and its doublet window are stable at two loops; the window as found here replaces t67's in public material.

## Scoring (2026-11-24)
Run 1 (t70_run1.log, script t70_twoloop.py, written after this file).
- S2 PASS: the Delta b_ij formula on three SM generations gives b_33 fermion part 76 and b_12 fermion part 9/5.
- S1 PASS: with the two-loop and Yukawa terms off, the code reproduces t67: 1108 meetings, M3 4.1e13-6.1e13 GeV (best point differs only among ties at spread 0.002).
- G1 PASS: at two loops 1203 meetings; none with one light pair; two pairs (709) at M_H = 1.0e3-7.5e6 GeV; three pairs (494) at 4.2e5-1.3e9 GeV; every meeting has M_H < M_D.
- G2 PASS: every meeting at M3 = 3.7e13-5.6e13 GeV, alpha^-1 = 37.1-39.3.
- G3 FAIL: with three light pairs the window reaches M_H = 1.3e9 GeV, above the pre-registered 2e8. Recorded as a fail.
- G4 (information): best M3 moves from 5.0e13 to 4.5e13 GeV (ratio 0.90).
- C1 PASS: Standard Model alone at two loops, spread 3.21. C2 PASS: all extras at one mass, spread 3.21.
Reading: the meeting is stable at two loops and its scale barely moves (about 4.5e13 GeV). The doublet window widens upward: two pairs up to 7.5e6 GeV, three pairs up to 1.3e9 GeV. Public wording becomes "below about 1e9 GeV". The scan starts at 1 TeV, so for two pairs the window may extend below it; collider limits decide the low end.
