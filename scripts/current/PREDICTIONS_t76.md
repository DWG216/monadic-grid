# t76 The polymorphism is invisible to every meeting (pre-registered 2026-11-24, before any code is written or run)

Closure statement under test [S, §183]: a polynomial-time reading is a sum of meetings plus whatever the problem's polymorphisms allow; composing meetings in time manufactures no polymorphism. Its sharp consequence: the power a polymorphism gives cannot be reached by meetings of any bounded degree. Here, exactly, on planted 3-XOR (the minority polymorphism, t75).

Correction carried in (§183): the polymorphism statement of §67 is about 3-SAT (projections only); clique enters through the reduction between NP-complete problems, not through its own polymorphisms.

Model: m random 3-subsets of n variables (clauses), right-hand sides y planted (y_i = x_a + x_b + x_c for a hidden x) or uniform. A reading of degree D is a polynomial in the signs (-1)^{y_i} of degree at most D. Its best advantage is governed by the low-degree norm
||L^{<=D}||^2 - 1 = sum_{t=1}^{D} C(m, t) * N_t / C(n, 3)^t,
where N_t is the number of ordered t-tuples of 3-subsets whose symmetric difference is empty (the clauses form an even cover; only these have E_planted != 0). Exactly, by Fourier analysis on {0,1}^n:
N_t = 2^{-n} * sum_w C(n, w) * K(w)^t, with K(w) = sum_j (-1)^j C(w, j) C(n - w, 3 - j) (the Krawtchouk polynomial of degree 3).
Threshold m*(n, D): the smallest m with norm^2 - 1 >= 1.

S1 Sanity: N_1 = 0 and N_2 = C(n, 3) (two equal clauses) for n = 20, by the formula.
S2 Sanity: N_4 by the formula equals a direct count over all 4-tuples of 3-subsets for n = 7.
G1 [M] The meetings need n^{3/2}: for D = 2, 4, 6, 8, m*/n^{3/2} stays within a factor 1.5 from n = 100 to n = 2000.
G2 [M] The polymorphism is invisible to them: at n = 2000, m* for D = 8 is above 10 n, while elimination separates at m = 2n (t75, 100/100).

Verdict: G1 and G2 pass -> meetings of bounded degree reach planted 3-XOR only at n^{3/2}; the polymorphism reaches it at n; the gap grows as sqrt(n) and no bounded degree closes it. For 3-SAT (projections only) the closure statement leaves the meetings alone, which places random 3-SAT refutation at n^{3/2} (the known best polynomial algorithms stop exactly there; Feige's hypothesis covers the linear regime).

## Scoring (2026-11-24)
Run 1 (t76_run1.log, script t76_polymorphism_invisible.py).
- S1 PASS: N_1 = 0, N_2 = C(20, 3) = 1140. S2 PASS: N_4 = 23765 by the formula and by direct count (n = 7).
- G1 PASS: m*/n^(3/2) is constant in n for every degree: D = 2: 0.57-0.58; 4: 0.27; 6: 0.19; 8: 0.15-0.16 (n = 100 to 2000).
- G2 FAIL as registered: at n = 2000 and D = 8, m* = 13412 = 6.7 n, not above 10 n. The gap m*/n = 0.15 sqrt(n) grows as registered in kind but passes 10 only beyond n of about 4500; the registered size was too small. Kept.
Reading (after the run): Gaussian elimination is itself a reading of degree about n: it finds one linear dependency, a single even cover of size up to n, among exponentially many. The polymorphism is what lets a polynomial computation pick out one long meeting; bounded-degree readings can only sum the short ones, and need n^(3/2).
