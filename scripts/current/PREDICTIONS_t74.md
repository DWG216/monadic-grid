# t74 Why no low-degree reading beats the root: the meeting term against exclusion (pre-registered 2026-11-24, before any code is written or run)

Step (from §180): show why the meeting of object and reference cannot be read below the root.

Derivation [M, standard low-degree method, written on our terms]:
- A reading of degree D is a polynomial in the signed edges s_e = 2x_e - 1 of degree at most D. Its basis is the characters chi_H = product of s_e over an edge set H: each edge at most once (multilinear: exclusion).
- The best degree-D reading separates yes from no only if the low-degree norm ||L^{<=D}||^2 - 1 = sum over nonempty H with |H| <= D of (E_yes chi_H)^2 is large.
- Against a uniform background, E_yes chi_H = Pr[all vertices of H lie in the clique] = (k)_v/(n)_v, v = |V(H)|: one factor k/n per vertex for the object, squared for the meeting of the object with its conjugate.
- Exclusion counts placements: H uses v distinct vertices, about n^v placements. Each vertex then contributes n (k/n)^2 = k^2/n. The sum is small when k^2/n < 1 and large when k^2/n > 1: the root is where the meeting term per vertex equals the number of places it can sit.
- On one slice the edge count is fixed, which removes |H| = 1 (approximation used here: drop the one-edge term; the other characters are taken as on the full cube).

Computation: exact sum with a(v, e) = number of labelled graphs on v vertices with e edges and no isolated vertex (inclusion-exclusion), times C(n, v), times ((k)_v/(n)_v)^2. Threshold k*(n, D): smallest k with norm^2 - 1 >= 1.

S1 Sanity: a(v, e) reproduces the counts 1 (v=2, e=1), 3 and 1 (v=3, e=2 and 3), and the total over e of graphs on 4 labelled vertices without isolated vertex is 41.
S2 Sanity: with D = 1 (one-edge term only) the threshold is k* close to 2^(1/4) sqrt(n) for large n (within 5% at n = 10^6).
G1 [M] Root: for D = 2, 4, 6, 8 with the one-edge term removed (slice), k*/sqrt(n) stays within a factor 1.5 from n = 10^3 to 10^7.
G2 [M] Degree does not beat the root: at n = 10^6, k*/sqrt(n) for D = 8 is at least 0.5 (raising the degree from 2 to 8 does not push the threshold below half the root).
C1 Control: a hypothetical reading that counted each placement once without exclusion (repeated vertices allowed: n^e placements with weight (k/n)^(2e)) would give threshold scaling n^(1/2) per edge, but its sum diverges in e at fixed k; reported as information only.

Verdict: G1, G2 pass -> no reading of degree up to 8 sees a clique below about the root on one slice, and the reason is exact: the meeting term (k/n)^2 per vertex against n distinct places per vertex. What remains is the step from bounded-degree readings to every polynomial-time reading (the low-degree conjecture) and from average to worst case.

## Scoring (2026-11-24)
Run 1 (t74_run1.log). All pass.
- S1 PASS: counts 1, 3, 1 and 41. S2 PASS: one-edge threshold 1.190 sqrt(n) against 2^(1/4) = 1.189.
- G1 PASS: with the one-edge term removed, k*/sqrt(n) settles as n grows: D = 2: 1.08; D = 4: 0.85; D = 6: 0.76; D = 8: 0.69 (n = 10^3 to 10^7, each within 1.5).
- G2 PASS: D = 8 at n = 10^6 gives 0.689 sqrt(n), above half the root.
Post hoc (t74_posthoc.py, after the run, not scored): at n = 10^6 the threshold keeps falling slowly as D grows past log n: D = 12: 0.586, 16: 0.506, 20: 0.442, 24: 0.390. The root holds up to a slowly varying factor in the degree; a reading of degree comparable to k^2 is exhaustive search over the clique itself.
