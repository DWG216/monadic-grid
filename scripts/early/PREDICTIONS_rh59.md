# Pre-registered before running rh59.py (2026-11-12). Label: math.
Aim: take the proven 59-domain case (golden gates) and locate exactly where its proof stops working for all primes at once.
Construction: icosians (2I) and tau60 = (0,1,1,2+phi) (norm 7+5phi, a prime of norm 59) reduced mod a prime q = +-1 mod 5
(so phi exists mod q), giving matrices in PGL2(F_q). Graph: vertices = cosets g.A5 (A5 = image of 2I); neighbours of g.A5 are
g.u.tau.A5 for the 60 elements u of A5. This is the Hecke operator of the 59 domain on a finite quotient of the 59-adic tree.
H1 [real test of a theorem]: the graph is 60-regular and every nontrivial eigenvalue (not +-60) satisfies |lambda| <= 2 sqrt59 = 15.36
   (Ramanujan = the graph's Riemann hypothesis), for q = 11, 19, 29, 31, 41.
H2 [control]: random 60-regular multigraphs of the same sizes: max nontrivial |lambda| sits near 2 sqrt59 and exceeds it in some samples.
H3 [the local-to-global break, real test]: each local Euler factor (1 - p^-s)^-1 has no zeros. At the first zeta zero s = 1/2 + 14.1347i the
   partial Euler products over p <= P (P = 10 .. 10^6) do not tend to 0: their absolute value stays of order 1 or grows, never below 0.1.
   At s = 2 they converge to zeta(2) = pi^2/6.
H4 [graph side contrast]: for the q = 11 graph, the count of closed non-backtracking walks of length L matches the eigenvalue formula
   (Ihara-Bass), so infinitely many graph "primes" are summarised by finitely many eigenvalues.

# Scored after run (2026-11-12)
H1 PASS: q = 11, 19, 29, 31 (22, 114, 406, 496 vertices): 60-regular, symmetric, bipartite (+-60 trivial); max nontrivial |lambda| = 6.0, 12.0, 9.05, 12.71, all <= 15.36. (q = 41 not run.)
H2 PASS: random 60-regular multigraphs: mean max |lambda| 15.2-15.35, exceeding 15.36 in 10, 6, 7, 3 of 20 samples. Arithmetic graphs sit well inside the bound.
H3 FAILED AS STATED: partial Euler products at the first zero do dip below 0.1 (0.215, 0.115, 0.061, 0.023, 0.013 for P = 10..1e5), then swing wildly
   (0.417 at 1e6; 2.8e4 at 1e7; minimum 1e-7). They do not converge on the critical line. Averaged (geometric mean over primes 1e6-1e7):
   0.036 and 0.027 at the first two zeros versus 3.43 at non-zero height t = 17. The zero shows up only in a global average, in no finite product.
   At s = 2 the products converge to pi^2/6 as predicted.
H4 PASS: q = 11 graph, 1320 directed edges: every nontrivial Hashimoto eigenvalue has |mu| = sqrt59 exactly (40 of them; 1278 at |mu| = 1, 2 at 59);
   Ihara-Bass determinant identity holds to 6 decimals; closed non-backtracking walk counts for L = 1..6 match the eigenvalue formula exactly.
