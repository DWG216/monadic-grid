# t96 Flavour from the grain: PSR directions and residual symmetries (pre-registered 2026-11-25, before any t96 code is written or run)

[S] A family symmetry is broken by vevs in three-generation space; a generic direction would be an unexplained choice. Directions fixed by maximal subgroups (maximal isotropy) are stationary for every invariant potential (Michel's critical orbits) and need no choice. The PSR keeps only those.
Groups from the grid [M]: 2T = SL(2,3) is the 24 Hurwitz units (sections 140-142); its conjugation action on imaginary quaternions gives A4 on a real triplet. The 9-point grain's clock D = diag(1, w, w^2) and shift C (cyclic permutation) generate the Heisenberg group of order 27, Delta(27), on a complex triplet.
[I] Dirac sectors (charged leptons, quarks) carry a phase: they keep the counting phase Z3 (the cyclic generator T). Majorana neutrinos are their own mirror: they keep a real Z2 of A4 (the hand swap's real form). Mixing = the angle between the two sectors' eigenbases.

S1 Sanity: the Hurwitz units close under multiplication (24 elements) and give 12 distinct rotations (A4); C and D generate 27 matrices (up to nothing: the scalars w, w^2 included).
P1 [M] A4 on R^3 has exactly two classes of critical axes: 4 axes fixed by Z3 subgroups ((1,1,1)-type) and 3 fixed by Z2 subgroups ((1,0,0)-type).
P2 [M] Delta(27) on C^3 has exactly 12 critical lines (eigenlines with maximal stabiliser), forming 4 mutually unbiased bases: any two lines from different bases have |<a|b>|^2 = 1/3.
C1 Control [M]: if both sectors keep Delta(27) subgroups (no hand swap), the mixing between two of its bases is |U|^2 = 1/3 in every entry (sin^2 theta13 = 1/3), far outside data: the Majorana Z2 is needed.
P3 [M] With charged leptons keeping Z3 = <T> and neutrinos keeping Z2 = <S> of A4, every allowed PMNS matrix has one column exactly (1,1,1)/sqrt3 in modulus (trimaximal), for every value of the one free angle and phase: TM2.
P4 [M on data] TM2's sum rule sin^2 theta12 = 1/(3 (1 - sin^2 theta13)) with NuFIT 6.0 sin^2 theta13 = 0.02215 lies inside NuFIT 6.0's 3-sigma range 0.275-0.345 (best fit 0.307).
Information: the predicted value and its pull from the best fit; the TM2 curve relating theta23 and delta at the measured theta13, against NuFIT's best fits (sin^2 theta23 = 0.470-0.561, delta = 212 deg).
Verdict: P1-P4 pass -> the PSR's critical directions in the grain's groups give trimaximal (TM2) lepton mixing with one free angle (theta13), quark mixing near identity (both Dirac sectors keep Z3), and a sharp test: sin^2 theta12 = 0.341, now at the edge of the data; JUNO's sin^2 theta12 will decide it. If JUNO lands far below 0.341, the A4 Z2 is the wrong Majorana residual and TM1 (needs S4) is next.

Addendum before any code ran (2026-11-25): JUNO's first result, sin^2 theta12 = 0.3092 +- 0.0087 (Nature 2026), was found after this file was committed. P4 stays as registered (NuFIT 6.0 range); the pull against JUNO is reported as information alongside it.

## Scoring (2026-11-25)
Run 1 (t96_run1.log). All pass as registered.
- S1 PASS: 24 Hurwitz units, closed; 12 rotations (A4); Delta(27) has 27 elements.
- P1 PASS: A4's critical axes are exactly 7: 4 with stabiliser Z3, 3 with Z2.
- P2 PASS: Delta(27)'s critical lines are exactly 12 (stabiliser order 9), in 4 mutually unbiased bases.
- C1 PASS: two Delta(27) bases mix with |U|^2 = 1/3 everywhere (excluded by data, as expected): the Majorana Z2 is needed.
- P3 PASS: Z3 (Dirac) with A4's Z2 (Majorana) always gives a trimaximal column: TM2.
- P4 PASS as registered: TM2's sin^2 theta12 = 0.341 is inside NuFIT 6.0's 3-sigma range (pull +2.8 sigma).
- Information: against JUNO's first result (0.3092 +- 0.0087) TM2 is +3.6 sigma off. JUNO disfavours TM2. The TM2 curve at the measured theta13 spans sin^2 theta23 = 0.39-0.61, |J| up to 0.035.
Verdict: the PSR's critical directions and the residual-symmetry picture work as registered, but A4's Z2 as the Majorana residual is disfavoured by JUNO.
Post hoc (t96_posthoc.py, labelled; motivated by JUNO's pull): the grid's hand swap (Frobenius x -> x^3, phi -> 1 - phi on F9) is not in SL(2,3); adding it extends A4 (12) to S4 = PGL(2,3) (24), and it acts on P^1(F3) as a transposition. S4's new Z2 axes split in two: (1,1,0)-type gives a TM1 column (2/3, 1/6, 1/6), sin^2 theta12 = 0.318 (JUNO pull +1.0 sigma); (1,-1,0)-type gives a column with a zero (theta13 = 0, excluded). Which one the Majorana sector keeps needs a reason; that is t97's question, to be pre-registered.
