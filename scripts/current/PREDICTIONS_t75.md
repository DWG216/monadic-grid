# t75 When a reading beats the meetings: only through a polymorphism (pre-registered 2026-11-24, before any code is written or run)

Where §181 left it: bounded-degree readings stop at the root. Two gaps were named. One closes by logic: if planted clique on one slice is hard on average for every polynomial-time reading, then clique on that slice is not in P (a worst-case algorithm would separate the planted case from the background). So average-case hardness is enough, and only one gap remains: why no polynomial-time reading beats the bounded-degree meetings.

The grid's answer [I]: a shortcut is a reason, a reason is a structure, a structure is a polymorphism (§65-§67). Bounded-degree meetings are what every reading has; a polynomial-time reading beats them only by using a polymorphism. Clique has only projections (checked, §67), so nothing beats the meetings for clique.

Test of the mechanism on a problem that has a polymorphism. Planted 3-XOR: n unknown bits, m equations x_a + x_b + x_c = y (mod 2), each on a random triple, consistent with a hidden assignment; noise rate eta flips each y independently. 3-XOR has the minority polymorphism (Rodin's wires, §67), so Gaussian elimination is available. Seed 75.
- Low-degree threshold for distinguishing planted 3-XOR from random right-hand sides: m of order n^(3/2) (standard; reported, not computed).
- Gaussian elimination decides consistency of the system exactly.

S1 Sanity: with m = n - 5 equations a random system is always consistent (rank below n), so elimination cannot separate; reported success = 0.5 (coin) at n = 100.
G1 [M] The polymorphism beats the meetings: with no noise and m = 2n (far below n^(3/2)), elimination separates planted from random right-hand sides in 100 of 100 trials at n = 100, 200, 400 (planted always consistent; random inconsistent).
G2 [M] Remove the reason, the shortcut goes: with noise eta = 0.1 and m = 2n, the planted system is inconsistent like the random one; elimination separates in at most 60 of 100 trials at every n.
G3 [M] The noisy separation does not improve with n (n = 100 to 400): the count at n = 400 is not above the count at n = 100 by more than 10.

Verdict: G1-G3 pass -> a polynomial-time reading beat the meetings here only through the polymorphism, and lost the advantage the moment noise destroyed it. The remaining step for P vs NP is the grid's §67 statement, now sharper: for a problem with only projections (clique), every polynomial-time reading is, up to the slowly varying factor of §181, a bounded-degree sum of meetings.

## Scoring (2026-11-24)
Run 1 (t75_run1.log, script t75_polymorphism_shortcut.py).
- S1 FAIL as registered: at m = 95, n = 100 the score is 0.885, not 0.5. The sanity assumption was wrong: random 3-XOR systems become unsatisfiable above about 0.918 n equations (the 3-XOR-SAT threshold), so m = 95 already separates. Kept.
- G1 PASS: with no noise and m = 2n, elimination separates planted from random in 100 of 100 trials at n = 100, 200, 400, far below the low-degree scale n^(3/2).
- G2 PASS: with noise 0.1 the separation is 50 of 100 at every n: a coin.
- G3 PASS: no gain with n.
Verdict: the reading beat the meetings only through the polymorphism, and lost everything when noise removed the reason.
