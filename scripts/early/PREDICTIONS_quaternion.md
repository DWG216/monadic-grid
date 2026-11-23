# Pre-registered before running quat_redo.py (2026-11-07)
Q1 [identity]: every rotation of 4D space is v -> p v q* for two unit quaternions p, q; the self-dual curvature directions turn
   only with p, the anti-self-dual only with q (the two hands = the two quaternion spheres).
Q2 [identity]: in real (Lorentzian) spacetime the two spheres become one complex sphere and its mirror: hand + (E - iB) turns by a
   complex rotation O, hand - (E + iB) by conj(O). Reality = the second is the conjugate of the first.
Q3 [identity]: the null vectors we used to read curvature on the sky, v(z) = (1 - z^2, i(1 + z^2), -2z), are exactly squares of
   spinors kappa = (1, z) (points of the quaternion sphere up to scale); the curvature quartic is degree 4 in kappa and picks up
   phase e^{4ia} when kappa -> e^{ia} kappa, so its size lives on the sky (Hopf base) and its phase on the circle fibre.
Q4 [real check of an earlier explanation]: unit quaternions (SU(2)) are self-mirrored: one fixed matrix S (sigma_y) maps every U
   to conj(U). For general complex (Lorentz, SL(2,C)) elements no such S exists. Predict: solution-space dimension 1 for SU(2),
   0 for SL(2,C). This is why maximally entangled (rotation-only) links hid the hands and thermal (boost) links revealed them.

# Q2-strong, pre-registered before running q2_strong.py
Build a random vacuum curvature (Weyl) tensor, apply a genuine real Lorentz transformation (built from a random spinor matrix M)
to the WHOLE tensor, re-extract E', B' from scratch. Nothing about how the hands transform is assumed.
PREDICT: hand+ (E - iB) transforms by one complex 3D rotation built from M; hand- (E + iB) by exactly its complex conjugate.
PREDICT (control): with a complexified transformation built from two independent spinor matrices M1, M2, the hands transform by
two unrelated rotations (one from each), and hand- is no longer the mirror of hand+.
