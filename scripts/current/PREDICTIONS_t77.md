# t77 A long meeting is selected only in the polymorphism's own doll (pre-registered 2026-11-24, before any code is written or run)

Step (§184): show that with only projections no sequence of meetings selects one long meeting. The grid's §67 lesson (Smolensky): a clock at prime p cannot hear prime q. A polymorphism lives in one domain, a doll; a long meeting is selected only by arithmetic in that doll. With only projections no doll is favoured, so none selects.

Measure: the Nullstellensatz degree of an unsatisfiable system over a field F: the least d such that polynomials g_i with deg(g_i f_i) <= d give sum g_i f_i = 1 in the multilinear ring (x^2 = x). Degree 1 means a linear certificate, the single long meeting elimination finds; high degree means only sums of short meetings remain.
- 3-XOR clause x_a + x_b + x_c = b: over F2 the polynomial x_a + x_b + x_c + b (degree 1, the minority polymorphism's own doll); over F3 the multilinear form of parity minus b (degree 3).
- 3-SAT clause: the product of (1 - literal) over its three literals (degree 3), over both fields.
Instances: random, checked unsatisfiable by brute force. 3-XOR with m = 2n clauses; 3-SAT with m = 10n. n = 7, 8, 9; 5 instances each; seed 77.

S1 Sanity: the degree found for one 3-XOR instance over F2 is 1, and a certificate of that degree is verified by multiplying out.
S2 Sanity: a satisfiable system never yields a certificate at any degree (one instance, n = 7, both fields).
P1 [M] 3-XOR over F2: degree 1 for every instance.
P2 [M] 3-XOR over F3: degree at least 3 for every instance, and its mean does not fall from n = 7 to 9.
P3 [M] 3-SAT over F2 and over F3: degree at least 3 for every instance, mean not falling with n.
P4 [M] Doll mismatch: at n = 9 the mean F3 degree of 3-XOR exceeds its F2 degree by at least 2.

Verdict: P1-P4 pass -> the long meeting exists as a certificate only in the polymorphism's doll; in another doll, and for a problem with only projections in every doll, only short meetings remain. Small n shows the pattern, not the asymptotics; the asymptotic statements are known theorems (Polynomial Calculus lower bounds over fields of the wrong characteristic for XOR systems, and over every field for random 3-SAT).

## Scoring (2026-11-24)
Run 1 (t77_run1.log, script t77_doll_mismatch.py). All pass.
- S1 PASS: degree 1 for 3-XOR over F2. S2 PASS: a satisfiable system has no certificate at any degree, over F2 and F3.
- P1 PASS: 3-XOR over F2 has degree 1 in all 15 instances: the single long meeting, a linear certificate.
- P2 PASS: 3-XOR over F3 has degree 3 to 5 (mean 3.4 at n = 7, 8 and 9).
- P3 PASS: 3-SAT has degree 3 to 4 over both fields (means 3.6, 3.4, 4.0 for n = 7, 8, 9), identical over F2 and F3.
- P4 PASS: at n = 9 the F3 degree of 3-XOR exceeds its F2 degree by 2.4.
Reading: the long meeting exists as a certificate only in the polymorphism's doll (F2 for the minority polymorphism). In F3 the same system needs high degree; 3-SAT, with only projections, needs high degree in both, with no doll preferred. Small n shows the pattern; the asymptotic statements are theorems: Buss, Grigoriev, Impagliazzo and Pitassi (2001) for XOR systems over the wrong characteristic, Ben-Sasson and Impagliazzo for random 3-CNF over every field.
