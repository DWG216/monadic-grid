# t117 Do Leibniz's levels appear? (pre-registered 2026-11-25 after the sanity runs in t117_sanity.log, seeds 5000–5003)
Model (t117_levels.py): t116's dialectic, κ = 0.2, M = 200, N = 64, T = 400, each monad with capacity a_j log-uniform on [0.01, 1] setting its listening rate (0.1 a_j) and turning strength (κ a_j). Per monad: distinctness C_j and lawfulness L_j (attention share on laws).
Measure: the median log10 C in each capacity decile (log a from −2 to 0, 10 bins); steps between neighbouring deciles; sharpness = largest step / mean step. Levels mean a threshold: one capacity range where distinctness jumps.
Sanity (seen): laws formed in 2 of 4 seeds; with laws, sharpness 3.6 (seed 5000); without, 2.3 (seed 5001). Memory (top content kept over the last 100 ticks) was 1 for everyone, so it is dropped as uninformative.
Test seeds 6000–6009:
P1 [information] fraction of seeds that form laws (K ≥ 1).
P2 [M] Seeds with laws: median sharpness > 3 (a threshold: levels).
P3 [M] Seeds without laws: median sharpness < 3 (smooth: no levels).
P4 [M] Seeds with laws: monads above the steepest step have median L > 0.5; below it, median L < 0.3.
P5 [M] Seeds with laws: the second-largest step is < 0.6 of the largest (one threshold: two levels, not three).
Reading fixed in advance: if P2–P5 pass, the grid's dialectic gives two levels from a continuum of capacity: monads below the threshold stay diffuse (bare), those above become distinct on the laws (souls); levels exist only where laws exist. Leibniz's third level (reflection) is not in this model.
