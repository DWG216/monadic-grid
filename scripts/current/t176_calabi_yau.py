"""t176: the clock of three as heterotic geometry: chi of the Tian-Yau cover, the Z3 Wilson line on E6, families per block.
Pre-registration: PREDICTIONS_t176.md."""
import numpy as np
from fractions import Fraction as F

D = 3   # polynomials in H1, H2 truncated at H1^4 = H2^4 = 0 on P3 x P3
def mul(a, b):
    c = [[F(0)]*(D + 1) for _ in range(D + 1)]
    for i in range(D + 1):
        for j in range(D + 1):
            if a[i][j] == 0: continue
            for k in range(D + 1 - i):
                for l in range(D + 1 - j):
                    c[i + k][j + l] += a[i][j]*b[k][l]
    return c
def lin(c0, c1, c2):
    p = [[F(0)]*(D + 1) for _ in range(D + 1)]; p[0][0] = F(c0); p[1][0] = F(c1); p[0][1] = F(c2); return p
def inv(p):  # 1/(1 + x) with x nilpotent (degree >= 1)
    x = [[-p[i][j] if (i, j) != (0, 0) else F(0) for j in range(D + 1)] for i in range(D + 1)]
    out = lin(1, 0, 0); term = lin(1, 0, 0)
    for _ in range(2*D):
        term = mul(term, x); out = [[out[i][j] + term[i][j] for j in range(D + 1)] for i in range(D + 1)]
    return out
def power(p, n):
    out = lin(1, 0, 0)
    for _ in range(n): out = mul(out, p)
    return out

conf = [(3, 0), (0, 3), (1, 1)]
c = mul(power(lin(1, 1, 0), 4), power(lin(1, 0, 1), 4))
for d1, d2 in conf: c = mul(c, inv(lin(1, d1, d2)))
c3 = [[c[i][j] if i + j == 3 else F(0) for j in range(D + 1)] for i in range(D + 1)]
top = c3
for d1, d2 in conf: top = mul(top, lin(0, d1, d2))
chi = top[3][3]                                              # coefficient of H1^3 H2^3
print('P1', dict(chi_cover=int(chi), pass_=chi == -18))

# E6 under SU(3)_C x SU(3)_L x SU(3)_R; W = centre element omega of SU(3)_C acts on (a,b,c) by omega^(trial(a))
w = np.exp(2j*np.pi/3); tri = {'1': 0, '3': 1, '3b': 2, '8': 0}
dims = {'1': 1, '3': 3, '3b': 3, '8': 8}
adj = [('8', '1', '1'), ('1', '8', '1'), ('1', '1', '8'), ('3', '3', '3'), ('3b', '3b', '3b')]
f27 = [('3', '3b', '1'), ('1', '3', '3b'), ('3b', '1', '3')]
def phase(rep): return w**tri[rep[0]]
dim78 = sum(dims[a]*dims[b]*dims[c] for a, b, c in adj); dim27 = sum(dims[a]*dims[b]*dims[c] for a, b, c in f27)
unbroken = sum(dims[a]*dims[b]*dims[c] for a, b, c in adj if abs(phase((a, b, c)) - 1) < 1e-12)
order = next(n for n in range(1, 10) if all(abs(phase(r)**n - 1) < 1e-12 for r in adj + f27))
labels = [round(np.angle(phase(r))/(2*np.pi/3)) % 3 for r in f27]
# u(1) factors: the unbroken algebra is the sum of the invariant irreducible pieces; a u(1) would be an invariant singlet (1,1,1)
u1 = sum(1 for r in adj if r == ('1', '1', '1'))
P2 = dim78 == 78 and dim27 == 27 and order == 3 and unbroken == 24 and u1 == 0 and sorted(labels) == [0, 1, 2]
print('P2', dict(dim78=dim78, dim27=dim27, order_W=order, unbroken_dim=unbroken, u1_factors=u1, block_labels=labels, pass_=P2))

# Free Z3: Lefschetz numbers of g, g^2 vanish, so each character sector carries chi/3 of the quotient's cover; net families
G = 3; chi_q = int(chi)//G
lef = {0: int(chi), 1: 0, 2: 0}                               # traces of 1, g, g^2 on cohomology (alternating)
sector = [sum(lef[k]*np.conj(w**(k*m)) for k in range(G)).real/G for m in range(G)]
families_per_block = [-s/2 for s in sector]
P3 = chi_q == -6 and all(abs(f - 3) < 1e-12 for f in families_per_block)
print('P3', dict(chi_quotient=chi_q, sector_chi=sector, net_families_per_block=families_per_block, pass_=P3))
