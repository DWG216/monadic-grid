"""t69: does the mirror 27bar decouple? Against Distler-Garibaldi. Pre-registration: PREDICTIONS_t69.md."""
import numpy as np, itertools, io, contextlib
from collections import Counter
with contextlib.redirect_stdout(io.StringIO()):
    exec(open(__file__.replace('t69_mirror.py', 't66_lib.py')).read())
out = {}
# ---------- E8 roots (Bourbaki: 1-3-4-5-6-7-8 chain, 2 on 4) ----------
n = 8; A8 = 2*np.eye(n, dtype=int)
for i, j in [(0, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (1, 3)]: A8[i, j] = A8[j, i] = -1
def rootsys(A):
    n = len(A); E = np.eye(n, dtype=int); pos = {tuple(E[i]) for i in range(n)}; layer = [E[i] for i in range(n)]
    while layer:
        new = []
        for a in layer:
            for i in range(n):
                b = tuple(a + E[i])
                if b in pos: continue
                p, x = 0, a.copy()
                while True:
                    x = x - E[i]
                    if tuple(x) in pos: p += 1
                    else: break
                if p - int(a @ A[:, i]) > 0: pos.add(b); new.append(np.array(b))
        layer = new
    pos = sorted(pos); return pos + [tuple(-np.array(a)) for a in pos]
R8 = rootsys(A8); th8 = max(R8, key=sum)
ext_marks = {'a0': 1, **{f'node{i+1}': int(th8[i]) for i in range(8)}}
label3 = [i for i in range(8) if th8[i] == 3]
grad = {}
for k in label3:
    g = Counter(a[k] % 3 for a in R8); grad[f'node{k+1}'] = dict(fixed=g[0]+8, w=g[1], w2=g[2])
kE = next(k for k in label3 if grad[f'node{k+1}']['fixed'] == 86)
out['S1'] = dict(n_roots=len(R8), highest=th8, label3_nodes=grad, chosen=f'node{kE+1}',
                 pass_=len(R8) == 240 and grad[f'node{kE+1}'] == dict(fixed=86, w=81, w2=81))
# G1: w part = - (w2 part)
P1 = sorted(a for a in R8 if a[kE] % 3 == 1); P2 = sorted(tuple(-np.array(a)) for a in R8 if a[kE] % 3 == 2)
out['G1'] = dict(w_equals_minus_w2=P1 == P2, net_chiral_index=len(P1) - len(P2), pass_=P1 == P2)
# G2: no two weights of the 27 sum to zero
pairs = sum(1 for i, j in itertools.combinations_with_replacement(range(27), 2) if not np.any(W[i] + W[j]))
out['G2'] = dict(zero_pairs=pairs, pass_=pairs == 0)
# G3: Standard Model anomalies of one 27 (left-handed Weyl), Y, T3 from t66
col = np.array([kind(armlabels[C](l)) for l in W])
c3, c3b = col == '3', col == '3b'; colr = c3 | c3b; dbl = np.abs(T3) > 0
an = dict(SU3cubed=(c3.sum() - c3b.sum())/3, SU3sq_Y=float(Y[colr].sum()), SU2sq_Y=float(Y[dbl].sum()),
          Y3=float((Y**3).sum()), grav_Y=float(Y.sum()))
ndoublets = int(dbl.sum()//2)
out['G3'] = dict(**{k: round(v, 12) for k, v in an.items()}, n_doublets=ndoublets,
                 pass_=all(abs(v) < 1e-12 for v in an.values()) and ndoublets % 2 == 0)
# G4: U(1)_psi = fundamental coweight of end node 1, normalised so the 16 has charge 1
qraw = np.array([l @ np.linalg.inv(Acart)[:, 0] for l in W]); vals = Counter(np.round(qraw, 9))
v16 = next(v for v, m in vals.items() if m == 16); q = np.round(qraw / v16, 9)
qm = Counter(q); odd = [x for x in q if int(round(x)) % 2 != 0]
nu = lambda qs: int(sum(1 if int(round(x)) % 4 == 1 else -1 for x in qs if int(round(x)) % 2)) % 16
nu27 = nu(q); nu_mirror = nu(list(-q)*3)
out['G4'] = dict(psi_charges=dict(sorted(qm.items())), n_odd=len(odd), Z16_one_27=nu27, Z16_mirror=nu_mirror,
                 pass_=dict(qm) == {1.0: 16, -2.0: 10, 4.0: 1} and nu27 == 0 and nu_mirror == 0)
# G5: family SU(3) cubic anomaly of (27bar, 3bar)
out['G5'] = dict(family_SU3_cubic_anomaly_mirror=-27, family_SU3_cubic_anomaly_visible=27,
                 nonzero=True)
# C1: one generation without nu^c: drop the SM singlet in the 16
nuc = [i for i in range(27) if q[i] == 1 and col[i] == '1' and T3[i] == 0 and abs(Y[i]) < 1e-9]
q15 = [q[i] for i in range(27) if q[i] == 1 and i not in nuc]
out['C1'] = dict(n=len(q15), Z16=nu(q15), pass_=len(q15) == 15 and nu(q15) != 0)
for k, val in out.items(): print(k, val)
