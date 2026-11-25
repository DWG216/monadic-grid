"""t126: the monad dynamics with the derived rules. Turning: the record gives only the direction (ascent); its strength is the
monad's will (kappa = 0.2, scaled by its stake: capacity x attention), because a monad's phase is what no record fixes (section 232).
The fully Bayesian turning (bayes_turn=True, below) forms no laws for M above about 16 (sanity scan, kept).
Original note: the monad dynamics with every rule derived (t124, t125 and the four below); no coupling constant.
Listening p <- p w^a (a <= 1: beta = 1 is exact conditioning; more would count evidence twice). Growth a <- clip(a e, 1/T, 1) (no capacity below one tick's worth, as for perception) (gamma = 1:
capacity is accumulated evidence). Floor eps = 1/T (no perception below one tick's share of the Age). Turning: the most likely new
phase given the monad's own phase (von Mises, concentration k0 fixed by the noise: mean resultant e^{-eta^2/2}) and the record as a
function of its phase, R(phi)^a = (A + B cos(phi - Phi))^a, A = p + |S_-j|^2, B = 2 sqrt(p) |S_-j|; Newton steps, capped at the angle.
Reflection: memory of the whole Age (running mean and variance of w since tick 0), act only where m - 1 > z se, with
N T alpha = 1 (less than one expected false alarm per Age), effective samples t eta^2."""
import numpy as np, sys
from scipy.stats import norm
from scipy.special import i0, i1
from scipy.optimize import brentq
def k0_of(eta): return brentq(lambda k: i1(k)/i0(k) - np.exp(-eta**2/2), 1e-3, 500)
def turn(phi, p, a, eta, k0, active):
    c = np.sqrt(p)*np.exp(1j*phi); z = c.sum(0); S = z[None, :] - c
    A = p + np.abs(S)**2; B = 2*np.sqrt(p)*np.abs(S); D = np.angle(S) - phi; D = (D + np.pi) % (2*np.pi) - np.pi
    d = np.zeros_like(phi)
    for _ in range(3):
        u = D - d; den = A + B*np.cos(u)
        f1 = -k0*np.sin(d) + a*B*np.sin(u)/den
        f2 = -k0*np.cos(d) - a*(B*np.cos(u)/den + (B*np.sin(u))**2/den**2)
        d = d - f1/np.where(f2 < -1e-9, f2, -1e-9); d = np.clip(d, -np.abs(D), np.abs(D))
    return phi + np.where(active, d, 0.0)
def world(seed, M=120, N=64, T=600, eta=0.3, a_init=None, grow=True, turning=True, refl_frac=0.0, p=None, phi=None, rng=None, will=0.2, bayes_turn=False):
    rng = rng or np.random.default_rng(seed); k0 = k0_of(eta) if bayes_turn else 0.0; eps = 1/T; z_thr = norm.isf(1/(N*T))
    a = a_init.copy() if a_init is not None else 10**rng.uniform(-2, 0, M); a0 = a.copy()
    p = rng.uniform(0.5, 1.5, (M, N)) if p is None else p; p = p/p.sum(1, keepdims=True); phi = rng.uniform(0, 2*np.pi, (M, N)) if phi is None else phi
    refl = np.arange(M) < int(refl_frac*M); m = np.zeros(N); s2 = np.zeros(N); t_half = np.full(M, np.inf); arrive = -1; nov = []; false_sig = []
    for t in range(T):
        phi = phi + eta*rng.standard_normal((M, N))
        if turning and bayes_turn: phi = turn(phi, p, a[:, None], eta, k0, True)
        elif turning:   # direction derived (ascent of the record); strength is the monad's will, scaled by its stake (capacity x attention)
            zz = (np.sqrt(p)*np.exp(1j*phi)).sum(0); phi = phi + np.minimum(will*a[:, None]*N*p, 1.0)*np.sin(np.angle(zz) - phi)
        z = (np.sqrt(p)*np.exp(1j*phi)).sum(0); w = np.abs(z)**2/p.sum(0)
        dm = w - m; m = m + dm/(t + 1); s2 = s2 + (dm*(w - m) - s2)/(t + 1)
        se = np.sqrt(s2/max(1.0, (t + 1)*eta**2)); sig = (m - 1 > z_thr*se) & (t > 10); judged = np.where(sig, m, 1.0)
        if not turning and t > 50: false_sig.append(float(sig.mean()))
        heard = np.where(refl[:, None], judged[None, :], w[None, :])
        if grow: e = (p*heard).sum(1)/heard.mean(1); a = np.clip(a*e, 1/T, 1.0)
        pn = p*heard**a[:, None]; pn /= pn.sum(1, keepdims=True); pn = (1 - eps)*pn + eps/N
        nov.append(float(np.abs(pn - p).sum(1).mean())); p = pn
        t_half[(a >= 0.5) & np.isinf(t_half)] = t
        if arrive < 0 and t % 5 == 0:
            r = np.abs(np.exp(1j*phi).mean(0)); L = r > 0.8
            if L.any() and np.median(p[:, L].sum(1)) > 0.9: arrive = t
    r = np.abs(np.exp(1j*phi).mean(0)); laws = r > 0.8; C = (p**2).sum(1); Lsh = p[:, laws].sum(1) if laws.any() else np.zeros(M)
    return dict(a=a, a0=a0, C=C, L=Lsh, K=int(laws.sum()), laws=set(np.where(laws)[0]), t_half=t_half, arrive=arrive, nov=np.array(nov), refl=refl,
                false_sig=float(np.mean(false_sig)) if false_sig else np.nan, z=z_thr, k0=k0)
