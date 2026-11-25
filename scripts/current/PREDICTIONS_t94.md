# t94 The dark-matter doublet's neutral splitting, and the singlet N (pre-registered 2026-11-25, before any t94 code is written or run)

Ground: t93 (P = (-1)^(Q_psi+F) odd on the 27's exotics; dark matter = lightest odd state). The 27^3 coupling 10.10.1 gives lambda H_u-like H_d-like N; with the electroweak vevs (v_u, v_d in the 10) it mixes the doublet pair's neutral states with N.
Bridge under test [S]: N has psi charge +4, so its Majorana mass needs charge -8; the grid's only psi-breaking vevs carry charge 2 (t65) at the meeting, v_psi = 4.5e13-7.3e13 GeV (t70, t71), and the only higher scale is gravity's meeting, M* = 2.435e18 GeV (t85). The minimal operator gives M_N = v_psi^4 / M*^3, a choice-free estimate.
Neutral mass matrix (N, h_u0, h_d0): [[M_N, lambda v_d, lambda v_u], [lambda v_d, 0, mu], [lambda v_u, mu, 0]], mu = 1100 GeV (t93's thermal doublet), v = 174 GeV, tan beta in {2, 10, 50}, lambda in {0.1, 0.3, 1.0}.

S1 Sanity: with lambda = 0 the doublet states are exactly +-mu (degenerate in |mass|, splitting 0) and N sits at M_N.
P1 [M] M_N lies between 1e-3 and 10 GeV (far below the doublet): the singlet is light.
P2 [M] For every lambda and tan beta in the grid, the two doublet-like neutral states are split by more than 200 keV (Z-exchange scattering on nuclei is then kinematically closed).
P3 [M] For every lambda and tan beta the lightest P-odd state is singlet-like (N fraction > 50%). This revises t93's G4: the grid's dark matter is a light, mostly-singlet Majorana fermion, not the doublet.
Information: the lightest state's mass and N fraction at each point.
Verdict: P1-P3 pass -> the doublet's splitting is automatic, and the dark matter is the singlino-like state of the 27; its relic abundance (not thermal freeze-out of a doublet) is the next computation.

## Scoring (2026-11-25)
Run 1 (t94_run1.log). All pass.
- S1 PASS. P1 PASS: M_N = v_psi^4 / M*^3 = 0.28 GeV (v_psi = 4.5e13) to 1.97 GeV (7.3e13).
- P2 PASS: the doublet-like neutral states are split by 11 MeV to 5.4 GeV over the grid (all far above 200 keV).
- P3 PASS: the lightest P-odd state is at least 97.6% singlet everywhere; its mass runs from 0.015 to 21 GeV across lambda and tan beta.
Verdict: the splitting is automatic, and t93's G4 is revised: the grid's dark matter is a light, mostly-singlet Majorana fermion (the 27's N, mixed slightly with the doublets), between about 0.015 and 21 GeV, not the 1.1 TeV doublet. Its abundance cannot be thermal freeze-out of a doublet; computing it is the next step. Correction map: the 1.1 TeV doublet reading (t93 G4) is withdrawn.
