# Pre-registered before running icosa_code.py (2026-11-08)
Code: 7-qubit icosahedral permutation-invariant code (Gross form from errorcorrectionzoo): |0_L> ~ sqrt3 D0 + sqrt7 D5, |1_L> ~ sqrt7 D2 - sqrt3 D7.
B1 [verify]: it corrects any single-qubit error (distance 3, Knill-Laflamme) and every icosian U gives U^(x7) acting inside the code (transversal 2I).
B2 [prediction]: the 5-qubit code (our perfect tensor) has NO distillation threshold for 5-fold (icosahedron-vertex) magic states:
    output never better than input.
B3 [prediction]: the 7-qubit icosahedral code DOES distill some icosahedral-class magic state (positive threshold).
B4 [open, stated in advance]: compared with the 5-qubit code's 0.173 for cube corners, we expect the icosahedral code's threshold to be LOWER
    (bigger code, more ways to fail). If it is higher, that is a genuine surprise in favour of the golden code.

# After run 1 (logged before run 2): transversal check failed in our default icosahedron orientation; thresholds hit scan edge (0.3).
# Run 2 adds: search for the code's own icosahedron frame (5-fold axis along z, scan azimuth of the second axis),
# extend scan to 0.5, and a CONTROL: at input error 0.5 (pure noise) a genuine distiller must output noise, not a pure state.
# Run 2 caveat (logged before run 3): the 5-fold target used was the pole |0>, a stabilizer state (no magic) -> trivial.
# Run 3: distill the NON-pole icosahedron vertices (genuinely magic in the standard Pauli frame). B3/B4 are judged on run 3 only.