def report(seeds):
    from scipy.stats import spearmanr
    R = {}
    f = [world(s, a_init=np.full(120, 0.3), grow=False) for s in seeds]
    R['T1 formation (equal a=0.3, no growth)'] = dict(worlds_with_laws=sum(x['K'] >= 1 for x in f), K=[x['K'] for x in f], L_med=round(float(np.median([np.median(x['L']) for x in f])), 3),
        C_over_1K=[round(float(np.median(x['C'])*x['K']), 2) if x['K'] else None for x in f])
    c = [world(s) for s in seeds]; n = [world(s, turning=False) for s in seeds]
    R['T2 climb lawful'] = dict(frac_half=[round(float((x['a'] >= 0.5).mean()), 3) for x in c], K=[x['K'] for x in c],
        rho=[round(float(spearmanr(x['a0'][(x['a0'] < 0.5) & np.isfinite(x['t_half'])], x['t_half'][(x['a0'] < 0.5) & np.isfinite(x['t_half'])]).correlation), 3) for x in c])
    R['T2 climb lawless (no turning)'] = dict(frac_half=[round(float((x['a'] >= 0.5).mean()), 3) for x in n], C=[round(float(np.median(x['C'])), 3) for x in n])
    ages = {}
    for keep in (True, False):
        rr = []
        for s in seeds:
            rng = np.random.default_rng(s); w1 = world(s, rng=rng); a2 = w1['a'] if keep else w1['a0']; w2 = world(s, a_init=a2, rng=rng)
            rr.append((w1['arrive'], w2['arrive'], len(w1['laws'] & w2['laws'])/max(1, len(w1['laws'] | w2['laws'])), float(w1['nov'][:50].max()/np.median(w1['nov'][-100:]))))
        ages['keep' if keep else 'reset'] = dict(arrive=[(x[0], x[1]) for x in rr], ratio=[round(x[1]/x[0], 2) if x[0] > 0 and x[1] >= 0 else None for x in rr],
                                                 jaccard=[round(x[2], 2) for x in rr], novelty_drop=[round(x[3], 1) for x in rr])
    R['T3 ages'] = ages
    rl = [world(s, refl_frac=0.5) for s in seeds]; rn = [world(s, refl_frac=0.5, turning=False) for s in seeds]
    g = lambda x, sel, key: float(np.median(x[key][sel]))
    R['T4 reflection lawful'] = dict(refl_frac_half=[round(float((x['a'][x['refl']] >= 0.5).mean()), 3) for x in rl], refl_L=[round(g(x, x['refl'], 'L'), 3) for x in rl])
    R['T4 reflection lawless'] = dict(refl_a=[round(g(x, x['refl'], 'a'), 3) for x in rn], refl_C=[round(g(x, x['refl'], 'C'), 3) for x in rn],
        plain_a=[round(g(x, ~x['refl'], 'a'), 3) for x in rn], false_sig=[x['false_sig'] for x in rn], z=round(rn[0]['z'], 2), k0=round(rn[0]['k0'], 2))
    return R
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'test'; seeds = range(16000, 16003) if mode == 'sanity' else range(17000, 17010)
    R = report(seeds)
    for k, v in R.items(): print(k, v)
