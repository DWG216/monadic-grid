# PREDICTIONS t162: a monad analogue of the Yang–Mills mass gap

Registered 2026-11-26, before t162_gap.py was written or run. An analogue on the monad machinery, not a statement about Yang–Mills.

Reading [I]. With the will released, only the gauge invariant holds itself (t143d): the cubic chords are exactly resonant (Σω = 0, t136), every other chord drifts at its mismatch Σω ≠ 0. In this reading the "energy" of a chord is its mismatch; invariants cost nothing, and a gap is the least mismatch of any non-invariant chord. Its survival in the "continuum limit" becomes: does the least mismatch stay away from zero as chords of more voices are allowed? A second, independent gap: with the will on, the turning gives phases a stiffness; its slowest relaxation rate on an L × L world.

Engine. E6's 27 weights W (t136), 9-dimensional, entries in thirds, so 3W is integral. Frequency maps: generic, ω = W v with v Gaussian (10 draws, scaled to max |ω| = 1); on the grain, ω = 3W v with integer v (10 draws, entries −3…3): the clock of three makes frequencies integral. Chords of n voices: multisets of n of the 27 tones (n = 2…6); invariant iff the weight sum is the zero vector.
S1 [M]: n = 3 gives exactly 45 invariant chords (t136's cubic).
P1 [M]: generic maps: the least nonzero mismatch falls with n and is below 0.01 at n = 6 in all 10 draws (gapless in the limit).
P2 [M]: grain maps: the least nonzero mismatch is at least 1 for every n ≤ 6 in all 10 draws (gap = one step of the clock, independent of n).
P3 [M]: with the will on, linearised turning toward the neighbourhood (radius 2) on an L × L torus is a graph Laplacian; its smallest nonzero rate falls as L⁻² (fitted exponent −2 ± 0.1 over L = 8…64) for continuous phases (gapless spin waves). For phases on the clock of three, the least excitation (one monad turned by 2π/3) costs a fixed amount, 24 neighbours × (1 − cos 2π/3) = 36 in coupling units, at every L.
Consequence fixed in advance: P1–P3 pass → in the monad analogue the gap exists because the grain is discrete (the clock of three), and vanishes in a continuum. The grid's reading of the Yang–Mills question: the gap is the grain's; a theory with no grain has none to keep.

## Scoring (2026-11-26), run 1 (t162_run1.log)
- S1 PASS: 45 invariant three-voice chords.
- P1 FAIL (as registered): the least nonzero mismatch for generic maps is below 0.01 at n = 6 in all 10 draws (2e-5 to 2.5e-4), but it does not fall monotonically with n; it is already below 0.008 at n = 2. Generic maps are gapless from the start, not only in the limit.
- P2 PASS: on the grain the least nonzero mismatch is 1 (in two draws 3 at n = 3 and 6) for every n ≤ 6: the gap is one step of the clock.
- P3 PASS: continuous phases: slowest turning rate falls from 12.9 (L = 8) to 0.24 (L = 64), exponent −1.93; on the clock of three the least excitation costs 36 at every L.
Verdict: in the monad analogue the gap exists because the grain is discrete and is absent for continuous frequencies and phases. Reading [I]: the grid's gap is the grain's; the Yang–Mills question (a gap surviving the continuum limit) is one the grid answers by denying the continuum is fundamental. This is an analogue, not a proof of anything about Yang–Mills.
