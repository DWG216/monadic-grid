import numpy as np
rng=np.random.default_rng(20261122); NT=256; t=np.pi*np.arange(NT)/NT; P=np.array([np.cos(t),np.sin(t)])
aa=rng.normal(size=4); bb=rng.normal(size=4); cc=rng.normal(size=4)
def lin(v,x): om=x@P; return v[0]*om[0]+v[1]*om[1]+v[2]*P[0]+v[3]*P[1]
def psi(x,w=lambda k:(4-k,k)):
    f=(lin(aa,x)**2+lin(bb,x)**2)**-3; return np.array([np.mean(P[0]**w(k)[0]*P[1]**w(k)[1]*f)*np.pi for k in range(5)])
def ff(p,k): out=1.0
    # falling factorial
def fall(p,k):
    r=1.0
    for j in range(k): r*=p-j
    return r
from math import comb
def series_inv(q,n):
    # power series of 1/q (q[0] != 0), coefficients along axis 0, to order n
    r=[1/q[0]]
    for k in range(1,n+1):
        acc=sum(q[j]*r[k-j] for j in range(1,min(k,len(q)-1)+1)); r.append(-acc/q[0])
    return r
def phi(x,shift=0):
    a=lin(aa,x); b=lin(bb,x); c=lin(cc,x)
    def D4(v):
        av=aa[0]*v[0]+aa[1]*v[1]; bv=bb[0]*v[0]+bb[1]*v[1]; cv=cc[0]*v[0]+cc[1]*v[1]
        Q=[a*a+b*b, 2*(a*av+b*bv), av*av+bv*bv]            # q along omega + s v
        iQ=series_inv(Q,4); iQ2=[sum(iQ[j]*iQ[k-j] for j in range(k+1)) for k in range(5)]
        C6=[comb(6,k)*c**(6-k)*cv**k for k in range(5)]
        g4=sum(C6[j]*iQ2[4-j] for j in range(5))           # coefficient of s^4
        return 24*g4
    vs=[np.array([1.0,s_]) for s_ in (-2,-1,0,1,2)]; M=np.array([[comb(4,m)*v[1]**m for m in range(5)] for v in vs])
    vals=np.array([np.mean(D4(v))*np.pi for v in vs]); comps=np.linalg.solve(M,vals)
    return np.roll(comps,shift) if shift else comps
def dx(F,x,i,j,h=1e-5):
    e=np.zeros((2,2)); e[i,j]=h; return (F(x+e)-F(x-e))/(2*h)
def res_plus(F):
    r=0
    for _ in range(20):
        x=rng.normal(size=(2,2))
        for A in (0,1):
            a=dx(F,x,A,0); b=dx(F,x,A,1)
            for k in range(4): r=max(r,abs(a[k+1]-b[k])/max(abs(a[k+1]),abs(b[k]),1e-300))
    return r
def res_minus(F):
    r=0
    for _ in range(20):
        x=rng.normal(size=(2,2))
        for Ap in (0,1):
            a=dx(F,x,0,Ap); b=dx(F,x,1,Ap)
            for m in range(4): r=max(r,abs(a[m+1]-b[m])/max(abs(a[m+1]),abs(b[m]),1e-300))
    return r
x0=rng.normal(size=(2,2)); real=np.isrealobj(psi(x0)) and np.isrealobj(phi(x0))
rp=res_plus(psi); rm=res_minus(phi)
print(f"S1 split: fields real {real}; helicity +2 residual {rp:.1e}; helicity -2 residual {rm:.1e} ->",'PASS' if real and rp<1e-7 and rm<1e-7 else 'FAIL')
np_=res_plus(lambda x: psi(x,lambda k:(4-k,2*k))); nm=res_minus(lambda x: phi(x,1))
print(f"S2 null: scrambled +2 residual {np_:.2e}; shifted -2 residual {nm:.2e} ->",'PASS' if np_>1e-2 and nm>1e-2 else 'FAIL')
# S3 Lorentzian contrast (contour integral, as in section 76)
al=rng.normal(size=4)+1j*rng.normal(size=4); be=rng.normal(size=4)+1j*rng.normal(size=4)
def psiL(x):
    a0=1j*(al[0]*x[0,0]+al[1]*x[1,0])+al[2]; a1=1j*(al[0]*x[0,1]+al[1]*x[1,1])+al[3]
    b0=1j*(be[0]*x[0,0]+be[1]*x[1,0])+be[2]; b1=1j*(be[0]*x[0,1]+be[1]*x[1,1])+be[3]
    za=-a0/a1; zb=-b0/b1; rho=abs(za-zb)/2; th=2*np.pi*np.arange(96)/96; z=za+rho*np.exp(1j*th); dz=1j*rho*np.exp(1j*th)*(2*np.pi/96)
    f=1/((a0+a1*z)**3*(b0+b1*z)**3); return np.array([np.sum(z**k*f*dz)/(2j*np.pi) for k in range(5)])
def dxL(F,x,i,j,h=1e-5):
    # derivative along the Hermitian direction e_ij + e_ji (and i(e_ij - e_ji)) decomposed back to complex coordinates
    E=np.zeros((2,2),complex); E[i,j]=h; return (F(x+E)-F(x-E))/(2*h)
r3=0; im=[]
for _ in range(20):
    a=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); x=(a+a.conj().T)/2; p=psiL(x); im.append(np.abs(p.imag).max()/np.abs(p).max())
    # conj(psi) is a function of conj(x) = x^T for Hermitian x: d conj(psi)/dx^{AB'} = conj(d psi/dx^{B'A}) ... indices swap
    for A in (0,1):
        a_=np.conj(dxL(psiL,x,A,0)); b_=np.conj(dxL(psiL,x,A,1))
        # swapped equation: d/dx^{0' A} conj(psi)_{k+1} - d/dx^{1' A} conj(psi)_k = 0, with x^{A'A} = conj(x^{AA'})
        for k in range(4): r3=max(r3,abs(a_[k+1]-b_[k])/max(abs(a_[k+1]),abs(b_[k])))
print(f"S3 Lorentzian: |Im psi|/|psi| median {np.median(im):.2f}; conj(psi) obeys the other hand's equation, residual {r3:.1e} ->",'PASS' if r3<1e-7 and np.median(im)>0.1 else 'FAIL')
