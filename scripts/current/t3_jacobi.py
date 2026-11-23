import numpy as np
src=open('mirror_pair.py').read()
exec(src[:src.index('for t in (14')]); exec(src[src.index('def theta'):src.index('def lam')])
def jacobi(ev):
    n=len(ev); q=np.ones(n)/np.sqrt(n); Q=[q]; a=[]; b=[]; qprev=np.zeros(n); beta=0
    for k in range(n):
        v=ev*Q[-1]-beta*qprev; al=Q[-1]@v; v-=al*Q[-1]
        for u in Q: v-=(u@v)*u
        a.append(al); beta=np.linalg.norm(v)
        if k<n-1: b.append(beta); qprev=Q[-1]; Q.append(v/beta)
    return np.array(a),np.array(b)
def power(z,xs):
    a,b=jacobi(z); k=np.arange(len(a)); d=a-np.polyval(np.polyfit(k,a,3),k)
    return np.array([abs(np.sum(d*np.exp(1j*a*x)))**2 for x in xs]),a,b
a0,b0=jacobi(g); J=np.diag(a0)+np.diag(b0,1)+np.diag(b0,-1)
print("eigenvalue check: max|eig(J)-zeros| =",f"{np.abs(np.sort(np.linalg.eigvalsh(J))-np.sort(g)).max():.2e}")
targets=np.log([2,3,5,7]); P,_,_=power(g,targets)
rng=np.random.default_rng(20261122); sp=np.diff(g); nulls=[]
for _ in range(200):
    z=np.concatenate([[g[0]],g[0]+np.cumsum(rng.permutation(sp))]); nulls.append(power(z,targets)[0])
nulls=np.array(nulls); q95=np.quantile(nulls,0.95,axis=0); pct=(nulls<P).mean(axis=0)
for t,p,q,c in zip([2,3,5,7],P,q95,pct): print(f"x=ln{t}: P={p:.3g} null95={q:.3g} percentile={c:.3f} {'ABOVE' if p>q else 'below'}")
print("3a: above for",int((P>q95).sum()),"of 4")
# post hoc diagnostic (labelled): does the same detector find the primes in the raw zeros?
def rawP(z,xs): return np.array([abs(np.sum(np.exp(1j*z*x)))**2 for x in xs])
R=rawP(g,targets); RN=np.array([rawP(np.concatenate([[g[0]],g[0]+np.cumsum(rng.permutation(sp))]),targets) for _ in range(200)])
print("post hoc raw zeros: above null95 at", [int(t) for t,r,q in zip([2,3,5,7],R,np.quantile(RN,0.95,axis=0)) if r>q], "percentiles", np.round((RN<R).mean(axis=0),3))
