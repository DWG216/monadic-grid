"""t96 post hoc (after scoring; motivated by JUNO's pull on TM2; labelled): does the grid's hand swap extend A4 to S4, and which S4 residual gives TM1?"""
import numpy as np, itertools
p = 3
pts = [(0, 1), (1, 0), (1, 1), (1, 2)]                      # P^1(F3)
def act(M, v):
    x = ((M[0][0]*v[0] + M[0][1]*v[1]) % p, (M[1][0]*v[0] + M[1][1]*v[1]) % p)
    for c in (1, 2):
        y = ((x[0]*c) % p, (x[1]*c) % p)
        if y in pts: return pts.index(y)
SL = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(3), repeat=4) if (a*d - b*c) % 3 == 1]
Frob = ((1, 1), (0, 2))                                      # x -> x^3 on F9 = F3[phi], basis (1, phi): phi -> 1 - phi
def perm(M): return tuple(act(M, v) for v in pts)
G = {perm(M) for M in SL}; Gf = set(G); frontier = list(G)
while frontier:
    g = frontier.pop()
    for h in list(Gf) + [perm(Frob)]:
        k = tuple(g[i] for i in h)
        if k not in Gf: Gf.add(k); frontier.append(k)
fp = perm(Frob); fixed = sum(1 for i in range(4) if fp[i] == i)
print('image of SL(2,3) on P^1(F3):', len(G), '(A4 = 12)'); print('with the hand swap:', len(Gf), '(S4 = 24)'); print('hand swap as a permutation of 4 points fixes', fixed, '(a transposition fixes 2)')
# column moduli in the charged-lepton (DFT) basis for the 2-fold axes of S4 not in A4 (edge axes)
w = np.exp(2j*np.pi/3); F = np.array([[w**(j*k) for k in range(3)] for j in range(3)])/np.sqrt(3)
for ax in ((1, 1, 0), (1, -1, 0)):
    a = np.array(ax)/np.linalg.norm(ax); print('axis', ax, 'column |U|^2 =', np.round(np.abs(F.conj() @ a)**2, 4))
s13 = 0.02215; tm1 = 1 - 2/(3*(1 - s13)); print('TM1 sin^2 theta12 =', round(tm1, 4), 'pull vs JUNO 0.3092+-0.0087:', round((tm1 - 0.3092)/0.0087, 2))
