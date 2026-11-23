import numpy as np, itertools
from scipy.linalg import expm
rng=np.random.default_rng(21); eta=np.diag([-1.,1,1,1])
def kn(h,k): return (np.einsum('ac,bd->abcd',h,k)+np.einsum('bd,ac->abcd',h,k)-np.einsum('ad,bc->abcd',h,k)-np.einsum('bc,ad->abcd',h,k))
def sym(): a=rng.normal(size=(4,4)); return a+a.T
R=sum(kn(sym(),sym()) for _ in range(4)); ei=np.linalg.inv(eta)
Ric=np.einsum('ac,abcd->bd',ei,R); Rs=np.einsum('bd,bd',ei,Ric)
C=R-0.5*kn(Ric,eta)+Rs/12*kn(eta,eta)
print('Weyl tensor is trace-free:',np.allclose(np.einsum('ac,abcd->bd',ei,C),0))
eps3=np.zeros((3,3,3))
for p in itertools.permutations(range(3)): eps3[p]=np.linalg.det(np.eye(3)[list(p)])
def EB(C):
    E=C[0,1:,0,1:]; B=0.5*np.einsum('ipq,pqj->ij',eps3,C[1:,1:,0,1:]); return E,B
s=[np.eye(2),np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1.,-1])]
def Lam(M1,M2): return np.array([[0.5*np.trace(s[a]@M1@s[b]@M2.conj().T) for b in range(4)] for a in range(4)])
def Orot(M): return np.array([[0.5*np.trace(s[a]@M@s[b]@np.linalg.inv(M)) for b in range(1,4)] for a in range(1,4)])
def transform(C,L): return np.einsum('ea,fb,gc,hd,efgh->abcd',L,L,L,L,C)
def randM(): return expm(sum((rng.normal()+1j*rng.normal())*0.5*s[k] for k in range(1,4)))
E,B=EB(C); Qp,Qm=E-1j*B, E+1j*B
print('E, B symmetric and trace-free:',np.allclose(E,E.T),np.allclose(B,B.T),abs(np.trace(E))<1e-9,abs(np.trace(B))<1e-9)
def which(Q,Q2,cands):
    return [n for n,X in cands.items() if np.allclose(Q2,X@Q@X.T,atol=1e-8)]
print('\nREAL Lorentz transformation (one spinor matrix M):')
M=randM(); L=Lam(M,M); print('  L is real:',np.allclose(L.imag,0),'| preserves the light cone (L^T eta L = eta):',np.allclose(L.real.T@eta@L.real,eta))
C2=transform(C,L.real); E2,B2=EB(C2); Qp2,Qm2=E2-1j*B2,E2+1j*B2
O=Orot(M); c={'O':O,'O^T':O.T,'conj O':O.conj(),'conj O^T':O.conj().T,'O^-1':np.linalg.inv(O)}
print('  O from M is a genuine complex rotation:',np.allclose(O@O.T,np.eye(3)),'| not real:',not np.allclose(O.imag,0))
print('  hand + transforms by:',which(Qp,Qp2,c)); print('  hand - transforms by:',which(Qm,Qm2,c))
print('  hand - is the mirror of hand + after transforming:',np.allclose(Qm2,Qp2.conj()))
print('\nCOMPLEXIFIED transformation (two independent spinor matrices M1, M2):')
M1,M2=randM(),randM(); Lc=Lam(M1,M2); print('  L preserves eta (complex bilinear):',np.allclose(Lc.T@eta@Lc,eta),'| L is not real:',not np.allclose(Lc.imag,0))
C3=transform(C,Lc); E3,B3=EB(C3); Qp3,Qm3=E3-1j*B3,E3+1j*B3
c1={'from M1: '+k:v for k,v in {'O':Orot(M1),'O^T':Orot(M1).T,'O^-1':np.linalg.inv(Orot(M1))}.items()}
c2={'from M2: '+k:v for k,v in {'conj O':Orot(M2).conj(),'conj O^T':Orot(M2).conj().T,'O':Orot(M2),'O^T':Orot(M2).T}.items()}
both={**c1,**c2}
print('  hand + transforms by:',which(Qp,Qp3,both)); print('  hand - transforms by:',which(Qm,Qm3,both))
print('  hand - still the mirror of hand +:',np.allclose(Qm3,Qp3.conj()),'| mismatch size: %.3f'%(np.linalg.norm(Qm3-Qp3.conj())/np.linalg.norm(Qp3)))
