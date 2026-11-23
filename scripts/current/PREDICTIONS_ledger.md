# Pre-registration (2026-11-22, 04:30): the fermionic ledger of a Boolean function
Definition: on the Boolean lattice, d(x) = the largest number of value changes of f along an increasing chain from 0^n to x (d(0) = 0; d(x) = max over y covered by x of d(y) + [f(y) != f(x)]). Alternation a(f) = max d. Layers m_i(x) = [d(x) >= i], i = 1..a(f).
L1 [identity] every m_i is monotone, m_1 >= m_2 >= ..., and f(x) XOR f(0) = sum_i (-1)^(i+1) m_i(x) = (1 - (-1)^d(x))/2: f is the parity of a counter of sign flips, an alternating sum of nested monotone (bosonic) layers. Checked for all 65,536 functions of 4 variables and 2,000 random functions each of 5..8 variables.
L2 [identity] no nested monotone XOR representation has fewer than a(f) layers (along a chain of a(f) changes each change needs a new layer): checked by brute force for all functions of 3 variables.
L3 [M, known] parity of n bits has a = n (every step flips: the Boolean Liouville function, lambda = (-1)^Omega on the divisor lattice of a squarefree number); majority and every monotone f have a = 1 (f(0) = 0); Markov: a function needs ceil(log2(a(f)+1)) NOT gates, so parity needs ceil(log2(n+1)), Fischer's count.
L4 [exploratory] distribution of a(f) over all functions of 4 variables.
AMENDMENT (after L1-L4 ran, before saving): L5 [identity] for f(0) = 0, the paired layers b_j = m_(2j-1) AND NOT m_(2j) are disjoint and their OR is f; each b_j is convex (monotone AND antimonotone), a band between an upward and a downward set.

## Results (ledger.py): all pass
L1 PASS (65,536 four-variable functions; 8,000 random five- to eight-variable functions). L2 PASS (all 3-variable functions with f(0) = 0: minimal number of nested layers = alternation). L3: parity a = n (n = 3, 4, 5, 8; NOT gates 2, 3, 3, 4 = ceil(log2(n+1))); majority a = 1. L4 histogram of a over 4-variable functions: 0: 2, 1: 332, 2: 7,208, 3: 32,436, 4: 25,558. L5 PASS.
