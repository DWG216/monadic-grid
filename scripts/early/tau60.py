import numpy as np, itertools
src=open('icosa_code2.py').read().split("for name,cls in")[0]
import io,contextlib
with contextlib.redirect_stdout(io.StringIO()): exec(src)      # V,P (code), ico (code-frame icosahedron), faces, rho, bloch, tens, q2u
phi=(1+5**.5)/2
# ---------- U1: tau60 ----------
N=np.sqrt(5*phi+7)
tau=np.array([[1j*(2+phi),1+1j],[-1+1j,-1j*(2+phi)]])/N
print('U1. unitary err %.1e | trace %.1e'%(np.linalg.norm(tau@tau.conj().T-I),abs(np.trace(tau))))
nt=np.real([1j*np.trace(tau@X),1j*np.trace(tau@Y),1j*np.trace(tau@Z)])/2      # tau = -i n.sigma
print('    axis n_tau =',np.round(nt,4),' ratio to (1,1,phi^2+1):',np.round(nt/np.array([1,1,phi**2+1])*np.linalg.norm([1,1,phi**2+1]),4))
w,v=np.linalg.eigh(np.array(1j*tau)); print('    eigenstates of i*tau along +-n: Bloch',[np.round(bloch(np.outer(v[:,k],v[:,k].conj())),4) for k in range(2)])
# standard (KT) icosian frame
icos=[]
for s in itertools.product([1,-1],repeat=1):
    for k in range(4): e=np.zeros(4); e[k]=s[0]; icos.append(e)
icos+= [np.array(s)/2 for s in itertools.product([1,-1],repeat=4)]
base=[0,1,1/phi,phi]; evens=[p for p in itertools.permutations(range(4)) if sum(1 for i in range(4) for j in range(i) if p[i]<p[j])%2==0]
for p in evens:
    for sg in itertools.product([1,-1],repeat=3):
        q=np.zeros(4); vals=[base[0]]+[sg[i]*base[i+1] for i in range(3)]
        for i in range(4): q[p[i]]=vals[i]
        icos.append(q/2)
icos=np.unique(np.round(icos,12),axis=0); print('    icosians:',len(icos))
G=[q2u(q) for q in icos]
intau=min(min(np.linalg.norm(g-tau),np.linalg.norm(g+tau)) for g in G); print('    distance of tau60 from 2I (std frame): %.3f (0 would mean cheap)'%intau)
def axis(U):
    a=np.real(np.trace(U))/2; v=np.real([1j*np.trace(U@X),1j*np.trace(U@Y),1j*np.trace(U@Z)])/2
    return a,v
def rot(U,x):  # SO(3) action
    r=U@rho(x)@U.conj().T; return bloch(r)
stdax={}
for g in G:
    a,v=axis(g)
    if np.linalg.norm(v)>1e-9:
        order=int(round(np.pi/np.arccos(np.clip(abs(a),0,1)))) if abs(a)<1-1e-9 else 1
        u=v/np.linalg.norm(v); key=tuple(np.round(u*np.sign(u[np.argmax(np.abs(u)>1e-9)]),6)); stdax[key]=max(stdax.get(key,0),order)
cnt={k:sum(1 for o in stdax.values() if o==k) for k in set(stdax.values())}; print('    std 2I rotation axes by order:',cnt)
# ---------- U2: geometry of n_tau ----------
def orbit(x,Gs):
    pts=[]
    for g in Gs:
        for s in [1,-1]:
            y=s*rot(g,x)
            if all(np.linalg.norm(y-p)>1e-7 for p in pts): pts.append(y)
    return pts
ot=orbit(nt,G); print('U2. +-orbit of n_tau under 2I: %d points'%len(ot))
ang=lambda u,w: np.degrees(np.arccos(np.clip(abs(u@w)/np.linalg.norm(u)/np.linalg.norm(w),-1,1)))
for o,name in [(5,'5-fold (vertex)'),(3,'3-fold (face)'),(2,'2-fold (edge)')]:
    print('    nearest %s axis: %.2f deg'%(name,min(ang(nt,np.array(k)) for k,v in stdax.items() if v==o)))
mir=min(abs(nt@np.array(k)) for k,v in stdax.items() if v==2)  # mirror planes are normal to 2-fold axes
print('    min |n.normal| over the 15 mirror planes: %.3f (0 = on a mirror)'%mir)
# ---------- align std frame to code frame ----------
stdV=[np.array(k) for k,v in stdax.items() if v==5]; stdV=stdV+[-x for x in stdV]
def kabsch(A,B):
    H=np.array(A).T@np.array(B); U,S,Wt=np.linalg.svd(H); d=np.sign(np.linalg.det(Wt.T@U.T)); return Wt.T@np.diag([1,1,d])@U.T
R=None
for a in ico:
    for b in ico:
        if abs(a@b-1/5**.5)<1e-6:
            s0=stdV[0]; s1=[x for x in stdV if abs(x@s0-1/5**.5)<1e-6][0]
            Rt=kabsch([s0,s1,np.cross(s0,s1)],[a,b,np.cross(a,b)])
            if abs(np.linalg.det(Rt)-1)<1e-6 and all(min(np.linalg.norm(Rt@x-y) for y in ico)<1e-6 for x in stdV): R=Rt;break
    if R is not None: break
