# Pre-registered before running tau60_braid.py (2026-11-12). Label: math.
Question: can the fluid level-8 theory (SU(2)_8, 4 spin-1/2 strands) build tau60 by braiding alone, with no injected magic?
Setup: qubit = 3 strands with total charge 1/2 (basis: first pair fuses to 0 or 1); 4th strand an ancilla; 4-strand total charge 1.
That sector is 3-dim: qubit (2) + one leakage state (first three strands fuse to 3/2).
Cost unit: s3-syllables (s3^k, k any power): the analogue of T-count. Frame braids (s1, s2) are free, as Cliffords are.
Target: tau60 on the qubit (up to phase, any phase on the leakage state), i.e. any element of the double coset 2I.tau.2I (the ends are free).
Error: e = min over phases of ||U - diag(e^{ib}C, e^{ia})||_F / sqrt2  (includes leakage).

B1 [identity]: in this sector s1, s2 are block-diagonal; on the qubit they generate 2I (60 rotations projectively); s3 couples |1> to leakage.
B2 [math, proof]: NO finite braid equals tau60, even up to phase. Reason: every braid matrix entry is an S-integer, S = primes above 2 and 5
   (Kauffman A is a root of unity; F-move entries are square roots of ratios of q-integers [n], whose norms involve only 2 and 5),
   whereas some entry of every element of 2I.tau.2I has |entry|^2 with the prime of norm 59 (7+5phi) in its denominator.
   Numeric check: norms of [1..9] at q = e^{i pi/10} are products of 2s and 5s only (and +-1).
B3 [real test]: approximate synthesis converges. Best error: m=1 syllable > 0.1 (leaks); m=2 < 0.1; m=3 (partial search) below m=2;
   decay factor per syllable between 0.15 and 0.5 (volume law for a 7-dim target space predicts about (19*600)^(-1/7) = 0.26).
B4 [comparison, conditional]: extrapolated syllables for e = 1e-10 is under 40, versus 1.9e5 raw tau60 states per rotation by distillation.
   Assumes ideal topological protection and an efficient synthesis algorithm (not built; we only search).
Controls: C1 a 2I element is reached exactly at m=0. C2 three random SU(2) targets: same error scaling as tau60 (tau60 not special for braids).
Interpretation fixed in advance (if B2-B4 hold): the fluid medium approaches tau60 as closely as wanted and cheaply, but can never reach it;
tau60 lives at the prime 59, which no braid touches.

# Scored after run (2026-11-12)
B1 PASS: sector unitary 1e-15; s1,s2 block-diagonal (leak coupling 0); qubit frame = 2I (60 projective, 600 with leakage phases); s3 couples |1>-leak 0.924.
   s3 has projective order 5 (only 4 useful powers), not the ~19 assumed in the volume estimate.
B2 PASS (proof; numeric support): q-integer norms 1, 25, 256 only (primes 2, 5); |tr(tau60 k)|^2 = 4(2+phi)^2/(7+5phi) = 3.4699, norm of 7+5phi = 59.
   No finite braid equals tau60, even up to phase. In grid terms: 2 inert (circle), 5 ramified (lines), 59 split (hyperbola).
B3 FAILED AS STATED at m=2 (0.166, not < 0.1). Exhaustive best errors: m=0 0.277, m=1 0.605 (leaks), m=2 0.166, m=3 0.103.
   Decay per syllable m=2 -> 3: 0.62 (outside the 0.15-0.5 band; fewer s3 powers than assumed).
B4 NOT SCORED: meet-in-the-middle search for m=4 too slow on this machine; stopped. Extrapolation not attempted.
C1 PASS: 2I element reached exactly at m=0.
C2 PASS: random targets track tau60 (m=2: 0.15-0.25; m=3 random 0.085 vs tau60 0.103). tau60 is not special for braids.
Verdict: the conclusion rests on B2 (logic): the fluid approaches tau60 without limit but never reaches it. Cost unmeasured beyond m=3.
