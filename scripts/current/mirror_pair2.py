import numpy as np
exec(open('mirror_pair.py').read().split('def lam')[0].split('for t in (14')[0])
src=open('mirror_pair.py').read()
exec(src[src.index('def theta'):src.index('def lam')])
def lam(X):
    spf=np.zeros(X+1,dtype=np.int64)
    for i in range(2,X+1):
        if spf[i]==0: spf[i::i][spf[i::i]==0]=i
    L=[]
    for m in range(2,X+1):
        p=spf[m]; k=m
        while k%p==0: k//=p
        if k==1: L.append((m,np.log(p)))
    return L
def S(T,X,fake=None):
    if X<2: return 0*T
    L=lam(X); m=np.array([a for a,_ in L],float); lp=np.array([b for _,b in L])
    ln=np.log(m) if fake is None else np.log(fake)
    w=1-np.log(m)/np.log(X)
    return -(np.sin(np.outer(T,ln))*(w*lp/(np.sqrt(m)*np.log(m)))).sum(1)/np.pi
def res(Sv): return theta(g)/np.pi+Sv-(n-1.5)
r0=res(S(g,1)); print(f"smooth only: RMS={np.sqrt(np.mean(r0**2)):.4f} mean={r0.mean():+.4f}")
prev=None; vals={}
for X in (10,100,1000,10**4,3*10**4):
    r=res(S(g,X)); rms=np.sqrt(np.mean(r**2)); vals[X]=(rms,r.mean())
    print(f"X={X}: RMS={rms:.4f} mean={r.mean():+.4f} max|r|={np.abs(r).max():.4f}")
rng=np.random.default_rng(20261122); L=lam(10**4); fake=rng.integers(2,10**4+1,size=len(L))
rf=res(S(g,10**4,fake=fake)); print(f"B4 fake primes X=1e4: RMS={np.sqrt(np.mean(rf**2)):.4f}")
seq=[vals[X][0] for X in (10,100,1000,10**4,3*10**4)]
print("B1 strictly decreasing:",all(a>b for a,b in zip(seq,seq[1:])))
print("B2:",vals[10**4][0]<0.028 and vals[3*10**4][0]<vals[10**4][0])
print("B3:",abs(vals[3*10**4][1])<0.01 and abs(vals[3*10**4][1])<abs(vals[10][1]))
