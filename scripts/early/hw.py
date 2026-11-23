import numpy as np, itertools, io, contextlib
src=open('tau60.py').read().split("# ---------- U4/U5")[0]
with contextlib.redirect_stdout(io.StringIO()): exec(src)
U=np.load('fixed_correct.npy')
# logical icosahedron and phys->logical rotations M
M=[]; a=ico[0]; b=[y for y in ico if abs(a@y-1/5**.5)<1e-6][0]
for c in orb0:
    for d in orb0:
        if abs(c@d-1/5**.5)<1e-6:
            Q=kabsch([a,b,np.cross(a,b)],[c,d,np.cross(c,d)])
            if abs(np.linalg.det(Q)-1)<1e-6 and all(min(np.linalg.norm(Q@x-y) for y in orb0)<1e-6 for x in ico) and all(np.linalg.norm(Q-m)>1e-6 for m in M): M.append(Q)
def ket(nv):
    th=np.arccos(np.clip(nv[2],-1,1)); ph=np.arctan2(nv[1],nv[0]); return np.array([np.cos(th/2),np.exp(1j*ph)*np.sin(th/2)])
def fmap(nv):
    k=ket(nv); K=k
    for _ in range(6): K=np.kron(K,k)
    a=V.conj().T@K; return bloch(np.outer(a,a.conj())/np.vdot(a,a).real)
dist=lambda x: min(min(np.linalg.norm(fmap(x)-m@x),np.linalg.norm(fmap(x)+m@x)) for m in M)
# ---- mirror partner of the 12-degree class ----
z36,z12=U[1],U[0]
v=max(ico,key=lambda w:abs(z12@w)); v=v*np.sign(z12@v); nb=[w for w in ico if abs(v@w-1/5**.5)<1e-6]
e1=nb[0]-(nb[0]@v)*v; e1/=np.linalg.norm(e1); e2=np.cross(v,e1)
az=np.arctan2(z12@e2,z12@e1); pol=np.arccos(z12@v)
mir=np.cos(pol)*v+np.sin(pol)*(np.cos(-az)*e1+np.sin(-az)*e2)
print('mirror image of the 12-deg class is itself a fixed class: residual %.1e'%dist(mir))
# ---- exact-ish form of the on-mirror class: solve 1-D fixed point to high precision in numpy then attempt identification ----
v36=max(ico,key=lambda w:abs(z36@w)); v36=v36*np.sign(z36@v36)
d36=z36-(z36@v36)*v36; d36/=np.linalg.norm(d36)
from scipy.optimize import brentq
g=lambda t: dist(np.cos(t)*v36+np.sin(t)*d36)
ts=np.linspace(0.2,0.38,400); vals=[g(t) for t in ts]; t0=ts[int(np.argmin(vals))]
from scipy.optimize import minimize_scalar
r=minimize_scalar(g,bracket=(t0-0.002,t0,t0+0.002),tol=1e-14); t36=r.x
print('on-mirror class: polar angle %.10f deg, cos^2 = %.12f, residual %.1e'%(np.degrees(t36),np.cos(t36)**2,r.fun))
# ---- transversal two-block gates ----
def two_block(gate):
    out=[]
    for i,j in [(0,0),(0,1),(1,0),(1,1)]:
        psi=np.kron(V[:,i],V[:,j]).reshape([2]*14)
        for q in range(7):
            psi=np.moveaxis(psi,[q,7+q],[0,1]); s=psi.shape; psi=(gate@psi.reshape(4,-1)).reshape(s); psi=np.moveaxis(psi,[0,1],[q,7+q])
        out.append(psi.reshape(-1))
    W=np.kron(V,V); Pw=W@W.conj().T
    return max(np.linalg.norm(o-Pw@o) for o in out)
CNOT=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]); CZ=np.diag([1,1,1,-1])
print('two-block transversal leak: CNOT %.3f | CZ %.3f  (0 = logical gate)'%(two_block(CNOT),two_block(CZ)))
# ---------------- hardware-noise distillation ----------------
def depol_each(Rr,n,p):   # Pauli depolarizing prob p on each qubit
    if p==0: return Rr
    Rr=Rr.reshape([2]*(2*n))
    for q in range(n):
        out=(1-p)*Rr
        for Pm in (X,Y,Z):
            T=np.tensordot(Pm,Rr,axes=([1],[q])); T=np.moveaxis(T,0,q)
            T=np.tensordot(T,Pm.conj(),axes=([n+q],[0])); T=np.moveaxis(T,-1,n+q)
            out=out+p/3*T
        Rr=out
    return Rr.reshape(2**n,2**n)
