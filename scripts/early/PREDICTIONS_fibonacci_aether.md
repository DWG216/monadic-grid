# Pre-registered before running fib_aether.py (2026-11-08)
Conceptual point fixed in advance. The golden ratio shows up in two phases of the same braid family (Jones/Temperley-Lieb, earlier run):
  r = 10: braid image FINITE, the 60-element icosahedral group. A rigid golden frame: cheap but not universal; universality must
          be injected from outside (tau60, which our codes can distill only at high cost).
  r = 5 : braid image DENSE: Fibonacci anyons. A fluid golden medium: braiding alone is universal; nothing has to be injected.
Aether thesis restated in QI terms: the frame is the frozen golden phase (r = 10); the aether is the fluid golden phase (r = 5).
Contrast: Ising anyons (r = 4) braid only Clifford gates: a finite, classically simulable frame with no magic.

F1 [identity]: Fibonacci F and R satisfy F^2 = 1 and the hexagon equations; 3-anyon braid generators are unitary and satisfy
   Yang-Baxter; n tau-anyons with total charge 1 span F_(n-1) states (Fibonacci numbers).
F2 [established, check]: Ising braid image (projective) is finite and stops growing; Fibonacci keeps growing exponentially with
   word length (no saturation up to length 12).
F3 [identity, ties to our grid]: sigma1 is a rotation by 7*pi/5 about the fusion axis, i.e. half-angle theta = 7*pi/10: the
   "braid regime" of our one formula f(n) = i^(n-1) sin(n theta)/sin(theta).
F4 [real test, magic]: in the fusion-basis Pauli frame, Ising braids reach ONLY stabilizer states from |0> (max M2 = 0).
   Fibonacci braids: (a) no exact stabilizer state other than the two fusion-basis states is reached up to length 12;
   (b) the largest M2 reached approaches the single-qubit maximum log2(3/2) = 0.585 to within 0.01 by length 12.
F5 [real test, navigation]: the averaging operator of {s1, s2, s1^-1, s2^-1} on PU(2) irreps (j = 1..40) has a spectral gap
   (largest |eigenvalue| < 0.97) but is NOT Ramanujan (some eigenvalue > 2*sqrt(3)/4 = 0.866). Ising: an eigenvalue equal to 1
   (finite group, no gap). Interpretation fixed in advance: the fluid golden medium is universal but not an optimal navigator;
   optimal navigation needs the frozen frame plus one injected gate (super-golden gates).
F6 [identity, observation]: Fibonacci total quantum dimension squared D^2 = 1 + phi^2 = 2 + phi; topological entanglement entropy
   gamma = ln D = 0.643; (2 + phi)^2 + 2 = 7 + 5*phi = tau60's normalisation (norm 59). Meaning of the coincidence: not claimed.

# Scored after run (2026-11-08)
F1 PASS: F^2 = 1 (2e-16), unitary, Yang-Baxter 4e-16; fusion dims 1,1,2,3,5,8,13,21,34,55,89. (Hexagon not separately checked; Yang-Baxter checked.)
F2 PASS: Ising saturates at 24 elements (the projective Clifford group) by length 4; Fibonacci 5,17,42,...,16704 at length 12 (ratio ~1.9 per step).
F3 PASS: sigma1 rotates by 1.4 pi; half-angle 0.7 pi (equivalently 0.3 pi) = the braid regime of f(n).
F4 PASS: Ising max M2 = 0 (only the 6 stabilizer states). Fibonacci: 16704 states, only ONE stabilizer state (|0>, the start);
   max M2 = 0.5848 vs ceiling 0.5850.
F5 PASS: Ising has eigenvalue 1 (no gap). Fibonacci max |eig| = 0.964 over j = 1..40 (gap), above the Ramanujan value 0.866 for 34 of 40 j
   (not Ramanujan). Caveat: j <= 40 only; a gap for all j is guaranteed by Bourgain-Gamburd-type theorems for algebraic gate sets.
F6 identity PASS: D^2 = 2 + phi = phi*sqrt5 = 3.618; gamma = 0.643; (2+phi)^2 + 2 = 7 + 5 phi.
