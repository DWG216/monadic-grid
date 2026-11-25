"""t119: a system of laws. After t118's third-order dynamics, every pair of locked triads (R > 0.8) sharing exactly one
frequency gives a derived relation: their sum or difference that cancels the shared frequency (four frequencies, never attended
as such). Compare its order R_d with the parents' product R1*R2; control: random four-frequency relations with the same
sign pattern built from frequencies of locked triads but not derivable from any locked pair."""
import numpy as np, sys, itertools
from t118_relations import run
def rows(tr, N):
    A = np.zeros((len(tr), N), int)
    for i, (a, b, c) in enumerate(tr): A[i, a] += 1; A[i, b] += 1; A[i, c] -= 1
    return A
def analyse(seed, rng):
    phi, p, tr = run(seed, 'triad', return_state=True); N = phi.shape[1]; A = rows(tr, N); Psi = phi @ A.T
    R = np.abs(np.exp(1j*Psi).mean(0)); S = np.where(R > 0.8)[0]; rank = int(np.linalg.matrix_rank(A[S])) if len(S) else 0
    def w4(v):
        f = np.nonzero(v)[0]; a = np.sqrt(np.prod(p[:, f], axis=1)); B = (a*np.exp(1j*(phi @ v))).sum(); return float(np.abs(B)**2/(a**2).sum())
    der, prod, used, w4d, w4c = [], [], set(), [], []
    for i, j in itertools.combinations(S, 2):
        shared = np.where((A[i] != 0) & (A[j] != 0))[0]
        if len(shared) != 1: continue
        k = shared[0]; s = -1 if A[i, k] == A[j, k] else 1; v = A[i] + s*A[j]
        if np.count_nonzero(v) != 4 or np.abs(v).max() > 1: continue
        used.add(tuple(v)); der.append(np.abs(np.exp(1j*(phi @ v)).mean())); prod.append(R[i]*R[j]); w4d.append(w4(v))
    ctrl = []; F = np.unique(tr[S].ravel()) if len(S) else np.arange(N)
    for _ in range(400):
        f = rng.choice(N, 4, replace=False); v = np.zeros(N, int); v[f] = rng.choice([-1, 1], 4)
        if tuple(v) in used or tuple(-v) in used: continue
        ctrl.append(np.abs(np.exp(1j*(phi @ v)).mean())); w4c.append(w4(v))
    return dict(locked=len(S), rank=rank, n_derived=len(der), R_derived=float(np.median(der)) if der else np.nan,
                R_parent_product=float(np.median(prod)) if prod else np.nan, R_control=float(np.median(ctrl)), ctrl_95=float(np.percentile(ctrl, 95)), w4_derived=float(np.median(w4d)) if w4d else np.nan, w4_control=float(np.median(w4c)))
if __name__ == '__main__':
    m = sys.argv[1] if len(sys.argv) > 1 else 'test'; rng = np.random.default_rng(119)
    seeds = range(7000, 7003) if m == 'sanity' else range(9000, 9012)
    rs = [analyse(s, rng) for s in seeds]
    for s, r in zip(seeds, rs): print(s, {k: round(v, 3) if isinstance(v, float) else v for k, v in r.items()})
    print('median', {k: round(float(np.nanmedian([r[k] for r in rs])), 3) for k in rs[0]})
