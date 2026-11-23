# Pre-registered before running potential.py (2026-11-09 ~11:50 ET). Label: math.
Question: does the replicator arena have a global potential (a quantity every pattern's selfish growth always increases)?
Known theory (from memory, flagged): replicator dynamics with fitness f = A x is a gradient system (Shahshahani) iff A is symmetric up to
adding a constant to each column; then mean fitness always rises (Fisher). A potential function rules out cycles.
Decomposition: A - mean-column shift = symmetric part (potential, "self-optimising") + antisymmetric part (pure cycling).
G1 [identity]: mutual-help control (everyone helps everyone equally): 100% potential, mean fitness rises monotonically.
G2 [calculation]: the hypercycle (each helps only its successor) is mostly NOT potential: antisymmetric share >= 40%.
G3 [real test]: a 6-member hypercycle in a well-mixed arena does not settle: mean fitness keeps oscillating (it rises and falls), which
   proves there is no potential. 4-member: settles (known: cycles of 5 or more oscillate). Prediction: 6 oscillates, 4 settles.
G4 [calculation]: adding the free-rider increases the non-potential share.

# Scored after run (2026-11-09)
G1 PASS: mutual help is 100% potential; mean fitness never falls.
G2 PASS: hypercycle n=4 is 33% potential / 67% cycling; n=6 40% / 60%.
G3 PASS: n=6 keeps oscillating (late swing in mean fitness 1.43; it falls on 64% of steps); n=4 nearly settles (swing 0.002) but its mean
   fitness still rises and falls (damped). Neither is monotone, so neither has a potential.
G4 FAILED: adding the free-rider slightly LOWERS the cycling share (0.60 -> 0.58), not raises it.
Caveat: the decomposition is a simple symmetric/antisymmetric split after removing column constants, not the full Hodge decomposition of
games (Candogan, Menache, Ozdaglar, Parrilo 2011).
