"""t115: what raises highlighting. Each tick every monad reweights its perceptions by the shared record's coherence at each
frequency: p_jk <- p_jk * w_k / sum_k(.), w_k = |sum_j sqrt(p_jk) e^{i phi_jk}|^2 / sum_j p_jk (record over its incoherent
baseline: about 1 for scattered phases, up to M for aligned ones). Lawful frequencies (set K) keep a shared phase across
monads every tick (small jitter); all other phases are redrawn every tick (no lasting relation). Control: no lawful set."""
import numpy as np, sys
def run(seed, M=50, N=64, K=4, T=60, lawful=True, jitter=0.3):
    rng = np.random.default_rng(seed); p = rng.uniform(0.5, 1.5, (M, N)); p /= p.sum(1, keepdims=True)
    law = rng.choice(N, K, replace=False); base_phase = rng.uniform(0, 2*np.pi, N)
    C0 = (p**2).sum(1).mean(); viol = 0; Cs = []
    for t in range(T):
        ph = rng.uniform(0, 2*np.pi, (M, N))
        if lawful: ph[:, law] = base_phase[law] + jitter*rng.standard_normal((M, K))
        amp = np.sqrt(p); w = np.abs((amp*np.exp(1j*ph)).sum(0))**2/p.sum(0)
        Ew = (p*w).sum(1); p2 = p*w; p2 /= p2.sum(1, keepdims=True); Ew2 = (p2*w).sum(1)
        viol += int(np.sum(Ew2 < Ew - 1e-12)); p = p2; Cs.append((p**2).sum(1).mean())
    share = p[:, law].sum(1).mean(); top_in_law = np.mean(np.isin(p.argmax(1), law))
    return dict(C0=C0, C_end=Cs[-1], C_10=Cs[9], share_law=share, top_in_law=top_in_law, violations=viol)
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'test'
    seeds = range(1000, 1005) if mode == 'sanity' else range(2000, 2020)
    for lawful in (True, False):
        rs = [run(s, lawful=lawful) for s in seeds]
        agg = {k: float(np.median([r[k] for r in rs])) for k in rs[0]}; agg['violations'] = int(sum(r['violations'] for r in rs))
        print('lawful' if lawful else 'control', {k: round(v, 4) for k, v in agg.items()})
    if mode != 'sanity':
        for K in (1, 2, 8):
            rs = [run(s, K=K) for s in seeds]; print('K', K, 'C_end', round(float(np.median([r['C_end'] for r in rs])), 4), '1/K', round(1/K, 4))
        for sg in (1.0, 2.5):
            rs = [run(s, jitter=sg) for s in seeds]; print('sigma', sg, 'share_law', round(float(np.median([r['share_law'] for r in rs])), 4), 'M e^-s^2', round(50*np.exp(-sg**2), 2))
