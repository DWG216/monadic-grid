# Pre-registered before running susy.py (2026-11-14). Labels: S1-S4 math (known results re-derived); interpretation fixed in advance.
Question: does pairing the two monadic modes (bosonic: any number per state; fermionic: 0 or 1 per state, Book 6 "on and off switch")
give the positivity/balance the RH gap needs? Model: primon gas. States = integers n; primes = modes; bosonic count Z_B = zeta(b);
fermionic sign (-1)^F = Mobius mu(n) (0 if a prime repeats, else (-1)^number of primes).
S1 [pairing]: for every 1 < n <= 10^5, the operator Q = "toggle the smallest prime of n" pairs the squarefree divisors of n into
   even/odd pairs with no fixed points, so sum_{d|n} mu(d) = 0. Only n = 1 (the vacuum, no primes) is unpaired: Witten index = 1.
S2 [index]: zeta(b) * sum mu(n) n^-b = 1 to within 1e-5 at b = 2, 3 (truncation N = 10^6).
S3 [RH-equivalent quantity]: Mertens M(x) = sum_{n<=x} mu(n); max |M(x)|/sqrt(x) over 100 <= x <= 10^7 is below 0.6.
S4 [null controls]: fair random +-1 on squarefree n: max |S(x)|/sqrt(x) over 100..10^7 between 0.3 and 3 (balanced walk).
   Biased signs (P(+) = 0.51): S(10^7)/sqrt(10^7) > 10 (a bias, however small, shows up as linear growth).
Interpretation (fixed): S1-S2 = the two modes pair exactly and cancel to the single vacuum state (the PSR zero ground plus one unpaired 1).
S3-S4 = the fermionic signs cancel at the balanced rate, not with a bias. Known: RH <=> M(x) = O(x^(1/2+eps)) (Littlewood 1912).
So in grid terms RH = "the fermionic sign has no bias at any scale". Finite data cannot prove this. Note: the stronger |M(x)| < sqrt(x)
for all x (Mertens conjecture) is FALSE (Odlyzko-te Riele 1985), so the claim must be the x^(1/2+eps) rate, not a fixed bound of 1.

# Scored after run (2026-11-14)
S1 PASS: sum_{d|n} mu(d) = 0 for every 1 < n <= 10^5; "toggle the smallest prime" is a sign-flipping pairing with no fixed points (checked n <= 3000); n = 1 sums to 1. Witten index 1.
S2 PASS: zeta(b) * sum mu(n) n^-b = 1.00000000 at b = 2 and 3.
S3 PASS: max |M(x)|/sqrt(x) = 0.567 (at x = 199) over 100..10^7; M(10^7) = 1037 (matches the published value).
S4 PASS: fair random signs max 1.18; biased (0.51) S(10^7)/sqrt(10^7) = 38.1, linear growth. Mobius signs behave like the fair walk, not the biased one.
Caveat: all known results (Mobius inversion; Spector 1990 on supersymmetry and Mobius; Littlewood 1912). Finite range proves nothing about RH.
