import numpy as np
exec(open('causet_variety.py').read().split("rows={}")[0])
def grow_leibniz(seed,K=30):
    r=np.random.default_rng(seed); R=np.zeros((N,N),bool); D=np.zeros((N,N)); links=np.zeros(N)
    for n in range(1,N):
        Rn=R[:n,:n]; past=Rn.T; fut=Rn; iu=np.triu_indices(n,1)
        Vs=[];Os=[];Ss=[];dn=[];Ls=[]
        for _ in range(K):
            q=r.uniform(0.02,0.5); l=r.random(n)<q; S=l.copy()
            if l.any(): S|=Rn[l].any(0)
            x=S.astype(float); Dn=D[:n,:n]+np.abs(x[:,None]-x[None,:])
            dnew=(past!=S[None,:]).sum(1)+fut.sum(1)+S.astype(int)
            Vs.append((1/(1+Dn[iu])).sum()+(1/(1+dnew)).sum())
            idx=np.nonzero(S)[0]
            L=int(sum(1 for j in idx if not Rn[j,idx].any()))
            m=links[:n].mean(); Os.append(abs(L-m)/(m+1)); Ss.append(S); dn.append(dnew); Ls.append(L)
        Vs=np.array(Vs); Os=np.array(Os)
        z=lambda a:(a-a.mean())/(a.std()+1e-12)
        k=int(np.argmin(z(Vs)+z(Os)))
        S=Ss[k]; x=S.astype(float); D[:n,:n]+=np.abs(x[:,None]-x[None,:]); D[n,:n]=D[:n,n]=dn[k]; links[n]=Ls[k]; R[:n,n]=S
    return R
rows={}
def run(name,gen):
    ms=[measures(gen(s)) for s in range(5)]; sc=[score(m) for m in ms]
    rows[name]=(np.mean([m[0] for m in ms]),np.mean([m[1] for m in ms]),np.nanmean([m[2] for m in ms]),np.mean([s[1] for s in sc]),np.mean([m[4] for m in ms]),min(m[4] for m in ms),max(m[4] for m in ms),np.mean([s[0] for s in sc]))
    print('%-14s f %.3f | d_MM %.2f | d_mid %.2f | abundance %.3f | height mean %.1f [%d-%d] | S %.2f'%((name,)+rows[name]),flush=True)
run('Leibniz-2term',lambda s: grow_leibniz(2000+s))
fL=rows['Leibniz-2term'][0]; lo,hi=0.0005,0.9
for _ in range(14):
    mid=(lo+hi)/2; fm=np.mean([grow_percolation(mid,2950+s).sum()/(N*(N-1)/2) for s in range(2)])
    lo,hi=(mid,hi) if fm<fL else (lo,mid)
p=(lo+hi)/2; print('matched percolation p = %.4f'%p)
run('A-percolation',lambda s: grow_percolation(p,2800+s))
