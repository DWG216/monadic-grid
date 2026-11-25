# t122 Reflection: judging one's own perceptions (pre-registered 2026-11-25 after three sanity runs)
Model (t122_reflection.py): t120's world (M = 120, N = 64, T = 800, capacities log-uniform, climbing γ = 0.02); half the monads reflective. A reflective monad keeps a running memory of what it hears (mean m and variance v, τ = 100) and acts, in listening and in climbing, only on what its memory shows significant, m_k − 1 > 3 standard errors (effective samples τ·η²); the rest it hears as baseline 1. Lawful worlds κ = 0.2, lawless κ = 0.
Sanity history (all kept): memory alone with τ = 20 (t122_sanity_tau20.log) and τ = 100 (t122_sanity_tau100_memoryonly.log) reduced but did not stop the lawless climb (finite memory carries lasting biases that multiplication turns into fixation); judged memory (t122_sanity.log) separated the cases. The definition was chosen after those runs; the test is on fresh seeds.
Leibniz's reflection (Monadology §29–30): knowing one's own states, from which come reasoning and the knowledge of necessary truths. Here: a perception is acted on only after it is judged.
Test seeds 15000–15009:
P1 [M] Lawful: reflective monads all reach a = 0.5 (fraction ≥ 0.95) with attention on laws > 0.9.
P2 [M] Lawful: reflective median arrival ≤ 1.5× plain.
P3 [M] Lawless: reflective median final capacity < 0.15 (no climb) and median C < 0.03 (no fixation).
P4 [M] Lawless: plain median final capacity > 0.4 (they climb by fixation, as in t120).
P5 [M, blind] Lawless: fraction of (tick, frequency) judged significant after tick 200 < 0.01: reflection is rarely fooled.
Reading fixed in advance: reflection is what separates reason from fixation: a judging mind climbs only where there are laws, and in a lawless world stays clear instead of fixating.

## Scoring (2026-11-25), run 1 (t122_run1.log)
- P1 PASS: lawful, reflective monads all reach 0.5 (1.0), attention on laws 0.997.
- P2 PASS: arrival 211 against 175 ticks (1.21×).
- P3 PASS: lawless, reflective median final capacity 0.096 (they started at a median near 0.09) and C = 0.016 (= 1/N): no climb, no fixation.
- P4 PASS: lawless, plain monads climb to 0.93 by fixation (C = 0.34).
- P5 PASS (blind): lawless, nothing judged significant after tick 200 (fraction 0.0); in lawful worlds 11.6% of (tick, frequency) pairs are judged significant: the laws.
Verdict as fixed in advance: reflection separates reason from fixation: a judging mind climbs only where there are laws, and in a lawless world stays clear.
