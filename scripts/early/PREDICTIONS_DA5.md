# Pre-registered before running da5.py (2026-11-08)
Question: does the doubled icosahedral phase D(A5) "do the aether's work through the boundary alone"? Where does its non-classical
(golden) content enter: braiding or measurement?

Background (from memory, to be labelled so): Property F conjecture (Naidu-Rowell): braid-group images are finite iff the theory is
weakly integral (all d^2 integers); proven for group-theoretical categories such as D(G) (Etingof-Rowell-Witherspoon). Mochon: D(G) for
non-solvable G (A5 smallest) is universal with braiding + fusion/charge measurement + ancillas.

Q1 [identity]: A5 has 5 conjugacy classes (sizes 1,15,20,12,12) and irreps of dims 1,3,3',4,5; D(A5) has 22 anyon types; every anyon
   quantum dimension (class size x irrep dim of centralizer) is an integer; total D^2 = |A5|^2 = 3600.
Q2 [real test]: pure-flux braiding of 3 fluxes from the 5-cycle class (total flux = identity) acts as PERMUTATIONS of the flux basis and
   generates a FINITE group (we report its order). Prediction: finite, and every braid maps basis states to basis states (classical).
Q3 [identity, the key point]: charge measurement on a flux pair = projecting the 12-dim permutation representation of A5 on its 5-cycles
   (1 + 3 + 3' + 5) onto an irrep. Prediction: the 3 and 3' projections are Galois twins: their amplitudes contain phi and -1/phi
   respectively (swapped), i.e. golden numbers appear ONLY through charge (Fourier) measurement, never through braiding.
Q4 [contrast, from earlier run]: Fibonacci (d = phi, not weakly integral) braids generate an infinite, dense set (16,704 distinct by length
   12, still growing).
Interpretation fixed in advance: if Q2 + Q3 hold, D(A5) is a frozen frame under braiding; its universality (Mochon) is supplied at the
measurement boundary, in the Fourier (charge) basis, carrying the golden numbers. This supports "universality enters through the boundary".
Scope stated: a full resource-cost race against tau60 distillation needs Mochon's gate constructions and is NOT attempted here.

# Scored after run (2026-11-08)
Q1 PASS: 22 anyons, all dims integers (1,3,3,4,5, 12x10, 15x4, 20x3), sum d^2 = 3600.
Q2 PASS: 60 three-flux configurations; braids act as permutations; image is a finite group of order 60. Braiding is classical here.
Q3 FAILED AS STATED: phi and -1/phi do not appear separately. Both projections show ratios +-1 and +-1/sqrt5 (sqrt5 = phi + 1/phi).
   POST-HOC (see output appended in conversation): the 3 and 3' projections have identical magnitudes and differ only in the SIGN of the
   1/sqrt5 components, i.e. the Galois twist acts as sqrt5 -> -sqrt5. Each charge outcome occurs with probability 1/4 and spreads the
   state over the flux basis; braiding never does.
Q4 (earlier run) stands. Cost race vs tau60: not attempted (scoped out in advance).
