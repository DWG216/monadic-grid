# Pre-registration (2026-11-22, 13:55): what [Z, Zbar] = hbar says, checked (record §78)
Twistor Z = (omega^A, pi_A'), omega = i x pi (x a 2x2 matrix: the spacetime point). Hermitian form Sigma(Z) = Z.Zbar = 2 Re(pi^dagger omega) (signature 2+2). Euler (scaling) operator Upsilon = Z^alpha d/dZ^alpha. Quantised (symmetric ordering, Zbar -> -hbar d/dZ): helicity s = -(Upsilon + 2)/2.
T1 [identity] real points (x Hermitian): Sigma(Z) = 0 for every pi (100 random cases): real light rays are exactly the null twistors, the plane PN.
T2 [identity] complex points with Im x positive definite (the forward tube): Sigma(Z) < 0 for every pi; Im x negative definite: Sigma > 0 (100 cases each): the two halves PT- and PT+.
T3 [identity] incidence = light: the twistor lines of points x and y meet iff det(x - y) = 0 (x - y null); 50 null and 50 generic pairs.
T4 [identity] the §76 function f = 1/((alpha.Z)^3 (beta.Z)^3) has Upsilon f = -6 f (finite differences, 20 points), so s = -(-6 + 2)/2 = +2: the helicity of the graviton field checked in §76.

## Results (twistor_pairing.log): all pass
T1 max |Sigma| 1.8e-15. T2 both signs as predicted. T3 pass (50 null, 50 generic). T4 Upsilon f / f = -6 to 1.7e-9.
