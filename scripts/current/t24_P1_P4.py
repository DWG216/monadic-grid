import numpy as np
from scipy.special import sph_harm_y
rng=np.random.default_rng(7); res={}
sig=[np.eye(2),np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
def Xmat(x): return sum(x[a]*sig[a] for a in range(4))/np.sqrt(2)
# ---------- P1
cr=lambda n: rng.normal(size=n)+1j*rng.normal(size=n)
A,B,C=cr(4),cr(4),cr(4); Ad,Bd,Dd=cr(4),cr(4),cr(4)
x=np.array([0.3,-0.2,0.5,0.1]); X=Xmat(x)
Zof=lambda p: np.concatenate([1j*X@p,p])
Wof=lambda l: np.concatenate([l,-1j*X.T@l])
f=lambda Z:1/((A@Z)**3*(B@Z)**3); g=lambda W:1/((Ad@W)**3*(Bd@W)**3)
def transform(F,which,v,coefvec):
    # contour around root of coefvec.Z(pi) in t, pi=(1,t)
    of=(lambda t:Zof(np.array([1,t]))) if which=='Z' else (lambda t:Wof(np.array([1,t])))
    a0=coefvec@of(0.0); a1=coefvec@of(1.0)-a0; ta=-a0/a1
    # other pole
    other=Bd if which=='W' else B
    b0=other@of(0.0); b1=other@of(1.0)-b0; tb=-b0/b1
    R=0.3*abs(ta-tb); N=4000; th=2*np.pi*np.arange(N)/N
    t=ta+R*np.exp(1j*th); dt=1j*R*np.exp(1j*th)*(2*np.pi/N)
    vals=np.array([F(of(tt)) for tt in t]); w=(v[0]+t*v[1])**4
    return np.sum(w*vals*dt)/(2j*np.pi)
v=cr(2); u=cr(2)
phi0=transform(f,'Z',v,A); psi0=transform(g,'W',u,Ad)
# incidence
mx=0
for _ in range(50):
    Z=Zof(cr(2)); W=Wof(cr(2)); mx=max(mx,abs(Z@W)/np.linalg.norm(Z)/np.linalg.norm(W))
res['P1a max|Z.W|']=float(mx)
def proj(I,a,b,Z,W,N=16):
    th=2*np.pi*np.arange(N)/N; s=0
    for t1 in th:
        for t2 in th: s+=I(np.exp(1j*t1)*Z,np.exp(1j*t2)*W)*np.exp(-1j*a*t1)*np.exp(-1j*b*t2)
    return s/N**2
for d,tag in [(2,'P1b'),(-6,'P1d')]:
    r=lambda Z:(C@Z)**d; s_=lambda W:(Dd@W)**d
    I=lambda Z,W:(f(Z)+r(Z))*(g(W)+s_(W))
    W0=Wof(cr(2)); Z0=Zof(cr(2))
    frec=lambda Z: proj(I,-6,d,Z,W0)/s_(W0)
    grec=lambda W: proj(I,d,-6,Z0,W)/r(Z0)
    # cheaper transform with fewer nodes for recovered functions
    def transform_small(F,which,vv,coefvec):
        of=(lambda t:Zof(np.array([1,t]))) if which=='Z' else (lambda t:Wof(np.array([1,t])))
        a0=coefvec@of(0.0); a1=coefvec@of(1.0)-a0; ta=-a0/a1
        other=Bd if which=='W' else B
        b0=other@of(0.0); b1=other@of(1.0)-b0; tb=-b0/b1
        R=0.3*abs(ta-tb); N=200; th=2*np.pi*np.arange(N)/N
        t=ta+R*np.exp(1j*th); dt=1j*R*np.exp(1j*th)*(2*np.pi/N)
        return np.sum((vv[0]+t*vv[1])**4*np.array([F(of(tt)) for tt in t])*dt)/(2j*np.pi)
    ref_phi=transform_small(f,'Z',v,A); ref_psi=transform_small(g,'W',u,Ad)
    pr=transform_small(frec,'Z',v,A); ps=transform_small(grec,'W',u,Ad)
    res[tag+f' d={d} phi0 rel err']=float(abs(pr-ref_phi)/abs(ref_phi))
    res[tag+f' d={d} psi0 rel err']=float(abs(ps-ref_psi)/abs(ref_psi))
    res[tag+' transform N=200 vs N=4000 (phi0)']=float(abs(ref_phi-phi0)/abs(phi0))
    if d==2:
        e=0
        for _ in range(5):
            Z=Zof(cr(2)); W=Wof(cr(2))
            e=max(e,abs(proj(I,-6,-6,Z,W)-f(Z)*g(W))/abs(f(Z)*g(W)))
        res['P1c (-6,-6) vs f g']=float(e)
# ---------- P2
L=8; th=np.linspace(0.05,np.pi-0.05,40); ph=np.linspace(0,2*np.pi,80,endpoint=False); TH,PH=np.meshgrid(th,ph)
def synth(c):
    out=np.zeros_like(TH,dtype=complex)
    for (l,m),val in c.items(): out+=val*sph_harm_y(l,m,TH,PH)
    return out
N_=lambda l:np.sqrt((l-1)*l*(l+1)*(l+2))
s={(l,m):complex(*rng.normal(size=2)) for l in range(2,L+1) for m in range(-l,l+1)}
Z1={k:(s[k]+(-1)**k[1]*np.conj(s[(k[0],-k[1])]))/N_(k[0]) for k in s}
F=synth(Z1); res['P2a Im/Re LCCE']=float(np.abs(F.imag).max()/np.abs(F.real).max())
ZH={k:s[k]/N_(k[0]) for k in s}; FH=synth(ZH); res['P2b Im/Re H-space generic']=float(np.abs(FH.imag).max()/np.abs(FH.real).max())
sE={k:(s[k]+(-1)**k[1]*np.conj(s[(k[0],-k[1])]))/2 for k in s}
sB={k:(s[k]-(-1)**k[1]*np.conj(s[(k[0],-k[1])]))/2 for k in s}
FHE=synth({k:sE[k]/N_(k[0]) for k in s}); res['P2b Im/Re H-space pure electric']=float(np.abs(FHE.imag).max()/np.abs(FHE.real).max())
Z1B={k:(sB[k]+(-1)**k[1]*np.conj(sB[(k[0],-k[1])]))/N_(k[0]) for k in s}
res['P2c Z1 from pure magnetic (max)']=float(max(abs(v_) for v_ in Z1B.values()))
# ---------- P3
def sachs(P,Pt,lam_end=0.05,n=20000):
    l0=1e-4; d=P*Pt*l0**3/45; sg=P*l0/3; st=Pt*l0/3; D=P*Pt*l0**4/90
    y=np.array([d,sg,st,D],dtype=complex); lam=l0; h=(lam_end-l0)/n
    def fn(l,y):
        d,sg,st,D=y
        return np.array([-2*d/l+d*d+sg*st, -2*sg/l+2*d*sg+P, -2*st/l+2*d*st+Pt, 2*d])
    for i in range(n):
        k1=fn(lam,y);k2=fn(lam+h/2,y+h/2*k1);k3=fn(lam+h/2,y+h/2*k2);k4=fn(lam+h,y+h*k3)
        y=y+h/6*(k1+2*k2+2*k3+k4); lam+=h
    return y[3]/lam**4
P,Pt=0.7+0.4j,-0.3+0.9j
res['P3a deficit/(P Pt/90)']=complex(sachs(P,Pt)/(P*Pt/90))
res['P3b one hand deficit']=float(abs(sachs(P,0)))
sc=1/max(abs(phi0),abs(psi0))
res['P3c with P1 fields ratio']=complex(sachs(psi0*sc,phi0*sc)/(psi0*phi0*sc*sc/90))
# ---------- P4
a=0.6
def lKS(p,a=a,twist=0.0):
    t,x,y,z=p; R2=x*x+y*y+z*z-a*a; r=np.sqrt((R2+np.sqrt(R2*R2+4*a*a*z*z))/2)
    n=np.array([(r*x+a*y)/(r*r+a*a),(r*y-a*x)/(r*r+a*a),z/r])
    if twist:
        c,s_=np.cos(twist*z),np.sin(twist*z); n=np.array([c*n[0]-s_*n[1],s_*n[0]+c*n[1],n[2]])
    return np.concatenate([[1.0],n]),r
def shear_check(p,twist=0.0):
    h=1e-5; G=np.zeros((4,4))
    for mu in range(4):
        e=np.zeros(4); e[mu]=h
        G[mu]=(lKS(p+e,twist=twist)[0]-lKS(p-e,twist=twist)[0])/(2*h)   # G[mu,b] = d_mu l_b
    l,_=lKS(p,twist=twist); n=l[1:]
    e1=np.cross(n,[0.3,0.7,0.2]); e1/=np.linalg.norm(e1); e2=np.cross(n,e1)
    m=np.concatenate([[0],(e1+1j*e2)/np.sqrt(2)])
    lu=np.concatenate([[-1],n])
    geo=lu@G; geo_perp=geo-(geo@np.concatenate([[-1],n]))*0  # check proportional to l_b
    ratio_geo=np.linalg.norm(geo-geo[0]/l[0]*l)/np.linalg.norm(G)
    return abs(m@G@m)/np.linalg.norm(G), ratio_geo
pts=[np.concatenate([[rng.uniform(-3,3)],rng.uniform(-6,6,3)]) for _ in range(400)]
pts=[p for p in pts if np.linalg.norm(p[1:])>2]
sh=[shear_check(p) for p in pts[:50]]; res['P4a max shear, max non-geodesic']=(float(max(s_[0] for s_ in sh)),float(max(s_[1] for s_ in sh)))
sht=[shear_check(p,0.1) for p in pts[:50]]; res['P4a twisted control max shear']=float(max(s_[0] for s_ in sht))
def twistor(p,twist=0.0):
    l,_=lKS(p,twist=twist); vdir=np.concatenate([[1.0],-l[1:]])
    V=Xmat(vdir); w,U=np.linalg.eigh(V); xi=U[:,np.argmax(abs(w))]
    pu=np.conj(xi); pl=np.array([-pu[1],pu[0]])
    Z=np.concatenate([1j*Xmat(p)@pl,pl]); Z2=np.concatenate([1j*Xmat(p+2.0*vdir)@pl,pl])
    return Z/np.linalg.norm(Z), np.linalg.norm(Z-Z2)/np.linalg.norm(Z)
idx=[(i,j) for i in range(4) for j in range(i,4)]
def quad_ratio(twist):
    rows=[];along=0
    for p in pts:
        Z,dz=twistor(p,twist); along=max(along,dz) if twist==0 else along
        rows.append([Z[i]*Z[j] for i,j in idx])
    sv=np.linalg.svd(np.array(rows),compute_uv=False)
    return sv[-1]/sv[-2], along
qr,along=quad_ratio(0.0); res['P4 sanity: twistor constant along ray']=float(along)
res['P4b quadric ratio Kerr']=float(qr); res['P4b quadric ratio twisted control']=float(quad_ratio(0.1)[0])
# P4c
def metric2(p,terms):
    g=np.diag([-1.,1,1,1])
    for (M_,a_) in terms:
        l,r=lKS(p,a=a_); f_=2*M_*r**3/(r**4+a_*a_*p[3]**2); g=g+f_*np.outer(l,l)
    return g
def ricci_rel(p,terms,h=1e-3):
    def chr_(q):
        gi=np.linalg.inv(metric2(q,terms)); dg=np.zeros((4,4,4))
        for c in range(4):
            e=np.zeros(4); e[c]=h
            dg[c]=(-metric2(q+2*e,terms)+8*metric2(q+e,terms)-8*metric2(q-e,terms)+metric2(q-2*e,terms))/(12*h)
        return 0.5*(np.einsum('ad,cdb->acb',gi,dg)+np.einsum('ad,bdc->acb',gi,dg)-np.einsum('ad,dbc->acb',gi,dg))
    G=chr_(p); dG=np.zeros((4,4,4,4))
    for c in range(4):
        e=np.zeros(4); e[c]=h
        dG[c]=(-chr_(p+2*e)+8*chr_(p+e)-8*chr_(p-e)+chr_(p-2*e))/(12*h)
    R=np.einsum('cabd->abcd',dG)-np.einsum('dabc->abcd',dG)+np.einsum('ace,ebd->abcd',G,G)-np.einsum('ade,ebc->abcd',G,G)
    Ric=np.einsum('abad->bd',R); return float(np.abs(Ric).max()/np.abs(R).max())
P=[np.array([0,4,1,1.5]),np.array([0,0,5,-2]),np.array([0,3,-3,3])]
res['P4c same l, M=0.4+0.6']=[ricci_rel(p,[(0.4,0.6),(0.6,0.6)]) for p in P]
res['P4c single Kerr M=1 (reference)']=[ricci_rel(p,[(1.0,0.6)]) for p in P]
res['P4c different l (a=0.6, 0.3)']=[ricci_rel(p,[(0.5,0.6),(0.5,0.3)]) for p in P]
for k,v_ in res.items(): print(k,v_)
