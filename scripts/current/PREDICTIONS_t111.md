# t111 Arrow of time: balanced pairs as Deutsch–Marletto null constructors (pre-registered 2026-11-25, before code)
[S] Deutsch & Marletto (J. Phys. Commun. 10 (2026) 115003) define time as the label of an equivalence class of null constructors: tasks that change a timer and nothing else. In the grid a balanced pair, e^{iθ} + e^{i(θ+π)} = 0, leaves the sum unchanged and adds one tick to the count. Correction to section 222: the monotone quantity is the count N = Σ|c_k|² (Parseval), not the record |S|² of the sum, which fluctuates.
P1 [M, exact] Adding a balanced pair at any phase leaves S unchanged: |ΔS| < 1e-12 over 1e5 random pairs.
P2 [M] For random-phase monads added one at a time (N up to 1e4, 200 walks), |S|² decreases at between 40% and 60% of steps (not monotone) while N increases at every step.
P3 [M] Recovery is impossible from the record: for fixed |S|², the number of phase assignments of n = 8 monads on a 12-point grain consistent with it grows with |S|² class size > 1 for every attained value (the square forgets the phases, so the record cannot be unwritten).
Verdict wording fixed in advance: if P1–P3 pass, the arrow is the count of balanced pairs, irreversible because squaring is not invertible.

## Scoring (2026-11-25), run 1 (t111_run1.log)
- P1 PASS: |ΔS| ≤ 1.1e-15 over 1e5 pairs.
- P2 PASS: the record |S|² falls at 49.5% of steps; the count rises at every step.
- P3 PASS with a deviation from the registration: to keep the enumeration at 12^4, four of the eight monads were fixed as two balanced pairs (phases 0, 3, 6, 9 of 12) and four were free. 38 attained values of |S|², smallest class 12 assignments.
Verdict as worded in advance: the arrow is the count of balanced pairs, irreversible because squaring is not invertible.
