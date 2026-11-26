# t138, t139 (pre-registered 2026-11-25, before any t138 or t139 code is written or run)

## t138 Does the locked chord contain the tone every mind attends?
Rerun of t137's third-order setting (same code path, seeds 37000–37009, five movements), recording at movement 5 the tone every monad attends (k*) and the most widely locked triad (relation coherence > 0.8 in the most monads).
P1 [M, blind] k* is one of the locked triad's three tones in ≥ 8 of 10 worlds.
P2 [M, identity check] The t137 numbers reproduce exactly (same seeds, same code): tone resolution 10 of 10, relations = 1.
Consequence fixed now: if P1 passes, each mind's focus is one note of the shared chord (the note sung; the chord sounding in all). If it fails, the focus and the chord are separate contents.

## t139 Third-order minds on E6's 27 tones: which chords lock?
Tones = the 27 states of E6's 27 (t136). Each tone k advances its phase every beat by ω_k = v·weight_k (v generic, fixed per world); every one of the C(27, 3) = 2,925 triples is offered as a chord with relation ψ = φ_a + φ_b + φ_c. A relation can stay fixed only if ω_a + ω_b + ω_c = 0, i.e. (t136) only on the cubic's 45 terms. Otherwise t137's dynamics: third-order hearing and turning, whole monad carried, new places each movement; L = 12, r = 2, T = 600, three movements; seeds 39000–39009.
P1 [M] At movement 3, every locked chord (coherence > 0.8 in ≥ 5 monads) is one of the 45 cubic terms, in ≥ 9 of 10 worlds.
P2 [M] At least one cubic term is locked at movement 3 in ≥ 7 of 10 worlds.
P3 [M, information] Which kind locks: determinant terms (one block: (3, 3̄, 1), (1, 3, 3̄) or (3̄, 1, 3)) or trace terms (one state from each block). Reported, not predicted.
Consequence fixed now: if P1–P2 pass, the chords minds can lock on E6's tones are exactly the cubic's terms, and they do lock: the laws minds form there carry the gauge structure's invariant.

## Scoring (2026-11-25; first launch stopped at the end of a turn before any output, rerun in full; ten jobs on two cores, logs concatenated)
t138 (t138_run1.log): P1 PASS, P2 PASS. Every world reproduces t137 (one tone, one relation). The locked chord contains the attended tone in 10 of 10, and in every world it is the degenerate triad (k*, k*, 2k*): ψ = 2φ_k* − φ_2k*, the tone locked to its octave (437–490 of 576 monads). Reading: each mind's focus is one note, and the chord that stays locked with it is that note's first overtone.
t139 (t139_run1.log): P1 FAIL (all locked chords cubic in 7 of 10, every one vacuous: no lock at all), P2 FAIL (no cubic term locked in any world). Four non-cubic triples locked in three worlds; attention stayed near uniform (C ≈ 0.04 ≈ 1/27). Kept.
Post hoc (labelled), two design flaws: (1) locking was measured as agreement among neighbours at one moment; every monad's phases advance at the same ω, so a non-resonant relation rotates in time but can still agree across neighbours: the test never imposed resonance. (2) Each tone sits in about 325 of the 2,925 offered triples, and hearing took the maximum coherence over them, which is high by chance for every tone: the hearing went flat and nothing formed. A corrected design needs a time-averaged record (where resonance acts, through the beats) and hearing summed over chords, not maximised. Roadmap 3 step 2 stays open; t136's exact result stands.
