"""t66: the Standard Model from cutting E6 at the meeting node. Pre-registration: PREDICTIONS_t66.md."""
import numpy as np, itertools, math
from collections import Counter

# ---------- 2T and its McKay graph (as in t55), with characters ----------
def qmat(a, b, c, d): return np.array([[a+1j*b, c+1j*d], [-c+1j*d, a-1j*b]])
def key(m): return tuple(np.round(np.concatenate([m.real.ravel(), m.imag.ravel()]), 6))
def close(gens):
    I = np.eye(2, dtype=complex); G = {key(I): I}; fr = [I]
    while fr:
        n = []
        for g in fr:
            for h in gens:
                x = g @ h; k = key(x)
                if k not in G: G[k] = x; n.append(x)
        fr = n
    return list(G.values())
T2 = close([qmat(0, 1, 0, 0), qmat(0, 0, 1, 0), qmat(.5, .5, .5, .5)])

def chartable(G):
    n = len(G); K = {key(g): i for i, g in enumerate(G)}; inv = [K[key(np.linalg.inv(g))] for g in G]
    mult = [[K[key(G[a] @ G[b])] for b in range(n)] for a in range(n)]
    cl = [-1]*n; C = []
    for a in range(n):
        if cl[a] >= 0: continue
        s = set(mult[mult[h][a]][inv[h]] for h in range(n)); C.append(sorted(s))
        for x in s: cl[x] = len(C)-1
    r = len(C); sz = np.array([len(c) for c in C])
    a = np.zeros((r, r, r))
    for I_ in range(r):
        for J in range(r):
            for k in range(r):
                z = C[k][0]; a[I_, J, k] = sum(1 for x in C[I_] if cl[mult[inv[x]][z]] == J)
    rng = np.random.default_rng(1); A = sum(rng.normal()*a[I_] for I_ in range(r))
    _, V = np.linalg.eig(A)
    e = next(i for i, c in enumerate(C) if np.allclose(G[c[0]], np.eye(2)))
    chars = []
    for v in V.T:
        om = v/v[e]; d = np.sqrt((n/np.sum(np.abs(om)**2/sz)).real); chars.append(d*om/sz)
    chars = np.array(chars); chiV = np.array([np.trace(G[c[0]]) for c in C])
    ip = lambda x, y: np.sum(sz*x*np.conj(y))/n
    Amk = np.round(np.real(np.array([[ip(chiV*ci, cj) for cj in chars] for ci in chars]))).astype(int)
    dims = np.round(np.real(chars[:, e])).astype(int)
    return chars, Amk, dims, ip

chars, Amk, dims, ip = chartable(T2)
def components(Adj, nodes):
    nodes = set(nodes); comps = []
    while nodes:
        s = nodes.pop(); comp = {s}; fr = [s]
        while fr:
            x = fr.pop()
            for y in np.where(Adj[x])[0]:
                if y in nodes: nodes.remove(y); comp.add(y); fr.append(y)
        comps.append(sorted(comp))
    return comps
def is_A(comp, Adj, n):   # path graph on n nodes
    sub = Adj[np.ix_(comp, comp)]; deg = sub.sum(1)
    return len(comp) == n and sub.sum()//2 == n-1 and max(deg) <= 2

res = {}
r = len(dims); i3 = [i for i in range(r) if dims[i] == 3]
arms = components(Amk, [i for i in range(r) if i != i3[0]])
res['G1'] = dict(n_dim3=len(i3), arms=[[int(dims[i]) for i in a] for a in arms],
                 pass_=len(arms) == 3 and all(is_A(a, Amk, 2) for a in arms) and all(sorted(dims[a]) == [1, 2] for a in arms))
# G2: tensor with nontrivial 1-dim characters
one = [i for i in range(r) if dims[i] == 1]
triv = next(i for i in one if np.allclose(chars[i], 1))
nontriv = [i for i in one if i != triv]
def tensor_map(c):
    m = {}
    for i in range(r):
        prod = chars[i]*chars[c]
        m[i] = next(j for j in range(r) if abs(ip(prod, chars[j])-1) < 1e-6)
    return m
g2 = []
for c in nontriv:
    m = tensor_map(c); armof = {x: k for k, a in enumerate(arms) for x in a}
    perm = [armof[m[a[0]]] for a in arms]
    consistent = all(armof[m[x]] == perm[k] for k, a in enumerate(arms) for x in a)
    g2.append(dict(perm=perm, consistent=consistent, fixes_none=all(perm[k] != k for k in range(3)), center_fixed=m[i3[0]] == i3[0]))
