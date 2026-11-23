# Pre-registered before running downtree.py (2026-11-16). Label: math (classical facts re-derived); reading interpretive.
Question: does the downward (mirror) tree resolve the infinities? Two cases: the Fibonacci strands (Millington's forward F(n) and reverse F(-n))
and the zeta function (upward Euler product over primes, downward side Re s < 0 reached by the mirror s -> 1-s).
T1 [upward tree]: U(x) = sum_{n>=1} F(n) x^n converges only for |x| < 1/phi; there it equals x/(1-x-x^2). Check at x = 0.3 (partial sums, 200 terms, to 1e-12).
T2 [downward tree]: D(x) = sum_{m>=0} F(-m) x^(-m) converges only for |x| > phi; there it equals -x/(1-x-x^2). Check at x = 3.
   The two regions do not overlap: between them is the golden annulus 1/phi <= |x| <= phi, where neither tree converges (each is a bad infinity there).
T3 [cancellation]: the continued upward and downward sums add to exactly 0 for every x off the two poles (x = 1/phi, x = -phi): check |U + D| < 1e-12 at
   20 random complex x. Reading: each tree's infinity is the other tree's finite side, and together the bilateral strand sums to zero.
T4 [zeta mirror]: completed Lambda(s) = pi^(-s/2) Gamma(s/2) zeta(s) satisfies Lambda(s) = Lambda(1-s): Lambda(2) = Lambda(-1) = pi/6 and Lambda(4) = Lambda(-3) = pi^2/90,
   using zeta(-1) = -1/12, zeta(-3) = 1/120 (Bernoulli). The downward values are fixed by the upward ones.
T5 [what remains]: Lambda has only two infinities, at s = 1 (residue +1) and s = 0 (residue -1): eps * Lambda(1+eps) -> 1 and eps * Lambda(eps) -> -1 as eps -> 0.
   Reading: the mirror cancels every infinity except the two ends, zero and the pole at 1 (the Hagedorn point beta = 1), matching R3.

# Scored after run (2026-11-16)
T1 PASS: upward series at x = 0.3 = 0.491803278688525 = closed form.
T2 PASS: downward series at x = 3 = 0.272727272727273 = -x/(1-x-x^2) = 3/11. (Upward partial sums at x = 1: 7, 88, 10945: divergent.)
T3 PASS but tautological as coded (D was defined as -U); the substance is T1 + T2: each series equals its own closed form in its own region, and
   those closed forms are negatives of each other, so the continued bilateral sum is 0.
T4 PASS: Lambda(2) = Lambda(-1) = pi/6; Lambda(4) = Lambda(-3) = pi^2/90.
T5 PASS: eps*Lambda(1+eps) -> 1 (0.99999); eps*Lambda(eps) -> -1 (-1.00001, via the mirror with zeta(1-eps) ~ -1/eps + gamma).
