"""t88 post hoc (after scoring, labelled): at what piece size do 3-SAT pieces first carry an F2 law? 50 subsets each."""
import subprocess, time
BIN = '/tmp/f2law_t88'
for n in (100, 200):
    for s in (60, 100, 150, 200):
        t0 = time.time()
        try:
            lines = subprocess.run([BIN, '0', str(n), str(s), '50', str(880 + n + s)], capture_output=True, text=True, timeout=240).stdout.split('\n')
        except subprocess.TimeoutExpired:
            print(n, s, 'timeout'); continue
        st = [int(l.split()[2]) for l in lines if l.strip()]
        print('n', n, 's', s, 'law', sum(x == 1 for x in st), 'unsat', sum(x == 2 for x in st), 'of', len(st), f'{time.time()-t0:.0f}s', flush=True)
