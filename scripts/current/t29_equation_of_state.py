import numpy as np, itertools
src=open('t23_checklist_kerr.py').read().split('res={}')[0]
exec(src)   # metric(x,Q), christ, riemann, weyl_low, frame, BR, leps (long double machinery)
LDp=LD
def ricci(x,Q):
    R=riemann(x,Q); return np.einsum('abad->bd',R), R
def Apot(x,Q):
    t,X,Y,Z=x; a=A
    R2=X*X+Y*Y+Z*Z-a*a; r2=(R2+np.sqrt(R2*R2+4*a*a*Z*Z))/2; r=np.sqrt(r2)
    l=np.array([LD(1),(r*X+a*Y)/(r2+a*a),(r*Y-a*X)/(r2+a*a),Z/r],dtype=LD)
    return -Q*r*r2/(r2*r2+a*a*Z*Z)*l
def Fmn(x,Q,h=LD('1e-4')):
    dA=deriv(lambda y:Apot(y,Q),x,h)   # dA[mu,nu] = d_mu A_nu
    return (dA-dA.T)
def Tkk(x,Qfield,Qmetric,k):
    F=Fmn(x,Qfield).astype(np.float64); g=metric(x,Qmetric).astype(np.float64); gi=np.linalg.inv(g)
    Fk=F.T@k   # F_ab k^a -> vector over b
    return float(Fk@gi@Fk)/(4*np.pi)   # (1/4pi) F_ac k^a F_bd k^b g^cd (null k: trace term drops)
def null_vectors(x,Q,n,rng):
    g=metric(x,Q).astype(np.float64); E=frame(g); out=[]
    for _ in range(n):
        u=rng.normal(size=3); u/=np.linalg.norm(u); kf=np.concatenate([[1.0],u])
        out.append(E.T@kf)   # coordinate components k^a = e_(i)^a kf^i
    return out,g
rng=np.random.default_rng(11); res={}
pts=[np.array([0,4,1,1.5],dtype=LD),np.array([0,0,5,-2],dtype=LD),np.array([0,3,-3,3],dtype=LD)]
h1=[];h2=[];h3=[];h4=[]
for x in pts:
    Ric,R=ricci(x,LD(0)); Ric=Ric.astype(np.float64); sc=np.abs(R.astype(np.float64)).max()
    ks,g=null_vectors(x,LD(0),200,rng)
    h1.append(max(abs(k@Ric@k) for k in ks)/sc)
    RicQ,RQ=ricci(x,LD('0.5')); RicQ=RicQ.astype(np.float64)
    ksQ,gQ=null_vectors(x,LD('0.5'),200,rng)
    nullchk=max(abs(k@gQ@k) for k in ksQ)
    rel=[];relc=[]
    for k in ksQ:
        lhs=k@RicQ@k; rhs=8*np.pi*Tkk(x,LD('0.5'),LD('0.5'),k); rhs_c=8*np.pi*Tkk(x,LD('0.4'),LD('0.5'),k)
        rel.append(abs(lhs-rhs)/abs(rhs)); relc.append(abs(lhs-rhs_c)/abs(lhs))
    h2.append(max(rel)); h3.append(min(relc))
    # H4 Bel-Robinson contraction on null k (frame computation from t23)
    T,Cf,D,E,gg=BR(x,LD('0.5'))
    vals=[]
    for _ in range(200):
        u=rng.normal(size=3); u/=np.linalg.norm(u); kf=np.concatenate([[1.0],u])
        vals.append(np.einsum('abcd,a,b,c,d->',T,kf,kf,kf,kf))
    h4.append(min(vals)/np.abs(T).max())
res['H1 Kerr max |R_kk|/|Riem|']=[float(v) for v in h1]
res['H2 KN max rel err R_kk vs 8pi T_kk']=[float(v) for v in h2]
res['H2 null-vector check']=float(nullchk)
res['H3 control Q=0.4 min mismatch']=[float(v) for v in h3]
res['H4 min BR(k,k,k,k)/max|T| at KN points']=[float(v) for v in h4]
for k,v in res.items(): print(k,v)
