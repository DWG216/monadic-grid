# t69 Does the mirror 27bar decouple? Against Distler-Garibaldi (pre-registered 2026-11-23, before run)

Bridge under test [I] (§106, P3): the mirror hand is present but gapped by interaction, in blocks that carry no anomaly. Distler and Garibaldi (2010) proved that E8 cannot give a chiral three-generation spectrum by representation theory alone.

S1 Sanity: E8 has 240 roots; the order-3 Kac grading at the node of label 3 fixes e6 + su(3) (dim 86) and its w and w^2 parts have dim 81 each.
G1 [M] (Distler-Garibaldi reproduced) The weights of the w part are exactly minus those of the w^2 part, so (27,3) and (27bar,3bar) pair into an invariant mass term: the E8 content is vector-like, net chiral index 0. Expected PASS: the theorem holds for us.
G2 [M] The mirror cannot be gapped by a bilinear on its own: no two weights of the 27 sum to zero (27 x 27 has no singlet). Expected count 0. So the gapping has to be by interaction.
G3 [M] One 27 carries no perturbative Standard Model anomaly (SU3^3, SU3^2 Y, SU2^2 Y, Y^3, grav-Y all 0, threshold 1e-12) and has an even number of doublets (no Witten anomaly).
G4 [M] Z16 count: with Z4 = exp(i pi q_psi / 2), q_psi the U(1) of the end-node grading normalised so that the 16 has charge 1, a 27 has 16 fermions of odd Z4 charge (16 -> 1, 10 -> -2, 1 -> 4). The Z16 index of one 27 is 0 mod 16 and of the mirror (27bar,3bar) is 48 = 0 mod 16. Expected PASS: the anomaly that would block interacting gapping vanishes.
G5 [M] (risk) The family SU(3) cubic anomaly of the mirror (27 copies of 3bar) is -27, not 0. Expected: non-zero. Then the mirror cannot be gapped while family SU(3) is exact; gapping requires the family symmetry broken at or above the gapping scale.

Control:
C1 One Standard Model generation without the right-handed neutrino (15 Weyl fermions): Z16 index 15, not 0 mod 16, so it cannot be gapped alone (the known reason the block is 16).

Verdict rule: G1 PASS means the theorem stands; our answer is outside its assumptions (interacting gapping, not a chiral representation). G2-G4 PASS means E6 and Z16 allow interacting gapping. G5 non-zero means the mirror gapping and family breaking must happen together [I]. If G4 fails the escape is closed.

## Scoring (2026-11-23)
Run 1 (t69_run1.log, script kept as t69_mirror_run1.py): G4 and C1 failed in the scorer only. The charges came out 1.000000001, -2.000000002, 4.000000004 (rounding to 9 places after normalising) and did not match the exact targets; C1's selection used the same comparison and found 0 fermions. G5 was entered as a fixed number, not computed. Run 2 (t69_run2.log): rounding to 6 places, and G5 computed from the family SU(3) weights of the E8 grading. Predictions unchanged.
- S1 PASS: 240 roots. Of the two label-3 nodes, node 7 fixes e6 + su(3) (86) with 81 + 81; node 2 fixes su(9) (80).
- G1 PASS: the w part is exactly minus the w^2 part; net chiral index 0. Distler-Garibaldi holds for us.
- G2 PASS: no two weights of the 27 sum to zero; the mirror has no bilinear mass of its own.
- G3 PASS: all Standard Model anomalies of one 27 vanish; 6 doublets (even).
- G4 PASS (run 2): psi charges 16 x 1, 10 x -2, 1 x 4; 16 odd; Z16 index 0 for one 27 and 0 for the mirror (27bar,3bar).
- G5 non-zero as expected: family SU(3) cubic anomaly 27 on the mirror and -27 on the visible part (the sign is the 3/3bar labelling convention).
- C1 PASS: 15 fermions without nu^c give Z16 index 15.
Post hoc note [I]: the Z4 acts as fermion parity squared only on the 16; the 10 and 1 have even charge. Once E6 is broken to SO(10) they can pair by ordinary masses, and only the 16s need interacting gapping.
Verdict: the theorem stands, and our answer lies outside its assumptions. E6 and Z16 allow the mirror to be gapped by interaction, not by a mass term. The family SU(3) anomaly forbids it while family symmetry is exact, so mirror gapping and family breaking must happen together [I]. That interacting gapping works in 4D for this content is not yet shown.
