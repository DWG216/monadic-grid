import numpy as np
src=open('mirror_pair.py').read()
exec(src[:src.index('for t in (14')]); exec(src[src.index('def theta'):src.index('def lam')])
def jacobi(ev,w):
    n=len(ev); q=np.sqrt(w/w.sum()); Q=[q]; a=[]; b=[]; qprev=np.zeros(n); beta=0
    for k in range(n):
        v=ev*Q[-1]-beta*qprev; al=Q[-1]@v; v-=al*Q[-1]
        for u in Q: v-=(u@v)*u
        v-=(Q[-1]@v)*Q[-1]
        a.append(al); beta=np.linalg.norm(v)
        if k<n-1: b.append(beta); qprev=Q[-1]; Q.append(v/beta)
    return np.array(a),np.array(b)
targets=np.log([2,3,5,7])
def power(w):
    a,b=jacobi(g,w); k=np.arange(len(a)); d=a-np.polyval(np.polyfit(k,a,3),k)
    return np.array([abs(np.sum(d*np.exp(1j*a*x)))**2 for x in targets]),a,b
h=1e-5; Zp=np.array([(Z(t+h)-Z(t-h))/(2*h) for t in g]); w_zeta=1/Zp**2
def Lam(N):
    L=[]
    for n in range(2,N+1):
        p=next(q for q in range(2,n+1) if n%q==0); k=n
        while k%p==0: k//=p
        if k==1: L.append((n,np.log(p)))
    return L
PL=Lam(50); rng=np.random.default_rng(20261122)
w_prime=np.abs(sum(l*n**(-0.5-1j*g) for n,l in PL))**2
fake=rng.integers(2,51,size=len(PL)); w_fake=np.abs(sum(l*float(m)**(-0.5-1j*g) for m,(n,l) in zip(fake,PL)))**2
def test(name,w):
    P,a,b=power(w); J=np.diag(a)+np.diag(b,1)+np.diag(b,-1); err=np.abs(np.sort(np.linalg.eigvalsh(J))-np.sort(g)).max()
    N=np.array([power(rng.permutation(w))[0] for _ in range(200)]); q95=np.quantile(N,0.95,axis=0); pct=(N<P).mean(axis=0)
    print(f"{name}: eig err {err:.1e}; percentiles at ln2,3,5,7 = {np.round(pct,3)}; above 95th at {int((P>q95).sum())} of 4")
print(f"weights 1/|zeta'|^2: range {w_zeta.min():.3g} .. {w_zeta.max():.3g}")
test("A1 zeta' weights",w_zeta); test("A2 prime-polynomial weights (built-in)",w_prime); test("A3 fake-prime weights",w_fake)
