import numpy as np, itertools, sys
from math import comb, lgamma, log
phi=(1+5**.5)/2
I2=np.eye(2);X=np.array([[0,1],[1,0]]);Y=np.array([[0,-1j],[1j,0]]);Z=np.diag([1.,-1])
def q2u(q): a,b,c,d=q; return a*I2-1j*(b*X+c*Y+d*Z)
# ---- icosians (standard frame) and Galois conjugation ----
ic=[]
for k in range(4):
    for s in [1,-1]: e=np.zeros(4); e[k]=s; ic.append(e)
ic+=[np.array(s)/2 for s in itertools.product([1,-1],repeat=4)]
base=[0,1,1/phi,phi]; ev=[p for p in itertools.permutations(range(4)) if sum(1 for i in range(4) for j in range(i) if p[i]<p[j])%2==0]
for p in ev:
    for sg in itertools.product([1,-1],repeat=3):
        q=np.zeros(4); vals=[0]+[sg[i]*base[i+1] for i in range(3)]
        for i in range(4): q[p[i]]=vals[i]
        ic.append(q/2)
ic=np.unique(np.round(ic,12),axis=0); assert len(ic)==120
def gal(x):
    for a in np.arange(-1,1.01,0.5):
        for b in np.arange(-1,1.01,0.5):
            if abs(a+b*phi-x)<1e-9: return a+b*(1-phi)
    raise ValueError(x)
icg=np.array([[gal(x) for x in q] for q in ic])
G=[q2u(q) for q in ic]; Gs=[q2u(q) for q in icg]
# homomorphism check
rng=np.random.default_rng(0)
def qmul(p,q):
    a1,b1,c1,d1=p;a2,b2,c2,d2=q
    return np.array([a1*a2-b1*b2-c1*c2-d1*d2,a1*b2+b1*a2+c1*d2-d1*c2,a1*c2-b1*d2+c1*a2+d1*b2,a1*d2+b1*c2-c1*b2+d1*a2])
for _ in range(20):
    i,j=rng.integers(120,size=2); pq=qmul(ic[i],ic[j]); assert np.allclose(np.array([gal(x) for x in pq]),qmul(icg[i],icg[j]))
# ---- spin-j machinery (Dicke basis |D_k>, k = number of 1s, Jz = j-k) ----
def spin(N):
    j=N/2; m=j-np.arange(N+1); Jp=np.zeros((N+1,N+1))
    for k in range(1,N+1): Jp[k-1,k]=np.sqrt(j*(j+1)-m[k]*(m[k]+1))
    Jx=(Jp+Jp.T)/2; Jy=(Jp-Jp.T)/(2j); Jz=np.diag(m); return Jx,Jy,Jz
def Dmat(U,J):
    a=np.real(np.trace(U))/2; v=np.real([1j*np.trace(U@X),1j*np.trace(U@Y),1j*np.trace(U@Z)])/2
    s=np.linalg.norm(v)
    if s<1e-12: return np.eye(J[0].shape[0])*(1 if a>0 else (-1)**(J[0].shape[0]-1))
    th=2*np.arctan2(s,a); n=v/s; H=n[0]*J[0]+n[1]*J[1]+n[2]*J[2]
    w,W=np.linalg.eigh(H); return (W*np.exp(-1j*th*w))@W.conj().T
def ket(nv):
    th=np.arccos(np.clip(nv[2],-1,1)); ph=np.arctan2(nv[1],nv[0]); return np.array([np.cos(th/2),np.exp(1j*ph)*np.sin(th/2)])
def bloch2(v): r=np.outer(v,v.conj()); return np.real([np.trace(r@X),np.trace(r@Y),np.trace(r@Z)])/np.real(np.trace(r))
def rotU(nv):  # SU(2) taking z to nv
    k=ket(nv); return np.array([[k[0],-k[1].conj()],[k[1],k[0].conj()]])
# check D(U) = U^{xN} on Sym for N=3
J3=spin(3); U=q2u(ic[37]);
def dicke_full(N,k):
    v=np.zeros(2**N)
    for c in itertools.combinations(range(N),k): v[sum(1<<(N-1-i) for i in c)]=1
    return v/np.linalg.norm(v)
