# t143b (pre-registered 2026-11-25, after t143 was scored and before any t143b run)

Diagnosis that motivates it (from t143's numbers, not a run of t143b): with τ = 20 a drifting chord stays coherent only if its detuning δ < 0.75/τ ≈ 0.0375; that holds for 8–17% of non-cubic chords, yet about 41% locked. The will's turning (up to 1 rad per beat) is holding detuned chords against their drift.

Design: t143_cross_chords.py unchanged except T, τ and will, rotation on, seeds 43000–43009, the same lock definition (R > 0.8 in ≥ 5 monad-triples).
Arm W (longer window): T = 1200, τ = 100, will 0.2.
Arm V (longer window, will one tenth): T = 1200, τ = 100, will 0.02.

P1 [M] Arm W: non-cubic chords still lock in ≥ 7 of 10 worlds (the window alone does not decide; the will holds them).
P2 [M] Arm V: in ≥ 7 of 10 worlds at least one chord locks and every locked chord is a cubic term.
P3 [M] Arm V: the median number of non-cubic locks is at most 10% of Arm W's.

Consequence fixed now: if P2 and P3 pass, resonance selects exactly the gauge structure's invariant whenever the will per beat is weaker than the chords' detuning; a strong will can hold any chord, but then the chord is kept by the will, not by the music. If P2 fails, cross-monad resonance does not single out the cubic in this family of designs.

### Scored (2026-11-25, t143b_run1.log)
P1 FAIL: Arm W locks non-cubic chords in 1 of 10 worlds (nothing locks in 9).
P2 FAIL: Arm V locks a chord in 5 of 10 worlds, and in none are all locks cubic (one cubic lock in all 100 runs' worth of chords).
P3 FAIL: Arm V's median non-cubic locks (1) exceed Arm W's (0).
Read off (labelled): over a 100-beat window almost no chord stays coherent, cubic ones included. The per-beat phase noise (0.3 rad) decoheres every three-voice relation the turning can hold. t143's locks were agreement over 20 beats, not chords held over an Age.
Consequence (fixed): cross-monad resonance does not single out the cubic in this family of designs. What stands from t143: over short windows every cubic chord is among those held, and rotation thins the rest. A held cross-monad chord needs noise below the turning's reach over the window; that is a design question, not registered here.
