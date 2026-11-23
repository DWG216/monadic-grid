import numpy as np
exec(open('causet_variety.py').read().split("rows={}")[0])
def grow_coexist(seed,soft=False,K=30):
    r=np.random.default_rng(seed); R=np.zeros((N,N),bool)
    for n in range(1,N):
        P=R[:n,:n].T.astype(float)       # row j = past of j
        cands=[]
        for _ in range(K):
            q=r.uniform(0.02,0.5); links=r.random(n)<q; past=links.copy()
            if links.any(): past|=R[:n,:n][links].any(0)
            cands.append(past)
        C=np.array(cands,float)
        inter=C@P.T; union=C.sum(1)[:,None]+P.sum(1)[None,:]-inter
        jac=np.where(union>0,1-inter/np.maximum(union,1),0.0)       # 0 if both pasts empty (identical)
        coex=(C==0)                                                   # event j not in candidate past -> coexists
        sc=np.where(coex,jac,np.inf).min(1); sc[np.isinf(sc)]=0
        k=r.choice(K,p=np.exp(5*sc)/np.exp(5*sc).sum()) if soft else int(np.argmax(sc))
        R[:n,n]=C[k].astype(bool)
    return R
rows={}
def run(name,gen):
    ms=[measures(gen(s)) for s in range(5)]; sc=[score(m) for m in ms]
    rows[name]=(np.mean([m[0] for m in ms]),np.mean([m[1] for m in ms]),np.nanmean([m[2] for m in ms]),np.mean([s[1] for s in sc]),np.mean([m[4] for m in ms]),min(m[4] for m in ms),max(m[4] for m in ms),np.mean([s[0] for s in sc]))
    print('%-14s f %.3f | d_MM %.2f | d_mid %.2f | abundance %.3f | height mean %.1f [%d-%d] | S %.2f'%((name,)+rows[name]),flush=True)
run('C-strict',lambda s: grow_coexist(600+s))
run('C-soft',lambda s: grow_coexist(700+s,soft=True))
fC=rows['C-strict'][0]; lo,hi=0.0005,0.9
for _ in range(14):
    mid=(lo+hi)/2; fm=np.mean([grow_percolation(mid,950+s).sum()/(N*(N-1)/2) for s in range(2)])
    lo,hi=(mid,hi) if fm<fC else (lo,mid)
p=(lo+hi)/2; print('matched percolation p = %.4f'%p)
run('A-percolation',lambda s: grow_percolation(p,800+s))
