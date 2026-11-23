import numpy as np
from math import gamma
N=256; rng=np.random.default_rng(7)
def f_of_d(d): return gamma(d+1)*gamma(d/2)/(2*gamma(3*d/2))
DS=np.linspace(1.05,8,4000); FD=np.array([f_of_d(x) for x in DS])
def d_mm(f): return DS[np.argmin(abs(FD-f))]
def close_past(R,links,n):
    return links | (R[:n,:n][:, :][links].any(0) if links.any() else np.zeros(n,bool))
def grow_percolation(p,seed):
    r=np.random.default_rng(seed); R=np.zeros((N,N),bool)
    for n in range(1,N):
        links=r.random(n)<p; past=links.copy()
        if links.any(): past|=R[:n,:n][links].any(0)
        R[:n,n]=past
    return R
def grow_variety(seed,soft=False,K=30):
    r=np.random.default_rng(seed); R=np.zeros((N,N),bool)
    for n in range(1,N):
        P=R[:n,:n].T          # row j = past of element j (over elements < n)
        cands=[]
        for _ in range(K):
            q=r.uniform(0.02,0.5); links=r.random(n)<q; past=links.copy()
            if links.any(): past|=R[:n,:n][links].any(0)
            cands.append(past)
        C=np.array(cands)
        D=(C[:,None,:]!=P[None,:,:]).sum(2).min(1)/n   # min normalised Hamming distance to existing pasts
        if soft:
            w=np.exp(5*D); k=r.choice(K,p=w/w.sum())
        else: k=int(np.argmax(D))
        R[:n,n]=C[k]
    return R
def sprinkle(d,seed):
    r=np.random.default_rng(seed); pts=[]
    while len(pts)<N:
        t=r.random(); x=r.uniform(-.5,.5,d-1); rr=np.linalg.norm(x)
        if rr<t and rr<1-t: pts.append(np.r_[t,x])
    P=np.array(pts); P=P[np.argsort(P[:,0])]
    dt=P[:,0][None,:]-P[:,0][:,None]; dx=np.linalg.norm(P[None,:,1:]-P[:,None,1:],axis=2)
    return dt>dx
def three_layer(seed):
    r=np.random.default_rng(seed); a,b=N//4,N//2; R=np.zeros((N,N),bool)
    R[:a,a:a+b]=r.random((a,b))<0.5; R[a:a+b,a+b:]=r.random((b,N-a-b))<0.5
    R[:a,a+b:]=(R[:a,a:a+b].astype(int)@R[a:a+b,a+b:].astype(int))>0
    return R
def measures(R):
    R=R.copy(); n=len(R)
    f=R.sum()/(n*(n-1)/2); dmm=d_mm(f)
    Ri=R.astype(np.int32); I=Ri@Ri    # I[i,j] = number of elements strictly between i and j
    # largest interval
    sizes=np.where(R,I,-1); i,j=np.unravel_index(np.argmax(sizes),sizes.shape); Nint=sizes[i,j]
    inside=np.nonzero(R[i,:]&R[:,j])[0]
    if Nint<4: dmid=np.nan
    else:
        best=0
        for c in inside: best=max(best,min(I[i,c],I[c,j]))
        dmid=np.log2((Nint)/max(best,1))
    prof=np.array([((I==k)&R).sum() for k in range(6)],float); prof/=max(prof.sum(),1)
    # height
    L=np.ones(n,int)
    for jj in range(n):
        prev=np.nonzero(R[:jj,jj])[0]
        if len(prev): L[jj]=1+L[prev].max()
    return f,dmm,dmid,prof,L.max()
ref={d:np.mean([measures(sprinkle(d,100+s))[3] for s in range(3)],0) for d in (2,3,4)}
def score(m):
    f,dmm,dmid,prof,h=m; dn=min((2,3,4),key=lambda d:abs(d-dmm))
    ab=np.abs(prof-ref[dn]).sum(); return (abs(dmm-dmid) if not np.isnan(dmid) else 9)+ab, ab
rows={}
def run(name,gen):
    ms=[measures(gen(s)) for s in range(5)]; sc=[score(m) for m in ms]
    rows[name]=(np.mean([m[0] for m in ms]),np.mean([m[1] for m in ms]),np.nanmean([m[2] for m in ms]),np.mean([s[1] for s in sc]),np.mean([m[4] for m in ms]),min(m[4] for m in ms),np.mean([s[0] for s in sc]),[round(s[0],2) for s in sc])
    print('%-14s f %.3f | d_MM %.2f | d_mid %.2f | abundance dist %.3f | height mean %.1f min %d | score S %.2f %s'%((name,)+rows[name]),flush=True)
for d in (2,3,4): run('sprinkle %dD'%d,lambda s,d=d: sprinkle(d,200+s))
run('three-layer',three_layer)
run('B-strict',lambda s: grow_variety(300+s))
run('B-soft',lambda s: grow_variety(400+s,soft=True))
fB=rows['B-strict'][0]
lo,hi=0.001,0.9
for _ in range(14):
    mid=(lo+hi)/2; fm=np.mean([grow_percolation(mid,900+s).sum()/(N*(N-1)/2) for s in range(2)])
    lo,hi=(mid,hi) if fm<fB else (lo,mid)
p=(lo+hi)/2; print('matched percolation p = %.4f'%p)
run('A-percolation',lambda s: grow_percolation(p,500+s))
