"""t90: flavoured leptogenesis with m_D = charged-lepton masses; Majorana-phase scan. Pre-registration: PREDICTIONS_t90.md."""
import numpy as np
rng = np.random.default_rng(90)
eV = 1e-9; v = 174.0; mstar = 1.08e-3*eV
m1 = 0.365e-3*eV; m2 = np.sqrt(m1**2 + 7.50e-5*eV**2); m3 = 59.16e-3*eV - m1 - m2
mD = np.diag([0.51099895e-3, 0.1056583755, 1.776969])
def pmns(t12, t13, t23, d, a21, a31):
    s12, c12, s13, c13, s23, c23 = np.sin(t12), np.cos(t12), np.sin(t13), np.cos(t13), np.sin(t23), np.cos(t23)
    e = np.exp(-1j*d)
    U = np.array([[c12*c13, s12*c13, s13*e],
                  [-s12*c23 - c12*s23*s13/e, c12*c23 - s12*s23*s13/e, s23*c13],
                  [s12*s23 - c12*c23*s13/e, -c12*s23 - s12*c23*s13/e, c23*c13]])
    return U @ np.diag([1, np.exp(1j*a21/2), np.exp(1j*a31/2)])
def takagi(M):
    # M symmetric complex: M = W* diag(s) W^dagger, s >= 0
    H = M.conj().T @ M; w, V = np.linalg.eigh(H); idx = np.argsort(w); V = V[:, idx]
    D = V.T @ M @ V                                      # should be diagonal
    ph = np.exp(-1j*np.angle(np.diag(D))/2); V = V @ np.diag(ph); D = V.T @ M @ V
    return np.real(np.diag(D)), V                         # M = V* diag V^dagger  <=> V^T M V = diag
def fV(x): return np.sqrt(x)*(1 + (1 - (1 + x)*np.log((1 + x)/x)))
def fS(x): return np.sqrt(x)/(1 - x)
def kappa(K):
    zB = 2 + 4*K**0.13*np.exp(-2.5/K); return 2/(K*zB)*(1 - np.exp(-K*zB/2))
def run(U):
    mnu = U.conj() @ np.diag([m1, m2, m3]) @ U.conj().T
    MR = -mD.T @ np.linalg.inv(mnu) @ mD
    Ms, V = takagi(MR)
    mDh = mD @ V.conj()                                   # Dirac couplings in heavy basis (columns i)
    rt = mDh @ np.diag(1/Ms) @ mDh.T                       # should equal -mnu up to sign convention
    H = mDh.conj().T @ mDh
    eps = np.zeros((3, 3)); K = np.zeros((3, 3))
    for i in range(3):
        for a in range(3):
            K[i, a] = abs(mDh[a, i])**2/(Ms[i]*mstar)
            s = 0.0
            for j in range(3):
                if j == i: continue
                x = (Ms[j]/Ms[i])**2
                s += np.imag(np.conj(mDh[a, i])*mDh[a, j]*H[i, j])*(fV(x) + fS(x)) + np.imag(np.conj(mDh[a, i])*mDh[a, j]*H[j, i])/(1 - x)
            eps[i, a] = s/(8*np.pi*v**2*np.real(H[i, i]))
    NBL = np.zeros(3)
    for i in range(3):
        for a in range(3):
            w = eps[i, a]*kappa(K[i, a])
            for j in range(3):
                if Ms[j] < Ms[i]: w *= np.exp(-3*np.pi*K[j, a]/8)
            NBL[i] += w
    return Ms, eps, K, 0.0096*NBL, rt, mnu
out = {}
Ms, eps, K, eta, rt, mnu = run(pmns(np.radians(33.4), np.radians(8.6), np.radians(49.0), np.radians(212), 0.3, 1.1))
out['S1'] = dict(rel=float(np.max(np.abs(np.abs(rt) - np.abs(mnu)))/np.max(np.abs(mnu))), pass_=np.max(np.abs(np.abs(rt) - np.abs(mnu)))/np.max(np.abs(mnu)) < 1e-8)
Ms0, eps0, *_ = run(np.eye(3, dtype=complex)); out['S2'] = dict(M=sorted(Ms0.tolist()), maxeps=float(np.max(np.abs(eps0))), pass_=float(np.max(np.abs(eps0))) < 1e-20)
etas, shares, masses = [], [], []
for _ in range(20000):
    a21, a31 = rng.uniform(0, 2*np.pi, 2)
    Ms, eps, K, eta, *_ = run(pmns(np.radians(33.4), np.radians(8.6), np.radians(49.0), np.radians(212), a21, a31))
    tot = abs(eta.sum()); etas.append(tot); masses.append(sorted(Ms)); iH = int(np.argmax(Ms))
    shares.append(abs(eta[iH])/max(tot, 1e-300))
etas = np.array(etas); shares = np.array(shares); masses = np.array(masses)
ok = etas >= 6.1e-10
out['P1'] = dict(frac=float(ok.mean()), max_eta=float(etas.max()), pass_=ok.mean() >= 0.01)
ib = int(np.argmax(etas)); out['P2'] = dict(share_heaviest_at_best=float(shares[ib]), pass_=shares[ib] > 0.5)
out['info'] = dict(median_masses=np.median(masses, axis=0).tolist(), within_factor2=float(((etas > 3.05e-10) & (etas < 1.22e-9)).mean()))
for k, x in out.items(): print(k, x)
