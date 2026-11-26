"""t169: one eta or two? Sorkin-Johnston field entanglement on the grid's grain (4D sprinkling, link propagator).
Pre-registration: PREDICTIONS_t169.md. Units rho = 1."""
import numpy as np, json, time

def sprinkle(N, rng):
    T = (24*N/np.pi)**0.25
    n = rng.poisson(N); P = []
    while len(P) < n:
        X = rng.uniform(-T/2, T/2, size=(4*n, 4))
        ok = np.abs(X[:, 0]) + np.linalg.norm(X[:, 1:], axis=1) < T/2
        P.extend(X[ok])
    P = np.array(P[:n]); return P[np.argsort(P[:, 0])], T

def ientropy(P, T):
    t, s = P[:, 0], P[:, 1:]
    dt = t[None, :] - t[:, None]; d2 = ((s[None, :, :] - s[:, None, :])**2).sum(2)
    C = ((dt > 0) & (dt*dt > d2)).astype(np.float32)          # C[i,j]: i precedes j
    L = ((C > 0) & ((C @ C) == 0)).astype(np.float64)          # links
    K = (1/(2*np.pi*np.sqrt(6))) * L.T                         # K_R[x,y] != 0 for y < x
    H = 1j*(K - K.T)                                           # i Delta, Hermitian
    lam, V = np.linalg.eigh(H)
    nD = int(round(np.pi/6*T**3))
    pos = np.argsort(lam)[::-1][:nD]
    W = (V[:, pos]*lam[pos]) @ V[:, pos].conj().T
    out = {}
    for name, idx in (('R', np.where(P[:, 1] < -np.abs(t))[0]), ("R'", np.where(P[:, 1] > np.abs(t))[0])):
        HR, WR = H[np.ix_(idx, idx)], W[np.ix_(idx, idx)]
        l, U = np.linalg.eigh(HR)
        nR = nD//2; o = np.argsort(l)
        keep = np.concatenate([o[::-1][:nR], o[:nR]])
        Uk = U[:, keep]; Wk = Uk.conj().T @ WR @ Uk
        mu = np.linalg.eigvals(Wk / l[keep][:, None]).real
        mu = mu[np.abs(mu) > 1e-12]
        out[name] = float(np.sum(mu*np.log(np.abs(mu)))); out['n_'+name] = len(idx)
    return out, nD, int(L.sum())

res = []
for N, seeds in ((1500, (1691, 1692)), (3000, (1693, 1694)), (6000, (1695, 1696))):
    for sd in seeds:
        t0 = time.time(); P, T = sprinkle(N, np.random.default_rng(sd))
        o, nD, nl = ientropy(P, T); A = np.pi*(T/2)**2
        r = dict(N=len(P), T=T, A=A, nD=nD, links=nl, S_R=o['R'], S_Rp=o["R'"], nR=o['n_R'], nRp=o["n_R'"], sec=round(time.time()-t0))
        res.append(r); print(r, flush=True)

S = np.array([(r['S_R']+r['S_Rp'])/2 for r in res]); A = np.array([r['A'] for r in res])
asym = [abs(r['S_R']-r['S_Rp'])/((r['S_R']+r['S_Rp'])/2) for r in res]
print('S1', dict(max_asym=max(asym), pass_=max(asym) < 0.15))
p = np.polyfit(np.log(A), np.log(S), 1)[0]
print('P1', dict(p=p, pass_=0.75 < p < 1.25))
eta_f = float(np.mean([s/a for s, a, r in zip(S, A, res) if r['N'] > 4500]))
print('P2', dict(eta_f=eta_f, eta_f_x118=118*eta_f, eta_m=0.190, ratio=118*eta_f/0.190, pass_=0.127 < 118*eta_f < 0.285))
print('reported', dict(eta_f_over_t27_lattice=eta_f/0.0235, S_over_A=[round(s/a, 4) for s, a in zip(S, A)]))
