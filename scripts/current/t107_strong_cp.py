"""t107: strong CP from the hand swap. Pre-registration: PREDICTIONS_t107.md."""
import numpy as np
from scipy.integrate import solve_ivp
rng = np.random.default_rng(107); k = 1/(16*np.pi**2)
def ckm(s12=0.22501, s13=0.003732, s23=0.04183, d=1.144):
    c12, c13, c23 = [np.sqrt(1 - s**2) for s in (s12, s13, s23)]; e = np.exp(1j*d)
    return np.array([[c12*c13, s12*c13, s13/e],
                     [-s12*c23 - c12*s23*s13*e, c12*c23 - s12*s23*s13*e, s23*c13],
                     [s12*s23 - c12*c23*s13*e, -c12*s23 - s12*c23*s13*e, c23*c13]])
def thetabar(Mu, Md): return np.angle(np.linalg.det(Mu @ Md))
def jarlskog(Mu, Md):
    _, Uu = np.linalg.eigh(Mu @ Mu.conj().T); _, Ud = np.linalg.eigh(Md @ Md.conj().T); V = Uu.conj().T @ Ud
    return np.imag(V[0, 1]*V[1, 2]*np.conj(V[0, 2])*np.conj(V[1, 1]))
mu, md = np.array([1.54e-3, 0.599, 169.6]), np.array([3.1e-3, 0.057, 2.87]); V = ckm()
Mu, Md = np.diag(mu).astype(complex), V @ np.diag(md) @ V.conj().T
out = {}
J = jarlskog(Mu, Md); tb = thetabar(Mu, Md)
out['P1'] = dict(thetabar=tb, J=J, pass_=abs(tb) < 1e-12 and abs(J/3.08e-5 - 1) < 0.05)
def rherm():
    U = np.linalg.qr(rng.standard_normal((3, 3)) + 1j*rng.standard_normal((3, 3)))[0]
    return U @ np.diag(10**rng.uniform(-3, 2, 3)) @ U.conj().T
tbs, Js = [], []
for _ in range(1000):
    A, B = rherm(), rherm(); tbs.append(abs(thetabar(A, B))); Js.append(abs(jarlskog(A, B)))
out['P2'] = dict(max_thetabar=max(tbs), frac_J_gt_1e8=np.mean(np.array(Js) > 1e-8), pass_=max(tbs) < 1e-12 and np.mean(np.array(Js) > 1e-8) >= 0.99)
v = 246.22; MZ, M3 = 91.19, 4.98e13
def gauge(t):   # one-loop SM gauge couplings from M_Z (g' , g2, g3)
    a0 = np.array([1/0.1278**2*0 + 1/0.3575**2, 1/0.6515**2, 1/1.2209**2]); b = np.array([41/6, -19/6, -7])
    return 1/np.sqrt(a0 - 2*k*b*(t - np.log(MZ)))
def rhs(t, y):
    Yu = (y[:9] + 1j*y[9:18]).reshape(3, 3); Yd = (y[18:27] + 1j*y[27:]).reshape(3, 3)
    gp, g2, g3 = gauge(t); Hu, Hd = Yu @ Yu.conj().T, Yd @ Yd.conj().T; T = np.trace(3*Hu + 3*Hd).real
    dYu = k*(1.5*(Hu - Hd) + (T - 17/12*gp**2 - 9/4*g2**2 - 8*g3**2)*np.eye(3)) @ Yu
    dYd = k*(1.5*(Hd - Hu) + (T - 5/12*gp**2 - 9/4*g2**2 - 8*g3**2)*np.eye(3)) @ Yd
    return np.concatenate([dYu.real.ravel(), dYu.imag.ravel(), dYd.real.ravel(), dYd.imag.ravel()])
Yu0, Yd0 = np.sqrt(2)*Mu/v*0.55, np.sqrt(2)*Md/v*0.45   # rough meeting-scale sizes, Hermitian
y0 = np.concatenate([Yu0.real.ravel(), Yu0.imag.ravel(), Yd0.real.ravel(), Yd0.imag.ravel()])
s = solve_ivp(rhs, [np.log(M3), np.log(MZ)], y0, rtol=1e-12, atol=1e-16)
y = s.y[:, -1]; YuZ = (y[:9] + 1j*y[9:18]).reshape(3, 3); YdZ = (y[18:27] + 1j*y[27:]).reshape(3, 3)
tbZ = thetabar(YuZ, YdZ); herm = np.abs(YdZ - YdZ.conj().T).max()/np.abs(YdZ).max()
out['P3'] = dict(thetabar_MZ=tbZ, J_MZ=jarlskog(YuZ, YdZ), Yd_nonhermiticity=herm, pass_=abs(tbZ) < 1e-10)
out['P4'] = 'future data: n2EDM null from theta; no QCD axion'
for a, b in out.items(): print(a, b)
