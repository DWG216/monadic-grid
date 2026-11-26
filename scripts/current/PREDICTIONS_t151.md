# PREDICTIONS t151: does the grain pick a frame?

Registered 2026-11-26, before t151_boost_diamonds.py was written or run.

Question. Diffeomorphism invariance on the grain means (i) the record depends only on causal order and count, not on labels, and (ii) the grain has no rest frame. Jacobson's route (t29) gives a covariant Einstein equation only if the area density of record cells is the same on every local cone at every boost. Test (ii) in 1+1 Minkowski: count grain points and the longest chain (the record's clock between two events) in causal diamonds of fixed volume, boosted by rapidity η = 0…5.
Prior work: Bombelli, Henson and Sorkin (2009): no Lorentz-invariant way to pick links from a Poisson sprinkling with finite valency, and sprinklings are the Lorentz-invariant discretisation; Bombelli, Lee, Meyer, Sorkin (1987).

Grains (density 1 per unit of u-v area, u = t − x, v = t + x): A regular lattice (the F9 grain laid out as a fixed array); B jittered lattice (each lattice point moved uniformly within its cell); C Poisson sprinkling. Diamonds: Δu Δv = 50 (expected count 50), Δu = √50 e^η, random placement; 3000 diamonds per (grain, η).

S1 [sanity]: mean count 50 within 3% for every grain at every η (random placement preserves the mean).
P1 [M]: lattice A fails frame-independence: Var(count) at η = 5 exceeds 10 × Var at η = 0.
P2 [M]: jittered lattice B fails: Var(count) at η = 0 is below 0.5 × mean (sub-Poisson), and at η = 5 within 20% of the mean: the variance changes with boost by more than a factor 2.
P3 [M]: Poisson C passes: Var/mean within 10% of 1 and mean longest chain within 5% of its η = 0 value at every η.
P4 [M]: mean longest chain differs from its η = 0 value by more than 20% at η = 5 for A and for B.
Reading fixed in advance [I]: if P1–P4 pass, the grain cannot be a fixed array in spacetime: the F9 grain is algebraic (the arithmetic each cell carries), and the cells' placement is a sprinkling. Labels: (i) holds by construction (the past-count is a function of the order alone, §276); (ii) holds only for C.

## Scoring (2026-11-26), run 1 (t151_run1.log)
- S1 FAIL on threshold: every mean within 3% of 50 except the regular lattice at η = 3, 4, 5 (51.8, 49.8, 47.2). Diagnosis: the lattice's count variance at high boost is 4.7e3–4.7e4, so the standard error of the mean over 3000 diamonds is 1.2–4.0; the deviations are 1.4, −0.1 and −0.7 standard errors. The threshold did not allow for the variance it was meant to expose. Kept as a fail.
- P1 PASS: lattice variance 6.6 at η = 0, 47,328 at η = 5.
- P2 PASS: jittered lattice Var/mean 0.09 at η = 0, 0.97 at η = 5.
- P3 PASS: Poisson Var/mean 0.98–1.03 and mean longest chain 11.25–11.31 at every η.
- P4 FAIL: the regular lattice's chain jumps (13.1 to 47.2), but the jittered lattice's chain moves only 5.6% (10.7 to 11.3), under the 20% registered. The jittered lattice keeps the clock nearly frame-free while failing on counts (P2).
Verdict: only the sprinkling passes both counts and chains at every boost. The grain cannot be a fixed array; the F9 structure is what each cell carries, and the cells' placement is a sprinkling (Bombelli, Henson and Sorkin 2009). Relabeling invariance holds by construction (§276).
