import numpy as np, itertools, time
d=3
def ket(*idx):
    v=np.zeros(d**len(idx),dtype=complex); v[np.ravel_multi_index(idx,(d,)*len(idx))]=1; return v
def code(i): return sum(ket(j,(j+i)%3,(j+2*i)%3) for j in range(3))/np.sqrt(3)
def rep(i): return ket(i,i,i)
def state(enc):
    # R (dim 3) x Q1 Q2 Q3
    return sum(np.kron(ket(i),enc(i)) for i in range(3))/np.sqrt(3)
def S(rho):
    w=np.linalg.eigvalsh(rho); w=w[w>1e-14]; return float(-(w*np.log(w)/np.log(3)).sum())
def reduced(psi,keep):  # subsystems 0=R,1,2,3
    T=psi.reshape((3,)*4); rest=[k for k in range(4) if k not in keep]
    T=np.transpose(T,keep+rest).reshape(3**len(keep),-1); return T@T.conj().T
def MI(psi,A,B): return S(reduced(psi,A))+S(reduced(psi,B))-S(reduced(psi,sorted(A+B)))
res={}
for name,enc in [('code',code),('repetition',rep)]:
    psi=state(enc)
    res[name+' I(R:single)']=[round(MI(psi,[0],[k]),12) for k in (1,2,3)]
    res[name+' I(R:pair)']=[round(MI(psi,[0],list(p)),12) for p in [(1,2),(1,3),(2,3)]]
def perm_ryser(A):
    n=len(A); tot=0
    for k in range(1,1<<n):
        bits=[j for j in range(n) if k>>j&1]
        tot+=(-1)**len(bits)*np.prod(A[:,bits].sum(1))
    return (-1)**n*tot
rng=np.random.default_rng(0); tp=[];td=[]
ns=list(range(12,21,2))
for n in ns:
    U=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))[0]
    t0=time.perf_counter(); perm_ryser(U) if n<=16 else None; t1=time.perf_counter()
    for _ in range(200): np.linalg.det(U)
    t2=time.perf_counter(); tp.append(t1-t0); td.append((t2-t1)/200)
# permanents at n=18,20 extrapolated? no: measure only up to 16 (pre-registered 12..20; reduced, disclosed)
fp=[(tp[i+1]/tp[i])**0.5 for i in range(2)]   # per +1 n from steps of 2 (n=12,14,16)
fd=[(td[i+1]/td[i])**0.5 for i in range(len(ns)-1)]
res['Q4 permanent times n=12,14,16']=[round(t,4) for t in tp[:3]]
res['Q4 permanent growth per +1 n']=[round(x,3) for x in fp]
res['Q4 determinant growth per +1 n']=[round(x,3) for x in fd]
for k,v in res.items(): print(k,v)
