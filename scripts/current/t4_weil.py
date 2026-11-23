import numpy as np
from scipy.special import psi
src=open('mirror_pair.py').read()
exec(src[:src.index('for t in (14')]); exec(src[src.index('def theta'):src.index('def lam')])
gam=np.concatenate([g,-g])
def Lam(N):
    L=[]
    for n in range(2,N+1):
        p=next(q for q in range(2,n+1) if n%q==0); k=n
        while k%p==0: k//=p
        if k==1: L.append((n,np.log(p)))
    return L
r=np.arange(-400,400,0.01)
def arch(hr): return np.trapezoid(hr*np.real(psi(0.25+0.5j*r)),r)/(2*np.pi)
# 4a Gaussian check
hz=np.exp(-gam**2/25); gx=lambda x: 5/(2*np.sqrt(np.pi))*np.exp(-25*x*x/4)
A=2*np.exp(1/100)-gx(0)*np.log(np.pi)+arch(np.exp(-r**2/25))-sum(l/np.sqrt(n)*2*gx(np.log(n)) for n,l in Lam(200))
print(f"4a Gaussian: zero side {hz.sum():.8f} arithmetic side {A:.8f} diff {abs(hz.sum()-A):.2e}")
# 4b bumps
xs=np.arange(-2.6,2.6,0.0005); cs=np.arange(-1.5,1.51,0.5); w=0.5
def bump(c): u=(xs-c)/w; out=np.zeros_like(xs); m=np.abs(u)<1; out[m]=np.exp(-1/(1-u[m]**2)); return out
fs=[bump(c) for c in cs]
def FT(f,z):
    z=np.atleast_1d(z); out=np.empty(len(z),complex)
    for s in range(0,len(z),2000): out[s:s+2000]=(np.exp(1j*np.outer(z[s:s+2000],xs))@f)*0.0005
    return out
Fr=[FT(f,r) for f in fs]; Fg=[FT(f,g) for f in fs]; Fp=[FT(f,[0.5j])[0] for f in fs]; Fm=[FT(f,[-0.5j])[0] for f in fs]
k=len(fs); Z=np.zeros((k,k)); Aq=np.zeros((k,k)); Af=np.zeros((k,k))
PL=Lam(60); rng=np.random.default_rng(20261122); fake=[(int(m),l) for m,(n,l) in zip(rng.integers(2,61,size=len(PL)),PL)]
def corr(i,j,x):  # g_ij(x) = int f_j(u) f_i(u+x) du
    sh=int(round(x/0.0005)); fi=fs[i]; fj=fs[j]
    if sh>=0: return np.sum(fj[:len(xs)-sh]*fi[sh:])*0.0005
    return np.sum(fj[-sh:]*fi[:len(xs)+sh])*0.0005
for i in range(k):
    for j in range(k):
        Z[i,j]=2*np.real(np.sum(Fg[i]*np.conj(Fg[j])))
        hr=Fr[i]*Fr[j][::-1] if False else Fr[i]*np.conj(Fr[j])
        base=(Fp[i]*Fm[j]+Fm[i]*Fp[j]).real-corr(i,j,0)*np.log(np.pi)+arch(hr.real)
        Aq[i,j]=base-sum(l/np.sqrt(n)*(corr(i,j,np.log(n))+corr(i,j,-np.log(n))) for n,l in PL)
        Af[i,j]=base-sum(l/np.sqrt(n)*(corr(i,j,np.log(n))+corr(i,j,-np.log(n))) for n,l in fake)
Aq=(Aq+Aq.T)/2; Af=(Af+Af.T)/2
ez=np.linalg.eigvalsh(Z); eq=np.linalg.eigvalsh(Aq); ef=np.linalg.eigvalsh(Af)
print(f"4b rel. error |A-Z|/|Z| = {np.abs(Aq-Z).max()/np.abs(Z).max():.2e}")
print(f"4b eigenvalues true primes: min/max = {eq.min()/eq.max():+.3e}  (zero-side Gram min/max = {ez.min()/ez.max():+.3e})")
print(f"4c eigenvalues fake primes: min/max = {ef.min()/ef.max():+.3e}")
