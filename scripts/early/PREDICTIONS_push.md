# Pre-registered before running push.py (2026-11-08)
Currency: single-qubit robustness-of-magic excess  m = max(0, |x|+|y|+|z| - 1)  (0 inside the stabilizer octahedron).
P1 (magic per raw state): the 5-qubit code delivers MORE magic per raw noisy state at low input error (its outputs carry more magic);
    the icosahedral code delivers more at higher input error (it keeps working where the 5-qubit code fails).
P2 (iteration): both suppress error roughly quadratically per round. Starting at input error 0.10, the icosahedral code reaches
    error 1e-6 with FEWER raw states in total. At 0.20 only the icosahedral code can start at all.
P3 (literature): unknown; reported as found.
Iteration assumption (stated in advance): each round's output is re-twirled about its own axis; for the icosahedral code we require
    the output to be another vertex of the SAME icosahedron (checked), so no extra non-transversal rotation is needed.
