# post hoc (labelled): 4b/4c rerun with interpolated correlations and a wider grid (t4_debug.py method)
import numpy as np
from scipy.special import psi
src=open('mirror_pair.py').read()
exec(src[:src.index('for t in (14')]); exec(src[src.index('def theta'):src.index('def lam')])
dx=0.001; xs=np.arange(-6,6,dx); r=np.arange(-400,400,0.02); cs=np.arange(-1.5,1.51,0.5)
def bump(c,w=0.5): u=(xs-c)/w; out=np.zeros_like(xs); m=np.abs(u)<1; out[m]=np.exp(-1/(1-u[m]**2)); return out
def FT(f,z):
    z=np.atleast_1d(z); out=np.empty(len(z),complex)
    for s in range(0,len(z),4000): out[s:s+4000]=(np.exp(1j*np.outer(z[s:s+4000],xs))@f)*dx
    return out
def Lam(N):
    L=[]
    for n in range(2,N+1):
        p=next(q for q in range(2,n+1) if n%q==0); k=n
        while k%p==0: k//=p
        if k==1: L.append((n,np.log(p)))
    return L
PL=Lam(60); rng=np.random.default_rng(20261122); fake=[(int(m),l) for m,(n,l) in zip(rng.integers(2,61,size=len(PL)),PL)]
fs=[bump(c) for c in cs]; Fr=[FT(f,r) for f in fs]; Fg=[FT(f,g) for f in fs]
Fp=[FT(f,[0.5j])[0] for f in fs]; Fm=[FT(f,[-0.5j])[0] for f in fs]; K=np.real(psi(0.25+0.5j*r))
k=len(fs); Z=np.zeros((k,k)); Aq=np.zeros((k,k)); Af=np.zeros((k,k))
for i in range(k):
    for j in range(k):
        gc=np.correlate(fs[i],fs[j],mode='full')*dx; lag=(np.arange(len(gc))-(len(xs)-1))*dx; G=lambda x: np.interp(x,lag,gc)
        Z[i,j]=2*np.real(np.sum(Fg[i]*np.conj(Fg[j])))
        base=(Fp[i]*Fm[j]+Fm[i]*Fp[j]).real-G(0)*np.log(np.pi)+np.trapezoid(np.real(Fr[i]*np.conj(Fr[j]))*K,r)/(2*np.pi)
        Aq[i,j]=base-sum(l/np.sqrt(n)*(G(np.log(n))+G(-np.log(n))) for n,l in PL)
        Af[i,j]=base-sum(l/np.sqrt(n)*(G(np.log(n))+G(-np.log(n))) for n,l in fake)
Aq=(Aq+Aq.T)/2; Af=(Af+Af.T)/2; ez=np.linalg.eigvalsh(Z); eq=np.linalg.eigvalsh(Aq); ef=np.linalg.eigvalsh(Af)
print(f"post hoc 4b: max|A-Z| = {np.abs(Aq-Z).max():.2e} (rel {np.abs(Aq-Z).max()/np.abs(Z).max():.2e}); eig min/max true primes {eq.min()/eq.max():+.3e}; zero-side Gram {ez.min()/ez.max():+.3e}")
print(f"post hoc 4c: eig min/max fake primes {ef.min()/ef.max():+.3e}")
print("eigenvalues true:",np.round(eq,8)); print("eigenvalues zero side:",np.round(ez,8))