B=np.column_stack([dicke_full(3,k) for k in range(4)]); UU=np.kron(np.kron(U,U),U)
assert np.allclose(B.T@UU@B,Dmat(U,J3)), 'spin rep mismatch'
print('checks: Galois map is a homomorphism; spin-j rep = U^(xN) on symmetric subspace')
# ---- multiplicities ----
def chi_mult(N,twist):
    J=spin(N); S=Gs if twist else G
    return round(np.real(sum(np.trace(s).conj()*np.trace(Dmat(g,J)) for g,s in zip(G,S)))/120)
if 'mult' in sys.argv:
    rows=[(N,chi_mult(N,True),chi_mult(N,False)) for N in range(1,260,2)]
    np.save('mults.npy',np.array(rows))
    print('N with 2\' multiplicity (twisted) / 2 multiplicity (untwisted):')
    print(' '.join('%d:%d/%d'%r for r in rows if r[1] or r[2]))
    sys.exit()
# ---------------- code construction ----------------
def isotypic(N,twist=True):
    J=spin(N); S=Gs if twist else G; Ds=[Dmat(g,J) for g in G]
    P=lambda a,b: (2/120)*sum(np.conj(s[a,b])*D for s,D in zip(S,Ds))
    P00=P(0,0); w,W=np.linalg.eigh((P00+P00.conj().T)/2); B0=W[:,w>0.5]
    B1=P(1,0)@B0
    return J,Ds,S,B0,B1
def check_rep(B0,B1,Ds,S):
    c=np.random.default_rng(3).normal(size=B0.shape[1])+0j; c/=np.linalg.norm(c)
    V=np.column_stack([B0@c,B1@c]); err=max(np.linalg.norm(D@V-V@s) for D,s in zip(Ds[::11],S[::11]))
    return np.linalg.norm(V.conj().T@V-np.eye(2)),err
def KL(V,J,deg):
    ops=[J[0],J[1],J[2]]; prods=[ops]
    for d in range(2,deg+1): prods.append([a@b for a in prods[-1] for b in ops])
    worst=0
    for lvl in prods[:deg]:
        for A in lvl:
            M=V.conj().T@A@V; worst=max(worst,np.linalg.norm(M-np.trace(M)/2*np.eye(2)))
    return worst
def distance(V,J,maxdeg=6):
    d=1
    for deg in range(1,maxdeg+1):
        if KL(V,J,deg)<1e-8: d=deg+1
        else: break
    return d
# tau60 physical state and logical target class
tau=np.array([[1j*(2+phi),1+1j],[-1+1j,-1j*(2+phi)]])/np.sqrt(5*phi+7)
nt=np.array([1,1,phi**2+1]); nt/=np.linalg.norm(nt)
def so3(U): return np.array([bloch2(U@ket(e)) if False else np.real([np.trace(U@(0.5*(I2+e[0]*X+e[1]*Y+e[2]*Z))@U.conj().T@P) for P in (X,Y,Z)]) for e in np.eye(3)]).T
G3=[so3(g) for g in G]; S3=[so3(s) for s in Gs]
def axes5(R3):
    out=[]
    for Rm in R3:
        t=np.trace(Rm)
        if abs(t-(1+2*np.cos(2*np.pi/5)))<1e-6:
            w,v=np.linalg.eig(Rm); u=np.real(v[:,np.argmin(abs(w-1))]); u/=np.linalg.norm(u)
            if all(min(np.linalg.norm(u-x),np.linalg.norm(u+x))>1e-6 for x in out): out.append(u)
    return out+[-x for x in out]
def kabsch(A,B):
    H=np.array(A).T@np.array(B); U_,S_,Wt=np.linalg.svd(H); d=np.sign(np.linalg.det(Wt.T@U_.T)); return Wt.T@np.diag([1,1,d])@U_.T
