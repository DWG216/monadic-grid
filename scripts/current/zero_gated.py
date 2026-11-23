import numpy as np, math
import sys
N=50; b=3.0; eps=float(sys.argv[1]) if len(sys.argv)>1 else 0.03; H=3000
f=lambda ph: np.log1p((math.e**b-1)*ph)/b
finv=lambda x: (np.exp(b*x)-1)/(math.e**b-1)
def run(seed,gated):
    rng=np.random.default_rng(seed); w=1+0.002*rng.standard_normal(N); ph=rng.random(N)
    kp=rng.random(N); kicked=np.zeros(N,bool); t=0.0; cycles=0
    while t<H:
        dt_reset=(1-ph)/w
        if gated: dt=dt_reset.min(); kind='r'
        else:
            dk=np.where((~kicked)&(kp>ph),(kp-ph)/w,np.inf)
            if dk.min()<dt_reset.min(): dt=dk.min(); kind='k'
            else: dt=dt_reset.min(); kind='r'
        ph=ph+w*dt; t+=dt
        if kind=='r':
            fire=ph>=1-1e-12
            if gated:
                fired=fire.copy(); new=fire.copy()
                while new.any():
                    x=f(np.clip(ph,0,1)); x[~fired]+=eps*new.sum(); x=np.minimum(x,1); ph=np.where(fired,ph,finv(x))
                    new=(~fired)&(ph>=1-1e-12); fired|=new
                ph[fired]=0.0
                if fired.all(): return True,1.0,t
            else:
                ph[fire]=0.0; kicked[fire]=False; kp[fire]=rng.random(fire.sum())
        else:
            j=int(np.argmin(dk)); kicked[j]=True
            x=f(np.clip(ph,0,1)); m=np.arange(N)!=j; x[m]+=eps; over=x>=1; x=np.minimum(x,1)
            ph=np.where(m,finv(x),ph); ph[over]=0.0; kicked[over]=False; kp[over]=rng.random(over.sum())
        d=np.angle(np.exp(2j*np.pi*ph)*np.exp(-2j*np.pi*ph[0]))/(2*np.pi)
        if np.abs(d).max()<0.01: return True,abs(np.exp(2j*np.pi*ph).mean()),t
    return False,abs(np.exp(2j*np.pi*ph).mean()),t
for gated in (True,False):
    res=[run(20261122+k,gated) for k in range(20)]
    ok=sum(r[0] for r in res); rs=sorted(r[1] for r in res); ts=sorted(r[2] for r in res if r[0])
    print(f"eps={eps} {"GATED" if gated else "UNGATED"}: times={[round(x,1) for x in ts][:5]}... agreement in {ok}/20; median final r = {np.median(rs):.4f}; median time to agree = {np.median(ts) if ts else float('nan'):.1f} cycles")
