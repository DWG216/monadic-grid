import numpy as np, itertools
LD=np.longdouble
M=LD(1); A=LD('0.6')
def metric(x,Q):
    t,X,Y,Z=x; a=A
    R2=X*X+Y*Y+Z*Z-a*a; r2=(R2+np.sqrt(R2*R2+4*a*a*Z*Z))/2; r=np.sqrt(r2)
    f=(2*M*r-Q*Q)*r2/(r2*r2+a*a*Z*Z)
    l=np.array([LD(1),(r*X+a*Y)/(r2+a*a),(r*Y-a*X)/(r2+a*a),Z/r],dtype=LD)
    eta=np.diag(np.array([-1,1,1,1],dtype=LD))
    return eta+f*np.outer(l,l)
st=[(-2,LD(1)/12),(-1,LD(-8)/12),(1,LD(8)/12),(2,LD(-1)/12)]
def deriv(F,x,h):
    out=[]
    for mu in range(4):
        acc=0
        for s,c in st:
            e=np.zeros(4,dtype=LD); e[mu]=s*h; acc=acc+c*F(x+e)
        out.append(acc/h)
    return np.array(out)   # out[mu,...] = d_mu F
def christ(x,Q,h=LD('1e-3')):
    g=metric(x,Q); gi=np.linalg.inv(g.astype(np.float64)).astype(LD)
    # refine inverse
    gi=gi+gi@(np.eye(4,dtype=LD)-g@gi)
    dg=deriv(lambda y:metric(y,Q),x,h)  # dg[c,a,b]
    G=0.5*(np.einsum('ad,cdb->acb',gi,dg)+np.einsum('ad,bdc->acb',gi,dg)-np.einsum('ad,dbc->acb',gi,dg))
    return G  # G[a,b,c] = Gamma^a_bc
def riemann(x,Q,h2=LD('1e-3')):
    G=christ(x,Q); dG=deriv(lambda y:christ(y,Q),x,h2)   # dG[m,a,b,c]
    R=np.einsum('cabd->abcd',dG)-np.einsum('dabc->abcd',dG)+np.einsum('ace,ebd->abcd',G,G)-np.einsum('ade,ebc->abcd',G,G)
    # R^a_bcd  (R[a,b,c,d])
    return R
leps=np.zeros((4,)*4)
for p in itertools.permutations(range(4)): leps[p]=np.linalg.det(np.eye(4)[list(p)])
def weyl_low(x,Q):
    g=metric(x,Q); R=riemann(x,Q); Rl=np.einsum('ae,ebcd->abcd',g,R)
    gi=np.linalg.inv(g.astype(np.float64)).astype(LD); Ric=np.einsum('abad->bd',R); s=np.einsum('bd,bd->',gi,Ric)
    gg=lambda A_,B_: (np.einsum('ac,bd->abcd',A_,B_)-np.einsum('ad,bc->abcd',A_,B_)-np.einsum('bc,ad->abcd',A_,B_)+np.einsum('bd,ac->abcd',A_,B_))
    C=Rl-0.5*gg(g,Ric)+s/6*0.5*gg(g,g)
    return C,g,gi
def frame(g):
    g=g.astype(np.float64); E=[]
    base=np.eye(4)
    for i in range(4):
        v=base[i].copy()
        for (e,n) in E: v=v-n*(e@g@v)*e
        nn=v@g@v; E.append((v/np.sqrt(abs(nn)),np.sign(nn)))
    order=sorted(range(4),key=lambda i:E[i][1]); # timelike first
    return np.array([E[i][0] for i in order])  # rows e_(i)^a
def T_tensor(C,gi):
    Cu=np.einsum('aebf,ec,fd->abcd',C,gi,gi) if False else None
    Cm=np.einsum('aecf,eE,fF->aEcF',C,gi,gi)   # C_a^E_c^F
    Cud=np.einsum('efgh,ei,fj->ijgh',C,gi,gi)  # C^ij_gh
    detg=None
    return Cm
def BR(x,Q):
    C,g,gi=weyl_low(x,Q); E=frame(g)
    Cf=np.einsum('abcd,ia,jb,kc,ld->ijkl',C.astype(np.float64),E,E,E,E)
    eta=np.diag([-1.,1,1,1])
    Cup=np.einsum('ijkl,im,jn->mnkl',Cf,eta,eta)
    D=0.5*np.einsum('ijmn,mnkl->ijkl',leps,Cup)*(-1)  # *C with eps_0123=-1 for (-+++), sign irrelevant (appears squared)
    T=np.einsum('aecf,bEdF,eE,fF->abcd',Cf,Cf,eta,eta)+np.einsum('aecf,bEdF,eE,fF->abcd',D,D,eta,eta)
    return T,Cf,D,E,g
