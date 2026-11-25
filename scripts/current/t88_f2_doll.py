"""t88: F2 laws in small connected pieces of random 3-SAT (density 4.5) vs 3-XOR (density 1). Driver for src/f2law.cpp.
Pre-registration: PREDICTIONS_t88.md. (A five-subset smoke test at n = 100 was run while compiling; disclosed in the scoring.)"""
import subprocess, os, time
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); BIN = '/tmp/f2law_t88'
subprocess.run(['g++', '-O2', '-o', BIN, os.path.join(ROOT, 'src', 'f2law.cpp')], check=True)
out = {}
out['S1'] = subprocess.run([BIN, '-1', '0', '0', '0', '1'], capture_output=True, text=True).stdout.strip()
res = {}
seed = 88
for fam in (0, 1):
    for n in (100, 200, 400, 800):
        for s in (5, 10, 20, 30):
            seed += 1; t0 = time.time()
            lines = subprocess.run([BIN, str(fam), str(n), str(s), '200', str(seed)], capture_output=True, text=True, timeout=3000).stdout.split('\n')
            st = [int(l.split()[2]) for l in lines if l.strip()]
            res[(fam, n, s)] = (sum(x == 1 for x in st), sum(x == 2 for x in st), len(st))
            print(('3SAT' if fam == 0 else '3XOR'), n, s, 'law', res[(fam, n, s)][0], 'unsat', res[(fam, n, s)][1], 'of', len(st), f'{time.time()-t0:.1f}s', flush=True)
out['S1_pass'] = out['S1'] == 'S1 four=1 single=0'
out['C1'] = dict(pass_=all(res[(1, 100, s)][0] + res[(1, 100, s)][1] == res[(1, 100, s)][2] for s in (5, 10)))
out['P1'] = dict(fracs={s: res[(0, 800, s)][0] / 200 for s in (5, 10, 20, 30)}, pass_=all(res[(0, 800, s)][0] / 200 <= 0.05 for s in (5, 10, 20, 30)))
f30 = [res[(0, n, 30)][0] / 200 for n in (100, 200, 400, 800)]
out['P2'] = dict(fracs_s30=f30, pass_=f30[3] <= f30[0])
out['P3'] = dict(pass_=all(res[(1, n, s)][0] + res[(1, n, s)][1] == 200 for n in (100, 200, 400, 800) for s in (5, 10, 20, 30)))
for k, v in out.items(): print(k, v)
