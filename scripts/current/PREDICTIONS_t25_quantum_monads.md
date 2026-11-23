# t25 quantum complexity and monads (pre-registered 2026-11-22 18:20)
Q1-Q3: three-qutrit code |i~> = (1/sqrt3) sum_j |j, j+i, j+2i> (mod 3) (Cleve-Gottesman-Lo; Almheiri-Dong-Harlow's toy holographic code). Reference R maximally entangled with the logical qutrit; entropies in log base 3.
Q1 [M] each single qutrit knows nothing: I(R:Q_k) = 0 (< 1e-12) for k = 1,2,3.
Q2 [M] any pair knows everything: I(R:Q_jQ_k) = 2 (the maximum) for all three pairs.
Q3 null [M] classical repetition record |iii>: I(R:Q_k) = 1 for each single (a copy in every part) and I(R:pair) = 1 (never 2: the quantum part is lost).
Q4 [M] bosons vs fermions: n-particle transition amplitudes through a random unitary are permanents (bosons) and determinants (fermions). Run-time growth per +1 in n over n = 12..20: permanent (Ryser) factor > 1.8; determinant factor < 1.3. (Timing; machine-dependent, reported as measured.)
