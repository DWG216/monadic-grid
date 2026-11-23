# Pre-registered before running golden_walk.py (2026-11-08)
Candidate algorithm: "golden-walk design generator". Alternate a FREE uniformly random element of a finite group C (frame) with ONE
expensive gate tau. After k expensive gates the single-qubit unitary is close to Haar-random (an approximate t-design). The
convergence factor per expensive gate in spin-j is the largest |eigenvalue| of P_C D_j(tau) P_C on the C-invariant subspace
(P_C = average of D_j over C), j = 1..60, PU(2) (integer j).

G1 [theorem check, Parzanchevski-Sarnak]: C = 2I (60 rotations), tau = tau60: every eigenvalue has |lambda| in
   {1/sqrt(59) = 0.1302, 1/59 = 0.0169} (tolerance 1e-6). If not, our operator is not their T-operator and we say so.
G2 [prediction, exploratory]: C = Clifford (24 rotations), tau = standard T (pi/8): max |lambda| ~ 1/sqrt(2) = 0.707.
G3 [consequence]: expensive gates needed for a fixed accuracy scale as 1/ln(1/lambda); ratio Clifford+T / icosahedral+tau60
   ~ ln(sqrt59)/ln(sqrt2) = log2(59) = 5.88, matching Blackman-Stier's navigation ratio.
G4 [comparison]: Fibonacci braids (no free frame, every gate costs the same): 0.964 per gate from the previous run, i.e. ~55
   braids per factor-e^2 reduction vs ONE tau60 for a factor 1/0.13 = 7.7.
Control: tau inside C (tau = an element of C) -> eigenvalue 1 (no mixing).

# Scored after run 1 (2026-11-08)
G1 FAILED as stated: eigenvalues are spread (0.006 ... 0.237), not the set {0.1302, 0.0169}. Our operator is not their T-operator.
G2 FAILED: Clifford+T max |lambda| = 0.9406, not 0.707.
G3 FAILED: ratio 23.5, not 5.88.
Control PASS: tau inside C -> 1.000.
POST-HOC pattern (NOT a result yet): icosahedral 0.2372 <= 2*sqrt(59)/60 = 0.2561 (60-branch Ramanujan bound); Clifford+T 0.9406 <= 2*sqrt(2)/3 = 0.9428
(3-branch bound, consistent with T-count growth ~2^t).

# Pre-registered BEFORE run 2: out-of-sample test of the post-hoc law on three other Parzanchevski-Sarnak sets
Law: alternating walk (free C, then T) has max |lambda| <= 2 sqrt(q)/(q+1) with q = |C| - 1 (super-golden sets), and within 10% below it.
 Pauli C4 + T4 = [[1,1-i],[1+i,-1]]/sqrt3            : q=3,  bound 0.8660
 Hurwitz C12 (tetrahedral) + T12 = [[3,1-i],[1+i,-3]]/sqrt11 : q=11, bound 0.5528
 Clifford C24 + T24 (PS matrix)                      : q=23, bound 0.3997
Pass = all three in [0.9*bound, bound]. Frame risk stated in advance: if PS's groups sit in a different frame than ours, the test can fail
for that reason; we report it either way.

# Scored after run 2 (2026-11-08)
PASS 3/3: Pauli C4+T4 0.8593 (bound 0.8660, ratio 0.992); Hurwitz C12+T12 0.5314 (0.5528, 0.961); Clifford C24+T24 0.3823 (0.3997, 0.957).
Status: the law "alternating walk spectral radius <= 2 sqrt(q)/(q+1), q = |C|-1" survived an out-of-sample test. It is the walk form of the
Parzanchevski-Sarnak Ramanujan property (known mathematics), checked numerically for j <= 40/60, not proved here.
Design cost to 1e-10 (all j <= 60): icosahedral+tau60 17 expensive gates; Clifford+standard T 377; Fibonacci 629 braids.
