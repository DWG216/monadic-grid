# PREDICTIONS t193: do the chord phases hold across scales?

Registered 2026-11-28, committed before t193_phase_scales.py is written or run.

The amplitudes are counted (§331–§337). Each sector's chord also has a phase δ (√m_k = A(1 + c cos(δ + 2πk/3))): leptons 2/9 (t98, pole masses), down 0.100(6), up 0.0518(8) at M_Z (t190). If a phase is structure, like the down and lepton amplitudes (t192), it should not move with the scale at which masses are read.

Data and method: t192's six scales (Huang–Zhou Tables 2–3, full SM), phase convention and fold of t98's chord(), 10⁵ draws. Phases at scales other than M_Z not computed before this file. Errors are correlated across scales (same inputs), so drift is compared with the M_Z error.

P1 [M]: δ_d moves by less than 2σ(M_Z) across all six scales.
P2 [M]: δ_u moves by less than 2σ(M_Z) across all six scales.
P3 [M]: the charged-lepton phase stays within 0.003 of 2/9 at all six scales (same running allowance as t192's P3).
Consequence fixed now: all pass → the phases are scale-free and are structure to be derived, like the amplitudes; a phase that moves names itself as set at one scale, as the up amplitude does (§336).
Gate: statement about nature; public.
