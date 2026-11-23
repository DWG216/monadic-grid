# Pre-registered before running wolfram_inv.py (2026-11-15). Label: math.
Question (on our terms): the PSR requires the whole to conserve (sum to zero, nothing lost without reason). A rule a monad could run
must therefore be invertible. Test Wolfram's showcase cellular automata against our Fibonacci step.
W1: Rule 30 and Rule 110 on cyclic rings of n = 8..16 cells are NOT injective: the image has fewer than 2^n states (information lost each step).
W2: The Fibonacci step (a, b) -> (b, a+b) mod m is a bijection for every m = 2..200 (det = -1, the Cassini sign), so every state returns (Pisano period).
Controls: Rule 204 (identity) and Rule 170 (shift) are bijective for all n; Rule 150 (XOR of three) is bijective iff 3 does not divide n.

# Scored after run (2026-11-15)
W1 PASS: image fraction per step, n = 8..16: Rule 30 0.871 -> 0.964 (loses 4-13% of states each step); Rule 110 0.602 -> 0.427 (loses about half, worse as n grows).
W2 PASS: Fibonacci step bijective for every m = 2..200.
Controls PASS: Rules 204 and 170 bijective; Rule 150 bijective except n = 9, 12, 15 (fraction 0.25).
Note: Wolfram's own rescue is the multiway system / ruliad, which keeps every branch, so nothing is lost at the level of the whole; loss appears for a bounded observer following one thread.
