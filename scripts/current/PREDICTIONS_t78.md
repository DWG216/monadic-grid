# t78 Mixed dolls: cheaper laws, no new laws (pre-registered 2026-11-24, before any code is written or run)

Step (§185): circuits can mix dolls (mod 2 and mod 3 in one computation), which a single-field certificate cannot. Does a mixture hear what no single doll hears?

Two kinds of mixing:
- Global mixing (a certificate valid as an identity): by the Chinese remainder theorem a certificate over Z6 is a pair of certificates over F2 and F3. Mixing gives nothing new [M, CRT].
- Pointwise mixing (a value is nonzero if it is nonzero mod 2 or mod 3): this is how composite-modulus circuits gain. Barrington, Beigel and Rudich (1994): OR has a weak representation over Z6 of degree about sqrt(n), while over a prime field it needs degree growing linearly in n.

The grid's reading [S]: OR is itself a law (the dual-Horn polymorphism, §67). Pointwise mixing of dolls makes a law cheaper to compute; it does not create a law the problem lacks. 3-SAT has only projections, so mixing has nothing to make cheaper.

Computation (exact, symmetric representations): a symmetric polynomial P = sum_{j=1}^{d} a_j C(w, j) over Z_m (w = number of ones) weakly represents OR_n if P = 0 at w = 0 (automatic) and P != 0 mod m for w = 1..n. Minimal degree d_m(n) by exhaustive search over a_j in Z_m, for m = 2, 3, 6 and n = 2..40.

S1 Sanity: d_2(n) for n = 1..8 matches the direct definition (checked by brute force over all subsets of coefficients) and d_m(1) = 1 for all m.
G1 [M] Single dolls are linear: d_2(n) >= n/2 and d_3(n) >= n/3 for every n tested... (prediction: d_p(n) grows at least linearly, slope at least 1/(p - 1) up to rounding: d_2(n) >= n/2, d_3(n) >= n/3).
G2 [M] The mixture beats both: d_6(n) < min(d_2(n), d_3(n)) for every n >= 12, and d_6(40) <= 2 sqrt(40) (about 12.6).

Verdict: G1, G2 pass -> pointwise mixing of dolls computes a law far more cheaply than any single doll; with §185 (global mixing adds nothing) the mixture's power is cheaper access to laws. The statement left for P vs NP: a law can be made cheaper by mixing dolls, never created; 3-SAT has none.

## Scoring (2026-11-24)
Run 1 (t78_run1.log; script kept as t78_mixed_dolls_run1.py) crashed before scoring: the exhaustive search stops at m^d > 2 million and returned None, which the scorer could not compare. Run 2 (t78_run2.log, script t78_mixed_dolls.py) records a stopped search as "degree at least d"; no threshold changed. All pass.
- S1 PASS: exhaustive search agrees with the direct definition for n = 1-8.
- G1 PASS: single dolls grow linearly: over F2, d = n for n up to 20 (search limit 21 beyond); over F3, d = 9 at n = 10 and 11 at n = 20 (limit 14 beyond).
- G2 PASS: over Z6, d = 3 at n = 12-24, 4 at n = 30-35, 5 at n = 40 (2 sqrt(40) = 12.6), below both single dolls at every n >= 12.
Reading: pointwise mixing of the mod-2 and mod-3 dolls computes OR, a law, at degree near sqrt(n) where each doll alone needs degree linear in n.
