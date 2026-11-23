# Pre-registered in this header (2026-11-08), before running:
# V1 [identity]: f11's numerator/denominator coefficients, divided by sqrt(C(11,k)), give two ORTHOGONAL vectors of EQUAL norm in the
#     11-qubit symmetric subspace, i.e. an 11-qubit permutation-invariant code whose N-copy map is exactly f11.
# V2 [identity]: f11 commutes with z -> e^(2 pi i/5) z and z -> -1/z (icosahedral equivariance, untwisted).
# V3 [prediction]: the 20 face-centre states are critical points of the map and go to their antipodes; feeding 11 noisy copies of a
#     face state (depolarising error eps) gives output error O(eps^2) toward the antipodal face state.
# V4 [prediction]: being untwisted, the code fails distance-3 (weight-1 Knill-Laflamme), like our N=11 untwisted control.
import numpy as np
from math import comb
N=11; c0=np.zeros(N+1); c1=np.zeros(N+1)
c0[0]=1; c0[5]=-66; c0[10]=-11          # denominator -> |0_L>
c1[1]=-11; c1[6]=66; c1[11]=1           # numerator   -> |1_L>
v0=np.array([c0[k]/np.sqrt(comb(N,k)) for k in range(N+1)]); v1=np.array([c1[k]/np.sqrt(comb(N,k)) for k in range(N+1)])
print('V1 norms^2 %.4f %.4f | overlap %.1e'%(v0@v0,v1@v1,v0@v1))
V=np.column_stack([v0,v1])/np.sqrt(v0@v0)
f=lambda z:(z**11+66*z**6-11*z)/(-11*z**10-66*z**5+1)
zs=np.random.default_rng(0).normal(size=5)+1j*np.random.default_rng(1).normal(size=5)
w=np.exp(2j*np.pi/5)
print('V2 rotation equivariance %.1e | inversion -1/z equivariance %.1e'%(max(abs(f(w*z)-w*f(z)) for z in zs),max(abs(f(-1/z)+1/f(z)) for z in zs)))
# Dicke-basis machinery
def spin(N):
    j=N/2; m=j-np.arange(N+1); Jp=np.zeros((N+1,N+1))
    for k in range(1,N+1): Jp[k-1,k]=np.sqrt(j*(j+1)-m[k]*(m[k]+1))
    return (Jp+Jp.T)/2,(Jp-Jp.T)/(2j),np.diag(m)
J=spin(N)
def Rot(z):  # SU(2) taking |0> to normalised (1,z)
    a=np.array([1,z])/np.sqrt(1+abs(z)**2); return np.array([[a[0],-np.conj(a[1])],[a[1],np.conj(a[0])]])
def Dm(U):
    from scipy.linalg import expm
    w_,v_=np.linalg.eig(U); L=np.log(w_); Hm=-1j*(v_@np.diag(L)@np.linalg.inv(v_))   # U = exp(iHm)... use axis-angle
    X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1,-1])
    U=U/np.sqrt(np.linalg.det(U)); a=np.real(np.trace(U))/2; v=np.real([1j*np.trace(U@P) for P in (X,Y,Z)])/2; s=np.linalg.norm(v)
    th=2*np.arctan2(s,a); n=v/s; Hh=n[0]*J[0]+n[1]*J[1]+n[2]*J[2]; ww,W=np.linalg.eigh(Hh); return (W*np.exp(-1j*th*ww))@W.conj().T
# face centres = critical points: roots of the Hessian-type polynomial; find numerically as critical points of f
from numpy.polynomial import polynomial as Pn
num=Pn.Polynomial([0,-11,0,0,0,0,66,0,0,0,0,1]); den=Pn.Polynomial([1,0,0,0,0,-66,0,0,0,0,-11])
crit=(num.deriv()*den-num*den.deriv()).roots()
print('   finite critical points found:',len(crit),'(20 expected, possibly some at infinity)')
def out_err(z,eps,target):
    D=Dm(Rot(z)); D0=D[:,0]; D1=D[:,1]  # |z^N> and one-flip state are rotated Dicke 0 and 1
    rho=np.zeros((2,2),complex)
    for k in range(N+1):
        a=V.conj().T@D[:,k]; rho+=eps**k*(1-eps)**(N-k)*np.outer(a,a.conj())
    p=np.real(np.trace(rho)); rho/=p; t=np.array([1,target])/np.sqrt(1+abs(target)**2)
    return 1-np.real(t.conj()@rho@t),p
zc=crit[np.argmin(abs(crit))]; tgt=f(zc)
print('V3 face state z=%.3f%+.3fi -> f(z)=%.3f%+.3fi ; antipode of z = %.3f%+.3fi'%(zc.real,zc.imag,tgt.real,tgt.imag,(-1/np.conj(zc)).real,(-1/np.conj(zc)).imag))
e1,p1=out_err(zc,1e-3,tgt); e2,_=out_err(zc,1e-4,tgt)
print('   output error at eps 1e-3: %.2e, 1e-4: %.2e -> exponent %.2f | acceptance %.3f'%(e1,e2,np.log10(e1/e2),p1))
th=[e for e in np.linspace(0.005,0.45,90) if out_err(zc,e,tgt)[0]<e]; print('   improves up to eps = %.3f'%(max(th) if th else 0))
# V4: KL degree 1
M=[V.conj().T@A@V for A in J]; print('V4 weight-1 KL residual (Frobenius, non-scalar part): %.3f'%max(np.linalg.norm(m-np.trace(m)/2*np.eye(2)) for m in M))
