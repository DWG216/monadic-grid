import sys
import numpy as np
from core import *

print("twist homomorphism max err", hom_err)
# sanity: Dmat at j=1/2 reproduces U, and homomorphism at j=7/2
J1 = spin_ops(1)
print("D^{1/2}=U err", max(np.abs(Dmat(U, J1) - U).max() for U in U_phys))
J7 = spin_ops(7)
D7 = [Dmat(U, J7) for U in U_phys]
print("D^{7/2} hom err", max(np.abs(D7[i] @ D7[k] - D7[MT[i, k]]).max() for i in range(0, 120, 7) for k in range(120)))
print("tau60 = -i n.sigma check", np.abs(T60 - (n_tau[0]*X + n_tau[1]*Y + n_tau[2]*Z)).max(),
      "is tau60*(-i) in 2I?", min(np.abs(U_phys - (-1j)*T60).reshape(120,-1).max(1)))

# Task 1
first = {}
ms = {}
for N in range(1, 141, 2):
    m = mult(N)
    ms[N] = m
    mi = int(round(m))
    assert abs(m - mi) < 1e-9
    for t in range(1, 6):
        if mi >= t and t not in first:
            first[t] = N
print("first N with m>=t:", first)
print("m(N) table:", {N: int(round(v)) for N, v in ms.items()})
print("first N with m==t exactly:", {t: min([N for N in ms if round(ms[N]) == t], default=None) for t in range(1, 6)})
