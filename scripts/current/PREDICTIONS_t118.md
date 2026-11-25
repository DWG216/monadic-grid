# t118 Laws with content: pure relations seen only at third order (pre-registered 2026-11-25 after the sanity run t118_sanity.log, seeds 7000–7002)
Model (t118_relations.py): M = 50, N = 24, T = 300, η = 0.3, κ = 0.2. A relation law is a triad k1 + k2 = k3 (mod N) whose phase sum ψ = φ_k1 + φ_k2 − φ_k3 is shared across monads (R_t > 0.8) while each of its frequencies alone is scattered (r_k < 0.3): a pure relation, the U(1) form of a parity law x1 + x2 + x3 = b. 'triad': monads turn ψ toward the record's third-order phase arg B_t, B_t = Σ_j √(p_k1 p_k2 p_k3) e^{iψ_jt}, and listen to third-order coherence. 'pair': t116 (second order). 'none': no turning.
Equation behind it: |z_k|² (second order) averages the pure relation away, since each φ_k is scattered; B_t (third order) keeps it, |B|² ∝ M² when ψ is shared.
Sanity (seen): triad 19 pure relations, power-spectrum weight 0.81 on their frequencies, attention share 0.82; pair 0 pure (4 single-frequency laws); none 0.
Test seeds 8000–8011:
P1 [M] triad: median number of pure relations ≥ 5.
P2 [M] pair: zero pure relations in every seed. P3 [M] none: zero in every seed.
P4 [M] Second-order blindness: on pure-relation frequencies the power-spectrum weight |z|²/Σp has median < 2 (noise level 1; a single-frequency law reaches up to M = 50).
P5 [M] Attention: median share on pure-relation frequencies > 0.5.
P6 [M, blind] Third-order sight: on pure relations |B|²/Σa² has median > 10.
Reading fixed in advance: laws with content are relations among phases, visible only to a reader of the right order; attention reading at that order forms them, and a second-order reader is blind to them however long it listens.
