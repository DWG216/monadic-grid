# t53 what the Fibonacci step generates inside the 216 (pre-registered 2026-11-23, before run)
Q = [[0,1],[1,1]] (Fibonacci step, = multiplication by phi on F9 = F3(phi), basis 1, phi); s = Galois swap phi <-> 1-phi; U = [[1,1],[0,1]] (counting step); T = the 9 shifts of F3^2.
G1 <Q>: order 8, all of F9* (Q is a Singer cycle) because x^2-x-1 is irreducible mod 3.
G2 <Q, s>: order 16; G2 inside SL(2,3): order 8, quaternion (one element of order 2).
G3 <Q^2, U>: order 24 = SL(2,3).
G4 <Q, U>: order 48 = GL(2,3).
Affine: T with <Q>: 72; T with G3: 216 = Hessian (= ASL(2,3)); T with G4: 432.
Control: <Q^2> with a different order-4 element alone (no U) stays inside a 2-group (order divides 16).
