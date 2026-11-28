# PREDICTIONS t184: the comma as holonomy; temperament as a choice of connection

Registered 2026-11-28, committed before t184_comma.py is written or run.

Reading [I]. Just intonation places pitches (octaves aside) on the lattice of 3s and 5s: (b, c) is 3^b 5^c. The Tonnetz torus of t183 is its quotient by the kernel of (b, c) ↦ 7b + 4c mod 12. Going once around a cycle of the torus returns to the same pitch class but not the same just pitch: the mismatch is a comma, the holonomy of a flat connection around a non-contractible loop (a Wilson line, as on the Calabi–Yau of t176). A temperament is a choice of connection; equal temperament is the one with zero holonomy.

P1 [M]: holonomy (in cents, octaves removed) is additive on the kernel lattice: the generators give the syntonic comma (4, −1): +21.506 and the lesser diesis (0, 3): −41.059; the Pythagorean comma (12, 0) = 3(4, −1) + (0, 3) gives +23.460 and the greater diesis (4, −4) gives +62.565 (each to 0.001 cents, computed directly from the just ratios).
P2 [M]: every closed loop in the just lattice itself (contractible) has zero holonomy: the connection is flat, and the commas are pure Wilson lines.
P3 [M]: with octaves pure, a temperament with fifth f and major third t (in cents) has zero holonomy on both generators exactly when 4f − t = 2400 and 3t = 1200, whose only solution is f = 700, t = 400: twelve-tone equal temperament.
Consequence fixed now: if P1–P3 pass, the record holds: a comma is a holonomy, just intonation is a flat connection with Wilson lines on the Tonnetz torus, and equal temperament is its trivialisation.
Gate: mathematics; public.

## Scoring (2026-11-28), run 1 (t184_run1.log)
- P1 PASS: syntonic comma +21.5063, lesser diesis −41.0589, Pythagorean +23.4600, greater diesis +62.5651 cents, equal to the direct ratios, and additive on the kernel.
- P2 PASS: contractible loops carry zero holonomy (largest 1e-11 cents over 10,000 random loops).
- P3 PASS: zero holonomy on both generators with pure octaves forces fifth 700 and third 400 cents (determinant 12, unique).
Verdict as fixed in advance: a comma is a holonomy; just intonation is a flat connection with Wilson lines on the Tonnetz torus; equal temperament is its trivialisation.
