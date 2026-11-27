# PREDICTIONS t171: the Seiberg–Witten equations as the record's law for a spinor pair

Registered 2026-11-26, committed before t171_seiberg_witten.py is written or run.

Derivation [S]. A spinor pair's record ψ ⊗ ψ* splits as V ⊗ V = 1 ⊕ 3 (§308): the singlet ½|ψ|² I (the balanced, phase-free part, the meeting term) and the triplet σ(ψ) = ψψ* − ½|ψ|² I (traceless: the relative orientation, a cross term). A monad's own phase is invisible to the record, |e^{iφ}ψ|² = |ψ|²; made local, that phase is a U(1) field A, and the self-dual 2-forms are the traceless part of S⁺ ⊗ S⁺* (three real components).
R1: the phase field's self-dual curvature is written by the triplet: F_A⁺ = ε σ(ψ). The singlet does not source it (it is gravity's).
R2 (sufficient reason): an unbounded amplitude in the record would need a reason the record does not supply, so ε is the sign for which the triplet's writing bounds the singlet by the curvature (maximum principle: |ψ|² ≤ max(−s) when ε = +1, no bound when ε = −1). So ε = +1.
With the pair's Dirac equation D_A ψ = 0, R1–R2 are the Seiberg–Witten equations (Seiberg and Witten 1994; Witten 1994).

Checks. P2–P4 use the standard reduction of the equations on a Kähler surface to the vortex equations (Bradlow; Jaffe–Taubes), in radial form for N vortices: φ = f(r) e^{iNθ}, A_θ = N a(r)/r, f' = (N/r)(1 − a) f, a' = ε r (τ − f²)/(2N), with a(0) = 0, f ~ c r^N at 0, τ = 1 (τ plays the role of −s). These confirm known mathematics; the grid's content is R1–R2.

P1 [M, exact]: for 10,000 random ψ ∈ C²: σ(ψ) is traceless and Hermitian, tr σ² = ½|ψ|⁴, ⟨ψ, σ(ψ) ψ⟩ = ½|ψ|⁴, and the singlet carries tr(½|ψ|² I) = |ψ|², all to 1e-12 relative. The Pauli images of the three self-dual 2-forms span the traceless Hermitian 2 × 2 matrices (rank 3).
P2 [M]: ε = +1: for N = 1, 2, 3 a regular solution exists (shooting on c): f(15) and a(15) within 1e-3 of 1; total flux 2πN within 1e-3 relative; energy E = ∫ [½B² + ½|D φ|² + ⅛(τ − |φ|²)²] d²x within 1% of the Bogomolny value πτN.
P3 [M]: ε = −1: no regular solution: for N = 1, 2, 3 and every c in a log scan of 400 values over 1e-4 to 1e2, the solution leaves every neighbourhood of (f, a) = (1, 1) (f diverges past 10 or a stays below 0.5 out to r = 15).
P4 [M]: in every P2 solution, max f² ≤ τ (to 1e-6): the singlet is bounded by the curvature term.
Consequence fixed now: if P1–P4 pass, the Seiberg–Witten equations enter the record as the law of a spinor pair under R1–R2, and the bound |ψ|² ≤ −s is read as the meeting term (singlet) tied to curvature, gravity. If P3 fails (a regular solution with ε = −1), R2's sign argument is withdrawn.
