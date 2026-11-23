import numpy as np, itertools
rng=np.random.default_rng(9)
def qmul(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return np.array([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0])
qc=lambda a: a*np.array([1,-1,-1,-1])
unit=lambda: (lambda v:v/np.linalg.norm(v))(rng.normal(size=4))
def R4(p,q): return np.array([qmul(qmul(p,e),qc(q)) for e in np.eye(4)]).T
# --- Q1 ---
print('Q1. 4D rotations from two quaternion spheres')
ok=True
for _ in range(20):
    R=R4(unit(),unit()); ok&=np.allclose(R.T@R,np.eye(4)) and np.isclose(np.linalg.det(R),1)
print('   v -> p v q* is always a rotation (orthogonal, det 1):',ok)
pairs=list(itertools.combinations(range(4),2))
def biv(i,j): B=np.zeros((4,4)); B[i,j]=1; B[j,i]=-1; return B
eps=np.zeros((4,)*4)
for p in itertools.permutations(range(4)): eps[p]=np.linalg.det(np.eye(4)[list(p)])
star=lambda B:0.5*np.einsum('abcd,cd->ab',eps,B)
SD=[biv(*pr)+star(biv(*pr)) for pr in pairs[:3]]; ASD=[biv(*pr)-star(biv(*pr)) for pr in pairs[:3]]
def act(R,B): return R@B@R.T
def moves(R,basis): return max(np.linalg.norm(act(R,B)-B) for B in basis)
p=unit(); q=unit(); one=np.array([1.,0,0,0])
print('   turning only p:  self-dual moves %.3f, anti-self-dual moves %.1e'%(moves(R4(p,one),SD),moves(R4(p,one),ASD)))
print('   turning only q:  self-dual moves %.1e, anti-self-dual moves %.3f'%(moves(R4(one,q),SD),moves(R4(one,q),ASD)))
# --- Q2 ---
print('Q2. Lorentzian: one complex sphere and its mirror')
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.array([[1,0],[0,-1]]); s=[sx,sy,sz]
X=(rng.normal(size=3)+1j*rng.normal(size=3))*0.7
M=__import__('scipy.linalg',fromlist=['expm']).expm(0.5*sum(X[k]*s[k] for k in range(3)))   # general Lorentz element (rotation + boost)
O=np.array([[0.5*np.trace(s[a]@M@s[b]@np.linalg.inv(M)) for b in range(3)] for a in range(3)])  # complex 3x3 rotation it induces
E=rng.normal(size=(3,3));E=E+E.T;E-=np.trace(E)/3*np.eye(3);B=rng.normal(size=(3,3));B=B+B.T;B-=np.trace(B)/3*np.eye(3)
Qp=E-1j*B; Qm=E+1j*B
Qp2=O@Qp@O.T; Qm2=np.conj(O)@Qm@np.conj(O).T
print('   O is a complex rotation (O O^T = 1):',np.allclose(O@O.T,np.eye(3)),'| O is not real (genuine boost):',not np.allclose(O.imag,0))
print('   after the transformation, hand - is still the mirror of hand +:',np.allclose(Qm2,np.conj(Qp2)))
print('   invariant of each hand alone, tr(Q^2), unchanged:',np.isclose(np.trace(Qp2@Qp2),np.trace(Qp@Qp)))
# --- Q3 ---
print('Q3. Sky readings are squares of spinors')
C=1j*sy
for z in [0.3+0.8j,-1.2+0.1j,2.0-0.5j]:
    k=np.array([1,z]); w=np.array([k@C@si@k for si in s]); v=np.array([1-z*z,1j*(1+z*z),-2*z])
    r=w/v; print('   z=%s: spinor-square / v(z) = %s (constant ratio -> same null direction)'%(z,np.round(r,6)))
Psi=rng.normal(size=5)+1j*rng.normal(size=5)
quart=lambda k: sum(Psi[j]*np.math.comb(4,j)*k[0]**(4-j)*k[1]**j for j in range(5)) if hasattr(np,'math') else None
import math
quart=lambda k: sum(Psi[j]*math.comb(4,j)*k[0]**(4-j)*k[1]**j for j in range(5))
k=np.array([0.6,0.8j]); a=0.7
print('   phase kappa -> e^{ia} kappa multiplies the quartic by e^{4ia}:',np.isclose(quart(np.exp(1j*a)*k),np.exp(4j*a)*quart(k)))
# --- Q4 ---
print('Q4. Is the quaternion sphere self-mirrored? (S M = conj(M) S for all M)')
def solspace(Ms):
    A=np.vstack([np.kron(np.eye(2),Mi.T)-np.kron(np.conj(Mi),np.eye(2)) for Mi in Ms])   # vec(S M - conj(M) S)=0 (row-major)
    sv=np.linalg.svd(A,compute_uv=False); return int((sv<1e-9).sum())
SU2=[]; SL2=[]
for _ in range(6):
    qq=unit(); SU2.append(qq[0]*np.eye(2)-1j*(qq[1]*sx+qq[2]*sy+qq[3]*sz))
    SL2.append(__import__('scipy.linalg',fromlist=['expm']).expm(sum((rng.normal()+1j*rng.normal())*si for si in s)))
print('   unit quaternions (SU(2)): solutions =',solspace(SU2),'| check sigma_y works:',all(np.allclose(sy@U,np.conj(U)@sy) for U in SU2))
print('   general Lorentz (SL(2,C)): solutions =',solspace(SL2))
