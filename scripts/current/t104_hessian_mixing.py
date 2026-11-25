"""t104: Hessian group (648) in SU(3); Klein residuals with <C, K> = G; fixed mixing. Pre-registration: PREDICTIONS_t104.md."""
import numpy as np, itertools
w = np.exp(2j*np.pi/3); e = np.exp(4j*np.pi/9)
C = np.roll(np.eye(3), 1, axis=0).astype(complex); D = np.diag([1, w, w**2])
V = np.array([[w**(j*k) for k in range(3)] for j in range(3)])/(1j*np.sqrt(3)); U = np.diag([e, e, e*w])
def key(M): return tuple(np.round(M, 7).ravel())
def gen(gens, cap=5000):
    G = {key(np.eye(3)): np.eye(3, dtype=complex)}; fr = [np.eye(3, dtype=complex)]
    while fr:
        g = fr.pop()
        for h in gens:
            k = g @ h; kk = key(k)
            if kk not in G: G[kk] = k; fr.append(k)
            if len(G) > cap: return list(G.values())
    return list(G.values())
G = gen([C, D, V, U]); D27 = gen([C, D])
out = {'S1': dict(order=len(G), D27=len(D27), pass_=len(G) == 648 and len(D27) == 27)}
inv = [g for g in G if np.allclose(g @ g, np.eye(3)) and not np.allclose(g, np.eye(3))]
klein = []
for a, b in itertools.combinations(inv, 2):
    if np.allclose(a @ b, b @ a) and not np.allclose(a @ b, np.eye(3)) and np.allclose((a @ b) @ (a @ b), np.eye(3)):
        K = {key(a), key(b), key(a @ b)}
        if K not in [k[0] for k in klein]: klein.append((K, a, b))
wC, UC = np.linalg.eig(C)
res = []
for K, a, b in klein:
    if len(gen([C, a, b], cap=700)) != len(G): continue
    # common eigenbasis of the Klein group
    M = a + 2*b; _, UK = np.linalg.eig(M)
    P = np.abs(UC.conj().T @ UK)**2
    best = None
    for rows in itertools.permutations(range(3)):
        for cols in itertools.permutations(range(3)):
            Q = P[np.ix_(rows, cols)]
            s13 = Q[0, 2]; s12 = Q[0, 1]/(1 - s13) if s13 < 1 else 1; s23 = Q[1, 2]/(1 - s13) if s13 < 1 else 1
            score = abs(s13 - 0.0222) + abs(s12 - 0.309) + abs(s23 - 0.5)
            if best is None or score < best[0]: best = (score, s13, s12, s23)
    res.append(best[1:])
uniq = sorted({tuple(np.round(r, 5)) for r in res})
ok = [r for r in uniq if 0.0205 <= r[0] <= 0.0240 and 0.283 <= r[1] <= 0.335 and 0.430 <= r[2] <= 0.596]
out['P1'] = dict(n_klein=len(klein), n_generating=len(res), patterns=uniq, viable=ok, pass_=bool(ok))
for k, v in out.items(): print(k, v)
