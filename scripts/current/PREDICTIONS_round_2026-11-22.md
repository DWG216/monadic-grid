# Pre-registration (2026-11-22, 01:35): three tests proposed in §58
## A. Zero-gated switching (§33): do kicks delivered at each oscillator's own zero (its gate) bring agreement, where the same kicks at random phases do not?
Model: Mirollo-Strogatz pulse-coupled oscillators. N = 50, state x = ln(1 + (e^b - 1) phase)/b with b = 3, kick eps = 0.03 to every other oscillator, natural rates 1 + 0.002 * normal (seeded), random initial phases, 20 seeds (20261122 + k), horizon 3000 cycles.
GATED: an oscillator kicks the others when it reaches phase 1 (its zero); kicked oscillators pushed to 1 fire at once (absorption).
UNGATED (null): identical kicks and counts, but each oscillator kicks at a fresh uniformly random phase of its cycle; resets at phase 1 carry no kick.
A1 [real] GATED reaches full agreement (all 50 within 0.01 in phase) in >= 18 of 20 seeds.
A2 [real] UNGATED reaches it in <= 2 of 20 seeds.
A3 [real] final order parameter r: GATED median > 0.99, UNGATED median < 0.5.
## B. Sharper mirror pair (§29): with the zeros now on the line by theorem, the residual of the prime staircase at the 201 zeros below t = 400 must shrink as primes are added, with no persistent offset.
B1 RMS strictly decreases along X = 10, 100, 1000, 10^4, 3*10^4 (same taper and code as mirror_pair.py).
B2 RMS(10^4) < 0.028 (the X = 1000 value) and RMS(3*10^4) < RMS(10^4).
B3 |mean residual| at X = 3*10^4 < 0.01 and smaller than at X = 10.
B4 null: fake primes at X = 10^4 give RMS above the smooth-only value 0.230.
## C. Golden Artin, exploratory (no theorem yet; GRH for Kummer fields needed for a proof)
Share of primes 7 <= p < 2*10^6 (p != 5) whose Fibonacci clock is maximal (pi(p) = p - 1 for p = +-1 mod 5; pi(p) = 2(p + 1) for p = +-2 mod 5).
C1 [weak] the share lies in [0.20, 0.45] and differs by < 0.01 between the halves [7, 10^6) and [10^6, 2*10^6).
C2 [descriptive] split and inert shares reported separately.

## Results
A1 pass (20/20), A2 pass (1/20), A3 pass in direction (GATED median r = 1.000; UNGATED median r = 0.627, not < 0.5: FAIL on the 0.5 threshold). Design flaw found: at the pre-registered eps = 0.03, eps*N = 1.5, so the first firing cascades and absorbs everyone (gated median time to agreement 0.0 cycles): the gated pass is trivial at that coupling.
Post hoc (labelled; eps = 0.003, eps*N = 0.15, everything else unchanged): GATED agrees in 20/20, median 7.5 cycles; UNGATED in 0/20 over 3000 cycles, median final r = 0.371. The same kicks, at the same rate, synchronise only when they are delivered at each oscillator's zero.
B1 pass: RMS 0.1142, 0.0439, 0.0280, 0.0220, 0.0198 for X = 10 .. 3*10^4 (smooth-only 0.2302). B2 pass. B3 pass: mean residual -0.0005 at X = 10, +0.0000 at 3*10^4. B4 pass: fake primes 0.3462 (worse than no primes). Note: the RMS floor near 0.02 is consistent with our first-order Riemann-Siegel zeros and the taper; not tested.
C1 FAIL: share of maximal Fibonacci clocks = 0.660, outside the predicted [0.20, 0.45] (my range came from Artin's constant for a primitive root, the wrong model: pi(p) is the lcm of the orders of phi and -1/phi, which is maximal more often than phi is primitive). Stability passes: halves 0.6603 / 0.6598. C2: split 39,655/74,408 = 0.533; inert 58,644/74,522 = 0.787. Brute-force check of 10 small primes agrees.