res['G2'] = dict(maps=g2, pass_=all(x['consistent'] and x['fixes_none'] and sorted(x['perm']) == [0, 1, 2] for x in g2))
# C1: remove a dimension-2 node
i2 = [i for i in range(r) if dims[i] == 2][0]
c1 = components(Amk, [i for i in range(r) if i != i2])
res['C1'] = dict(component_sizes=sorted(len(c) for c in c1), not_three_A2=not (len(c1) == 3 and all(len(c) == 2 for c in c1)))

# ---------- E6 roots (Bourbaki: 1-3-4-5-6 chain, 2 attached to 4) ----------
Acart = np.array([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
                  [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])
simple = [tuple(int(i == j) for j in range(6)) for i in range(6)]
pos = set(simple); layer = list(simple)
while layer:
    new = []
    for a in layer:
        av = np.array(a)
        for i in range(6):
            b = tuple(av + np.eye(6, dtype=int)[i])
            if b in pos: continue
            # b is a root iff a + alpha_i: use string: p - q = -<a, alpha_i^v>; p = how far a - k alpha_i stays a root
            p = 0; x = av.copy()
            while True:
                x = x - np.eye(6, dtype=int)[i]
                if tuple(x) in pos: p += 1
                else: break
            q = p - int(av @ Acart[:, i])
            if q > 0: pos.add(b); new.append(b)
    layer = new
pos = sorted(pos); roots = pos + [tuple(-np.array(a)) for a in pos]
marks = np.array([1, 2, 2, 3, 2, 1]); theta = max(pos, key=lambda a: sum(a))
res['sanity_roots'] = dict(n=len(roots), highest=theta, marks_ok=tuple(marks) == theta)

def kac(node_coeff_fn):
    grades = Counter(node_coeff_fn(np.array(a)) % 3 for a in roots)
    return {g: grades[g] for g in range(3)}
g3 = kac(lambda a: a[3])                    # s = 1 at central node (index 3 = node 4, mark 3)
res['G3'] = dict(fixed_roots=g3[0], dim_fixed=g3[0]+6, dim_w=g3[1], dim_w2=g3[2],
                 pass_=g3[0] == 18 and g3[1] == 27 and g3[2] == 27)
c2 = kac(lambda a: a[0])                    # s = 1 at end node 1 (mark 1), s0 = 2
res['C2'] = dict(dim_fixed=c2[0]+6, so10_u1=c2[0]+6 == 46)

# ---------- the 27 ----------
hw = np.array([1, 0, 0, 0, 0, 0]); W = {tuple(hw)}; fr = [hw]
while fr:
    n = []
    for l in fr:
        for i in range(6):
            if l[i] > 0:
                m = l - Acart[i]
                if tuple(m) not in W: W.add(tuple(m)); n.append(m)
    fr = n
W = [np.array(w) for w in sorted(W)]
res['sanity_27'] = len(W)
# arm labels: arms of the extended diagram minus node 4: (1,3), (5,6), (2,0)
def lab0(l): return -int(l @ marks)
armlabels = [lambda l: (l[0], l[2]), lambda l: (l[4], l[5]), lambda l: (l[1], lab0(l))]
TRIP = {(1, 0), (-1, 1), (0, -1)}; ATRIP = {(0, 1), (1, -1), (-1, 0)}
def kind(lbls):
    t = tuple(int(x) for x in lbls)
    return '3' if t in TRIP else ('3b' if t in ATRIP else ('1' if t == (0, 0) else '?'))
pattern = Counter(tuple(kind(f(l)) for f in armlabels) for l in W)
flip = {'3': '3b', '3b': '3', '1': '1'}
pattern_flip = Counter((flip[k[0]],) + k[1:] for k in pattern.elements())
res['G4_posthoc_arm1_relabelled'] = dict(pattern={','.join(k): v for k, v in pattern_flip.items()},
    all_3_3bar=all(sorted(k) == ['1', '3', '3b'] for k in pattern_flip) and all(v == 9 for v in pattern_flip.values()))
res['G4'] = dict(pattern={','.join(k): v for k, v in pattern.items()},
                 pass_=len(pattern) == 3 and all(v == 9 for v in pattern.values())
                 and all(sorted(k) in (['1', '3', '3b'],) for k in pattern))

# ---------- G5, G6: Standard Model inside ----------
arm_roots = [[0, 2], [4, 5], [1, None]]        # simple roots of each arm (None = alpha0 = -theta)
def rootvec(i): return -np.array(theta) if i is None else np.eye(6, dtype=int)[i]
def dynk(rv): return Acart.T @ rv              # Dynkin labels of a root given in simple-root coords
target = {('3', 2): [1/6]*3, ('3', 1): [-1/3]*3, ('3b', 1): [-2/3]*3 + [1/3]*6,
          ('1', 2): [-1/2, -1/2, 1/2], ('1', 1): [1, 0, 0]}   # coloured multiplets listed once per colour
best = None
for C, L in itertools.permutations(range(3), 2):
    for lroot in arm_roots[L]:
        cons = [dynk(rootvec(x)) for x in arm_roots[C]] + [dynk(rootvec(lroot))]
        # charges are q(l) = l . c with c orthogonal to the constraint roots' Dynkin vectors? No: q(alpha) = alpha_dynkin . c must vanish
        Ccons = np.array(cons, float); _, s, Vt = np.linalg.svd(Ccons); basis = Vt[np.sum(s > 1e-9):]
        a_l = rootvec(lroot); hL = None
        # group weights into SM multiplets
        def col(l): return kind(armlabels[C](l))
        lab_L = lambda l: int(l @ (Acart @ np.zeros(6)) ) if False else None
        t3 = lambda l: (l @ (np.linalg.inv(Acart.T).T @ dynk(a_l)) if False else None)
        # <l, alpha_L^v> for simply laced = l . a_l (Dynkin labels dotted with simple-root coords)
        pair = lambda l: int(l @ a_l)
        seen = set(); mults = []
        for l in W:
            if tuple(l) in seen: continue
            if pair(l) == 1: partner = l - dynk(a_l); size = 2
            elif pair(l) == -1: partner = l + dynk(a_l); size = 2
            else: partner = None; size = 1
            seen.add(tuple(l))
            if partner is not None: seen.add(tuple(partner))
            mults.append((col(l), size, l))
        types = Counter((c, s) for c, s, _ in mults)
        for conj in (False, True):
            tgt = {((('3b' if c == '3' else '3' if c == '3b' else c) if conj else c), s): v for (c, s), v in target.items()}
            if Counter({k: len(v) for k, v in tgt.items()}) != types: continue
            groups = {k: [m for m in mults if (m[0], m[1]) == k] for k in tgt}
            opts = [set(itertools.permutations(tgt[k])) for k in tgt]
            for choice in itertools.product(*opts):
                rows, rhs = [], []
                for k, vals in zip(tgt, choice):
                    for m, v in zip(groups[k], vals): rows.append(m[2] @ basis.T); rhs.append(v)
                rows = np.array(rows, float); rhs = np.array(rhs)
                coef, *_ = np.linalg.lstsq(rows, rhs, rcond=None); dev = np.abs(rows @ coef - rhs).max()
                if best is None or dev < best[0]:
                    best = (dev, C, L, lroot, conj, basis.T @ coef, a_l)
dev, C, L, lroot, conj, cvec, a_l = best
Y = np.array([l @ cvec for l in W]); T3 = np.array([0.5*int(l @ a_l) for l in W]); Q = T3 + Y
res['G5'] = dict(max_dev=float(dev), colour_arm=C, weak_arm=L, conjugate_convention=conj, pass_=dev < 1e-9)
s2w = float(np.sum(T3**2)/np.sum(Q**2))
res['G6'] = dict(sin2_thetaW=s2w, Q_charges=sorted(Counter(np.round(Q, 6)).items()), pass_=abs(s2w-3/8) < 1e-12)

# ---------- G7: one-loop running (information) ----------
MZ = 91.1876; a = np.array([59.0, 29.6, 8.47]); b = np.array([41/10, -19/6, -7])
t12 = 2*math.pi*(a[0]-a[1])/(b[0]-b[1]); M12 = MZ*math.exp(t12)
ainv = a - b/(2*math.pi)*t12
res['G7'] = dict(M12_GeV=f'{M12:.2e}', alpha_inv_at_M12=np.round(ainv, 2).tolist(), in_range=1e12 <= M12 <= 1e14)

for k, v in res.items(): print(k, v)