def recovery(Vc,n):
    E=[np.eye(2**n)]
    for i in range(n):
        for Pm in (X,Y,Z):
            m=np.array([[1.]])
            for q in range(n): m=np.kron(m,Pm if q==i else I)
            E.append(m)
    C=np.array([[Vc[:,0].conj()@Ea.conj().T@Eb@Vc[:,0] for Eb in E] for Ea in E])
    d,Um=np.linalg.eigh(C); Ks=[]
    for k in range(len(d)):
        if d[k]>1e-10:
            F=sum(Um[a,k]*E[a] for a in range(len(E))); Ks.append(F@Vc/np.sqrt(d[k]))
    Pi=sum(K@K.conj().T for K in Ks); return Ks,np.eye(2**n)-Pi
def run(Vc,n,x,eps,pre,post,pm,rec):
    Ks,Pc=rec; Pcode=Vc@Vc.conj().T
    r=(1-eps)*rho(x)+eps*rho(-x); Rr=r
    for _ in range(n-1): Rr=np.kron(Rr,r)
    Rr=depol_each(Rr,n,pre)
    A=Pcode@Rr@Pcode; B=(np.eye(2**n)-Pcode)@Rr@(np.eye(2**n)-Pcode)
    acc=(1-pm)*A+pm*B; pacc=np.real(np.trace(acc))
    acc=depol_each(acc,n,post)
    L=sum(K.conj().T@acc@K for K in Ks)+np.real(np.trace(Pc@acc))*I/2
    L=L/np.trace(L); return L,pacc
# 5-qubit code
S5=['XZZXI','IXZZX','XIXZZ','ZXIXZ']; Pmap={'I':I,'X':X,'Z':Z}
def k5(s):
    m=np.array([[1.]])
    for c in s: m=np.kron(m,Pmap[c])
    return m
P5=np.eye(32)
for s in S5: P5=P5@(np.eye(32)+k5(s))/2
w_,v_=np.linalg.eigh(P5@k5('ZZZZZ')@P5); a0=v_[:,np.argmax(w_)]; V5=np.column_stack([a0,k5('XXXXX')@a0]).astype(complex)
rec7=recovery(V,7); rec5=recovery(V5,5)
print('recovery subspaces: 7-qubit %d, 5-qubit %d'%(len(rec7[0]),len(rec5[0])))
cube=np.ones(3)/3**.5
def target(Vc,n,x,rec):
    L,_=run(Vc,n,x,0,0,0,0,rec); return bloch(L)
protocols={'5-qubit BK, cube corner (T-type)':(V5,5,cube,rec5),
           'icosahedral, zeta (on-mirror class)':(V,7,np.cos(t36)*v36+np.sin(t36)*d36,rec7),
           'icosahedral, vertex (free in 2I world)':(V,7,ico[2],rec7)}
tg={k:target(*v) for k,v in protocols.items()}
k=6; pm=5e-3
def err(name,eps,p2,pmm=pm):
    Vc,n,x,rec=protocols[name]; L,pa=run(Vc,n,x,eps,k*p2,k*p2,pmm if p2>0 else 0,rec); return (1-bloch(L)@tg[name])/2,pa
print('\nControl (ideal, p2=0) thresholds and small-eps suppression:')
for name in protocols:
    es=np.linspace(0.005,0.45,90); good=[e for e in es if err(name,e,0)[0]<e]
    e1,_=err(name,1e-3,0); e2,_=err(name,1e-4,0); order=np.log(e1/e2)/np.log(10)
    print('  %-40s threshold %.3f | out(1e-3)=%.2e, scaling exponent %.2f'%(name,max(good) if good else 0,e1,order))
res={}
for p2 in [1e-3,3e-3,1e-2]:
    print('\nHardware p2=%.0e (pre/post per-qubit %.3f, false-accept %.3f):'%(p2,k*p2,pm))
    for name in protocols:
        es=np.linspace(0.005,0.45,90); good=[e for e in es if err(name,e,p2)[0]<e]
        # fixed-point floor: iterate the map from input error = raw error (assume raw injected error = p2*10)
        e=max(10*p2,0.01); cost=1.0; traj=[e]; n=protocols[name][1]
        for rnd in range(8):
            eo,pa=err(name,e,p2)
            if eo>=e*0.999: break
            cost*=n/pa; e=eo; traj.append(e)
        res[(name,p2)]=(max(good) if good else 0,e,cost,traj)
        print('  %-40s threshold %.3f | floor %.2e after %d rounds | raw states per output %.3g'%(name,max(good) if good else 0,e,len(traj)-1,cost))
np.save('hw_res.npy',np.array([[str(k),v[0],v[1],v[2]] for k,v in res.items()],dtype=object),allow_pickle=True)
