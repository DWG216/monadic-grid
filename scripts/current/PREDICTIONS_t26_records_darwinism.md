# t26 classical records from monadic ones (pre-registered 2026-11-22 18:30)
System qubit S = a|0> + b|1>, |a|^2 = p = 0.3. Copy into N = 8 environment qubits by CNOT (S control). Entropies in bits.
D1 [M] S's reduced state loses its off-diagonal term exactly (|rho_01| < 1e-12): decoherence = copying.
D2 [M] Mutual information I(S:F) for an environment fragment of f qubits equals H(p) (Shannon, 0.881 bits) for every 1 <= f <= N-1 (the classical plateau; error < 1e-10), and 2 H(p) for f = N.
D3 [M] The plateau value is the Shannon entropy of the Born weights |a|^2, |b|^2.
C1 null: no copying (N = 0 CNOTs, environment untouched): I(S:F) = 0 for all f.
C2 [M] Only one basis is copied: the fragment holds no information about S's X-basis value: a single environment qubit's state is the same whether S was prepared as |+> or |->  (trace distance < 1e-12).
