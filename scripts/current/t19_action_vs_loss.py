import numpy as np, math
N=400
def hess(T,euclid=False):
    h=T/N; n=N-1
    H=np.zeros((n,n))
    for i in range(n):
        H[i,i]=2/h+(h if euclid else -h)
        if i+1<n: H[i,i+1]=H[i+1,i]=-1/h
    b=np.zeros(n); b[-1]=1/h   # from x_N=1 boundary
    return H,b
res={}
idx={}
for T in [1,2,4,7,10]:
    H,b=hess(T); ev=np.linalg.eigvalsh(H); idx[T]=(int((ev<0).sum()), math.floor(T/math.pi))
res['A1 index vs floor(T/pi)']=idx
res['A1 pass']=all(a==b for a,b in idx.values())
def gd(T,euclid,steps=200000):
    H,b=hess(T,euclid); ev=np.linalg.eigvalsh(H); lr=1/ev.max()
    x=np.zeros(N-1); xs=np.linalg.solve(H,b); d0=np.linalg.norm(x-xs)
    for _ in range(steps):
        x-=lr*(H@x-b)
        if np.linalg.norm(x)>1e6: break
    return x,xs,d0
t=lambda T:np.linspace(0,T,N+1)[1:-1]
x,xs,d0=gd(1,False); res['A2 T=1 err vs sin']=float(np.abs(x-np.sin(t(1))/np.sin(1)).max())
x,xs,d0=gd(4,False,20000); res['A2 T=4 dist ratio']=float(np.linalg.norm(x-xs)/d0)
H,b=hess(4,True); res['A3 S_E min eig>0']=bool(np.linalg.eigvalsh(H).min()>0)
x,xs,d0=gd(4,True); res['A3 T=4 err vs sinh']=float(np.abs(x-np.sinh(t(4))/np.sinh(4)).max())
# A4
rng=np.random.default_rng(0); W=[rng.normal(size=(5,5))*0.7 for _ in range(4)]; a0=rng.normal(size=5); y=rng.normal(size=5)
def fwd(W):
    a=[a0]
    for Wk in W: a.append(np.tanh(Wk@a[-1]))
    return a
def loss(W): return 0.5*np.sum((fwd(W)[-1]-y)**2)
a=fwd(W); lam=a[-1]-y; grads=[None]*4
for k in reversed(range(4)):
    delta=lam*(1-a[k+1]**2)        # costate through the nonlinearity
    grads[k]=np.outer(delta,a[k])  # backward x forward
    lam=W[k].T@delta
eps=1e-6; err=0
for k in range(4):
    for i in range(5):
        for j in range(5):
            Wp=[w.copy() for w in W]; Wm=[w.copy() for w in W]; Wp[k][i,j]+=eps; Wm[k][i,j]-=eps
            fd=(loss(Wp)-loss(Wm))/(2*eps); err=max(err,abs(fd-grads[k][i,j])/(abs(fd)+1e-12))
res['A4 max rel err']=float(err)
H,_=hess(7); R=rng.normal(size=H.shape); R=(R+R.T)/2; np.fill_diagonal(R,np.diag(H))
res['null random index (T=7 diag)']=int((np.linalg.eigvalsh(R)<0).sum())
for k,v in res.items(): print(k,v)
