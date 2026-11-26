"""t143: chords across monads on E6's tones. Pre-registration: PREDICTIONS_t143_t144.md."""
import numpy as np, sys, itertools
from t128_community import nsum
exec(open('t136_e6_resonance.py').read().split('out = {}')[0])           # W, states, idx
cubic = set()
for X in 'ABC':
    for perm in itertools.permutations(range(3)): cubic.add(frozenset(idx[(X, i, perm[i])] for i in range(3)))
for c_, l_, r_ in itertools.product(range(3), repeat=3): cubic.add(frozenset((idx[('A', c_, l_)], idx[('B', l_, r_)], idx[('C', r_, c_)])))
OFF1 = [(1, 0), (0, 1), (-1, -1)]; OFF2 = [(-1, 0), (0, -1), (1, 1)]              # label +1 and label +2 neighbours
PAIRS = [(d1, d2) for d1 in OFF1 for d2 in OFF2]
def roll(X, L, d):
    G = X.reshape((L, L) + X.shape[1:]); return np.roll(np.roll(G, -d[0], 0), -d[1], 1).reshape(X.shape)
def run(seed, rotate=True, L=12, T=600, r=2, eta=0.3, will=0.2, tau=20.0):
    rng = np.random.default_rng(seed); M = L*L; eps = 1/T; k = 1/tau
    xs, ys = np.meshgrid(np.arange(L), np.arange(L), indexing='ij'); lab = ((xs + ys) % 3).ravel()
    v = rng.normal(size=9); om = W @ v; om = 0.3*om/np.abs(om).max()
    if not rotate: om = np.zeros(27)
    tone = np.array([lab[i]*9 + np.arange(9) for i in range(M)])          # global tone index of each monad's 9 tones
    omm = om[tone]
    a = 10**rng.uniform(-2, 0, M); p = rng.uniform(0.5, 1.5, (M, 9)); p /= p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, 9))
    Pz = None; Eb = None
    for t in range(T):
        phi = phi + omm + eta*rng.standard_normal((M, 9))
        cf = np.zeros((M, 27), complex); pf = np.zeros((M, 27))
        np.put_along_axis(cf, tone, np.sqrt(p)*np.exp(1j*phi), 1); np.put_along_axis(pf, tone, p, 1)
        z = np.take_along_axis(nsum(cf, L, r), tone, 1); den = np.take_along_axis(nsum(pf, L, r), tone, 1)
        Pz = np.abs(z)**2/den if Pz is None else (1 - k)*Pz + k*np.abs(z)**2/den
        phi = phi + np.minimum(will*a[:, None]*9*p, 1.0)*np.sin(np.angle(z) - phi)
        E = np.empty((M, 9, 9, 9, 9), complex); A = np.empty((M, 9, 9, 9, 9))
        for q, (d1, d2) in enumerate(PAIRS):
            pj, pl = roll(phi, L, d1), roll(phi, L, d2); qj, ql = roll(p, L, d1), roll(p, L, d2)
            E[:, q] = np.exp(1j*(phi[:, :, None, None] + pj[:, None, :, None] + pl[:, None, None, :]))
            A[:, q] = np.sqrt(p[:, :, None, None]*qj[:, None, :, None]*ql[:, None, None, :])
        Eb = E if Eb is None else (1 - k)*Eb + k*E
        R = np.abs(Eb); psi = np.angle(E)
        g = np.minimum(will*a[:, None, None, None, None]*A*9**1.5, 1.0)*R*np.sin(np.angle(Eb) - psi)/3
        phi = phi + g.sum(axis=(1, 3, 4))
        w3 = R.mean(axis=(1, 3, 4)); w = np.maximum(Pz, w3)
        e = (p*w).sum(1)/w.mean(1); a = np.clip(a*e, 1/T, 1.0)
        p = p*w**a[:, None]; p /= p.sum(1, keepdims=True); p = (1 - eps)*p + eps/9
    hits = {}
    for q, (d1, d2) in enumerate(PAIRS):
        tj, tl = roll(tone, L, d1), roll(tone, L, d2)
        ii, aa, bb, cc = np.where(R[:, q] > 0.8)
        for i_, a_, b_, c_ in zip(ii, aa, bb, cc):
            key = frozenset((int(tone[i_, a_]), int(tj[i_, b_]), int(tl[i_, c_]))); hits[key] = hits.get(key, 0) + 1
    locked = [kk for kk, n in hits.items() if n >= 5]
    kinds = ['cubic' if kk in cubic else 'non-cubic' for kk in locked]
    return dict(n_locked=len(locked), n_cubic=kinds.count('cubic'), n_noncubic=kinds.count('non-cubic'), C_med=round(float(np.median((p**2).sum(1))), 3))
if __name__ == '__main__':
    mode, s0, s1 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    for s in range(s0, s1): print(mode, s, run(s, rotate=(mode == 'rot')), flush=True)
