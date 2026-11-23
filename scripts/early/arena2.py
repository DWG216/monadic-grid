import numpy as np
eps=0.01; q=lambda L:(1-eps)**L
# ---------- well-mixed ----------
def well(types,T=4000,seed=0):
    # types: list of dicts with r, L, cat_from (index or None), cat_c
    rng=np.random.default_rng(seed); n=len(types)
    x=np.array([t['x0'] for t in types]+[0.05]); x/=x.sum()
    for _ in range(T):
        f=np.array([t['r']+(t['c']*x[t['cat']] if t['cat'] is not None else 0) for t in types])
        out=np.zeros(n+1); qq=np.array([q(t['L']) for t in types])
        out[:n]=x[:n]*f*qq; out[n]=x[n]*1.0+np.sum(x[:n]*f*(1-qq))
        x=out/out.sum()
    E=sum(x[i]*types[i]['L'] for i in range(n)); return x,E
simple=dict(r=1.5,L=20,cat=None,c=0,x0=0.5); cx=dict(r=2,L=200,cat=None,c=0,x0=0.5)
x,E=well([simple]); print('R1 lone simple: share %.3f, E=%.1f'%(x[0],E)); Es=E
x,E=well([cx]); print('   lone complex: share %.4f, E=%.2f'%(x[0],E))
hc=[dict(r=2,L=50,cat=(i-1)%4,c=10,x0=0.24) for i in range(4)]
x,E=well(hc); print('R2 hypercycle: member shares %s, junk %.3f, E=%.1f (lone simple E=%.1f)'%(np.round(x[:4],3).tolist(),x[4],E,Es))
par=dict(r=2,L=20,cat=0,c=12,x0=0.01)
x,E=well(hc+[par],T=20000); print('R3 well-mixed + parasite: members %s, parasite %.3f, junk %.3f, E=%.2f'%(np.round(x[:4],4).tolist(),x[4],x[5],E))
# ---------- spatial ----------
def spatial(seed,Ng=80,T=1500,with_par=True):
    rng=np.random.default_rng(seed)
    # states: 0 empty, 1..4 members, 5 parasite, 6 junk
    G=rng.choice([0,1,2,3,4],size=(Ng,Ng),p=[0.2,0.2,0.2,0.2,0.2])
    if with_par: G[rng.random((Ng,Ng))<0.02]=5
    L=np.array([0,50,50,50,50,20,0]); r=np.array([0,2,2,2,2,2,1.0]); qv=np.array([0,q(50),q(50),q(50),q(50),q(20),1.0])
    cat={1:4,2:1,3:2,4:3,5:1}; cc={1:10,2:10,3:10,4:10,5:12}
    shifts=[(a,b) for a in (-1,0,1) for b in (-1,0,1) if (a,b)!=(0,0)]
    for t in range(T):
        # neighbour counts of each species
        cnt=np.zeros((7,Ng,Ng))
        for s in range(1,7):
            m=(G==s).astype(float); cnt[s]=sum(np.roll(np.roll(m,a,0),b,1) for a,b in shifts)
        W=np.zeros((7,Ng,Ng))
        for s in range(1,7):
            boost=cc.get(s,0)*cnt[cat[s]]/8 if s in cat else 0
            W[s]=cnt[s]*(r[s]+boost)/8
        empty=(G==0); tot=W.sum(0)+1.5   # 1.5 = weight of staying empty
        u=rng.random((Ng,Ng))*tot; cum=np.cumsum(W,0); choice=(u[None]>cum).sum(0)   # 0..6 index of winner; 7 = stay empty
        win=np.where(choice<=6,choice,0)
        ok=rng.random((Ng,Ng))<qv[win]
        newv=np.where(win==0,0,np.where(ok,win,6))
        G=np.where(empty,newv,G)
        # death
        G=np.where((G>0)&(rng.random((Ng,Ng))<0.2),0,G)
        # mixing: swap with random neighbour
        if t%2==0:
            a,b=shifts[rng.integers(8)]; mask=rng.random((Ng,Ng))<0.1; Gs=np.roll(np.roll(G,a,0),b,1); G=np.where(mask,Gs,G)
    shares=np.array([(G==s).mean() for s in range(7)]); occ=shares[1:].sum()
    E=sum(shares[s]*L[s] for s in range(1,7))/max(occ,1e-9)
    return shares,E
res=[spatial(s) for s in range(10)]
surv=sum(1 for sh,E in res if sh[1:5].min()>0.001)
print('R4 spatial + parasite, 10 runs: hypercycle survives in %d | mean member share %.3f | mean parasite share %.3f | mean E %.1f'%(
    surv,np.mean([sh[1:5].sum() for sh,_ in res]),np.mean([sh[5] for sh,_ in res]),np.mean([E for _,E in res])))
res0=[spatial(s,with_par=False) for s in range(3)]
print('   control, spatial without parasite (3 runs): survives in %d'%sum(1 for sh,E in res0 if sh[1:5].min()>0.001))
