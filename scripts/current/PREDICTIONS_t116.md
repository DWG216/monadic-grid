# t116 Laws that form themselves (pre-registered 2026-11-25 after sanity runs: t116_sanity_run1_flawed.log, t116_sanity.log)
Model (t116_dialectic.py): no lawful set is given. M = 50 monads, N = 64 frequencies, T = 300 ticks, noise η = 0.3. Each tick: noise on phases; choice: each monad turns its phase at k toward the record's phase by min(κ N p_jk, 1)·sin(Φ_k − φ_jk) (attention-weighted) or min(κ, 1)·sin(·) (uniform control); listening p ← p·w^β (β = 0.1) with a floor ε = 1e-3 (a monad is never without perceptions, Monadology §21). Law: phase order r_k > 0.8.
Sanity history: run 1 had no floor and listening at full rate; attention fell to zero (NaN) and fixation outran alignment. Fixed before registering: floor, listening rate, turn capped at a full turn.
Equation behind the reading: attention and alignment feed each other: alignment raises w_k (coherent record ∝ M²), w raises p_jk, p_jk raises the turn toward the record's phase.
Test seeds 4000–4019:
P1 [M] κ = 0: no laws (K = 0), weighted and uniform.
P2 [M] Weighted κ = 0.02: median K ≥ 1 and share of attention on laws > 0.95. Uniform κ = 0.02 and 0.05: K = 0.
P3 [M] Weighted: median K rises monotonically over κ = 0.02, 0.05, 0.1, 0.2, 0.4.
P4 [M] Weighted, every κ ≥ 0.02: median C within a factor 2 of 1/K (plural attention over the laws formed).
P5 [M] Uniform κ = 0.2 and 0.4: K = 64 (everything locks) and C < 2/N = 0.031 (nothing distinct).
P6 [M, blind] Dissent: 30% of monads never turn their phases (κ = 0.1, weighted): laws still form (K ≥ 1), and the dissenters, who still listen, put > 50% of their attention on the laws the others formed.
Reading fixed in advance: attention is what makes laws: it lowers the coupling needed for order and keeps the laws few and distinct; coupling without attention either fails or locks everything, which is uniformity, not law. A refusing monad still hears the laws.
