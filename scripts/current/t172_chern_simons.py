"""t172: the grid's binary groups fix SU(2) Chern-Simons levels and their exceptional modular invariants.
Pre-registration: PREDICTIONS_t172.md."""
import numpy as np, itertools

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return np.array([a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0])
def key(q): return tuple(np.round(q, 9) + 0.0)
def closure(gens):
    G = {key(np.array([1., 0, 0, 0])): np.array([1., 0, 0, 0])}
    frontier = list(G.values())
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                p = qmul(g, h); k = key(p)
                if k not in G: G[k] = p; new.append(p)
        frontier = new
    return list(G.values())
def conj(q): return np.array([q[0], -q[1], -q[2], -q[3]])

phi = (1 + 5**0.5)/2
groups = {'2T': [np.array([0., 1, 0, 0]), np.array([.5, .5, .5, .5])],
          '2O': [np.array([2**-.5, 2**-.5, 0, 0]), np.array([.5, .5, .5, .5])],
          '2I': [np.array([.5, .5, .5, .5]), np.array([phi/2, 1/(2*phi), .5, 0])]}
expect = {'2T': ('E6', 12, [1, 4, 5, 7, 8, 11], [2, 2, 1]), '2O': ('E7', 18, [1, 5, 7, 9, 11, 13, 17], [3, 2, 1]),
          '2I': ('E8', 30, [1, 7, 11, 13, 17, 19, 23, 29], [4, 2, 1])}

def char_table(G):
    idx = {key(g): i for i, g in enumerate(G)}; n = len(G)
    cls = [-1]*n; classes = []
    for i, g in enumerate(G):
        if cls[i] >= 0: continue
        orb = {idx[key(qmul(qmul(h, g), conj(h)))] for h in G}
        for j in orb: cls[j] = len(classes)
        classes.append(sorted(orb))
    r = len(classes); size = np.array([len(c) for c in classes])
    mult = np.array([[idx[key(qmul(G[a], G[b]))] for b in range(n)] for a in range(n)])
    M = np.zeros((r, r, r))                                   # M[i][j,k] = c_ij^k
    for i in range(r):
        for j in range(r):
            for a in classes[i]:
                for b in classes[j]:
                    M[i, j, cls[mult[a, b]]] += 1
            M[i, j] /= size                                   # each z in C_k counted |C_k| times
    rng = np.random.default_rng(1720)
    X = np.tensordot(rng.normal(size=r), M, axes=1)
    w, V = np.linalg.eig(X)
    e = cls[idx[key(np.array([1., 0, 0, 0]))]]
    chars = []
    for t in range(r):
        om = V[:, t]/V[e, t]
        d = np.sqrt(n/np.sum(np.abs(om)**2/size))
        chars.append(d*om/size)
    rep = np.array([G[c[0]] for c in classes])
    return np.array(chars), size, rep, n

out = {}
for name, gens in groups.items():
    G = closure(gens); ch, size, rep, n = char_table(G)
    chiV = 2*rep[:, 0]
    dims = np.real(ch[:, np.argmax(rep[:, 0])])               # identity class has q0 = 1
    A = np.real(np.array([[np.sum(size*chiV*ca*np.conj(cb))/n for cb in ch] for ca in ch]))
    A = np.round(A).astype(int)
    triv = int(np.argmin(np.abs(dims - 1) + np.abs(np.real(ch).sum(1) - len(size))))   # trivial: all ones
    triv = [t for t in range(len(dims)) if np.allclose(ch[t], 1)][0]
    keep = [t for t in range(len(dims)) if t != triv]
    Af = A[np.ix_(keep, keep)]
    ev = np.sort(np.linalg.eigvalsh(Af))[::-1]
    h = int(round(np.pi/np.arccos(ev[0]/2)))
    expo = sorted(int(round(h*np.arccos(x/2)/np.pi)) for x in ev)
    deg = Af.sum(1); branch = int(np.argmax(deg))
    arms = []
    for nb in np.where(Af[branch] > 0)[0]:
        L, prev, cur = 1, branch, nb
        while True:
            nxt = [x for x in np.where(Af[cur] > 0)[0] if x != prev]
            if not nxt: break
            prev, cur = cur, nxt[0]; L += 1
        arms.append(L)
    arms = sorted(arms, reverse=True)
    out[name] = dict(order=n, nodes=len(keep), max_degree=int(deg.max()), arms=arms, sum_dims=int(round(dims.sum())), h=h, exponents=expo)
    print(name, out[name])
P1 = all(out[g]['order'] == o and out[g]['nodes'] == len(expect[g][2]) and out[g]['arms'] == expect[g][3] and out[g]['sum_dims'] == expect[g][1]
         and out[g]['h'] == expect[g][1] and out[g]['exponents'] == expect[g][2] for g, o in (('2T', 24), ('2O', 48), ('2I', 120)))
print('P1', dict(pass_=P1))

def invariants(k):
    n = k + 1; lam = np.arange(n)
    S = np.sqrt(2/(k + 2))*np.sin(np.pi*np.outer(lam + 1, lam + 1)/(k + 2))
    hw = lam*(lam + 2)/(4*(k + 2))
    slots = [(a, b) for a in range(n) for b in range(n) if abs((hw[a] - hw[b]) - round(hw[a] - hw[b])) < 1e-9]
    m = len(slots); L = np.zeros((n*n, m))
    for s, (a, b) in enumerate(slots):
        E = np.zeros((n, n)); E[a, b] = 1
        L[:, s] = (S @ E - E @ S).ravel()
    _, sv, Vt = np.linalg.svd(L)
    null = Vt[np.sum(sv > 1e-9):].T                          # m x d
    d = null.shape[1]
    _, _, piv = __import__('scipy.linalg', fromlist=['qr']).qr(null.T, pivoting=True)
    pv = list(piv[:d]); i00 = slots.index((0, 0))
    if i00 not in pv: pv[-1] = i00
    B = null[pv]                                              # d x d
    sols = []
    for vals in itertools.product((0, 1, 2), repeat=d):
        vals = np.array(vals, float)
        if vals[pv.index(i00)] != 1: continue
        try: c = np.linalg.solve(B, vals)
        except np.linalg.LinAlgError: continue
        x = null @ c
        if np.all(np.abs(x - np.round(x)) < 1e-7) and np.all(np.round(x) >= 0):
            Mx = np.zeros((n, n))
            for s, (a, b) in enumerate(slots): Mx[a, b] = round(x[s])
            if np.abs(S @ Mx - Mx @ S).max() < 1e-10: sols.append(Mx)
    return sols, d

diag_sets = {}
for k in range(1, 31):
    sols, d = invariants(k)
    diag_sets[k] = [sorted(int(l + 1) for l in range(k + 1) if M[l, l] > 0) for M in sols]
    print('k=%d commutant_dim=%d invariants=%d' % (k, d, len(sols)), [ds for ds in diag_sets[k] if len(ds) < k + 1])
P2 = {g: expect[g][2] in diag_sets[expect[g][1] - 2] for g in expect}
P3 = {g: [k for k in diag_sets if expect[g][2] in diag_sets[k] and k != expect[g][1] - 2] for g in expect}
print('P2', dict(found=P2, pass_=all(P2.values())))
print('P3', dict(other_levels=P3, pass_=all(len(v) == 0 for v in P3.values())))
print('reported', {n: dict(k=n - 2, qdim_half=2*np.cos(np.pi/n)) for n in (3, 5)})
