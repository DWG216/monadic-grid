# Pre-registered before running frozen_fluid.py (2026-11-08 ~23:00 ET)
Claim under test: "frozen vs fluid" is set by WEAK integrality (every d^2 an integer), not by integer vs irrational d.
Model: SU(2)_k, spin-1/2 strands, Jones/Temperley-Lieb path representation, n = 3, 4, 5, 6 strands; count braid-group image elements
(up to phase) by BFS, cap 30,000.
P1 [known theorem, check]: finite for k = 1, 2, 4 (ell = k+2 in {3,4,6}) at every n; these are exactly the weakly integral levels.
   Note k = 2 (Ising, d = sqrt2) and k = 4 (d = sqrt3) have IRRATIONAL d yet are finite: integer d is not the criterion.
P2 [known theorem, check]: k = 3, 5, 6, 7 exceed the cap at n = 3 already (dense; Freedman-Larsen-Wang).
P3 [accident check]: k = 8 (ell = 10, the golden level) is FINITE at n = 3 (icosahedral) but exceeds the cap from n = 4 on.
   Its d^2 = 2 + phi is not an integer, so the 3-strand finiteness is an accident of small size, not frozenness.

# Scored after run 1 (2026-11-08)
P1 PARTIAL: k=1, 2 finite at every n (Ising 24, 192, 1920, 23040); k=4 finite at n=3, 4 (24, 648) but our BFS hit the 30k cap at n=5, 6
   (theorem says finite; not confirmed by us). P2 PASS. P3 PASS: k=8 finite at n=3 (600 on the full reducible space), cap exceeded from n=4.

# Pre-registered before running level8.py (2026-11-08 ~23:00 ET)
New picture under test: the icosahedral frame is the 3-strand shadow of one fluid golden theory (SU(2)_8); golden numbers sit in its COUNTING.
L1 [identity]: two-step growth of the n-strand path-space dimension -> d^2 of the strand. Level 8 -> 2 + phi = 3.618 (irrational, golden);
   level 4 -> 3; level 2 -> 2 (whole numbers).
L2 [real test, decisive]: an element of INFINITE order proves an infinite group. Search all positive braid words of length <= 6.
   Prediction: level 8 at n = 4, 5, 6 has a word whose eigenvalue phase ratio is not a rational multiple of pi (no denominator <= 500
   within 1e-9). Level 8 at n = 3, level 4 at n = 5, 6 (the capped cases) and level 2 at n = 6: EVERY word has finite order
   (all phase ratios rational, denominator <= 500). If level 4 at n = 5 shows an infinite-order word, our code or the theorem
   reading is wrong, and we say so.
L3 [built-in]: inside the 4-strand level-8 representation, sigma1 and sigma2 alone generate a finite group (the shadow), and adding
   sigma3 makes it infinite.

# Scored after level8.py (2026-11-08)
L1 PASS (identity): two-step growth 2.0000 (k=2), 3.0000 (k=4), 3.6180 = 2+phi (k=8). Golden sits in the counting at level 8.
L2 PASS: level 8 at n=4,5,6: word s1 s1 s2 s2 s3 has phase ratio 0.5589700133, not p/q with q<=500 -> infinite order (numerical evidence,
   consistent with Jones's classification; not a proof of irrationality). Level 8 at n=3, level 4 at n=5,6, level 2 at n=6: every word of
   length <=6 has finite order. The capped level-4 cases behave as the theorem says.
L3 PASS: in the 4-strand level-8 rep, <s1,s2> closes at 600 (the icosahedral shadow); adding s3 exceeds 30,000.
Note: the infinite-order word uses all three generators, so the escape from the shadow needs the 4th strand.
