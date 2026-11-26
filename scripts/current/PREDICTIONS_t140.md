# t140 Chords on E6's 27 tones, corrected design (pre-registered 2026-11-25, before any t140 code is written or run)

t139 failed by design (record §266): shared phase advance let non-resonant relations agree among neighbours at one moment, and hearing by maximum over ~325 triples per tone went flat. Corrections, both fixed now:
(1) The record a monad hears is time-averaged: B̄ ← (1 − 1/τ) B̄ + (1/τ) B, τ = 20 beats, for tones (z̄) and chords (B̄). A relation whose ψ rotates at Ω = ω_a + ω_b + ω_c ≠ 0 averages away (by about 1/(Ωτ)); a resonant one does not. Turning uses the averaged record.
(2) Third-order hearing of tone k is the mean coherence over the chords containing k, not the maximum.
Everything else as t139: the 27 weights of E6 (t136), ω_k = v·weight_k scaled to at most 0.3 rad per beat, all 2,925 triples offered with ψ = φ_a + φ_b + φ_c, L = 12, r = 2, T = 600, three movements, whole monad carried, new places each movement; seeds 40000–40009. Locked chord: local coherence of the averaged relation > 0.8 in ≥ 5 monads.
P1 [M] In ≥ 7 of 10 worlds at least one chord is locked at movement 3, and every locked chord in those worlds is one of the cubic's 45 terms.
P2 [M] No non-cubic chord is locked at movement 3 in any world.
P3 [M] Attention resolves (median C > 0.5) in ≥ 7 of 10 worlds.
P4 [M, information] The kinds locked: determinant terms (one block) or trace terms (one state from each block); and whether the attended tone belongs to a locked chord.
Consequence fixed now: if P1–P2 pass, minds on E6's tones lock exactly the cubic's terms: the chords minds hold there are the gauge structure's invariant.

## Scoring (2026-11-25, t140_run1.log; two jobs on two cores, concatenated)
- P1 FAIL: no chord locked in any world (0 of 10). Kept.
- P2 PASS: no non-cubic chord locked in any world (the averaging removed t139's false locks).
- P3 PASS: attention resolves to one tone in 10 of 10 (median C = 0.997, every monad on the same tone).
- P4 (information): no chords; the shared tone is from block A in 5 worlds, B in 4, C in 1.
Post hoc (labelled): on E6's 27 tones no chord can contain a tone twice (t136: no triple with a repeated state sums to zero), so there is no octave for a single note to carry (t138's chord), and every cubic term needs three different tones. A mind whose focus resolves to one tone hears the other two at its attention floor, so the chord's amplitude in any one mind is negligible. Reading: a cubic chord on E6's tones cannot be held by one mind; it needs three voices singing three different notes. That is also how the cubic acts in physics: one coupling among three different fields. Next design: chords across monads (the relation among the phases of neighbouring monads that attend different tones), with focus allowed to differ.
