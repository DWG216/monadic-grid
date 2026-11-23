# Pre-registered before running dolls.py (2026-11-16). Labels: math; readings interpretive.
Source: Millington, "Fibonacci Numbers & SpaceTime" (mill2): space-time "composed of different areas appearing to govern with different
physical laws, ... embedded within one another like a series of russian dolls ... separated by ... envelopes, dividing converse orderly and
chaotic behaviours"; the veil at n = 0 "separates bright orderly day from chaotic shrouded night"; Equation A (F(n)^2, never negative,
orderly) vs Equation B (F(n)F(-n), sign switching, "chaotic"); Resistive Space (like charges repel) vs Reactive Space (like attract, inner atom).
D1 [different laws per doll]: for a Fibonacci-prime doll p^2 (p = F(n)), the multiplier at the doll's first zero has order
   1 for p = 2 (mod 4), 2 for p = 3 (mod 9; the only even-index Fibonacci prime), 4 for p = 5, 13, 89, 233, 1597, 28657 (odd index).
   Reading: mod 9 is the unique half-turn (720-degree, spin-1/2) doll; all larger Fibonacci dolls are quarter-turn dolls.
D2 [orderly nesting in depth]: pi(p^k) = p^(k-1) pi(p) for k = 1..4 and every prime p < 500 (each envelope multiplies the clock by p).
D3 [chaotic across envelopes]: the comma c(p) = (F(alpha(p))/p mod p)/p over primes 7 <= p <= 20000 is consistent with uniform on [0,1)
   (KS p > 0.01) and |lag-1 correlation| < 0.05 between consecutive primes.
C1 [orderly control]: the domain type (circle if p = +-2 mod 5, hyperbola if p = +-1 mod 5) predicts whether pi(p) divides 2(p+1) (circle) or p-1
   (hyperbola) for 100% of primes 7..20000.
D4 [A vs B]: F(n)F(-n) = (-1)^(n+1) F(n)^2 for n = 1..60 (B is A with the fermionic sign).
Interpretation fixed: if all pass, Millington's dolls have exact arithmetic content: laws fixed within each doll (D1, D2, C1), drift that
looks random across the envelopes (D3), and his two equations are the two modes (D4).

# Scored after run (2026-11-16)
D1 PASS: doll 4 order 1; doll 9 order 2 (multiplier 8 = -1, first zero 12); dolls 25, 169, 7921, 54289, 2550409, 821223649 all order 4
   (first zeros 25, 91, 979, 3029, 27149, 659111; doll 169 multiplier 99 = -70, as recorded earlier).
D2 PASS: pi(p^k) = p^(k-1) pi(p) exactly for all 95 primes < 500 and k = 2, 3, 4 (285 checks). Method change before scoring: the first script
   iterated the sequence (about 1e11 steps for p^4) and was stopped; dolls2.py checks the same statement with fast matrix powers
   (M^e = I mod p^k and M^(e/q) != I for each prime q | e). Prediction unchanged.
D3 PASS: comma over 2259 primes 7..20000: KS p = 0.550, lag-1 r = -0.032, no zero comma (no WSS).
C1 PASS: 2259/2259.
D4 PASS: identity holds n = 1..60.
