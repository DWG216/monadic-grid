"""t177 analysis: plaquette, Creutz ratio chi(3,3), glueball effective mass ln C(1)/C(2), jackknife over 20 bins."""
import numpy as np
NB = 20
def jack(data, f):
    n = len(data); b = n//NB; data = data[:b*NB]
    full = f(data)
    est = np.array([f(np.concatenate([data[:i*b], data[(i + 1)*b:]])) for i in range(NB)])
    return full, np.sqrt((NB - 1)*np.mean((est - est.mean())**2))
res = {}
for g in ('SU2', '2I'):
    d = np.load('t177_%s.npz' % g); P, W, O = d['plaq'], d['W'], d['O']
    p, pe = jack(P, np.mean)
    def creutz(Ws):
        m = Ws.mean(0); return -np.log(m[3, 3]*m[2, 2]/(m[3, 2]*m[2, 3]))
    s, se = jack(W, creutz)
    L = O.shape[1]
    def corr(Os, t):
        Oc = Os - Os.mean(); return np.mean([np.mean(Oc[:, x]*Oc[:, (x + t) % L]) for x in range(L)])
    def meff(Os): return np.log(corr(Os, 1)/corr(Os, 2))
    m, me = jack(O, meff)
    def ratio(idx_frac):
        return None
    # ratio with jackknife over matched bins (W every 5 sweeps, O every 2): bin by sweep fraction
    nbW, nbO = len(W)//NB, len(O)//NB
    rs = []
    for i in range(NB):
        Wi = np.concatenate([W[:i*nbW], W[(i + 1)*nbW:NB*nbW]]); Oi = np.concatenate([O[:i*nbO], O[(i + 1)*nbO:NB*nbO]])
        rs.append(meff(Oi)/np.sqrt(creutz(Wi)))
    rs = np.array(rs); r = m/np.sqrt(s); re = np.sqrt((NB - 1)*np.mean((rs - rs.mean())**2))
    res[g] = dict(plaq=p, plaq_err=pe, chi33=s, chi33_err=se, m_eff=m, m_eff_err=me, ratio=r, ratio_err=re)
    print(g, res[g])
su, i2 = res['SU2'], res['2I']
print('S1', dict(plaq=su['plaq'], lit=0.630, rel=abs(su['plaq']/0.630 - 1), pass_=abs(su['plaq']/0.630 - 1) < 0.005))
print('S2', dict(ratio=su['ratio'], lit=3.78, rel=abs(su['ratio']/3.78 - 1), pass_=abs(su['ratio']/3.78 - 1) < 0.25))
print('P1', dict(rel=abs(i2['plaq']/su['plaq'] - 1), pass_=abs(i2['plaq']/su['plaq'] - 1) < 0.005))
comb = np.hypot(su['ratio_err'], i2['ratio_err']); diff = abs(i2['ratio'] - su['ratio'])
print('P2', dict(diff=diff, two_sigma=2*comb, rel=diff/su['ratio'], pass_=diff < 2*comb and diff/su['ratio'] < 0.10))
