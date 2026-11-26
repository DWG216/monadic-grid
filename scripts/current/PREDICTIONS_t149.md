# PREDICTIONS t149: record-sourced gravity and the decoherence–diffusion trade-off

Registered 2026-11-26, before t149_tradeoff.py was written or run.

Question. If gravity is sourced by the record (bridge §102, read as copies, t33 S3), the gravitational field is classical and must obey the trade-off between decoherence and diffusion that any consistent coupling of classical gravity to quantum matter obeys (Oppenheim, PRX 13, 041040 (2023); Oppenheim, Sparaciari, Šoda and Weller-Davies, Nat. Commun. 14, 7910 (2023)). Where does the grid sit?

Setup. A which-path qubit (σ_z = ±1) pushes a classical probe with mean force g σ_z. Let γ be the decay rate of the qubit's coherence |ρ01| and D the probe's momentum diffusion (Var p = D t at fixed σ_z).
Bound [M, derived here, checked numerically below]. If p is classical (readable), coherence cannot exceed the overlap of the two branch distributions of p: after time t the means differ by 2gt and each has variance Dt, so the Bhattacharyya overlap is exp(−g²t/(2D)). Hence γ ≥ g²/(2D), i.e. R ≡ γD/(g²/2) ≥ 1.
Grid reading [S]: the field is written from the record and from nothing else (sufficient reason: no uncaused noise), and the record is read once, whole. In measurement language: efficient continuous measurement of σ_z, with the force fed from the full measurement current. Prediction: R = 1, the grid saturates the bound.

Engine. Stochastic master equation for the qubit (dephasing k D[σ_z], current dY = 2√k⟨σ_z⟩dt + dW), probe dp = g dY/(2√k). 4000 trajectories, dt = 1e-3, T = 2 (units g = k = 1 unless varied).

S1 [sanity]: the simulated coherence of the ensemble decays at γ = 2k within 2%; the probe diffusion at fixed σ_z is D = g²/(4k) within 3%.
P1 [M]: record-sourced gravity (efficient, full current): R within 3% of 1, at k = 0.5, 1, 2.
P2 [M] controls, each R within 5% of 2: (a) extra unread dephasing equal to k; (b) extra force noise equal to D; (c) measurement efficiency 0.5 with the force fed from the recorded current.
P3 [M] bound: across 200 random CP settings (k, efficiency in [0.1, 1], extra dephasing and extra noise in [0, 2]), no R below 1 − 3%.
P4 [I, number fixed in advance] Bose geometry (two diamond masses 1e-14 kg, ρ = 3500 kg/m³, superposition 250 μm, centres 450 μm, collinear): the grid's coherence time is the reduction time τ = πħ/E_G (t146), so γ = 1/τ; with R = 1 the probe's acceleration diffusion is fixed, D_a = g_a²/(2γ) where g_a is half the difference of the two branch accelerations. Reported: τ, γ, g_a and D_a. Prediction: τ is below 0.1 s (the experiment needs coherence over about 2.5 s), so the grid predicts no gravity-mediated entanglement and which-path decoherence within 0.1 s from gravity alone.

Consequence fixed in advance: if P1 passes, the grid is the minimal classical-gravity coupling (equality in the trade-off), and with t146 it has no free parameter: decoherence and diffusion are both fixed by E_G.

## Scoring (2026-11-26), run 1 (t149_run1.log)
- S1 PASS: γ = 2.004 (2k = 2), D = 0.2523 (g²/4k = 0.25).
- P1 PASS: R = 0.981, 0.994, 1.001 at k = 0.5, 1, 2. Record-sourced gravity saturates the bound.
- P2 PASS: R = 1.99 (extra unread dephasing), 2.02 (extra force noise), 2.05 (efficiency 0.5).
- P3 PASS: 200 random settings, smallest R = 2.03, none below 0.97.
- P4 PASS: diamond spheres of 1e-14 kg (radius 0.88 μm) displaced 250 μm: E_G = 9.07e-33 J, τ = πħ/E_G = 0.037 s, γ = 27.4 /s; branch acceleration half-difference g_a = 2.15e-18 m/s², so the grid's acceleration diffusion is D_a = g_a²/(2γ) = 8.4e-38 m² s⁻³. Coherence is lost to gravity alone about 70 times faster than the 2.5 s run needs: no gravity-mediated entanglement.
Verdict as fixed in advance: the grid is the minimal classical-gravity coupling (equality in the trade-off), with no free parameter once t146 fixes γ.
