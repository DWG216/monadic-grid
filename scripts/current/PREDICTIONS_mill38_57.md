# Pre-registration (2026-11-21, evening): Millington pp. 38-57 (video IMG_0573)
S1 [id] p.40 five equations (i) F(-2) = F(0)^2 - F(-2)^2, (ii) F(-1) = F(0)^2 + F(-1)^2, (iii) F(0) = F(1)^2 - F(-1)^2, (iv) F(1) = F(1)^2 + F(0)^2, (v) F(2) = F(2)^2 - F(0)^2 are the n = -1, 0, 1 cases of F(2n-1) = F(n)^2 + F(n-1)^2 and F(2n) = F(n+1)^2 - F(n-1)^2. With F(0) = 0 each self-referential one is a quadratic with roots {0, his value}: his "may not be the only solutions" = the other root is 0.
S2 [id] p.41-42: with F(2)c = F(2) + iF(0) and (v), F(2)c = F(2)c^2 + iF(0)(1 - 2F(2)) holds identically. So his Mandelbrot form is a FIXED-POINT equation z = z^2 + A, not an orbit. Prediction: his Fibonacci root z = 1 (F(0) = 0) is the repelling fixed point of z^2 (|2z| = 2, on the Julia set, the unit circle); the other root 0 is attracting.
S3 [id] Golden link: x^2 = x + 1 <=> x = x^2 - 1, so phi and -1/phi are the fixed points of the Mandelbrot map at c = -1 (centre of the period-2 bulb, the "basilica"); both repelling (|2x| = 3.24, 1.24); the attracting orbit there is the 2-cycle 0 <-> -1.
S4 [real] Fibonacci in the Mandelbrot set (known theorem; our numerical check): the bulb attached to the main cardioid at internal angle p/q has period q. Along the golden angle's convergents F(n-1)/F(n) the periods are 2, 3, 5, 8, 13, 21 (one numerical probe per bulb, just outside the cardioid point). Null: a probe at a non-Fibonacci angle 2/7 gives 7.
S5 [id] p.44-45 EQN 6 "0 = (1+1)(1-1) = 2 x 0" is F(0) = (F(1)+F(-1))(F(1)-F(-1)) = L(0) F(0), the n = 0 case of F(2n) = F(n)L(n); his "2 = 0/0" is the limit value: with continuous Binet F(t) = (phi^t - cos(pi t) phi^-t)/sqrt5, F(2t)/F(t) -> 2 as t -> 0 (R3: a value at the gate defined only by the limit).
S6 [id] p.49-52 EQN 9 and EQN 10 worked examples (x = 4, 7; x = 5 r = 2; x = 10 r = 3; x = 0 r = 1) all evaluate as printed: 1, 1, -1, 4, 0.
S7 [real] p.57 system F(-1) = F(0)^2 + F(-1)^2, F(0) = F(1)^2 - F(-1)^2, F(1) = F(1)^2 + F(0)^2 (no initial conditions): exactly two real solutions, (0,0,0) (vacuum) and (1,0,1) (Fibonacci); any others complex.

## Results
S1 pass. S2 pass (residual 3e-15; Fibonacci root z = 1 repelling, 0 attracting). S3 pass (c = -1 orbit settles on the 2-cycle 0, -1). S4 pass: periods 2, 3, 5, 8, 13, 21 at angles 1/2, 2/3, 3/5, 5/8, 8/13, 13/21; null 2/7 gives 7. S5 pass: F(2t)/F(t) = 2.56, 2.096, 2.010, 2.0001 at t = 0.1 .. 1e-5. S6 pass (x = 0, r = 1 is the p.54 rewritten form, = 0 = F(0)^2).
S7 FAIL as predicted (2 real solutions) -> 4 real solutions, all exact:
  (0, 0, 0) vacuum; (1, 0, 1) Fibonacci; (1/(phi sqrt5), 1/sqrt5, phi/sqrt5) = the pure growing Binet mode phi^n/sqrt5; (phi/sqrt5, -1/sqrt5, 1/(phi sqrt5)) = the pure reversing mode -psi^n/sqrt5 (psi = -1/phi).
  Each pure mode satisfies every doubling formula by itself; Fibonacci is their sum; F(0) = 0 is their cancellation (1/sqrt5 - 1/sqrt5). Scaled modes fail (the system is not linear), so the four solutions are exactly {0, 1} x {0, 1} combinations of the two modes.

## Addendum (2026-11-21, 20:30; stills of pp. 44-45, 58-69)
Correction: the p.44 equation "0 = (1+1)(1-1) = (0)(2)" is EQN 8 (the video frame was misread as EQN 6).
S8 [built-in, from the S7 case analysis; added after S7, so not a test] p.58's resolution "assign 1 and 1 to F(1) and F(-1)" is the mirror condition F(1) = F(-1). Under it the p.57 system keeps exactly two solutions, vacuum (0,0,0) and Fibonacci (1,0,1); the two pure Binet modes are excluded because they are not mirror-symmetric.
