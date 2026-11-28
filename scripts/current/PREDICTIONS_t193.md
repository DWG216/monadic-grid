# PREDICTIONS t193: do the chord phases hold across scales?

Registered 2026-11-28, committed before t193_phase_scales.py is written or run.

The amplitudes are counted (§331–§337). Each sector's chord also has a phase δ (√m_k = A(1 + c cos(δ + 2πk/3))): leptons 2/9 (t98, pole masses), down 0.100(6), up 0.0518(8) at M_Z (t190). If a phase is structure, like the down and lepton amplitudes (t192), it should not move with the scale at which masses are read.

Data and method: t192's six scales (Huang–Zhou Tables 2–3, full SM), phase convention and fold of t98's chord(), 10⁵ draws. Phases at scales other than M_Z not computed before this file. Errors are correlated across scales (same inputs), so drift is compared with the M_Z error.

P1 [M]: δ_d moves by less than 2σ(M_Z) across all six scales.
P2 [M]: δ_u moves by less than 2σ(M_Z) across all six scales.
P3 [M]: the charged-lepton phase stays within 0.003 of 2/9 at all six scales (same running allowance as t192's P3).
Consequence fixed now: all pass → the phases are scale-free and are structure to be derived, like the amplitudes; a phase that moves names itself as set at one scale, as the up amplitude does (§336).
Gate: statement about nature; public.

## Scoring (2026-11-28), run 1 (t193_run1.log)
- P1 PASS: δ_d moves 0.0058 across the six scales (0.0999 to 0.1057), against 2σ = 0.0120.
- P2 FAIL: δ_u falls 0.0027 (0.0518 to 0.0492), against 2σ = 0.0016.
- P3 PASS: the lepton phase sits at 2/9 − 0.0011 at every scale (running masses; steady to 4e-5).
Verdict as fixed in advance: the down and lepton chords are scale-free in both numbers; the up chord moves in both. Post hoc, labelled: the up chord is the one sector with a voice (the top, Yukawa ≈ 1) loud enough to retune itself under running; the drift in both of its numbers follows the top Yukawa. The up chord therefore has to be read at the scale where its hands are joined.
