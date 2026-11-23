import numpy as np
q=lambda L:0.99**L
def spatial(seed,death,ew,cs,Ng=80,T=1500,with_par=True):
    rng=np.random.default_rng(seed)
    G=rng.choice([0,1,2,3,4],size=(Ng,Ng),p=[0.2,0.2,0.2,0.2,0.2])
    if with_par: G[rng.random((Ng,Ng))<0.02]=5
    L=np.array([0,50,50,50,50,20,0]); r=np.array([0,2,2,2,2,2,1.0]); qv=np.array([0,q(50),q(50),q(50),q(50),q(20),1.0])
    cat={1:4,2:1,3:2,4:3,5:1}; cc={1:10,2:10,3:10,4:10,5:12}
    sh=[(a,b) for a in (-1,0,1) for b in (-1,0,1) if (a,b)!=(0,0)]
    for t in range(T):
        cnt=np.zeros((7,Ng,Ng))
        for s in range(1,7):
            m=(G==s).astype(float); cnt[s]=sum(np.roll(np.roll(m,a,0),b,1) for a,b in sh)
        W=np.zeros((7,Ng,Ng))
        for s in range(1,7):
            boost=cs*cc[s]*cnt[cat[s]]/8 if s in cat else 0
            W[s]=cnt[s]*(r[s]+boost)/8
        empty=(G==0); tot=W.sum(0)+ew
        u=rng.random((Ng,Ng))*tot; cum=np.cumsum(W,0); choice=(u[None]>cum).sum(0)
        win=np.where(choice<=6,choice,0); ok=rng.random((Ng,Ng))<qv[win]
        G=np.where(empty,np.where(win==0,0,np.where(ok,win,6)),G)
        G=np.where((G>0)&(rng.random((Ng,Ng))<death),0,G)
        if t%2==0:
            a,b=sh[rng.integers(8)]; mask=rng.random((Ng,Ng))<0.1; G=np.where(mask,np.roll(np.roll(G,a,0),b,1),G)
    shares=np.array([(G==s).mean() for s in range(7)]); occ=shares[1:].sum()
    return shares, sum(shares[s]*L[s] for s in range(1,7))/max(occ,1e-9)
chosen=None
for setting in [(0.1,0.5,1),(0.1,0.5,2),(0.05,0.3,2),(0.05,0.3,4)]:
    ok=sum(1 for s in range(3) if spatial(s,*setting,with_par=False)[0][1:5].min()>0.001)
    print('control',setting,'survives',ok,'/3',flush=True)
    if ok==3: chosen=setting; break
if chosen:
    res=[spatial(s,*chosen) for s in range(100,110)]
    surv=sum(1 for sh,E in res if sh[1:5].min()>0.001)
    print('R4 run 3, setting',chosen,': hypercycle survives parasite in %d/10 | mean member share %.3f | parasite %.3f | junk %.3f | mean E %.1f'%(
        surv,np.mean([sh[1:5].sum() for sh,_ in res]),np.mean([sh[5] for sh,_ in res]),np.mean([sh[6] for sh,_ in res]),np.mean([E for _,E in res])))
else: print('no setting passed the control')
