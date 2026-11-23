import numpy as np
exec(open('causet_variety.py').read().split("rows={}")[0])
def grow_fullrel(seed,K=30):
    r=np.random.default_rng(seed); R=np.zeros((N,N),bool); D=np.zeros((N,N))
    for n in range(1,N):
        Rn=R[:n,:n]; past=Rn.T; fut=Rn      # row j: past of j / future of j (within first n)
        best=None
        for _ in range(K):
            q=r.uniform(0.02,0.5); links=r.random(n)<q; S=links.copy()
            if links.any(): S|=Rn[links].any(0)
            x=S.astype(float)
            Dn=D[:n,:n]+np.abs(x[:,None]-x[None,:])                       # existing pairs split by the newcomer
            dnew=(past!=S[None,:]).sum(1)+fut.sum(1)+ (~S).astype(int)*0 + S.astype(int)  # newcomer vs j: pasts differ, j's future vs empty (+ j's future now has n if j in S)
            iu=np.triu_indices(n,1)
            V=(1/(1+Dn[iu])).sum()+(1/(1+dnew)).sum()
            if best is None or V<best[0]: best=(V,S,dnew)
        V,S,dnew=best
        x=S.astype(float); D[:n,:n]+=np.abs(x[:,None]-x[None,:]); D[n,:n]=D[:n,n]=dnew
        R[:n,n]=S
    return R
rows={}
def run(name,gen):
    ms=[measures(gen(s)) for s in range(5)]; sc=[score(m) for m in ms]
    rows[name]=(np.mean([m[0] for m in ms]),np.mean([m[1] for m in ms]),np.nanmean([m[2] for m in ms]),np.mean([s[1] for s in sc]),np.mean([m[4] for m in ms]),min(m[4] for m in ms),max(m[4] for m in ms),np.mean([s[0] for s in sc]))
    print('%-14s f %.3f | d_MM %.2f | d_mid %.2f | abundance %.3f | height mean %.1f [%d-%d] | S %.2f'%((name,)+rows[name]),flush=True)
run('D-fullrel',lambda s: grow_fullrel(1000+s))
fD=rows['D-fullrel'][0]; lo,hi=0.0005,0.9
for _ in range(14):
    mid=(lo+hi)/2; fm=np.mean([grow_percolation(mid,1950+s).sum()/(N*(N-1)/2) for s in range(2)])
    lo,hi=(mid,hi) if fm<fD else (lo,mid)
p=(lo+hi)/2; print('matched percolation p = %.4f'%p)
run('A-percolation',lambda s: grow_percolation(p,1800+s))
