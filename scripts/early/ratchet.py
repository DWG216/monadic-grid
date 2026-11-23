import numpy as np, sys
sys.argv=['x','4']
exec(open('cycles2.py').read().split("def history")[0])
def hist(e,nu=0.2,ncyc=200):
    out=[]; summary=None
    for c in range(ncyc):
        p=np.ones(3)/3 if summary is None else np.array([summary/2,1-summary,summary/2])
        x0=rng.multinomial(200,p)/200; x,coop=cycle(x0); out.append(coop)
        coopEnd=(x[0]+x[2])>0.5; lose=nu*(1-e) if coopEnd else nu*(1+e)
        summary=None if rng.random()<lose else float(round(x[0]+x[2]))
    return np.array(out)
p=0.45; pi=lambda e:(1+e)*p/((1+e)*p+(1-e)*(1-p))
print(' e   | simulated share of cooperative cycles | predicted pi(e) | mean cooperation')
for e in (0,0.25,0.5,0.75,1.0):
    H=np.array([hist(e) for _ in range(40)]); tail=H[:,50:]
    print('%.2f | %.3f | %.3f | %.3f'%(e,(tail>0.5).mean(),pi(e),tail.mean()),flush=True)
