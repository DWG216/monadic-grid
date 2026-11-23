# t67 Do the couplings meet? The E6 extras as thresholds (pre-registered 2026-11-23, before any code is written or run)

Bridge under test [I]: the equal couplings at the cut (t66 G2) are the Standard Model couplings meeting at one scale M3, with the running between M_Z and M3 set by the Standard Model plus the extra fermions of the three 27s (the 10 + 1 beyond each 16). The ground (the cut, the counting phases, t66) is not on trial.

Method: one-loop running of alpha_i^-1 (alpha_1 in GUT normalisation), from M_Z = 91.1876 GeV with alpha_1^-1 = 59.0, alpha_2^-1 = 29.6, alpha_3^-1 = 8.47 (as t66). Each extra fermion multiplet enters at its mass as a step in b_i, Weyl fermions contributing (2/3) T(R) to SU(N) and (2/3)(3/5) Y^2 to U(1). Contents per generation beyond the 16: colour triplets D + D^c (3, 1, -1/3) + (3bar, 1, +1/3), doublets H + Hbar (1, 2, -1/2) + (1, 2, +1/2), singlet N (no effect). U(1)_psi and Z'_psi do not change the Standard Model coefficients. "Meet" means: at some scale, max pairwise difference of the three alpha_i^-1 < 0.5.

S1 Sanity: Standard Model alone reproduces t66 G7: alpha_1 = alpha_2 at 1.0e13 GeV with alpha^-1 = 42.4 and alpha_3^-1 = 36.8; no meeting.
G1 [M] The extras of one 27 beyond the 16 (D + D^c + H + Hbar) are a complete SU(5) 5 + 5bar: added at one common mass they shift b_1, b_2, b_3 by the same amount (expected Delta b = 2/3 per generation for each), so they cannot make the couplings meet. Expected PASS (equal shifts, exactly).
G2 [M] Split thresholds can: with the triplets heavy and the doublets light, a meeting exists. Scan n_H = 1, 2, 3 light doublet pairs at M_H in [1e3, 1e16] GeV and all three triplet pairs at M_D in [5.5e11, 1e16] GeV (the t68 proton bound below, the cut above). Expected: at least one (n_H, M_H, M_D) gives a meeting, and every meeting has M_H < M_D.
G3 [M] Every meeting found in G2 has its scale M3 between 1e13 and 1e17 GeV and alpha^-1 at M3 between 30 and 45 (perturbative, and consistent with t68's E6 bound being reachable above or at the cut).
G4 [M] Expected: the light doublets sit at M_H <= 1e10 GeV for every meeting (a prediction for colliders only if M_H comes out near the TeV scale; recorded either way).

Controls:
C1 Standard Model alone (S1) does not meet.
C2 All extras at one common mass (G1) do not change whether the couplings meet, for any common mass in [1e3, 1e16] GeV.
C3 Light triplets instead (M_D < M_H, same scan ranges) give no meeting, or only with M_D below the t68 bound.

Information (not scored): two-loop running at the best G2 point; the shift in M3 and in the residual mismatch.

Verdict rule: G2 fails (no meeting anywhere in the scan) -> the bridge "the equal couplings at the cut are the measured couplings meeting, with only E6 extras as thresholds" fails and goes in the correction map. G2 passes -> the doublet scale M_H is a prediction of the grid, to be tested at colliders if low.
