# t120 The climb (pre-registered 2026-11-25 after the sanity run t120_sanity.log, seeds 10000–10002)
Model (t120_climb.py): t117's world with M = 120, T = 800, capacities log-uniform on [0.01, 1]; each tick capacity grows with experience, a ← clip(a·e^γ, 0.01, 1), γ = 0.02, e_j = E_{p_j}[w]/mean_k w (what j's attention hears, over a uniform listener). Fixed-capacity worlds as control. Change after sanity: the arrival-order correlation is computed only over monads that started below 0.5 (those above arrive at tick 0).
Equation: e > 1 exactly when a monad's attention sits where the record is more coherent than average; t115 showed attention climbs toward coherence (Cauchy–Schwarz), so experience feeds capacity, which feeds attention.
Sanity (seen): every monad reaches 0.5 by about tick 200, ρ ≈ −0.997, K 3–5 laws with climbing against 2 fixed, C near 1/K, attention on laws 0.998.
Test seeds 11000–11009:
P1 [M] Climbing: in every world at least 90% of monads reach a = 0.5.
P2 [M] Median Spearman ρ(initial capacity, arrival time) < −0.8: those who start higher arrive first.
P3 [M] Climbing worlds form at least as many laws as fixed worlds with the same seed in ≥ 8 of 10.
P4 [M] Climbing: median C within a factor 2 of 1/K, attention on laws > 0.9.
P5 [M, blind; writer's expectation stated, uncertain] κ = 0 (no turning, so no laws form): the climb fails, median final capacity < 0.3. If it climbs anyway, the climb does not need laws and runs on fixation.
Reading fixed in advance: if P1–P4 pass, an Age carries every monad up the continuum, the more capable first, and the end state is every monad at full capacity holding every law in balance (the corpus's Omega Point). P5 decides whether laws are needed for the ascent.
