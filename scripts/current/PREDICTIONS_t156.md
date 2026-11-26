# PREDICTIONS t156: the record as a classical–quantum dynamics (weak field)

Registered 2026-11-26, before t156_cq_record.py was written or run.

Aim. Write the grid's gravity in Oppenheim's formalism (PRX 13, 041040, 2023; weak-field limit: Layton, Oppenheim, Russo, Weller-Davies, JHEP 2024), with every kernel fixed. Closest prior construction: Tilloy and Diósi (2016), gravity sourced by the signal of a continuous collapse; Kafri, Taylor and Milburn (2014).

The dynamics [S + M]. Mass density m̂(x) is recorded continuously; the record's current dY(x) = ⟨m̂(x)⟩dt + dW(x) has noise covariance C dt; the Newtonian potential is written from the record, Φ = −G K ∗ (dY/dt), with K the smeared Coulomb kernel (Gaussian mass resolution R₀). Choices fixed by earlier results: the decoherence of a two-branch mass is E_G/(πħ) (t146), so C⁻¹ = (4G/(πħ)) K; the record is read once, whole (t149), so the trade-off is saturated. In Oppenheim's notation: D₁ = −G K (drift of Φ), D₂ = (4G/(πħ)) K (decoherence kernel in this normalisation), D₀ = D₁ D₂⁻¹ D₁ = (πħG/4) K (white noise of Φ per unit time, state-independent).

S1 [M]: on a 1D chain of 24 sites with the 3D smeared kernel (G = ħ = m = h = R₀ = 1), the block matrix [[D₀, D₁],[D₁, D₂]] is positive semidefinite with exactly 24 zero eigenvalues (saturation), smallest eigenvalue above −1e-10 relative.
P1 [M]: unravelling (Gaussian Kraus update of one mass in a two-site superposition, 20,000 trajectories, dt = 0.01, T = 2/Γ): (a) the ensemble coherence decays at Γ = E_G/(πħ), E_G = Gm²(K(0) − K(d)), within 2%; (b) the mean Φ at three probe sites equals −G K ⟨m⟩ within 3 standard errors; (c) the sample covariance of the Φ noise at the probe sites equals (πħG/4) K within 5%.
P2 [M, number]: the Gran Sasso radiation bound (Donadi et al., Nat. Phys. 17, 74 (2021): R₀ > 0.54 Å for the parameter-free rate, rate ∝ 1/R₀³) becomes R₀ > 0.54/π^(1/3) Å = 0.37 Å for the grid's rate, which is 1/π of Diósi–Penrose.
P3 [I, proposal, not derived]: the record resolves mass at the atomic scale, R₀ = a₀ = 0.529 Å. Consequence: the grid's radiation signal is (0.37/0.529)³ = 0.34 of the present 95% bound; a threefold improvement in sensitivity would see it or exclude this proposal.
Not built here: the full general-relativistic version (the Hamiltonian constraint in a covariant classical–quantum dynamics); stated as open.
