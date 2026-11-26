# t143c Chords across monads with sufficient reason applied to the noise (pre-registered 2026-11-25, after t143b, before any t143c run)

Why: t143 and t143b added independent random phase kicks (η = 0.3 rad per beat) to every tone. Nothing in the grid causes them: a tone advances by its own frequency, and a phase changes only by a monad's turning (§1, t124). Uncaused kicks violate sufficient reason; they were a modelling choice. The only disorder with a reason is the others' unrelated phases. t143b's collapse over 100 beats is exactly what those kicks produce.

Design: t143_cross_chords.py with η = 0, T = 600, τ = 100, will 0.2, seeds 43000–43009; lock as before (R > 0.8 in ≥ 5 monad-triples).
Arm R: tones rotate (ω from E6's weights, as t143). Arm Z (control): ω = 0.

P1 [M] Arm R: at least one cubic chord locks in ≥ 7 of 10 worlds.
P2 [M] Arm R: cubic chords are at least half of all locked chords in ≥ 7 of 10 worlds.
P3 [M, control] Arm Z: cubic chords are under 20% of locked chords in ≥ 7 of 10 worlds (with no drift nothing singles them out; they are 27 of the 729 relations per triple of blocks).

Consequence fixed now: if all pass, once no uncaused kicks are allowed, the tones' own drift selects the gauge structure's invariant across minds over long windows: t143b failed on the noise, not on the resonance. If P1 fails, chords across minds do not hold over 100 beats in this design even without noise.
