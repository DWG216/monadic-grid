# Pre-registered before running da5_race.py (2026-11-08 ~22:50 ET)
Question: what does ONE charge measurement in D(A5) buy, in qubit-magic terms, and how does that compare with tau60 distillation?
Scope stated in advance: Mochon's full gate constructions (turning these states into rotations) are NOT built. We measure the YIELD at
the boundary and compute a break-even overhead. Assumptions: (a) topological operations are exact (no thermal anyons); (b) an idealised
"flux sort" that keeps a chosen pair {h0, y} of flux values coherent (Aharonov-Bohm interferometry with reference fluxes) is free.
Encoding: qubit |0> = flux pair value h0, |1> = y; magic measured as M2 in that qubit's Pauli frame (max 0.585).
Pipeline: start in |h0> (flux basis, free) -> measure pair charge (the expensive event) -> sort onto {h0,y} -> qubit state.

R1 [identity]: outcomes 3 and 3' (prob 1/4 each) give |0> +- (1/sqrt5)|1> for 10 choices of y: Bloch (+-sqrt5/3, 0, 2/3),
   M2 = 0.409, joint success 0.075; the remaining y gives |-> (stabilizer). Outcome 1 gives |+> only (stabilizer). Outcome 4 never occurs.
R2 [real test]: outcome 5 gives only RATIONAL amplitude ratios (no sqrt5); golden numbers come only from 3 and 3'.
R3 [consequence]: best expected cost about 6.7 charge measurements per magic qubit state (0.5 x 0.3 per measurement).
R4 [race, conditional]: tau60 route costs 1.9e5 raw states per full rotation at 1e-10 (bigcode V4). D(A5) wins on event count iff the
   (unbuilt) Mochon conversion uses fewer than 1.9e5/6.7 ~ 2.8e4 charge-measurement-derived states per rotation. Verdict will be
   "conditional", never "D(A5) wins".
Control C1 (solvable A4, 3-cycle class, 4 states = 1 + 3): only rational ratios; magic states still possible but no sqrt5.
Control C2 (flux measurement instead of charge): only |0>,|1>, M2 = 0.

# Scored after run (2026-11-08)
R1 PASS: 3 and 3' each P=1/4; ratio +-1/sqrt5 (5 each) -> Bloch (+-0.7454, 0.6667), M2 0.4091, joint 0.075; ratio -1 -> |-> (M2 0).
   Charge 1 -> |+> only; charge 4 never occurs. The Galois twins 3 and 3' give IDENTICAL qubit-state sets (the sign is absorbed).
R2 PASS: charge 5 (P=5/12) gives only rational ratios: -1/5 (x10, M2 0.194, joint 0.181) and +1 (stabilizer).
R3 FAILED AS STATED: we forgot that a rational ratio is also magic. Counting all magic: 0.331 per measurement = 3.0 measurements
   per magic state. Counting golden (sqrt5) states only: 0.15 per measurement = 6.7, as predicted.
R4 (conditional): break-even Mochon overhead 6.3e4 magic states per rotation (2.8e4 golden-only). Not decided: conversion not built.
C1 (A4) PASS as stated: only rational ratios (-1/3), but A4 ALSO yields magic (M2 0.378, joint 0.625, about 1.6 measurements per state).
   Consequence: cheap boundary magic is NOT special to the non-solvable group. What A5 adds is in the FRAME: non-solvability lets
   braiding alone build classical reversible universality (Toffoli; Ogburn-Preskill / Barrington, from memory), which A4 cannot.
C2 PASS: flux measurement yields only |0>, |1>.
Caveat: M2 is measured in the encoded qubit's Pauli frame, but D(A5) braiding does not supply that frame's Cliffords; M2 is a proxy.
