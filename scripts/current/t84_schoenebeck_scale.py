"""t84: Schoenebeck's reduction at n = 16k-64k, density 4.5. Driver for src/closure4.cpp; local PSD in numpy.
Pre-registration: PREDICTIONS_t84.md."""
import subprocess, json, itertools, os, numpy as np, time
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BIN = '/tmp/closure4_t84'
subprocess.run(['g++', '-O2', '-o', BIN, os.path.join(ROOT, 'src', 'closure4.cpp')], check=True)
def run(n, seed, mode, nballs=0):
    r = subprocess.run([BIN, str(n), str(int(4.5 * n)), str(seed), str(mode), str(nballs), '30', '20'], capture_output=True, text=True)
    return json.loads(r.stdout)
def min_eig(ball):
    vs = ball['vars']; K = {frozenset(s): e for s, e in ball['eqs']}
    monos = [frozenset()] + [frozenset([v]) for v in vs] + [frozenset(p) for p in itertools.combinations(vs, 2)]
    E = lambda S: 1.0 if not S else float(K.get(S, 0))
    return float(np.linalg.eigvalsh(np.array([[E(a ^ b) for b in monos] for a in monos]))[0])
out = {}
r = run(16000, 830001, 2); out['S1'] = dict(result=r['status'], pass_=r['status'] == 'conflict'); print('S1', out['S1'], flush=True)
s2 = [run(16000, 830010 + i, 1) for i in range(3)]
out['S2'] = dict(results=[(x['status'], x.get('hidden_sat'), x.get('clause_viol')) for x in s2],
                 pass_=all(x['status'] == 'ok' and x['hidden_sat'] == x['clauses'] and x['clause_viol'] == 0 for x in s2)); print('S2', out['S2'], flush=True)
cons, p2, psd = {}, [], []
for n in (16000, 32000, 64000):
    cons[n] = 0
    for i in range(10):
        t0 = time.time(); r = run(n, 840000 + i, 0, 20 if n == 64000 else 0)
        line = dict(n=n, i=i, status=r['status'], size=r['size'])
        if r['status'] == 'ok':
            cons[n] += 1; ok = r['clause_viol'] == 0 and r['prod_viol'] == 0; p2.append(ok)
            line.update(clause_viol=r['clause_viol'], prod_viol=r['prod_viol'])
            if r['balls']:
                lam = min(min_eig(b) for b in r['balls']); psd.append(lam); line['min_local_eig'] = lam
        line['sec'] = round(time.time() - t0, 1); print(line, flush=True)
out['P1'] = dict(consistent_64000=cons[64000], pass_=cons[64000] >= 8)
out['P2'] = dict(pass_=bool(p2) and all(p2))
out['P3'] = dict(min_eig=min(psd) if psd else None, pass_=bool(psd) and min(psd) >= -1e-8)
out['P4'] = dict(consistent=cons, pass_=cons[64000] >= cons[16000])
for k, v in out.items(): print(k, v)
