import sys,json; sys.argv=['x']
exec(open('bigcode.py').read())
codes={k:design(*k) for k in [(67,2),(97,3),(127,4)]}
for eps0 in [0.1,0.2,0.3,0.4]:
    best=None
    for k,c in codes.items():
        e=eps0; cost=1; r=0; ok=True
        while e>1e-10/40 and r<30:
            eo,p=out(c,e)
            if eo>=e: ok=False;break
            e=eo; cost*=k[0]/p; r+=1
        if ok and (best is None or cost<best[0]): best=(cost,k[0],r)
    print('raw error %.1f: 15-to-1 %s | BK %s | icosahedral best N=%d, %d rounds, %.3g raw states per tau60 at 2.5e-12'%(eps0,'works' if eps0<0.141 else 'cannot start','works' if eps0<0.173 else 'cannot start',best[1],best[2],best[0]))
