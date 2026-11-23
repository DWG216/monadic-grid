import numpy as np, math, sys
b=3.0; f=lambda p: np.log1p((math.e**b-1)*p)/b; finv=lambda x: (np.exp(b*x)-1)/(math.e**b-1)
def cmean(ph): return np.angle(np.mean(np.exp(2j*np.pi*ph)))/(2*np.pi)%1
def run(rule,s,seed,N=60,T=400,dt=0.002,eps=0.004):
    rng=np.random.default_rng(seed); w=1+0.005*rng.standard_normal(N)
    world=np.array([0]*30+[1]*30); ph=np.where(world==0,0.0,0.5)+0.001*rng.standard_normal(N); ph%=1
    pending=np.full(N,-1); switched_at=np.full(N,np.nan); lockrun=np.zeros(N,int); locktimes=[]
    rs=[]; steps=int(T/dt); per=int(1/dt)
    for st in range(steps):
        t=st*dt
        req=rng.random(N)<s*dt
        for i in np.nonzero(req&(pending<0))[0]:
            tgt=1-world[i]
            if rule=='ANY': world[i]=tgt; switched_at[i]=t; lockrun[i]=0
            else: pending[i]=tgt
        ph+=w*dt; fired=np.zeros(N,bool); new=ph>=1
        while new.any():
            fired|=new
            for W in (0,1):
                k=(new&(world==W)).sum()
                if k:
                    if rule=='TARGET':
                        joiners=(pending==W)&(~fired)
                        world[joiners]=W; switched_at[joiners]=t; lockrun[joiners]=0; pending[joiners]=-1
                    rec=(world==W)&(~fired)
                    x=f(np.clip(ph[rec],0,1))+eps*k; ph[rec]=np.where(x>=1,1.0,finv(np.minimum(x,1)))
            new=(ph>=1)&(~fired)
        if fired.any():
            ph[fired]=0.0
            if rule=='OWN':
                own=fired&(pending>=0); world[own]=pending[own]; switched_at[own]=t; lockrun[own]=0; pending[own]=-1
        if st%per==0:
            m=[cmean(ph[world==W]) if (world==W).sum() else 0 for W in (0,1)]
            if t>=T-200: rs.append(np.mean([abs(np.mean(np.exp(2j*np.pi*ph[world==W]))) for W in (0,1)]))
            d=np.abs((ph-np.array(m)[world]+0.5)%1-0.5)
            for i in range(N):
                if not np.isnan(switched_at[i]):
                    lockrun[i]=lockrun[i]+1 if d[i]<0.02 else 0
                    if lockrun[i]>=3: locktimes.append(t-switched_at[i]); switched_at[i]=np.nan
    return np.mean(rs),locktimes
res={}
for s in (0.01,0.05,0.2):
    for rule in ('OWN','TARGET','ANY'):
        R=[]; LT=[]
        for k in range(3):
            r,lt=run(rule,s,20261122+k); R.append(r); LT+=lt
        res[(s,rule)]=(np.mean(R),np.median(LT) if LT else np.nan,len(LT))
        print(f"s={s} {rule:6s}: mean within-world r = {np.mean(R):.4f}; median lock time = {res[(s,rule)][1]:.2f} cycles over {len(LT)} switches",flush=True)
