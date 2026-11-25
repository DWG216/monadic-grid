# t133 The limit of free will: h/2 per tick (pre-registered 2026-11-25, before any t133 code is written or run)

Claim [S]. The record is sampled once per tick (one balanced pair, one Planck cell; t111). Between two samples a phase step Δφ is registered only as wrap(Δφ) ∈ (−π, π]: any larger turn writes the same record as a smaller one. Action is ħ times phase, so the action a monad's will can write into the record per tick is at most πħ = h/2. Equivalently, a monad frequency above the Nyquist frequency π/t_P writes the same samples as its alias below it. Corpus (Ontological Mathematics, quoting JP): spacetime samples the frequency domain at a Planck-set sampling frequency, and the limit is what allows free will; basic monads stray little from what the wave already does.

S1 [M, identity] Aliasing: for 1,000 random ω and ω + 2π m/t_P (m = ±1, ±2), the sampled phasors e^{iωn t_P}, n = 0…999, agree to 1e-12.
P1 [M] Indistinguishability: M = 6 monads, N = 8 frequencies, random weights and phases; monad 0 turns by Δφ on every frequency. For 100,000 random Δφ in (−4π, 4π), the full next-tick record (|Σ_j √p_jk e^{iφ_jk}|² for every k, plus every pairwise cross term 2√(p_i p_j) cos(φ_i − φ_j)) equals the record for wrap(Δφ) to 1e-12 relative.
P2 [M] The bound is reached: an observer who knows the other monads' phases recovers the turn from the record (two references in quadrature give cos and sin) as wrap(Δφ); recovered = Δφ to 1e-9 for every |Δφ| < π − 1e-6, and |recovered| ≤ π always. So the largest turn the record registers is π: ΔS ≤ πħ = h/2 per tick.
P3 [M] Development and use of the bound: in t117's dynamics (seeds 6000–6009, unchanged), the willed turn per tick, |min(κ a N p, 1) sin(Φ − φ)|, averaged over each monad's frequencies and the whole run, rises with capacity: Spearman ρ(capacity, mean willed turn) > 0.5 in at least 8 of 10 worlds; and the lowest capacity decile uses less than 1% of the bound (median mean turn < 0.01π).
Consequence fixed now: if S1, P1 and P2 pass, the bound enters the theory of monads as derived: the limit of free will per tick is h/2. P3 is the corpus's "basic monads stray little"; if it fails, that reading is dropped and the bound stands alone.

## Scoring (2026-11-25, t133_run1.log)
- S1 FAIL as registered: largest difference 2.5e-12 against the registered 1e-12. The script's threshold was written as 1e-9 (a deviation from the registration, noted here); the residual is floating-point rounding of phases up to about 10⁴ rad (n ≤ 999 times |ω + 4π|), and the identity e^{i2πmn} = 1 is exact. Kept as a fail.
- P1 PASS: the record of a turn Δφ equals the record of wrap(Δφ) to 2.7e-15 over 100,000 turns in (−4π, 4π).
- P2 PASS: recovered turn = Δφ to 1.8e-15 for |Δφ| < π; = wrap(Δφ) to 2.6e-15 always; largest recovered 3.14158 < π.
- P3 PASS: ρ(capacity, willed turn) = 0.979–0.999 in 10 of 10 worlds; lowest decile 0.05% of the bound, top decile 0.7%.
Verdict: the limit of free will per tick is h/2 (derived). Development raises how much of it a monad uses, and in t117's worlds even the most developed use under 1%: lawful physics is will far below its bound.
