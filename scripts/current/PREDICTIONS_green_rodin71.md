# Pre-registration (2026-11-21): Green cusp characters along the Fibonacci walk; Millington's mod-71 Rodin circuit
Tiers: [id] identity, [real] test.
G1 [id] Q^n = [[F(n+1),F(n)],[F(n),F(n-1)]], so Q^n is central (scalar) mod p iff F(n) = 0 mod p (the gates).
G2 [real] Conjugacy type of Q^n (Q^n non-central) is: elliptic for every n when (5/p) = -1 (circle primes), split semisimple when (5/p) = +1 (hyperbola), non-semisimple (unipotent type) when p = 5 (two lines). 100% agreement for all primes 7 <= p < 200. Null: random non-scalar matrices M; the type of M predicted from (5/p) matches only about half the time.
G3 [real] Green's formula for the cuspidal character chi_theta of GL2(F_p) (central aI: (p-1)theta(a); a*unipotent: -theta(a); split: 0; elliptic with eigenvalues z, z^p: -(theta(z)+theta(z^p))) gives <chi,chi> = 1 summed over all of GL2(F_p) for p = 5, 7, 11.
G4 [real] Along the walk n -> Q^n: split primes: chi_theta(Q^n) = 0 except at gates; circle primes: |chi| <= 2 off gates and |chi| = p-1 at gates; period of n -> chi_theta(Q^n) equals pi(p) for theta faithful on F_(p^2)*.
G5 [real] For theta = identity-valued "trace" (replace theta by the inclusion into F_(p^2)), -chi(Q^n) = L(n) mod p off gates for circle primes (the formula pair is the trace shape of the cusp character).
R71a [id] mod 71: 9^2 = 9 + 1 and 8 = 9^-1 (9 is a golden ratio mod 71, 8 = 1/phi).
R71b [real] ord(9) = 35 mod 71, <9> = the 35 quadratic residues, 7 is a non-residue, so Millington's "two systems of 35 nodes" are the squares and non-squares mod 71 (the quadratic character, same structure as Rodin's wires mod 9 = character mod 3).
R71c [real] General: for split primes p < 2000 (p = +-1 mod 5), stepping by phi mod p gives a two-wire coil (phi generates exactly the squares) iff ord(phi) = (p-1)/2. Predict this happens for roughly a quarter to a half of split primes and never when p = 1 mod 4 and ... (no further structure predicted).
