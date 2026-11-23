# Pre-registered before running yinyang.py (2026-11-16). Labels: math (known results re-derived); readings interpretive.
Millington: envelopes divide "converse orderly and chaotic behaviours ... much like the line separating Yin and Yang". In the symbol each half
holds a dot of the other. Grid version: order = laws inside dolls and the domain type (circle p = +-2 mod 5 / hyperbola p = +-1 mod 5);
chaos = the comma and the prime count across envelopes.
Y1 [separation]: the comma (section 31, D3) has the same distribution in circle and hyperbola primes (two-sample KS p > 0.01, 7 <= p <= 20000)
   and in each turn class (multiplier order 1, 2, 4; pairwise KS p > 0.01). Mean comma differs between circle and hyperbola by < 0.03.
   (Dot of chaos in order: the doll's own laws do not predict its comma.)
Y2 [dot of order in chaos]: the race D(x) = #circle primes - #hyperbola primes up to x is positive for > 90% of primes x in [100, 10^7]
   (Chebyshev bias). Reason fixed in advance: every prime square p^2 (the next doll down) is a residue, so the depth direction pushes about
   sqrt(x)/ln x into the hyperbola side of the weighted count, and the count of primes is pushed the other way. Normalised B(x) = D(x) ln x / sqrt(x)
   has mean in [0.5, 2.5] over log-spaced x in [1e4, 1e7].
Y3 [control]: race 1 vs 4 mod 5 (both hyperbola; prime squares split evenly between them): mean |B| < 0.3 and sign changes many times
   (fraction of positive x between 0.1 and 0.9).
Interpretation fixed: if all pass, the order/chaos split is clean (Y1), the chaos holds a small orderly bias whose source is the next doll
(Y2), and the bias vanishes when the classes share a domain type (Y3). The bias is governed by the golden L-function L(s, chi_5), whose value
L(1, chi_5) = 2 ln phi / sqrt 5 is already in the grid.

# Scored after run (2026-11-16)
Y1 PASS: circle vs hyperbola KS p = 0.337, mean diff -0.006 (1137 vs 1122 primes); turn classes 1/2/4 pairwise KS p = 0.106, 0.848, 0.399.
Y2 PASS: circle primes ahead at 100% of primes x in [100, 1e7]; normalised bias B mean 1.28 (range 0.44-2.02).
Y3 PASS (narrowly on |B|): 1 vs 4 mean |B| = 0.280 (< 0.3), positive 53.9% of the time, 6648 sign changes.
