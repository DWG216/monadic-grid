"""t84 post hoc (after scoring, labelled): find the ball with the negative eigenvalue on instance seed 840001 and test whether the missing piece is products of disjoint derived equations (the t82 combination rule only combines equations that share a variable)."""
import subprocess, json, itertools, numpy as np
r = json.loads(subprocess.run(['/tmp/closure4_t84', '64000', '288000', '840001', '0', '20', '30', '20'], capture_output=True, text=True).stdout)
def mat(vs, K):
    monos = [frozenset()] + [frozenset([v]) for v in vs] + [frozenset(p) for p in itertools.combinations(vs, 2)]
    E = lambda S: 1.0 if not S else float(K.get(S, 0))
    return np.array([[E(a ^ b) for b in monos] for a in monos])
for bi, b in enumerate(r['balls']):
    K = {frozenset(s): e for s, e in b['eqs']}
    lam = np.linalg.eigvalsh(mat(b['vars'], K))[0]
    if lam < -1e-8:
        low = {S: e for S, e in K.items() if len(S) <= 2}
        print('ball', bi, 'min eig', lam, 'derived equations of degree <= 2 in ball:', sorted((sorted(S), e) for S, e in low.items()))
        # close under ALL products up to degree 4 (including disjoint), restricted to the ball
        K2 = dict(K); changed = True
        while changed:
            changed = False
            items = list(K2.items())
            for (A, a), (B, c) in itertools.combinations(items, 2):
                C = A ^ B
                if 0 < len(C) <= 4:
                    if C in K2 and K2[C] != a * c: print('  inconsistent under full products'); changed = False; break
                    if C not in K2: K2[C] = a * c; changed = True
        print('  added by full products:', len(K2) - len(K), ' min eig after:', np.linalg.eigvalsh(mat(b['vars'], K2))[0])
