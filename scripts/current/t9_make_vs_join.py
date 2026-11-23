import numpy as np, math, sys
b=3.0; f=lambda p: np.log1p((math.e**b-1)*p)/b; finv=lambda x: (np.exp(b*x)-1)/(math.e**b-1)
EPS=0.003; DT=0.002
def step_kicks(ph,kickers,eps,fired):
    new=kickers.copy()
    while new.any():
        rec=~fired; x=f(np.clip(ph[rec],0,1))+eps*new.sum(); ph[rec]=np.where(x>=1,1.0,finv(np.minimum(x,1)))
        new=(ph>=1)&(~fired); fired|=new
    return ph,fired
def formation(seed,gated,N=60,T=300):
    rng=np.random.default_rng(seed); w=1+0.005*rng.standard_normal(N); ph=rng.random(N); kp=rng.random(N); done=np.zeros(N,bool)
    for st in range(int(T/DT)):
        old=ph.copy(); ph=ph+w*DT; fired=ph>=1
        if gated:
            if fired.any(): ph,fired=step_kicks(ph,fired.copy(),EPS,fired.copy())
        else:
            cross=(~done)&(old<kp)&(ph>=kp)
            if cross.any():
                done|=cross; rec=np.ones(N,bool); x=f(np.clip(ph,0,1)); x=x+EPS*cross.sum()-EPS*cross; ph=np.where(x>=1,1.0,finv(np.minimum(x,1)))
            fired=ph>=1
        if fired.any():
            ph[fired]=0.0; kp[fired]=rng.random(fired.sum()); done[fired]=False
        if st%int(1/DT)==0:
            d=np.angle(np.exp(2j*np.pi*(ph-ph[0])))/(2*np.pi)
            if np.abs(d).max()<0.01: return True,st*DT
    return False,T
def joining(seed,newcomer_gated,N=60,T=120):
    rng=np.random.default_rng(seed); w=1+0.005*rng.standard_normal(N); ph=0.0005*rng.standard_normal(N)%1; ph[-1]=rng.random(); kp=rng.random(); kdone=False; run=0
    for st in range(int(T/DT)):
        old=ph.copy(); ph=ph+w*DT; fired=ph>=1
        world_fired=fired.copy(); world_fired[-1]=False
        kickers=world_fired.copy()
        if newcomer_gated and fired[-1]: kickers[-1]=True
        if kickers.any(): ph,fired=step_kicks(ph,kickers,EPS,fired.copy())
        if (not newcomer_gated) and (not kdone) and old[-1]<kp<=ph[-1]:
            kdone=True; x=f(np.clip(ph[:-1],0,1))+EPS; ph[:-1]=np.where(x>=1,1.0,finv(np.minimum(x,1)))
        fired=ph>=1
        if fired.any():
            ph[fired]=0.0
            if fired[-1]: kp=rng.random(); kdone=False
        if st%int(0.05/DT)==0:
            m=np.angle(np.mean(np.exp(2j*np.pi*ph[:-1])))/(2*np.pi); d=abs((ph[-1]-m+0.5)%1-0.5)
            if d<0.02:
                if run==0: t_in=st*DT
                run+=1
            else: run=0
            if run>=60: return t_in
    return np.nan
if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)>1 else 'full'
    nF,nJ=(3,6) if mode=='sanity' else (20,40)
    for gated in (True,False):
        r=[formation(20261122+k,gated) for k in range(nF)]
        print(f"{mode} formation {'gated ' if gated else 'random'}: {sum(x[0] for x in r)}/{nF} formed; median time {np.median([x[1] for x in r if x[0]]) if any(x[0] for x in r) else float('nan'):.1f}",flush=True)
    for ng in (True,False):
        L=[joining(30000+k,ng) for k in range(nJ)]
        print(f"{mode} joining newcomer {'gated ' if ng else 'random'}: locked {np.sum(~np.isnan(L))}/{nJ}; median {np.nanmedian(L):.2f} cycles",flush=True)
