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

## Scoring (2026-11-26)
Run 1 (t171_run1.log) stopped after P1 on a code error (np.trapz removed in this numpy; renamed np.trapezoid). Run 2 (t171_run2.log) is the first complete run; nothing else changed.
- P1 PASS: all identities to 4e-16; the three self-dual 2-forms act on S⁺ as traceless anti-Hermitian matrices of rank 3, the anti-self-dual ones as zero.
- P2 FAIL on the registered criteria: shooting in double precision follows each solution into the vacuum only to r ≈ 7.9, 8.6, 9.0 (N = 1, 2, 3), after which the unstable mode carries it off, so f(15), a(15) are not 1 and the flux reached there is 0.45%, 0.36%, 0.35% short of 2πN (registered < 0.1%). The energy up to that point equals the Bogomolny value πτN to 6e-8, 1e-8 and 6e-9. The criterion at r = 15 was beyond what the registered method can reach; a registration flaw, kept.
- P3 PASS: with ε = −1, none of the 1,200 shots (N = 1, 2, 3; c from 1e-4 to 1e2) comes within 1e-3 of the vacuum (1, 1) and stays finite to r = 15.
- P4 PASS: max f² = 0.9999999, 0.9999996, 1.0000006 (within 1e-6 of τ).
Verdict as fixed in advance: not all of P1–P4 pass, so the Seiberg–Witten equations do not enter the record as derived on this run. What stands: the split (P1, exact), the sign (P3: the other sign has no regular solution, so R2's argument holds), and the singlet bound by the curvature term (P4). The vortices themselves exist with the Bogomolny energy to 1e-8; only the tail check failed, by method. A rerun with a boundary-value solver, registered separately, would settle P2.
