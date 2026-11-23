# Pre-registration (2026-11-21): Millington pp. 104-125 (video IMG_0569, 55 s flip-through)
P1 [id] EQN 10 (p. 107): F(x)F(-x) - (-1)^r F(x-r)F(-(x+r)) = F(r)F(-r) for all integers x, r.
P2 [id] EQN 11 (p. 113): (-1)^a F(x-a)F(-(x+a)) - (-1)^r F(x-r)F(-(x+r)) = (-1)^a F(r-a)F(-(r+a)) for all x, r, a (EQN 10 is a = 0).
P3 [id] Normalised tables (pp. 109-111): entry (r, k) = c_k - c_r with c_k = F(k)F(-k) = (-1)^(k+1) F(k)^2, constant down every column; and c_k - c_r = +-F(k+r)F(k-r) (the Catalan identity in table form).
P4 [id] EQN 12 (p. 120) for balanced U = m F and m L: holds with CI_U = |Cassini| (49 for 7F, 245 for 7L = 49 * 5); Lucas tables = 5 x Fibonacci tables (p. 116).
P5 [real] For unbalanced U (U0, U1 = 1, 6 and 1, 4) the reflected normalised columns are still constant in x but are NOT CI_U * (c_k - c_r) (p. 120: "this relationship cannot be perceived").
P6 [id] p. 125 "modified-lite Catalan": U(x-r)U(x+r) - U(x-a)U(x+a) = (-1)^(x-r) CI_U F(a-r)F(a+r) for every U with U(n+1) = U(n) + U(n-1), with CI_U = U1^2 - U0 U1 - U0^2 (= the norm e, sign as in section 50).
P7 [real] Reading of p. 230 columns: Millington's unbalanced component table uses the pairing U(x-k)U(-(x+k)) for k = 0, 2, 3, 5 but the mirrored pairing U(x+k)U(-(x-k)) for k = 1 and 4; with a single pairing his r = 0 row would read 0, 26, -15, 82, -168, 485 instead of 0, 37, -15, 82, -399, 485. (Tentative: read from photos.)
P8 [id] pp. 104-105: the 20 powers of 2 and of 13 mod 25 in balanced form; 2 * 13 = 26 = 1 and F(3)F(-7) - F(5)F(-5) = 26 - 25 = 1.

## Results (2026-11-21)
P1 pass. P2 pass. P3 pass (matrix 0,1,-1,4,-9,25 shifted by row; |entries| = F(k+r)F(k-r)). P4 pass (7F: 49, 7L: 245, L: 5).
P5 pass: unbalanced columns constant; r = 0 row is c_k(U) = U0^2 - (-1)^k U(-k)^2, not e*c_k.
P6 FAIL as photographed: sign exponent must be (x-a), not (x-r). Post-hoc correct forms (verified for F, L, U(1,6), U(1,4), U(3,-7)):
  U(x-r)U(x+r) - U(x-a)U(x+a) = (-1)^(x-a) e F(a-r)F(a+r) = (-1)^(x-r) (-e) F(r-a)F(a+r), e = U1^2 - U0U1 - U0^2.
  So Millington's line is right if CI_U is the signed Cassini U(-1)U(1) - U(0)^2 = -e and the first factor is F(r-a). Possibly a reading/sign-convention issue.
P7 pass: mixed pairing reproduces his row exactly (0, 37, -15, 82, -399, 485).
P8 pass: 2*13 = 26 = 1 mod 25; F(3)F(-7) - F(5)F(-5) = 1.
