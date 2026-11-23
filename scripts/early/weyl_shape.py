# Calculation 1: where the two hands' Weyl curvatures can meet (4D Euclidean, vacuum: mixed/Ricci block = 0)
import numpy as np
exec(open('chiral_curv.py').read().split('for ein in')[0])
def weyl(A=None,B=None):
    def tl(): m=rng.normal(size=(3,3)); m=m+m.T; return m-np.trace(m)/3*np.eye(3)
    A=tl() if A is None else A; B=tl() if B is None else B
    M=np.block([[A,np.zeros((3,3))],[np.zeros((3,3)),B]]); return riemann_from_operator(M,SD+ASD),A,B
_fr=np.random.default_rng(7).normal(size=(4,3))
def frame(u):  # orthonormal basis with u first (fixed completion)
    Q,_=np.linalg.qr(np.column_stack([u,_fr])); Q[:,0]*=np.sign(Q[:,0]@u); return Q
eps3=np.zeros((3,3,3))
for (i,j,k),s in {(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}.items(): eps3[i,j,k]=s
def EB(R,u):
    F=frame(u); Rf=np.einsum('abcd,ai,bj,ck,dl->ijkl',R,F,F,F,F)
    E=Rf[0,1:,0,1:]                                   # tidal (shape) part seen by observer u
    Bm=0.5*np.einsum('jkl,ikl->ij',eps3,Rf[0,1:,1:,1:])   # twisting part
    return E,Bm
# (a) volume-type invariant: |Rm|^2 = sum of each hand's own square, no cross term
R,A,B=weyl(); full=np.einsum('abcd,abcd',R,R)
print('(a) |Riemann|^2 =',round(full,6),'  |W+|^2+|W-|^2 (x1/4 norm.) =',round(0.25*(np.sum(A*A)+np.sum(B*B)),6),' -> hands add, no cross term')
# (b) shape (tidal) part is linear in BOTH hands: E(A,B)=E(A,0)+E(0,B)
u=rng.normal(size=4); u/=np.linalg.norm(u)
RA,_,_=weyl(A,np.zeros((3,3))); RB,_,_=weyl(np.zeros((3,3)),B)
E,Bm=EB(R,u); EA,BA=EB(RA,u); EB_,BB=EB(RB,u)
print('(b) tidal part E is the sum of the two hands:',np.allclose(E,EA+EB_),' | twist part B too:',np.allclose(Bm,BA+BB))
print('    one hand alone has |E|=|B| (self-dual):',np.isclose(np.linalg.norm(EA),np.linalg.norm(BA)),np.isclose(np.linalg.norm(EB_),np.linalg.norm(BB)))
# (c) quadratic invariants: E.E+B.B is the same for every observer; E.E-B.B (the cross-hand term) changes with the observer
rows=[]
for _ in range(6):
    u=rng.normal(size=4); u/=np.linalg.norm(u); E,Bm=EB(R,u); rows.append((np.sum(E*E)+np.sum(Bm*Bm), np.sum(E*E)-np.sum(Bm*Bm)))
rows=np.array(rows)
print('(c) over 6 observers: E.E+B.B ranges %.6f..%.6f (constant) ; E.E-B.B ranges %.4f..%.4f (observer-dependent)'%(rows[:,0].min(),rows[:,0].max(),rows[:,1].min(),rows[:,1].max()))
# (d) with only one hand present the cross term vanishes for every observer
c=[ (lambda E,Bm: np.sum(E*E)-np.sum(Bm*Bm))(*EB(RA,v/np.linalg.norm(v))) for v in rng.normal(size=(6,4))]
print('(d) only one hand present: E.E-B.B over 6 observers =',np.round(c,10),' -> cross term needs both hands')
