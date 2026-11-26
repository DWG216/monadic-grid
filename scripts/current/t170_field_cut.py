"""t170: Sorkin-Johnston field entanglement on the grain with the record's frequency cut (omega <= pi per tick, t133).
Pre-registration: PREDICTIONS_t170.md. Units rho = 1. One field (record section 316)."""
import numpy as np, time

def sprinkle(N, rng):
    T = (24*N/np.pi)**0.25
    n = rng.poisson(N); P = []
    while len(P) < n:
        X = rng.uniform(-T/2, T/2, size=(4*n, 4))
        ok = np.abs(X[:, 0]) + np.linalg.norm(X[:, 1:], axis=1) < T/2
        P.extend(X[ok])
    P = np.array(P[:n]); return P[np.argsort(P[:, 0])], T

def run(P, T):
    t, s = P[:, 0], P[:, 1:]
    dt = t[None, :] - t[:, None]; d2 = ((s[None, :, :] - s[:, None, :])**2).sum(2)
    C = ((dt > 0) & (dt*dt > d2)).astype(np.float32)
    L = ((C > 0) & ((C @ C) == 0)).astype(np.float64)
    K = (1/(2*np.pi*np.sqrt(6))) * L.T
    H = 1j*(K - K.T)
    lam, V = np.linalg.eigh(H)
    tauD = len(P)/((np.pi/6)*T**3); lamND = tauD/(2*np.pi)
    pos = lam >= lamND
    W = (V[:, pos]*lam[pos]) @ V[:, pos].conj().T
    out = dict(tauD=tauD, keptD=int(pos.sum()), nyqD=(np.pi/6)*(np.pi/6)*T**3)
    for name, idx in (('R', np.where(P[:, 1] < -np.abs(t))[0]), ("Rp", np.where(P[:, 1] > np.abs(t))[0])):
        HR, WR = H[np.ix_(idx, idx)], W[np.ix_(idx, idx)]
        l, U = np.linalg.eigh(HR)
        tauR = len(idx)/((np.pi/12)*T**3); keep = np.abs(l) >= tauR/(2*np.pi)
        out['kept_'+name] = int(keep.sum()); out['n_'+name] = len(idx)
        if keep.sum() == 0: out['S_'+name] = 0.0; continue
        Uk = U[:, keep]; Wk = Uk.conj().T @ WR @ Uk
        mu = np.linalg.eigvals(Wk / l[keep][:, None]).real
        mu = mu[np.abs(mu) > 1e-12]
        out['S_'+name] = float(np.sum(mu*np.log(np.abs(mu))))
    return out

if __name__ == '__main__':
    res = []
    for N, seeds in ((1500, (1697, 1698)), (3000, (1699, 1700)), (6000, (1701, 1702))):
        for sd in seeds:
            t0 = time.time(); P, T = sprinkle(N, np.random.default_rng(sd)); o = run(P, T)
            r = dict(N=len(P), T=T, A=np.pi*(T/2)**2, **o, sec=round(time.time()-t0)); res.append(r); print(r, flush=True)
    S = np.array([(r['S_R']+r['S_Rp'])/2 for r in res]); A = np.array([r['A'] for r in res])
    asym = [abs(r['S_R']-r['S_Rp'])/max(abs((r['S_R']+r['S_Rp'])/2), 1e-12) for r in res if r['N'] > 2500]
    print('S1', dict(asym=[round(a, 3) for a in asym], pass_=max(asym) < 0.15))
    p = np.polyfit(np.log(A), np.log(np.abs(S)), 1)[0]
    print('P1', dict(p=p, pass_=0.75 < p < 1.25))
    eta = float(np.mean([s/a for s, a, r in zip(S, A, res) if r['N'] > 4500]))
    print('P2', dict(eta_f=eta, eta_m=0.190, ratio=eta/0.190, pass_=0.127 < eta < 0.285))
    print('reported', dict(S_over_A=[round(s/a, 4) for s, a in zip(S, A)], three_eta_f=3*eta))
