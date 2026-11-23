# Pre-registration (2026-11-22, 04:20): Boolean polymorphisms (identity check of the chain in record §66)
All Boolean operations of arity 2 and 3, tested coordinatewise on every tuple choice from each relation.
Q1 [identity] 3-SAT (all 8 clause relations of arity 3): only the projections (2 binary, 3 ternary).
Q2 [identity] Schaefer's easy classes each have a non-projection law: 2-SAT has majority; 3-XOR (x+y+z = 0 and = 1) has minority x+y+z; Horn has AND; dual Horn has OR; 0-valid has constant 0; 1-valid has constant 1.
Q3 [identity] each such law fails for 3-SAT (no law of any easy class survives).

## Results (polymorphisms.py): all pass
Q1: 3-SAT has exactly 2 binary and 3 ternary polymorphisms, all projections. Q2: majority (2-SAT), minority (3-XOR), AND (Horn), OR (dual Horn), constants (0-, 1-valid) each preserve their class. Q3: none preserves 3-SAT.
