# t126 The monad dynamics with the derived rules (pre-registered 2026-11-25 after sanity runs: t126_sanity_run1.log, t126_noise_scan_bayesian_turning.log, t126_sanity.log)
Rules (t126_derived.py): listening p·w^a with a ≤ 1 (β = 1 is exact conditioning); growth a ← clip(a·e, 1/T, 1) (γ = 1: capacity is accumulated evidence; no capacity or perception below one tick's share, 1/T); perception floor ε = 1/T; reflection on a memory of the whole Age with threshold z from N·T·α = 1 (4.05σ for N = 64, T = 600). Turning: direction derived (ascent of the record); strength is the monad's will (κ = 0.2, scaled by capacity × attention), since a monad's phase is what no record fixes (§232).
Sanity history (kept): fully Bayesian turning (prior from the noise, likelihood R(φ)^a) formed no laws at M = 120 for any noise level: the noise cancels, and the record's evidence about one monad's phase is about 2/√M of its self-knowledge; laws by evidence alone need M below about 16. That is why turning strength is will.
Seen in sanity (seeds 16000–16002): one law per world, attention 0.998 on it; lawful climb universal (ρ ≈ −0.98); lawless plain monads fixate but do not climb (reverses t120); Ages keep 0.33, reset 1.0; reflection clear in 2 of 3 lawless worlds.
Test seeds 17000–17009:
P1 [M] Formation (equal capacity 0.3, no growth): laws in ≥ 8 of 10 worlds; median attention on laws > 0.9; C·K in [0.5, 2].
P2 [M] Lawful climb: ≥ 90% of monads reach 0.5 in every world; median ρ < −0.8.
P3 [M] Lawless (no turning): median fraction reaching 0.5 < 0.2.
P4 [M] Ages: keep ratio median < 0.5; reset in [0.7, 1.4]; Jaccard median < 0.3; novelty drop > 10 in every world.
P5 [M] Reflection: lawful reflective ≥ 95% reach 0.5 with attention on laws > 0.9; lawless reflective median capacity < 0.15 and C < 0.03 in ≥ 8 of 10 worlds.
P6 [M, blind] Lawless false alarms: median fraction of (tick, frequency) judged significant < 1e-3.
Reading fixed in advance: if P1–P6 pass, the theory's results hold with every rule but one derived, and the one left is will.

## Scoring (2026-11-25), run 1 (t126_run1.log)
- P1 PASS: laws in 10 of 10 worlds, attention on laws 0.998, C·K = 1.0 (one law per world in every case).
- P2 PASS: 100% reach 0.5 in every world; ρ −0.964 to −0.988.
- P3 FAIL: lawless plain monads climb by fixation in 7 of 10 worlds (median fraction 1.0); sanity showed 0 of 3. t120's split returns, by world.
- P4 PASS: keep ratio median 0.33, reset 1.0, Jaccard 0, novelty drop 5×10⁴ or more.
- P5 FAIL: lawful part passes (100%, attention 0.998); lawless reflective monads stay clear in 6 of 10 worlds (registered ≥ 8).
- P6 PASS on the median (0), but false alarms occur in 4 of 10 worlds at 3×10⁻⁴–9×10⁻⁴, far above the nominal 2.6×10⁻⁵: the effective-sample count t·η² (from the noise's correlation time) is assumed, not derived, and it is the weak link of reflection's threshold.
Verdict: formation, the climb and the Ages hold with the derived rules; exact conditioning makes one law per world (the plural end state of t115–t116 depended on the chosen slower listening); reflection's derived threshold is too permissive because its noise estimate is not derived.