vs,vg=axes5(G3),axes5(S3)
Q=None
for c_ in vg:
    for d_ in vg:
        if abs(c_@d_-1/5**.5)<1e-6:
            a_=vs[0]; b_=[x for x in vs if abs(x@a_-1/5**.5)<1e-6][0]
            Qt=kabsch([a_,b_,np.cross(a_,b_)],[c_,d_,np.cross(c_,d_)])
            if abs(np.linalg.det(Qt)-1)<1e-6 and all(min(np.linalg.norm(Qt@x-y) for y in vg)<1e-6 for x in vs): Q=Qt;break
    if Q is not None: break
assert Q is not None
def orbit(x,R3):
    P_=[]
    for Rm in R3:
        for s in [1,-1]:
            y=s*(Rm@x)
            if all(np.linalg.norm(y-p)>1e-6 for p in P_): P_.append(y)
    return P_
targets=[Q@y for y in orbit(nt,G3)]       # logical tau class (120 points)
def dicke_x(J,nv,kmax):
    D=Dmat(rotU(nv),J); return [D[:,k] for k in range(kmax+1)]   # D_k in the x-basis
def design(N,order,twist=True,verbose=True):
    J,Ds,S,B0,B1=isotypic(N,twist); m=B0.shape[1]
    Dk=dicke_x(J,nt,max(order,3)+2)
    best=None
    for w in targets:
        wk=ket(w)
        cons=[wk[1]*(B0.conj().T@Dk[0])-wk[0]*(B1.conj().T@Dk[0])]          # fixed: output = w
        for k in range(1,order): cons.append(wk[0]*(B1.conj().T@Dk[k])-wk[1]*(B0.conj().T@Dk[k]))  # k-error terms parallel to w
        C=np.array(cons)                       # c^dagger . conj?  we need c^H v = 0  ->  v^H c = 0
        A=np.conj(C)                           # rows a with a.c = conj(v^H c)... use null space of C^H
        Ns=np.linalg.svd(C.conj(),full_matrices=True)
        # solve v^H c = 0 for each v:  rows v^H
        M=np.array([v.conj() for v in cons]); u,s,vh=np.linalg.svd(M); null=vh[len(cons):].conj().T if M.shape[0]<m else np.zeros((m,0))
        if null.shape[1]==0: continue
        # maximise success probability |V^H D0|^2 over c in null space
        u0=B0.conj().T@Dk[0]; u1=B1.conj().T@Dk[0]
        Qf=np.outer(u0,u0.conj())+np.outer(u1,u1.conj()); Qn=null.conj().T@Qf@null
        ev,evec=np.linalg.eigh((Qn+Qn.conj().T)/2); c=null@evec[:,-1]; c/=np.linalg.norm(c)
        if best is None or ev[-1]>best[0]: best=(ev[-1],c,w)
    if best is None: return None
    p0,c,w=best; V=np.column_stack([B0@c,B1@c]); return dict(N=N,m=m,V=V,w=w,J=J,p0=p0,Ds=Ds,S=S)
def out(code,eps):
    J,V,w=code['J'],code['V'],code['w']; N=code['N']
    Dk=dicke_x(J,nt,N); ks=np.arange(N+1)
    logw=ks*np.log(eps)+(N-ks)*np.log1p(-eps)
    A=np.array([V.conj().T@d for d in Dk])            # (N+1) x 2 logical images
    rhoL=(A.T*np.exp(logw))@A.conj()
    p=np.real(np.trace(rhoL)); rhoL/=p; wk=ket(w)
    return 1-np.real(wk.conj()@rhoL@wk),p
def CZleak(V,N):
    E=np.zeros((N+1,N+1))
    for a in range(N+1):
        for b in range(N+1):
            E[a,b]=sum((-1)**t*comb(a,t)*comb(N-a,b-t) for t in range(max(0,a+b-N),min(a,b)+1))/comb(N,b)
    worst=0
    for i in range(2):
        for j in range(2):
            vec=np.outer(V[:,i],V[:,j])*E           # CZ^N |i_L j_L> in Dicke x Dicke basis
            M=np.array([[np.sum(np.conj(np.outer(V[:,k],V[:,l]))*vec) for l in range(2)] for k in range(2)])
            worst=max(worst,1-np.sum(abs(M)**2))
    return worst