print('    rotation std->code frame found:',R is not None)
# code-frame group (SU(2) lift of R applied by conjugation)
def so3_to_su2(Rm):
    q=np.zeros(4); t=np.trace(Rm); q[0]=np.sqrt(max(0,1+t))/2
    if q[0]>1e-6: q[1:]=np.array([Rm[2,1]-Rm[1,2],Rm[0,2]-Rm[2,0],Rm[1,0]-Rm[0,1]])/(4*q[0])
    else:
        w,v=np.linalg.eig(Rm); u=np.real(v[:,np.argmin(abs(w-1))]); q[1:]=u
    return q2u(q/np.linalg.norm(q))
UR=so3_to_su2(R); assert np.linalg.norm(rot(UR,np.array([.3,.5,.8]))-R@np.array([.3,.5,.8]))<1e-8
Gc=[UR@g@UR.conj().T for g in G]
leakmax=max(np.linalg.norm(tens(g)@V-P@tens(g)@V) for g in Gc[::7]); print('    transversal check of code-frame 2I (sampled): max leak %.1e'%leakmax)
# Galois partner of n_tau (phi -> -1/phi), in std frame
ntg=np.array([1,1,2-1/phi]); ntg/=np.linalg.norm(ntg)
classes={'tau':[R@x for x in ot],"tau' (Galois)":[R@x for x in orbit(ntg,G)]}
# ---------- U3 ----------
def logical(Uphys): return V.conj().T@tens(Uphys)@V
LG=[logical(g) for g in Gc]
zL=np.array([0,0,1.]) ; v0=bloch(V.conj().T@V[:,[0]]@V[:,[0]].conj().T@V)
orb0=orbit(v0,LG)
print('U3. logical |0_L> Bloch',np.round(v0,3),'| 2I orbit size (incl. antipodes) %d | all on code icosahedron: %s'%(len(orb0),all(min(np.linalg.norm(p-y) for y in ico)<1e-6 for p in orb0)))
# ---------- U4/U5: pure-state map and fixed classes ----------
def ket(nv):
    th=np.arccos(np.clip(nv[2],-1,1)); ph=np.arctan2(nv[1],nv[0]); return np.array([np.cos(th/2),np.exp(1j*ph)*np.sin(th/2)])
def fmap(nv):
    k=ket(nv); K=k
    for _ in range(6): K=np.kron(K,k)
    a=V.conj().T@K; p=np.vdot(a,a).real; return bloch(np.outer(a,a.conj())/p),p
def noisy_out(nv,eps):
    r=(1-eps)*rho(nv)+eps*rho(-nv); Rr=r
    for _ in range(6): Rr=np.kron(Rr,r)
    num=V.conj().T@Rr@V; p=np.real(np.trace(num)); return bloch(num/p),p
for name,cl in classes.items():
    x=cl[0]; b,p=fmap(x); d=min(np.linalg.norm(b-y) for y in cl)
    print('U4. %s: pure 7-copy output lands %.3f from nearest %s-class point (0 = fixed class); success prob %.3f'%(name,d,name,p))
    for e in [0.01,0.05,0.1]:
        bo,_=noisy_out(x,e); fo=max((1+bo@y)/2 for y in cl); print('      input err %.2f -> output err to class %.4f'%(e,1-fo))
# global scan: orbit-fixed points of f relative to the code-frame rotation group
Gso=[np.array([rot(g,e) for e in np.eye(3)]).T for g in LG]
Gso=[g for i,g in enumerate(Gso) if all(np.linalg.norm(g-h)>1e-6 for h in Gso[:i])]; print('    logical rotation group size',len(Gso))
rng=np.random.default_rng(1); pts=rng.normal(size=(6000,3)); pts/=np.linalg.norm(pts,axis=1)[:,None]
def dist(x):
    b,_=fmap(x); return min(min(np.linalg.norm(b-g@x),np.linalg.norm(b+g@x)) for g in Gso)
from scipy.optimize import minimize
found=[]
ds=np.array([dist(x) for x in pts]); idx=np.argsort(ds)[:200]
for i in idx:
    res=minimize(lambda a: dist(np.array([np.sin(a[0])*np.cos(a[1]),np.sin(a[0])*np.sin(a[1]),np.cos(a[0])])),
                 [np.arccos(pts[i,2]),np.arctan2(pts[i,1],pts[i,0])],method='Nelder-Mead',options={'xatol':1e-10,'fatol':1e-13})
    if res.fun<1e-6:
        a=res.x; x=np.array([np.sin(a[0])*np.cos(a[1]),np.sin(a[0])*np.sin(a[1]),np.cos(a[0])])
        if all(min(np.linalg.norm(g@x-y) for g in Gso for y in [f,-f])>1e-4 for f in found): found.append(x)
def stab_order(x): return sum(1 for g in Gso if np.linalg.norm(g@x-x)<1e-5)
print('U4/U5. distinct fixed classes of the code map (up to symmetry):',len(found))
for x in found:
    o=stab_order(x); typ={5:'vertex (5-fold)',3:'face/dodeca vertex (3-fold)',2:'edge (2-fold)',1:'generic'}.get(o,str(o))
    M2=-np.log2((1+np.sum(x**4))/2)
    good=[e for e in np.linspace(0.002,0.499,250) if (lambda b:(1-max((1+b@(g@x))/2 for g in Gso for _ in [0])))(noisy_out(x,e)[0])<e]
    print('   class %-28s | free in 2I world: %-5s | Pauli-frame M2 %.3f | threshold %.3f'%(typ,o==5,M2,max(good) if good else 0))
np.save('tau60_fixed.npy',np.array(found))
# control
r=I/2; Rr=r
for _ in range(6): Rr=np.kron(Rr,r)
num=V.conj().T@Rr@V; print('Control: max-mixed input -> output Bloch length %.2e'%np.linalg.norm(bloch(num/np.trace(num))))
