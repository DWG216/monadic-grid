# Pre-registration (2026-11-22, 03:35), round 6, under the rules: positive control first, sanity run first
Data: zeros of Z(t) up to t = 600 by the same Riemann-Siegel code (341 zeros; Riemann-von Mangoldt main term 340.7). Taper 1 - gamma/600. Operator: Jacobi matrix J with these zeros as eigenvalues, read from its entries only (Chebyshev recurrence, t10/t11_lib). Nulls: 100 draws each (seed 20261122).

SANITY RUNS (before freezing):
- t11_sanity.py: 341 zeros found (202 below 400, where the earlier grid found 201: noted, not chased). Old peak detector with the sparse plant 1 + 2^-s + 3^-s was mixed (ln 3 below null; fake plant above null at ln 2), so the plant detector was changed (below). DISCLOSURE: this sanity run also computed the Mobius readout on the new zeros (full 18/18; top-left 85 rows 17/18; 170 rows 18/18). That result is therefore SEEN and is not a test here. The real tests below use a target not yet computed: the Liouville function.
- t11_sanity2.py (30 draws): plant detector D(u) = S_w(u) - S_uniform(u) (the zeros' own spectrum cancels): sparse plant 56.8 / 29.1 / 33.2 at ln 2 / ln 3 / ln 3/2 vs null 95th ~3; fake plant (1 + 2.37^-s + 3.71^-s) 0.74 / 0.04 / 0.25.

## P. Positive controls (gate: the L tests count only if P1-P3 pass)
P1 sparse plant w = |1 + 2^-s + 3^-s|^2 on the critical line: D peak above its null's 95th at ln 2, ln 3 and ln 3/2.
P2 fake sparse plant w = |1 + 2.37^-s + 3.71^-s|^2: D peak NOT above its null's 95th at any of the three.
P3 pipeline control, c = taper/rho through the operator (J from |c|, phases in f): all 10 prime-power jumps in 2..30 negative, median |jump| prime powers / others > 3. (Seen in the sanity run: 10/10, 4.44. A control is allowed to be seen.)

## L. Real: the Liouville function lambda(n) = (-1)^Omega(n), not yet computed on any data
Math [M]: sum lambda(n) n^-s = zeta(2s)/zeta(s); residues give e^(-u/2) L(e^u) = 1/zeta(1/2) + sum_rho e^(i gamma u) zeta(2 rho)/(rho zeta'(rho)) + small, so S(u) = sum 2 Re[taper c e^(i gamma u)] with c = zeta(2 rho)/(rho zeta'(rho)) should jump by lambda(n)/sqrt(n) at u = ln n for EVERY n (squares and all), unlike Mobius. zeta(2 rho) = zeta(1 + 2 i gamma) by Euler-Maclaurin (checked to 3e-5 at t = 600).
L1 [real] full operator: sign(jump(n)) = lambda(n) for >= 26 of the 29 n in 2..30; median of jump(n) sqrt(n) lambda(n) in [0.7, 1.0]; corr(|jump|, 1/sqrt n) > 0.9.
L2 [real] null, zero spacings shuffled (c kept by index): L1's sign count above the null's 95th, and L1's median above the null's 95th.
L3 [real] magnitudes only (J from |c|, read from e1, no phase vector): sign count NOT above the L2-type null's 95th (a positive spectral measure cannot carry the signs).
L4 [real] locality: top-left K x K block with the first K components of f. K = 170 (half): >= 26/29 signs. K = 85 (quarter): >= 22/29. (Expectation borrows the seen Mobius behaviour; if Liouville needs more rows, locality depends on the function, not only on the operator.)
L5 [exploratory] the same counts at K = 43, 128, 255, 341.

## Results (t11_controls.log, t11_liouville.log; 100 null draws)
Correction to the text above: there are 16 prime powers in 2..30, not 10; P3's rule ("all negative") is unchanged.
P1 PASS: sparse plant 56.75 / 29.14 / 33.19 vs null 95th 2.61 / 2.48 / 2.92.
P2 PASS: fake plant 0.74 / 0.04 / 0.25 vs 3.39 / 2.55 / 3.03.
P3 PASS: 16/16 prime-power jumps negative, ratio 4.44.
Gate open: the L tests count.
L1 PASS: 29/29 Liouville signs (every n in 2..30, squares included); median jump sqrt(n) lambda(n) = 0.900; corr(|jump|, 1/sqrt n) = 0.966. Per n: 0.71-1.13.
L2 PASS: shuffled-spacings null 95th: signs 26.0 (real 29), median 0.359 (real 0.900).
L3 PASS: magnitudes only 9/29 vs null 95th 14.0: the signs are not in a positive spectral measure.
L4 PASS: K = 170: 29/29; K = 85: 28/29.
L5 (exploratory): K = 43: 12/29 (median |J_K/J| 0.41); 85: 28 (0.64); 128: 29 (0.71); 170: 29 (0.91); 255: 29 (1.03); 341: 29 (1.00).
Note (exploratory, labelled): on 201 zeros the Mobius signs needed ~100 rows (15/18 at 50); on 341 zeros ~85 rows suffice for both Mobius (seen in sanity) and Liouville. The rows needed may be set by the frequency range read (n <= 30), not by the matrix size: a candidate test for the next round.
