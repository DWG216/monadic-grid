# t66 The Standard Model from cutting E6 at the meeting node (pre-registered 2026-11-23, before run)

Bridge under test [I]: the rule that gave three generations (cut the McKay diagram at the dimension-3 node, t60, E8 -> E6 x SU(3)) applies to E6 itself. The ground (the steps, McKay) is not on trial.

Sanity: the E6 root system built from its Cartan matrix has 72 roots; the 27 has 27 distinct weights.

G1 [M] The McKay graph of 2T (t55) minus its dimension-3 node is three disjoint A2 diagrams, node dimensions {1,2} on each arm.
G2 [M] Tensoring with the two non-trivial 1-dim characters of 2T (the counting phases w, w^2) permutes the three arms cyclically, fixing none. Hence the three factors have equal couplings at the cut.
G3 [M] The order-3 Kac automorphism of E6 with s = 1 at the central node (label 3) fixes 18 roots + rank 6: dim 24 = su(3)^3. Its w and w^2 eigenspaces each have dim 27.
G4 [M] Under su(3)^3 the 27 splits into three 9-dim blocks, each a (3, 3bar) of two different factors.
G5 [M] Take SU(3)_C as one factor and SU(2)_L inside a second. A U(1) in the Cartan, commuting with both, has charges on the 27 equal to the Standard Model hypercharges of one generation plus the E6 extras: (3,2) 1/6; (3,1) -1/3; (3bar,1) -2/3, 1/3, 1/3; (1,2) -1/2, -1/2, +1/2; (1,1) 1, 0, 0. Threshold: max deviation < 1e-9.
G6 [M] With that Y and equal couplings (G2), sin^2 theta_W = Tr(T3^2)/Tr(Q^2) over the 27 = 3/8 exactly.
G7 [information] One-loop Standard Model running from M_Z (alpha1^-1 = 59.0 in GUT normalisation, alpha2^-1 = 29.6, alpha3^-1 = 8.47): the scale M12 where sin^2 theta_W = 3/8 lies between 1e12 and 1e14 GeV, and alpha3 does not meet there (known); thresholds from the E6 extras near 1e14 GeV are needed. Recorded, not scored.

Controls:
C1 Remove a dimension-2 node instead: the remainder is not three A2 (expected A5 + A1).
C2 Kac s = 1 at an end node (label 1): fixed algebra dim 46 = so(10) + u(1), the U(1)_psi grading, not the Standard Model.

## Scoring (2026-11-23)
Run 1 (t66_run1.log, script kept as t66_sm_cut_run1.py) crashed in the G5 scorer: it counted coloured multiplets once per colour against a target listed once per multiplet. Scorer fixed (targets repeated per colour); predictions unchanged. Run 2 (t66_run2.log):
- Sanity: 72 roots, highest root (1,2,2,3,2,1); 27 weights. PASS.
- G1 PASS: removing the dimension-3 node leaves three A2, each {1, 2}.
- G2 PASS: tensoring with w and w^2 permutes the three arms cyclically (perm [1,2,0] and [2,0,1]); the dimension-3 node is fixed.
- G3 PASS: 18 fixed roots, dim 24 = su(3)^3; the w and w^2 parts have dim 27 each.
- G4 FAIL as scored: blocks came out (3,1,3), (3bar,3bar,1), (1,3,3bar). Post hoc: the 3/3bar label of each arm depends on the order of its two nodes; with arm 1 relabelled all three blocks are (3,3bar) of two different factors, (3bar,1,3), (3,3bar,1), (1,3,3bar): trinification. Recorded as a fail of the check as written.
- G5 PASS: a U(1) commuting with SU(3)_C x SU(2)_L gives exactly the Standard Model hypercharges of one generation plus the E6 extras (max deviation 1e-16). Colour = arm 2, weak = arm 1.
- G6 PASS: sin^2 theta_W = 0.375 = 3/8. Electric charges on the 27: -1 (2), -2/3 (3), -1/3 (6), 0 (5), 1/3 (6), 2/3 (3), +1 (2).
- G7 (information): with Standard Model running alone, sin^2 theta_W = 3/8 at 1.0e13 GeV, where alpha1^-1 = alpha2^-1 = 42.4 but alpha3^-1 = 36.8. The couplings do not meet without thresholds; the E6 extras and Z'_psi near 1e14 GeV must supply them (next test).
- C1 PASS: removing a dimension-2 node leaves components of sizes 1 and 5. C2 PASS: the end-node grading fixes dim 46 = so(10) + u(1).
