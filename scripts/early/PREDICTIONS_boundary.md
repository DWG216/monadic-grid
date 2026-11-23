# Pre-registered before running boundary.py (2026-11-08)
Claim under test: the mind-body feedback loop = linear quantum evolution + record-and-update steps (nonlinearity only at the
measurement boundary). Second claim: the measurement boundary coincides with the light boundary (records travel by light).

STEP 1: no-signalling. Bell pair; Alice measures in Z or X (Bob does not learn her outcome). Bob runs a feedback loop for
8 rounds; signalling = total-variation distance between Bob's record-string distributions for Alice's two choices, plus the
trace distance between his final averaged states.
 A [identity]: linear evolution + weak measurement + feedback conditioned on Bob's own RECORDS -> distance < 1e-12 for
   20 random loop settings.
 B [established result, Gisin]: feedback driven by the QUANTUM STATE ITSELF (mean-field Hamiltonian kappa<psi|sz|psi> sx)
   -> distance > 1e-3, growing with kappa.
 C [new variant]: a "will" that tilts Born probabilities by the branch state (p_k -> p_k (1 + kappa s_k <psi|sx|psi>), renormalised)
   -> distance > 1e-3.
 Control: kappa = 0 in B and C -> < 1e-12.
 Interpretive consequence fixed in advance: if A passes and B/C fail, a monadic influence that respects relativity must act
 through which records are kept, with outcome statistics that depend only on Bob's reduced state, not by reading or steering
 the branch state directly.

STEP 2: is the measurement boundary the light boundary?
 M1 [prediction, Joos-Zeh numbers]: in air at room temperature, molecular collisions dominate decoherence for all three sizes
   (dust grain 1e-3 cm, particle 1e-5 cm, large molecule 1e-6 cm) by >= 1e10 over sunlight. So "light makes the boundary"
   FAILS for where decoherence happens on Earth.
 M2 [prediction]: in a laboratory vacuum, residual gas still beats sunlight and 300 K photons; only in deep space (CMB only)
   is light the sole channel.
 M3 [real toy test, quantum Darwinism]: a system qubit records into 12 environment qubits. Photon-like environment: records
   never interact again. Gas-like environment: after recording, environment qubits scramble among themselves (random two-qubit
   unitaries). Prediction: photon-like redundancy R_0.1 >= 4 (many small fragments each hold the record); gas-like redundancy
   collapses to <= 1.5 after 6 scrambling layers, while total system-environment information is unchanged (control).
 M4 [identity]: every record-forming interaction in matter here is electromagnetic, i.e. photon-mediated (near-field for
   collisions, radiative for light). Stated in advance as the possible reconciliation: "light boundary" = electromagnetic
   coupling broadly; readable, spreading records = radiative light specifically.

# Scored after run (2026-11-08)
Mid-run corrections logged: (i) variant C at kappa=2 is unphysical (tilt > 1 gives negative probabilities; TV came out 18) -> dropped,
only kappa <= 1 reported; (ii) Step 2b first run too slow (full density matrices) -> entropies via SVD of the smaller side; same model.
A PASS: max signalling 7.8e-16 over 20 random record-driven feedback loops.
B PASS: state-driven nonlinear feedback signals: TV 0.19 (kappa 0.5), 0.22 (kappa 1).
C PASS: state-tilted Born rule signals: TV 0.25 (kappa 0.5), 0.57 (kappa 1).
Control PASS: kappa = 0 -> ~4e-16.
M1 PASS: air/light decoherence ratio 1e15-1e17 for all three sizes.
M2 PASS: lab vacuum still beats sunlight by 1e2-1e4; only deep space leaves light alone.
M3 DIRECTION PASS, THRESHOLD MISSED: photon-like R_0.1 = 12 (maximum); gas-like R_0.1 = 2.0 (predicted <= 1.5). Total I(S:E) = 2.000 in
   both (control PASS).
M4 identity, stated.
