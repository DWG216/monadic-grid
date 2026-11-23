import numpy as np
from scipy.special import psi
src=open('mirror_pair.py').read()
exec(src[:src.index('for t in (14')]); exec(src[src.index('def theta'):src.index('def lam')])
dx=0.001; xs=np.arange(-6,6,dx); r=np.arange(-400,400,0.02)
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
PL=Lam(200)
for c1,c2 in ((0,0),(1,1),(0,1),(-1.5,1.5)):
    f1,f2=bump(c1),bump(c2)
    gc=np.correlate(f1,f2,mode='full')*dx; lag=(np.arange(len(gc))-(len(xs)-1))*dx   # g(x)=int f2(u) f1(u+x) du
    G=lambda x: np.interp(x,lag,gc)
    F1g,F2g=FT(f1,g),FT(f2,g); Z=2*np.real(np.sum(F1g*np.conj(F2g)))
    F1r,F2r=FT(f1,r),FT(f2,r); hr=np.real(F1r*np.conj(F2r))
    hp=FT(f1,[0.5j])[0]*FT(f2,[-0.5j])[0]+FT(f1,[-0.5j])[0]*FT(f2,[0.5j])[0]
    A=hp.real-G(0)*np.log(np.pi)+np.trapezoid(hr*np.real(psi(0.25+0.5j*r)),r)/(2*np.pi)-sum(l/np.sqrt(n)*(G(np.log(n))+G(-np.log(n))) for n,l in PL)
    print(f"c=({c1},{c2}): zero side {Z:.6e} arithmetic {A:.6e} rel diff {abs(A-Z)/abs(Z):.2e}")
