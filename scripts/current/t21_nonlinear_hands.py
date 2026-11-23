import numpy as np, itertools
exec(open('t20_holo_hands.py').read().split('res={}')[0])
res={}
def orders(kap,k=120.0):
    O=obj(2); R=np.exp(1j*k*X); I=np.abs(O+R)**2; J=np.tanh(kap*I)/kap
    S=np.fft.fft2(J); rad=0.45*k
    def band(c): M=(np.hypot(KX-c,KY)<rad); return np.fft.ifft2(S*M), np.sum(np.abs(S*M)**2)
    out={}
    for nn in [-2,-1,1,2]:
        F,E=band(nn*k); out[nn]=(F*np.exp(-1j*nn*k*X),E)
    return O,out
rows=[]
for kap in [1e-4,0.1,0.3,0.6,1.0]:
    O,out=orders(kap)
    # identify sign carrying O at linear level
    sgn=1 if corr(out[1][0],O)>corr(out[-1][0],O) else -1
    e1=out[sgn][1]; e2=out[2*sgn][1]
    rows.append(dict(kap=kap, r21=e2/e1, w1=winding(out[sgn][0]), wm1=winding(out[-sgn][0]),
        w2=winding(out[2*sgn][0]), wm2=winding(out[-2*sgn][0]), c1=corr(out[sgn][0],O),
        sym1=abs(out[1][1]-out[-1][1])/out[1][1], sym2=abs(out[2][1]-out[-2][1])/max(out[2][1],1e-300)))
for r in rows: print({k:(round(v,6) if isinstance(v,float) else v) for k,v in r.items()})
res['N0']=rows[0]['r21']<1e-6
res['N1 windings']=all(r['w2']==4 and r['wm2']==-4 for r in rows[1:])
res['N1 monotone']=all(rows[i+1]['r21']>rows[i]['r21'] for i in range(len(rows)-1))
res['N2 windings']=all(r['w1']==2 and r['wm1']==-2 for r in rows)
res['N2 corr monotone down']=all(rows[i+1]['c1']<rows[i]['c1'] for i in range(1,len(rows)-1)) and rows[-1]['c1']<1
res['N3 symmetry']=max(max(r['sym1'],r['sym2']) for r in rows)<1e-10
# Part G
sig=[np.eye(2),np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
eta=np.diag([1.,-1,-1,-1]); epsS=np.array([[0,1],[-1,0]])
S=np.array([[[s[Ap,A]/np.sqrt(2) for Ap in range(2)] for A in range(2)] for s in sig])  # S[a,A,A']
def sym4(P):
    Q=np.zeros_like(P)
    for p in itertools.permutations(range(4)): Q+=P.transpose(p)
    return Q/24
rng=np.random.default_rng(1)
def weyl(Psi,both=True):
    X=np.einsum('ABCD,PQ,RT->APBQCRDT',Psi,epsS,epsS)
    if both: X=X+np.einsum('PQRT,AB,CD->APBQCRDT',Psi.conj(),epsS,epsS)
    C=np.einsum('aAP,bBQ,cCR,dDT,APBQCRDT->abcd',S,S,S,S,X)
    return C
def lower(C): return np.einsum('ae,bf,cg,dh,efgh->abcd',eta,eta,eta,eta,C)
leps=np.zeros((4,)*4)
for p in itertools.permutations(range(4)):
    leps[p]=np.linalg.det(np.eye(4)[list(p)])
def BR_kkkk(C,k):
    Cl=lower(C)                                  # C_abcd
    Cdual=0.5*np.einsum('abef,efcd->abcd',leps,C)   # *C_abcd = 1/2 eps_abef C^ef_cd (C upper ef, need ^ef_cd)
    Cud=np.einsum('efgh,gc,hd->efcd',C,eta,eta)  # C^ef_cd
    Cdual=0.5*np.einsum('abef,efcd->abcd',leps,Cud)
    def EE(A):
        E=np.einsum('aecf,a,c->ef',A,k,k)        # E_ef (lower)
        Eu=np.einsum('ef,eg,fh->gh',E,eta,eta)
        return np.einsum('ef,ef->',E,Eu)
    return EE(Cl)+EE(Cdual)
sanity=[];ratios=[];mins=[]
for t in range(200):
    Psi=sym4(rng.normal(size=(2,)*4)+1j*rng.normal(size=(2,)*4))
    C=weyl(Psi)
    if t<5:
        Cl=lower(C)
        s1=np.abs(Cl+Cl.transpose(1,0,2,3)).max(); s2=np.abs(Cl-Cl.transpose(2,3,0,1)).max()
        tr=np.abs(np.einsum('ac,abcd->bd',eta,Cl)).max(); im=np.abs(C.imag).max()
        sanity.append(max(s1,s2,tr,im))
    o=rng.normal(size=2)+1j*rng.normal(size=2)
    k=np.einsum('aAP,A,P->a',S,o,o.conj()).real
    T=BR_kkkk(C.real,k); ol=np.einsum('B,BA->A',o,epsS); P0=np.einsum('ABCD,A,B,C,D->',Psi,ol,ol,ol,ol)  # amended after run1: lower the spinor index
    ratios.append(T/abs(P0)**2); mins.append(T)
ratios=np.array(ratios)
res['G1 sanity max']=float(max(sanity))
res['G1 null check |k.k|']=float(abs(k@eta@k))
res['G1 ratio mean, rel spread']=(float(ratios.mean()), float(ratios.std()/abs(ratios.mean())))
res['G1 min T']=float(min(mins))
Psi=sym4(rng.normal(size=(2,)*4)+1j*rng.normal(size=(2,)*4)); C1=weyl(Psi,both=False)
o=rng.normal(size=2)+1j*rng.normal(size=2); k=np.einsum('aAP,A,P->a',S,o,o.conj()).real
# complex single-hand: use same formula with complex C (no conjugation)
def BR_complex(C,k):
    Cl=lower(C); Cud=np.einsum('efgh,gc,hd->efcd',C,eta,eta); Cd=0.5*np.einsum('abef,efcd->abcd',leps,Cud)
    def EE(A):
        E=np.einsum('aecf,a,c->ef',A,k,k); Eu=np.einsum('ef,eg,fh->gh',E,eta,eta); return np.einsum('ef,ef->',E,Eu)
    return EE(Cl)+EE(Cd)
res['G2 one hand |T|/|C|^2']=float(abs(BR_complex(C1,k))/np.abs(C1).max()**2)
res['G2 both hands |T|/|C|^2 (ref)']=float(abs(BR_complex(weyl(Psi),k))/np.abs(weyl(Psi)).max()**2)
for k_,v in res.items(): print(k_,v)
