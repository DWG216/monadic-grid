"""t99: Q for quarks; leading-order CKM vs PMNS. Pre-registration: PREDICTIONS_t99.md."""
import numpy as np
rng = np.random.default_rng(99)
def Q(m): m = np.array(m); return m.sum()/np.sqrt(m).sum()**2
def sample(vals, errs, n=20000): return [Q([max(v + e*rng.standard_normal(), 1e-9) for v, e in zip(vals, errs)]) for _ in range(n)]
up, upe = [1.54e-3, 0.599, 169.6], [0.50e-3, 0.050, 2.3]; dn, dne = [3.1e-3, 0.057, 2.87], [0.5e-3, 0.012, 0.06]
qu, qd = sample(up, upe), sample(dn, dne)
out = {}
out['P1'] = dict(Q_u=float(np.mean(qu)), sd=float(np.std(qu)), pass_=abs(np.mean(qu) - 2/3) < 0.02)
out['P2'] = dict(Q_d=float(np.mean(qd)), sd=float(np.std(qd)), pass_=abs(np.mean(qd) - 2/3) < 0.02)
Vus, Vcb, Vub = 0.2250, 0.0418, 0.00369
off_ckm = 2*(Vus**2 + Vcb**2 + Vub**2)                         # approx: |V_cd| ~ |V_us|, |V_ts| ~ |V_cb|, |V_td| ~ |V_ub| scale
s12, s13, s23 = 0.307, 0.02215, 0.561; d = np.radians(212)
c12, c13, c23 = np.sqrt(1 - s12), np.sqrt(1 - s13), np.sqrt(1 - s23); S12, S13, S23 = np.sqrt(s12), np.sqrt(s13), np.sqrt(s23); e = np.exp(1j*d)
U = np.array([[c12*c13, S12*c13, S13/e], [-S12*c23 - c12*S23*S13*e, c12*c23 - S12*S23*S13*e, S23*c13], [S12*S23 - c12*c23*S13*e, -c12*S23 - S12*c23*S13*e, c23*c13]])
off_pmns = float(sum(abs(U[i, j])**2 for i in range(3) for j in range(3) if i != j))
out['P3'] = dict(off_ckm=off_ckm, off_pmns=off_pmns, ratio=off_ckm/off_pmns, pass_=off_ckm/off_pmns < 0.2)
out['info'] = dict(Q_scb=Q([0.057, 0.599, 2.87]), Q_cbt=Q([0.599, 2.87, 169.6]))
for k, v in out.items(): print(k, v)