res={}
pts=[np.array([0,4,1,1.5],dtype=LD),np.array([0,0,5,-2],dtype=LD),np.array([0,3,-3,3],dtype=LD)]
rng=np.random.default_rng(3); eta=np.diag([-1.,1,1,1])
k1=[];k1s=[];k2=[];k3=[];k3c=[];k6=[]
for x in pts:
    T,Cf,D,E,g=BR(x,LD(0))
    sc=np.abs(T).max()
    k2.append(max(np.abs(T-T.transpose(1,0,2,3)).max(),np.abs(T-T.transpose(2,1,0,3)).max(),np.abs(np.einsum('aacd,aa->cd',T,eta)).max() if False else np.abs(np.einsum('abcd,ab->cd',T,eta)).max())/sc)
    for _ in range(100):
        n=rng.normal(size=3); n/=np.linalg.norm(n); k=np.concatenate([[1.0],n])
        a_=rng.normal(size=3); a_-=a_@n*n; a_/=np.linalg.norm(a_); b_=np.cross(n,a_)
        m=np.concatenate([[0],(a_+1j*b_)/np.sqrt(2)])
        P0=np.einsum('abcd,a,b,c,d->',Cf,k,m,k,m)
        Tk=np.einsum('abcd,a,b,c,d->',T,k,k,k,k); k1.append(Tk/abs(P0)**2)
        th=rng.uniform(0,6.3); P0r=np.einsum('abcd,a,b,c,d->',Cf,k,m*np.exp(1j*th),k,m*np.exp(1j*th))
        k6.append(abs(P0r-np.exp(2j*th)*P0)/abs(P0))
        for sgn in [1,-1]:
            Cp=(Cf+sgn*1j*D)/2; Dp=-sgn*1j*Cp  # dual of self-dual part
            Ts=np.einsum('aecf,bEdF,eE,fF->abcd',Cp,Cp,eta,eta)+np.einsum('aecf,bEdF,eE,fF->abcd',Dp,Dp,eta,eta)
            # verify Dp is really the dual of Cp
            Dchk=-0.5*np.einsum('ijmn,mnkl->ijkl',leps,np.einsum('ijkl,im,jn->mnkl',Cp,eta,eta))
            k1s.append(max(abs(np.einsum('abcd,a,b,c,d->',Ts,k,k,k,k))/Tk, np.abs(Dchk-Dp).max()/np.abs(Cp).max()))
    def fut():
        n=rng.normal(size=3); s=rng.uniform(0,1)
        return np.concatenate([[1.0], s*n/np.linalg.norm(n)]) if rng.uniform()<0.7 else np.concatenate([[1.0],n/np.linalg.norm(n)])
    vals=[];valsc=[]
    CC=np.einsum('aecf,bEdF,eE,fF->abcd',Cf,Cf,eta,eta)
    for _ in range(20000):
        u,v,w,z=fut(),fut(),fut(),fut()
        vals.append(np.einsum('abcd,a,b,c,d->',T,u,v,w,z)); valsc.append(np.einsum('abcd,a,b,c,d->',CC,u,v,w,z))
    k3.append(min(vals)/sc); k3c.append(min(valsc)/np.abs(CC).max())
k1=np.array(k1)
res['K1 ratio mean, CV']=(float(np.mean(k1)),float(np.std(k1)/abs(np.mean(k1))))
res['K1 single hand max rel (and dual check)']=float(max(k1s))
res['K2 sym/trace rel']=[float(v) for v in k2]
res['K3 min T / max|T| per point']=[float(v) for v in k3]
res['K3 null CC-only min (reported)']=[float(v) for v in k3c]
res['K6 phase err max']=float(max(k6))
# K4 divergence
def divT(x,Q,h3=LD('1e-2')):
    C,g,gi=weyl_low(x,Q)
    def Tcoord(y):
        C_,g_,gi_=weyl_low(y,Q)
        C_=C_.astype(np.float64); gi_=gi_.astype(np.float64)
        Cup=np.einsum('ijkl,im,jn->mnkl',C_,gi_,gi_)
        sq=np.sqrt(-np.linalg.det(g_.astype(np.float64)))
        D=-0.5*sq*np.einsum('ijmn,mnkl->ijkl',leps,Cup)
        return np.einsum('aecf,bEdF,eE,fF->abcd',C_,C_,gi_,gi_)+np.einsum('aecf,bEdF,eE,fF->abcd',D,D,gi_,gi_)
    T0=Tcoord(x); dT=deriv(lambda y:Tcoord(y).astype(LD),x,h3).astype(np.float64)
    G=christ(x,Q).astype(np.float64); gif=gi.astype(np.float64)
    nab=dT-np.einsum('eba,ebcd->abcd',G,T0)[None] if False else None
    # nabla_e T_abcd
    nab=dT-np.einsum('fea,fbcd->eabcd',G,T0)-np.einsum('feb,afcd->eabcd',G,T0)-np.einsum('fec,abfd->eabcd',G,T0)-np.einsum('fed,abcf->eabcd',G,T0)
    div=np.einsum('ea,eabcd->bcd',gif,nab)
    r=float(np.sqrt(sum(float(v)**2 for v in x[1:])))
    E=frame(g); Ei=np.linalg.inv(E)
    divf=np.einsum('bcd,bj,ck,dl->jkl',div,Ei,Ei,Ei)  # frame components (covector index -> E^-1)
    T0f=np.einsum('abcd,ai,bj,ck,dl->ijkl',T0,Ei,Ei,Ei,Ei)
    return float(np.abs(divf).max()/(np.abs(T0f).max()/r))
res['K4 Kerr rel div']=[divT(x,LD(0)) for x in pts]
res['K4 Kerr-Newman rel div (control)']=[divT(x,LD('0.5')) for x in pts]
for k,v in res.items(): print(k,v)
