# PREDICTIONS t160: the record does not depend on how it is sliced

Registered 2026-11-26, before t160_order.py was written or run.

Reading [S]. Monads update per tick by listening and turning, each event reading only its own past (its links). Time is the count, not a foliation. If the update is caused only by the past (sufficient reason: no uncaused noise), every order of updating that respects causality gives the same record, and no slicing enters. This is the record's answer to evolution between curved slices (obstacle 5).

Engine. 1+1 diamond, 400 sprinkled events (seed 1600). Each event carries a monad state over N = 16 tones (p, φ, capacity a); its state is computed from its linked past events by t134's rules (z = Σ√p e^{iφ} over past links; turning toward arg z with strength will × a × N p ≤ 1; listening p ← p w^a; capacity a ← clip(a e)). Minimal events start from seeded random states.
S1 [M]: two different random linear extensions of the causal order (seeds 1, 2) give identical final states with η = 0, to 1e-12.
P1 [M]: with η = 0.3 and noise drawn in update order (uncaused noise), the same two orders give different records (max difference > 0.1).
P2 [M]: a foliation update (all events in a time slice updated from the previous slice's states, slices of width 0.05) in two frames (rapidity 0 and 0.8) gives different records (max difference > 0.1), while the link update gives the same record in both frames (frame enters only through the order, which is invariant: difference 0 to 1e-12).
Consequence fixed in advance: S1 and P2 pass → the record is slicing-free exactly because nothing uncaused enters (P1).
