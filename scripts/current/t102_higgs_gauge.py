"""t102: gauge coefficient c for the light doublet in (3, 3bar) of SU(3)_L x SU(3)_R; m_h. Pre-registration: PREDICTIONS_t102.md."""
import os, numpy as np
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from scipy.optimize import brentq
def gm(n):                                   # Gell-Mann / Pauli generators T = lambda/2 (SU(n), n = 2, 3)
    G = []
    for i in range(n):
        for j in range(i + 1, n):
            A = np.zeros((n, n), complex); A[i, j] = A[j, i] = 1; G.append(A/2)
            B = np.zeros((n, n), complex); B[i, j] = -1j; B[j, i] = 1j; G.append(B/2)
    for d in range(1, n):
        D = np.zeros((n, n), complex); D[:d, :d] = np.eye(d); D[d, d] = -d; G.append(D/np.sqrt(2*d*(d + 1)))
    return G
def coeff(actions, phi):
    """actions: list of (coupling, function X -> generator acting on field); returns (3/2) sum m^4 / |phi|^4."""
    vecs = [g*f(phi).ravel() for g, f in actions]
    M2 = np.array([[2*np.real(np.vdot(a, b)) for b in vecs] for a in vecs])
    ev = np.linalg.eigvalsh(M2); n2 = np.vdot(phi.ravel(), phi.ravel()).real
    return 1.5*np.sum(ev**2)/n2**2
out = {}
# S1: SM doublet (neutral component second), hypercharge 1/2
g, gp = 0.7, 0.5; phi = np.array([[0], [1.0]], complex)
acts = [(g, lambda p, T=T: T @ p) for T in gm(2)] + [(gp, lambda p: 0.5*p)]
c_sm = coeff(acts, phi); target = 3/8*(2*g**4 + (g**2 + gp**2)**2)
acts_u = [(1.0, lambda p, T=T: T @ p) for T in gm(2)] + [(np.sqrt(3/5), lambda p: 0.5*p)]
out['S1'] = dict(c=c_sm, formula=target, c_unified=coeff(acts_u, phi), pass_=abs(c_sm - target) < 1e-9 and abs(coeff(acts_u, phi) - 1.71) < 1e-9)
# P1: bifundamental Phi ~ (3, 3bar): Phi -> U_L Phi U_R^dagger; neutral direction e1 e1^T, unified coupling 1
Phi = np.zeros((3, 3), complex); Phi[0, 0] = 1
acts3 = [(1.0, lambda p, T=T: T @ p) for T in gm(3)] + [(1.0, lambda p, T=T: -p @ T) for T in gm(3)]
c3 = coeff(acts3, Phi); out['P1'] = dict(c=c3)
src = open('t101_sensitivity.py').read(); ns = {'__file__': os.path.abspath('t101_sensitivity.py')}; exec(src[:src.index('\nfor c in')], ns)
res = {nh: brentq(lambda mh: ns['run'](mh, 172.57, 1.0e3, 2, 3.16e12, 4.98e13, nh, c3), 80, 200) for nh in range(4)}
out['P2'] = dict(mh={k: round(v, 2) for k, v in res.items()}, pass_=all(abs(v - 125.20) <= 1.0 for v in res.values()))
for k, v in out.items(): print(k, v)
