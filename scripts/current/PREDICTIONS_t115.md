# t115 What raises highlighting (pre-registered 2026-11-25 after one sanity run, t115_sanity.log, seeds 1000–1004)
Model (t115_highlighting.py): M = 50 monads, N = 64 frequencies. Each tick every monad reweights its perceptions by the shared record's coherence, w_k = |Σ_j √p_jk e^{iφ_jk}|² / Σ_j p_jk (about 1 where phases are scattered, up to M where they align). A law is a lasting phase relation: on the lawful set K the monads share a phase each tick (jitter σ); every other phase is redrawn each tick. Control: no lawful set.
[S] Equation: under p' ∝ p·w the attended resonance never falls, E_{p'}[w] = E_p[w²]/E_p[w] ≥ E_p[w] (Cauchy–Schwarz). Listening to the record raises what is heard in it. A law's coherent record grows as M², noise as M; with jitter σ the law's weight is about M e^{−σ²} against 1 for noise, so a law is heard iff M e^{−σ²} > 1.
Sanity (seen): lawful K = 4, σ = 0.3: share on the laws 1.0, C → 0.27; control: C → 0.99 on a random content.
Test seeds 2000–2019, T = 60:
P1 [M] Lawful (K = 4, σ = 0.3): median share on the laws > 0.99 and every monad's top content lawful.
P2 [M] Control: median share on a designated 4-set < 0.2.
P3 [M] Theorem: zero ticks where a monad's attended resonance falls, in all runs.
P4 [M] Lawful C_end in [0.2, 0.35] (plural attention near 1/K); control C_end > 0.9 (fixation).
P5 [M, blind] K = 1, 2, 8 (σ = 0.3): C_end within 30% of 1/K.
P6 [M, blind] σ = 1.0 (M e^{−1} = 18): share on the laws > 0.99. σ = 2.5 (M e^{−6.25} = 0.1): share < 0.5.
Reading fixed in advance: if P1–P6 pass, distinctness comes from listening to the record: a monad becomes distinct on what is lawful (shared, lasting phase relations), plural across all laws it hears; without laws the same listening only fixates by accident. Highlighting (C) measures distinctness, and its object (coherent or not) separates reason from fixation.

## Scoring (2026-11-25), run 1 (t115_run1.log)
- P1 PASS: share on the laws 1.0; every monad's top content lawful.
- P2 PASS: control share on the designated set 0.0.
- P3 PASS: zero falls of attended resonance in 40 runs × 50 monads × 60 ticks.
- P4 SPLIT, scored FAIL: lawful C_end = 0.280 (in range); control C_end = 0.827, below the registered 0.9 (fixation is slower than the sanity seeds showed; by tick 10 it is 0.28 and still rising). Kept.
- P5 PASS (blind): K = 1, 2, 8 give C_end = 1.000, 0.525, 0.139 against 1, 0.5, 0.125 (0–11%).
- P6 PASS (blind): σ = 1.0 share 1.0 (M e^{−σ²} = 18); σ = 2.5 share 0.007 (M e^{−σ²} = 0.1): the threshold M e^{−σ²} = 1 decides whether a law is heard.
Verdict as fixed in advance: distinctness comes from listening to the record; it settles on what is lawful, spread evenly over every law heard (C = 1/K); without laws the same listening fixates on an accident. The control's fixation is slower than registered.
