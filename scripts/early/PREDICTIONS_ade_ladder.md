# Pre-registered before running ade_ladder.py (2026-11-08 ~23:35 ET)
Grid question: why does the ladder of finite golden/sky frames stop at E8, and is it the same reason the sky-sphere tiling stops?
A1 [math, identity]: the Y-shaped diagram T(2,3,n) (arms of 2, 3, n nodes counted from the centre) has Cartan determinant 9 - n... 
   precisely: det = 6 - n + 3?  We fix it by known values: E6 (n=3) 3, E7 (n=4) 2, E8 (n=5) 1, affine E8 (n=6) 0, n=7 negative.
   Prediction: positive definite (finite Lie type) exactly for n <= 5: the same condition 1/2 + 1/3 + 1/n > 1 as the sphere tiling.
A2 [math, calculation]: McKay graphs (tensor with the 2-dim spin rep) of the binary groups 2T (24), 2O (48), 2I (120) are affine E6, E7, E8:
   9, 8, 7 ... number of irreps 7, 8, 9; irrep dimensions equal the affine node marks; Perron eigenvalue exactly 2.
A3 [math]: braid levels map onto the rungs by crossing order n: level 4 (n=3) -> E6, Ising (n=4) -> E7, level 8 (n=5) -> E8;
   Fibonacci (n=10) -> T(2,3,10), indefinite: no finite rung.

# Scored after run (2026-11-08)
A1 PASS: det T(2,3,n) = 6 - n (n=2..10); positive definite exactly for n <= 5 (E6, E7, E8); n=6 is affine E8 (det 0); n >= 7 indefinite.
   Same inequality 1/2+1/3+1/n > 1 as the sphere tiling.
A2 PASS (after fixing a phase bug for 2T's complex characters): 2T 7 irreps dims 1,1,1,2,2,2,3 arms (2,2,2) = affine E6;
   2O 8 irreps 1,1,2,2,2,3,3,4 arms (1,3,3) = affine E7; 2I 9 irreps 1,2,2,3,3,4,4,5,6 arms (1,2,5) = affine E8. Perron 2; dims = Perron vector.
A3 (math by the same inequality): level 4 -> E6, Ising -> E7, level 8 -> E8, Fibonacci (n=10) -> indefinite T(2,3,10).
