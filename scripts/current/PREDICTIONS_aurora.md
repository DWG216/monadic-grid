# Pre-registration: Aurora Equation check (2026-11-21)
Tier labels: [id] identity, [num] numerical check of a stated value.
A1 [num] D = phi^2 ln(1 + zeta(phi)) != 2.914 as the paper states; we expect about 3.08.
A2 [num] D' = 1/(phi^2 ln(1 + sum_{n<=10} n^phi)) is about 0.0735 (paper: 0.077).
A3 [num] D*D' is not close to 1 (paper hopes ~1).
A4 [id] The mirror s -> 1-s maps phi to its Galois conjugate 1-phi = -1/phi, and -phi to phi^2. Completed Lambda(s) = pi^(-s/2) Gamma(s/2) zeta(s) agrees at both pairs to < 1e-9, with zeta at negative s computed independently by Euler-Maclaurin (not from the functional equation).
A5 [id] zeta(phi) * sum mu(n) n^(-phi) = 1 to < 1e-4 (truncated Mobius sum): the exact reciprocal pair the paper's D*D' was reaching for.
Null for A4: Lambda(phi) vs Lambda(-phi) (not mirror images) differ by more than 10%.
