# PREDICTIONS t159: topology changes only where the record is not written

Registered 2026-11-26, before t159_topology.py was written or run.

Reading [S]. Within an Age the record is written tick by tick, each entry from the monad's own neighbourhood record. A change of neighbourhood (topology) while the record is being written would change the next entries with nothing in the record to cause it; sufficient reason excludes it. At a closing the record is not being written (no rest mass, no proper time, no ticks: t121), and monads are carried whole into new neighbourhoods (t134). Geroch (1967): in a smooth Lorentzian spacetime without closed timelike curves, spatial topology cannot change; the grid has none (§276), so change can happen only where proper time degenerates: the closings.

Engine. t134's monad dynamics with sufficient reason's η = 0 (t143c), L = 12, N = 64, T = 600, r = 2, will 0.2, seeds 59000–59009. Record entry per monad and tick: w at its attended tone. Variant M: neighbourhoods permuted at tick 300 of Age 1 (topology change while writing). Control 0: no permutation. Variant C: Age 1 complete, permutation at the closing, Age 2 run.
P1 [M]: in M, the mean change of a monad's record entry across tick 300 exceeds 10× the median tick-to-tick change over ticks 250–299 of the same run, in 10 of 10 seeds; in control 0 it does not exceed 2× in any seed.
P2 [M]: in M, the fraction of monads holding a law falls by more than half across tick 300 in at least 8 of 10 seeds.
P3 [M]: in C (change only at the closing) the world still reaches one law held completely (completeness > 0.9) by the end of Age 2 in at least 8 of 10 seeds (t134's result, with η = 0).
Consequence fixed in advance: P1–P3 pass → topology changes are uncaused jumps in a record being written, and harmless at closings; with Geroch, the grid allows topology change only between Ages.

## Scoring (2026-11-26), run 1 (t159_run1.log)
- P1 FAIL (9 of 10, registered 10 of 10): a mid-Age change of neighbourhoods jumps the record entries 520× to 3.5×10⁵× the natural tick-to-tick change in 9 seeds; control 0.05–1.79×. Seed 59002 had reached one law held by every monad before tick 300, and the change left the record unchanged (jump 0): where every neighbourhood already agrees, a topology change writes nothing different.
- P2 PASS: laws held fall from 0.54–0.81 to 0–0.19 across the change in 9 of 9 unsettled seeds (59002: 1.0 → 1.0).
- P3 PASS: with the change only at the closing, every seed completes Age 2 at completeness 1.0 (Age 1: 0.60–1.0).
Verdict: a topology change while the record is written is an uncaused jump in it, except in a world already at unison, where it changes nothing; at closings it is harmless. With Geroch: topology changes only between Ages, or where it makes no difference to the record.
