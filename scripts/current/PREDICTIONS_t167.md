# PREDICTIONS t167: no which-path in the horizon's field beyond the record

Registered 2026-11-26, committed before t167_horizon_memory.py is written or run.

Question (anticipated from Danielson–Satishchandran–Wald): if gravity is classical, the field of a superposed mass still differs between branches; why does its classical memory on a horizon not carry which-path information?
Grid [S]: the field is written from the record (t156, t157): Φ = −GK(dY/dt). Whatever a horizon reads of Φ is a function of the record dY, so by the data-processing inequality it cannot tell the branches apart faster than the record already does. Before the record writes, the field is the weighted common field and carries no branch difference; after, it is one branch's. No field ever holds both branches.
Engine: t157's lattice (24 sites, Gaussian-smeared kernel, G = ħ = m = R₀ = 1), record covariance C with C⁻¹ = (4aG/ħ)K at a = 1/2. A horizon reading is any linear functional y = Lᵀ dY of the record (field values or memory steps at distant sites, any weights). Its branch-discrimination rate is (LᵀΔ)²/(8LᵀCL); the record's is ΔᵀC⁻¹Δ/8.
P1 [M]: over 10,000 random readings (random far-site weights, including the field at single distant sites and its time-integral), none exceeds the record's rate (largest ratio ≤ 1 + 1e-9), and the bound is reached only by the reading L ∝ C⁻¹Δ.
P2 [M]: in the unravelling of t157 (20,000 trajectories), conditioning additionally on a distant-site field reading changes the ensemble coherence decay rate by less than 1% (it adds no information).
P3 [M, number]: for the Bose superposition (1e-14 kg, 250 μm) at b = 6GM/c² from a solar-mass black hole, the record-written field's step at writing, ΔΦ ≈ p_B G m d/b², is reported; it is one history's field, and the horizon's which-path count from gravity is zero, against DSW's soft-graviton count ⟨N⟩ ~ T/T_D^GR.
Consequence fixed in advance: P1 and P2 pass → the horizon's classical memory carries no which-path information beyond the record, so the gravitational DSW term is absent in the grid for a stated reason, not by assumption.
