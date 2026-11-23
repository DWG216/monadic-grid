import numpy as np, itertools
src=open('t21_nonlinear_hands.py').read().split('# Part G')[1].split('sanity=[]')[0]
exec("import itertools\n"+src)   # sig, eta, epsS, S, leps (signature +---)
rng=np.random.default_rng(2); res={}
def maxwell(phi,both=True):
    X=np.einsum('AB,PQ->APBQ',phi,epsS)
    if both: X=X+np.einsum('PQ,AB->APBQ',phi.conj(),epsS)
    return np.einsum('aAP,bBQ,APBQ->ab',S,S,X)   # F^{ab}
def Tkk(F,k):
    Fl=eta@F@eta                 # F_ab
    Fk=Fl.T@k                    # F_ab k^a
    return Fk@eta@Fk             # F_ac k^a F_b^c k^b ; trace term drops for null k  (sign conv: +---)
r=[];one=[]
for _ in range(200):
    phi=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); phi=(phi+phi.T)/2
    F=maxwell(phi)
    o=rng.normal(size=2)+1j*rng.normal(size=2); k=np.einsum('aAP,A,P->a',S,o,o.conj()).real
    ol=np.einsum('B,BA->A',o,epsS); p0=np.einsum('AB,A,B->',phi,ol,ol)
    r.append(Tkk(F.real,k)/abs(p0)**2)
    F1=maxwell(phi,both=False); one.append(abs(Tkk(F1,k))/np.abs(F1).max()**2)
r=np.array(r)
res['M1 ratio mean, rel spread']=(float(r.mean()),float(r.std()/abs(r.mean())))
res['M1 one hand max']=float(max(one))
# Dirac at rest, chiral basis: H = m * [[0, I],[I, 0]] (p=0); gamma5 = diag(-1,-1,1,1)
def chir(m,t):
    H=m*np.block([[np.zeros((2,2)),np.eye(2)],[np.eye(2),np.zeros((2,2))]])
    g5=np.diag([-1,-1,1,1.]); psi0=np.array([1,0,0,0],dtype=complex)
    w,V=np.linalg.eigh(H); psit=V@(np.exp(-1j*w*t)*(V.conj().T@psi0))
    return float((psit.conj()@g5@psit).real)
ts=np.linspace(0,10,101)
res['M2 max |<g5> + cos(2mt)| (m=0.7)']=float(max(abs(chir(0.7,t)+np.cos(2*0.7*t)) for t in ts))
res['M2 m=0 range']=(min(chir(0,t) for t in ts),max(chir(0,t) for t in ts))
for k_,v in res.items(): print(k_,v)
