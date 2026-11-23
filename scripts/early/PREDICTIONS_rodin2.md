# Pre-registered before running rodin2.py (2026-11-12). Label: math.
Observation behind it (from rodin.py): mod 9 the grey wire {1,4,7} = units that are squares, brown {2,5,8} = non-squares, vacant = multiples of 3.
So Rodin's coil is the quadratic character (Legendre symbol) mod 3 laid out on slots. Generalise to every Fibonacci doll F(n)^2 with F(n) = p an odd prime:
coil wires = units mod p^2 that are squares / non-squares (decided by the residue mod p); vacant = multiples of p (roots of zero).
Q1 [identity]: shifts 3, 4, 5 of the counter-wound product give 8, 7, 5 = -1, -2, -4 mod 9: the negatives of shifts 0, 1, 2 (other side of the plate; 2^3 = -1).
Q2 [real test]: the Fibonacci word-sum multiplier r (words between zeros, mod p^2) reduces mod p to m = F(n+1) mod p, with m^2 = (-1)^n (Cassini).
Q3 [real test, the prediction]: the word sums alternate between the two wires (r a non-square mod p) exactly when
    n even and p = 3 mod 4 (m = -1 non-square), or n odd and p not = 1 mod 8 (m = +-i non-square).
    Fibonacci primes: F(4)=3 alternate; F(5)=5 alternate; F(7)=13 alternate; F(11)=89 (= 1 mod 8) NO, words stay on one wire;
    F(13)=233 (= 1 mod 8) NO; F(17)=1597 (= 5 mod 8) alternate.
Q4 [check]: for p = 5 the two-wire coil (wires = +-1 vs +-2 mod 5) carries the mod-25 word sums 7, 1, 18, 24 as 2 non-square / 2 square in alternation.
Control: a random non-Fibonacci recurrence x(n+1) = x(n) + 2x(n-1) gives no such systematic rule (report only).

# Scored after run (2026-11-12)
Q1 PASS: shifts 3, 4, 5 give 8, 7, 5 = -1, -2, -4.
Q2 PASS: word sums are geometric in every doll; r = F(n+1) mod p; r^2 = (-1)^n mod p (3, 5, 13, 89, 233, 1597).
Q3 PASS (all six, including both predicted failures): alternate for 3, 5, 13, 1597; one wire only (all non-square) for 89 and 233.
Q4 PASS: mod 25 word sums 7, 1, 18, 24 = non-square, square, non-square, square.
Control: x(n+1) = x(n) + 2x(n-1) multipliers are squares or not with no Cassini-type rule (1 at p = 5, 7, 13).
