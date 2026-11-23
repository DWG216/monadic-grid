# Pre-registered before running bigcode.py (2026-11-08)
Setting: N-qubit permutation-invariant codes living in the symmetric subspace (spin j=N/2). Transversal U^(xN) acts as the spin-j
representation, so a code with transversal 2I = a 2-dim copy of a 2I irrep inside spin j. Copies of the Galois-twisted irrep 2' come in
a multiplicity space C^m; each point c in CP^(m-1) is a code.

Conceptual points fixed in advance:
 (a) Schur: for a 2' code, logical errors from weight-1 and weight-2 errors are forbidden because spin-1 and spin-2 operators restrict to
     the irreps 3 and 5 of the icosahedral group, while the code's traceless logical operators carry 3'. So every 2' code has distance >= 3
     for free. The Galois twist is what makes the code correct errors.
 (b) The distillation map is a rational map f(z) of degree N on the Riemann sphere, equivariant under 2I. Quadratic distillation of a
     state x needs x to be a FIXED point (up to the cheap group) AND a CRITICAL point of f (single errors leave no logical trace).
     A rational map of degree N has 2N-2 critical points; tau60 states form a 60-point orbit, so this needs N >= 31.
 (c) Fixed = 1 linear condition on c, critical = 1 quadratic condition: generic solutions exist once m >= 3.

V1 [identity/Schur]: every 2' code we build passes distance-3 Knill-Laflamme (reduced 2-qubit states independent of the logical state).
    Control: a 2 (untwisted) code fails it.
V2 [count]: we predict the first N with m >= 3 is between 120 and 200.
V3 [real test]: at that N there exist codes with tau60 as a superattracting fixed point: output error ~ C*eps^2 (exponent 2.0 +- 0.1).
V4 [prediction]: per-round acceptance probability is small (~ few/N), so raw-state cost per output at 1e-3 -> 1e-10 is LARGER than 15-to-1
    T distillation even after crediting tau60's ~6x fewer expensive gates. (If cheaper overall: genuine surprise.)
V5 [prediction]: transversal CZ between two blocks is not a logical gate (leak > 0.5).
Control: a code chosen at random in the same multiplicity space (fixed condition only, not critical) gives exponent 1.

# Scored after run (2026-11-08)
V1 PASS: Galois-twisted codes pass distance-3 KL (N=7: 1e-15, N=67: 6e-13); untwisted controls fail (KL 2.6 and 15.6).
V2 FAILED (good direction): first N with m>=3 is 67 (m=4 at 97, m=5 at 127). Predicted 120-200.
V3 PASS: N=67 tau60 superattracting, exponent 2.02. Beyond prediction: N=97 exponent 3.00, N=127 order-4 (1e-3 -> 1.6e-13 in one round).
    Thresholds 0.486 / 0.494 / 0.481 (control: eps=0.5 in -> 0.500000 out).
V4 PASS: acceptance 2.6-4.5% per round. Per full rotation at 1e-10 from raw 1e-3: icosahedral 1.9e5 raw vs Clifford+T (15-to-1) 5.3e4 = 3.6x worse;
    near parity (1.1x) at 1e-6; much worse at 1e-15 or raw 1e-2. Icosahedral is the ONLY option for raw error 0.15-0.48, but at 1e19-1e40 raw states.
V5 PASS: transversal CZ leak 0.998 (N=67), 0.997 (N=97).
Control (fixed-only code) exponent 1.00 PASS.
Caveat: post-projection noise on a distance-3 block of ~100 qubits needs per-qubit error < ~1e-7, i.e. a protected host layer.
