"""t125: deriving capacity growth (identity checks, no fit).
(i) Capacity a is the exponent of listening (p w^a): a scale with no privileged zero or unit, so a change of capacity acts by
    multiplication, a -> a h(e), and h may depend only on the monad's experience e.
(ii) Experience is what the monad's attention hears over a bare (uniform) listener, e = E_p[w] / mean_k w. For a record made of
    independent parts, w = w1 w2, experience multiplies only approximately: e(w1 w2) ~ e(w1) e(w2), median error 13%, 6.5%, 1.7% at N = 64, 1024, 16384
    (run 1); the derivation holds in the limit of many frequencies. The 'correlated parts' line is not a discriminating control (5%).
(iii) Growth must not depend on how the record is split: h(e1 e2) = h(e1) h(e2), so h = e^gamma (Cauchy), i.e. d ln a = gamma d ln e:
    capacity grows by the information the monad's attention gains over a bare listener, in nats.
(iv) Since E_{p'}[w] >= E_p[w] (t115), experience grows as attention sharpens on what lasts: the climb feeds itself."""
import numpy as np
rng = np.random.default_rng(125); out = {}
for N in (64, 1024, 16384):
    errs = []
    for _ in range(200):
        p = rng.dirichlet(np.ones(N)); w1 = rng.exponential(1, N)*(1 + 30*(rng.random(N) < 0.05)); w2 = rng.exponential(1, N)
        e = lambda w: (p*w).sum()/w.mean(); errs.append(abs(e(w1*w2)/(e(w1)*e(w2)) - 1))
    out[f'ii independent parts, N={N}: median |e(w1 w2)/(e(w1)e(w2)) - 1|'] = round(float(np.median(errs)), 4)
p = rng.dirichlet(np.ones(64)); w1 = rng.exponential(1, 64); w2 = w1**2
out['ii correlated parts (w2 = w1^2): ratio - 1'] = round(float(((p*w1*w2).sum()/(w1*w2).mean())/(((p*w1).sum()/w1.mean())*((p*w2).sum()/w2.mean())) - 1), 3)
e1, e2, a = 1.7, 2.3, 0.2
for name, h in (('power e^0.02', lambda e, a: a*e**0.02), ('additive a + 0.02(e-1)', lambda e, a: a + 0.02*(e - 1)), ('linear-in-e a(1 + 0.02(e-1))', lambda e, a: a*(1 + 0.02*(e - 1)))):
    out[f'iii split vs whole, {name}'] = float(abs(h(e2, h(e1, a)) - h(e1*e2, a)))
for k, v in out.items(): print(k, v)
