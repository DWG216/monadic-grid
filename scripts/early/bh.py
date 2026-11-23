import numpy as np, sys
SH=[(a,b) for a in (-1,0,1) for b in (-1,0,1) if (a,b)!=(0,0)]
def nsum(m): return sum(np.roll(np.roll(m,a,0),b,1) for a,b in SH)
def margolus(G,off,rng):
    G=np.roll(np.roll(G,-off,0),-off,1); N=G.shape[0]
    B=G.reshape(N//2,2,N//2,2).transpose(0,2,1,3)          # blocks
    cw=rng.random((N//2,N//2))<0.5
    Bc=np.where(cw[...,None,None],np.rot90(B,-1,axes=(2,3)),np.rot90(B,1,axes=(2,3)))
    G=Bc.transpose(0,2,1,3).reshape(N,N)
    return np.roll(np.roll(G,off,0),off,1)
def run(seed,n=6,N=100,T=1500,par=True,q=1.0,d=0.2,k=1.0,K=100.0,Kp=150.0,E=11.0,tpar=300):
    rng=np.random.default_rng(seed)
    J=n+2; P=n+1   # species 1..n, parasite P=n+1, junk J=n+2
    G=rng.integers(0,n+1,size=(N,N))
    for t in range(T):
        if par and t==tpar: G[(rng.random((N,N))<0.01)&(G>0)]=P
        cnt={s:nsum((G==s).astype(float)) for s in range(1,J+1)}
        W=[]
        for s in range(1,J+1):
            if s<=n: sup=k+K*cnt[(s-2)%n+1]
            elif s==P: sup=k+Kp*cnt[1]
            else: sup=np.full((N,N),k)
            W.append(nsum(((G==s)*sup).astype(float)))
        W=np.array(W); tot=W.sum(0)+E
        u=rng.random((N,N))*tot; cum=np.cumsum(W,0); idx=(u[None]>cum).sum(0)+1   # 1..J or J+1 = stay empty
        win=np.where(idx<=J,idx,0)
        if q<1: win=np.where((win>=1)&(win<=n)&(rng.random((N,N))>q),J,win)
        G=np.where(G==0,win,G)
        G=np.where((G>0)&(rng.random((N,N))<d),0,G)
        G=margolus(G,t%2,rng)
    sh=np.array([(G==s).mean() for s in range(J+1)])
    return sh
mode=sys.argv[1]
if mode=='V1':
    r=[run(s,par=False) for s in range(3)]; print('V1 no parasite: survive',sum(x[1:7].min()>0.001 for x in r),'/3 | member share',np.round([x[1:7].sum() for x in r],3).tolist())
elif mode=='V2':
    r=[run(s) for s in range(100,110)]; print('V2 parasite: survive',sum(x[1:7].min()>0.001 for x in r),'/10 | members',round(np.mean([x[1:7].sum() for x in r]),3),'| parasite',round(np.mean([x[7] for x in r]),3))
else:
    qq=float(mode); r=[run(s,q=qq) for s in range(200,210)]
    print('E q=%.2f: survive'%qq,sum(x[1:7].min()>0.001 for x in r),'/10 | members',round(np.mean([x[1:7].sum() for x in r]),3),'| parasite',round(np.mean([x[7] for x in r]),3),'| junk',round(np.mean([x[8] for x in r]),3))
