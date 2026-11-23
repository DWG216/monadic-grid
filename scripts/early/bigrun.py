import sys; sys.argv=['x']
exec(open('bigcode.py').read())
import pickle
res={}
def report(code,label):
    N=code['N']; e3,p3=out(code,1e-3); e4,_=out(code,1e-4); e5,_=out(code,1e-5)
    expo=np.log10(e3/e4)
    es=np.linspace(0.002,0.3,150); good=[e for e in es if out(code,e)[0]<e]; thr=max(good) if good else 0
    # rounds/raw states from 1e-3 to 1e-10
    e=1e-3; cost=1; r=0
    while e>1e-10 and r<40:
        eo,p=out(code,e)
        if eo>=e: r=None; break
        e=eo; cost*=N/p; r+=1
    d=distance(code['V'],code['J'],5)
    print('%-34s N=%3d m=%d | out(1e-3)=%.2e out(1e-4)=%.2e exponent %.2f | accept p=%.3f | threshold %.3f | distance %d | %s'%(
        label,N,code['m'],e3,e4,expo,p3,thr,d,'no improvement' if r is None else '%d rounds, %.3g raw/out'%(r,cost)))
    return dict(expo=expo,p=p3,thr=thr,d=d,rounds=r,cost=cost)
for N,order in [(67,2),(73,2),(77,2),(79,2),(97,3),(103,3),(127,4)]:
    c=design(N,order)
    if c is None: print('N=%d order %d: no solution'%(N,order)); continue
    res[(N,order)]=report(c,'quadratic target' if order==2 else 'order-%d target'%order)
    if N in (67,97): res[(N,order,'CZ')]=CZleak(c['V'],N); print('      transversal CZ leak between two blocks: %.3f'%res[(N,order,'CZ')])
    if N==67: code67=c
# control: fixed-only code (order 1) at N=67
c=design(67,1); res['ctrl']=report(c,'CONTROL fixed only (order 1)')
# control 2: tau60 state is really where we think: pure output lands exactly on target
e0,_=out(code67,1e-12); print('control: near-pure input -> output error %.1e (should be ~0)'%e0)
pickle.dump(res,open('bigres.pkl','wb'))
