# Pre-registered before running rodin.py (2026-11-12). Label: math (paper check, no experiment).
Source: Millington, Aether volume pp. 203-210 (Rodin coil), pp. 162-185 (MNS circuits).
Coil as he describes it: 36 slots; grey wire 1,16,31,10,25,4,19,34,13,28,7,22 (step +15 mod 36); brown = grey + 1; slots 3,6,...,36 vacant.

R1 [identity]: forward doubling cycle 1,2,4,8,7,5 (mod 9) times the reverse cycle shifted by s is constant 2^s:
    s = 0, 1, 2 give 1, 2, 4 (his three carrier states, p. 209-210); s = 3, 4, 5 give 8, 7, 5 (not stated by him).
R2 [real test]: mod 9 the coil splits into three classes: grey = {1,4,7}, brown = {2,5,8}, vacant = {0,3,6} (multiples of 3, his "roots of zero").
    The 2-operator swaps grey and brown and fixes the vacant class, so one doubling cycle alternates wires: 1g 2b 4g 8b 7g 5b.
R3 [real test]: the doubling cycle is the word sums of the Fibonacci forward strand mod 9 (words of 3 between zeros at multiples of 4):
    4, 8, 7, 5, 1, 2 (ratio 2); the reverse strand gives ratio 5 = 2^-1. (His supra-MNS table, p. 176.)
R4 [real test, generalisation]: word sums in MNS-F(n)^2 for n = 5, 6, 7. Prediction: geometric progressions with his multipliers
    (mod 25 ratio 7 or 18; mod 169 ratio 164 or 135). His mod-64 table looks additive (+8); prediction: n = 6 is additive, not geometric.
R5 [link to our identity]: the shift-2 coil carrier 4 equals L(x)L(-x) at every Fibonacci zero (formula-pair identity).
Controls: C1 a different multiplier (4 mod 9, order 3; 3 mod 7, order 6) also gives constant shifted products: R1 is a group fact, not special to Rodin.
          C2 other coil steps (7, 11, 13, 17 mod 36): R2's three-class structure needs gcd(step, 36) = 3 and step = 6 mod 9.

# Scored after run (2026-11-12)
R1 PASS: products constant 2^s for every shift: s=0..5 give 1, 2, 4, 8, 7, 5. His three carriers are shifts 0, 1, 2.
R2 PASS: grey = {1,4,7}, brown = {2,5,8}, vacant = {0,3,6} = slots 3, 6, ..., 36. Doubling swaps the wires and fixes the vacant class: 1g 2b 4g 8b 7g 5b.
R3 PASS: Fibonacci forward-strand word sums mod 9 = 4, 8, 7, 5, 1, 2 (ratio 2); reverse strand 2, 1, 5, 7, 8, 4 (ratio 5). Matches his p. 176 table.
R4 PASS: mod 25 ratio 18 forward, 7 reverse (7^2 = -1: words advance by quarter-turns); mod 64 additive (+8 forward, -8 reverse; word sums are not units);
   mod 169 ratio 164 forward, 135 reverse (order 52). All match his tables (pp. 176-184).
R5 PASS: L(x)L(-x) = 4 at every Fibonacci zero mod 9, 25, 64, 169.
C1: other multipliers also give constant shifted products (4 mod 9: 1, 4, 7; 3 mod 7: six constants). R1 is a general group fact.
C2: only steps with gcd(step, 36) = 3 (15, 21, 33) give the three-class coil; steps 7, 11, 13, 17 make one wire through all 36 slots.
Verdict: the coil's layout is the MNS-9 Fibonacci word-sum circuit (R2 + R3); the counter-wound carrier constants are its group structure (R1, generic).
