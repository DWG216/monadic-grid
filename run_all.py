#!/usr/bin/env python3
"""Run the R2R grid test scripts and compare with recorded outputs.

Usage:
  python3 run_all.py                 # quick group, compare with expected/
  python3 run_all.py --group all     # every script (some take long)
  python3 run_all.py --only susy     # one script (name without .py)
  python3 run_all.py -j 4 --timeout 900
Each script runs in a fresh copy of its folder under results/work/, so the
shipped folders are never modified. Results: results/summary.json and
results/out/<folder>__<name>.out
"""
import argparse, json, os, shutil, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
def load_tests():
    return json.load(open(os.path.join(HERE, 'tests.json')))
def run_one(t, timeout, workroot, outdir):
    folder, name = t['script'].split('/')[-2], os.path.basename(t['script'])[:-3]
    src = os.path.join(HERE, os.path.dirname(t['script']))
    key = f'{folder}__{name}' + ''.join('_' + str(x) for x in t.get('args', []))
    work = os.path.join(workroot, key)
    if os.path.exists(work): shutil.rmtree(work)
    shutil.copytree(src, work)
    t0 = time.time()
    try:
        p = subprocess.run([sys.executable, '-E', '-s', name + '.py'] + [str(x) for x in t.get('args', [])], cwd=work, capture_output=True, text=True,
                           timeout=t.get('timeout', timeout) or timeout)
        code, out, err = p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired as e:
        code, out, err = 'timeout', (e.stdout or b'').decode() if isinstance(e.stdout, bytes) else (e.stdout or ''), ''
    dt = time.time() - t0
    open(os.path.join(outdir, key + '.out'), 'w').write(out)
    open(os.path.join(outdir, key + '.err'), 'w').write(err)
    exp_path = os.path.join(HERE, 'expected', key + '.out')
    match = None
    if os.path.exists(exp_path):
        match = open(exp_path).read().strip() == out.strip()
    shutil.rmtree(work, ignore_errors=True)
    return dict(script=t['script'], key=key, args=t.get('args', []), exit=code, seconds=round(dt, 1), matches_expected=match)
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--group', default='quick', choices=['quick', 'early', 'heavy', 'grid', 'all'])
    ap.add_argument('--only', default=None)
    ap.add_argument('--timeout', type=int, default=900)
    ap.add_argument('-j', type=int, default=1)
    ap.add_argument('--record', action='store_true', help='write outputs into expected/ (maintainer use)')
    a = ap.parse_args()
    tests = load_tests()
    if a.only: tests = [t for t in tests if os.path.basename(t['script'])[:-3] == a.only]
    tests = [t for t in tests if a.only or a.group == 'all' or t.get('group') == a.group]
    res_dir = os.path.join(HERE, 'results'); outdir = os.path.join(res_dir, 'out'); workroot = os.path.join(res_dir, 'work')
    os.makedirs(outdir, exist_ok=True); os.makedirs(workroot, exist_ok=True)
    with ThreadPoolExecutor(a.j) as ex:
        results = list(ex.map(lambda t: run_one(t, a.timeout, workroot, outdir), tests))
    for r in results:
        print(f"{r['key']:45s} exit={r['exit']!s:8s} {r['seconds']:8.1f}s  expected={r['matches_expected']}")
    json.dump(results, open(os.path.join(res_dir, 'summary.json'), 'w'), indent=1)
    if a.record:
        os.makedirs(os.path.join(HERE, 'expected'), exist_ok=True)
        for r in results:
            if r['exit'] == 0:
                key = r['key']
                shutil.copy(os.path.join(outdir, key + '.out'), os.path.join(HERE, 'expected', key + '.out'))
    bad = [r for r in results if r['exit'] != 0]
    print(f"\n{len(results)} run, {len(results) - len(bad)} exited 0, "
          f"{sum(r['matches_expected'] is True for r in results)} match recorded output, "
          f"{sum(r['matches_expected'] is False for r in results)} differ")
if __name__ == '__main__': main()
