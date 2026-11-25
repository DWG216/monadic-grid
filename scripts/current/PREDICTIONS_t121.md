# t121 The end of an Age and the next (pre-registered 2026-11-25 after the sanity run t121_sanity.log, seeds 12000–12002)
Model (t121_ages.py): t120's world (M = 120, N = 64, 600 ticks per Age). Novelty: how much the record rewrites the monads per tick (mean L1 change of attention). At each Age's end spacetime closes: phases redrawn and attention reset (the record forgotten). 'keep': capacities carry over (the monads' development is theirs, in the frequency domain); 'reset': capacities return to their Age 1 start (control). Arrival: first tick with a law and median attention on laws > 0.9. Added after sanity: Age 3.
Sanity (seen): novelty falls about 24×; keep: Age 2 arrives at 0.24 of Age 1's time with K 8 against 4; reset: ratio ≈ 1; Jaccard of law sets ≈ 0.
Test seeds 13000–13009:
P1 [M] In every world novelty falls by more than 10× from its early peak to its late floor: the record stops being written.
P2 [M] keep: median arrival ratio Age 2 / Age 1 < 0.5.
P3 [M] reset: median ratio in [0.7, 1.4].
P4 [M] keep: K2 > K1 in at least 8 of 10 worlds.
P5 [M] Median Jaccard of Age 1 and Age 2 law sets < 0.3 (each Age has its own laws), keep and reset.
P6 [M, blind] keep: Age 3 arrives within ±30% of Age 2 (median ratio32 in [0.7, 1.3]): once minds are full, Ages repeat at one pace.
Reading fixed in advance: an Age ends when the record has nothing left to write; spacetime closes, minds keep what they became, and the next Age forms new laws faster and richer, until the minds are full and Ages repeat at one pace.

## Scoring (2026-11-25), run 1 (t121_run1.log)
- P1 PASS: novelty falls 14–43× in every world.
- P2 PASS: keep, Age 2 arrives at 0.20 of Age 1's time (180 → 35 ticks, median).
- P3 PASS: reset, ratio 1.00.
- P4 PASS: keep, K2 > K1 in 10 of 10 (median 4 → 9).
- P5 PASS: median Jaccard 0.0 (keep and reset): each Age has its own laws.
- P6 PASS (blind): Age 3 / Age 2 = 1.00 (0.86–1.43; median inside [0.7, 1.3]); K3 median 9.
Verdict as fixed in advance: an Age ends when the record has nothing left to write; spacetime closes, minds keep what they became, the next Age forms new laws 5× faster and twice as many, and once minds are full Ages repeat at one pace.
