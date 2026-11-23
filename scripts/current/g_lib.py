# Paths 2, 3, 6 library.
import numpy as np
# ---- path 3: Ricci by nested central differences; R_ab k^a k^b on random null k
def christoffel(g,x,h=1e-4):
    gi=np.linalg.inv(g(x)); dg=np.zeros((4,4,4))
    for c in range(4):
        e=np.zeros(4); e[c]=h; dg[c]=(g(x+e)-g(x-e))/(2*h)
    G=np.zeros((4,4,4))
    for a in range(4):
        for b in range(4):
            for c in range(4):
                G[a,b,c]=0.5*sum(gi[a,d]*(dg[b][d,c]+dg[c][d,b]-dg[d][b,c]) for d in range(4))
    return G
def ricci(g,x,h=1e-3):
    G=christoffel(g,x); dG=np.zeros((4,4,4,4))
    for e_ in range(4):
        e=np.zeros(4); e[e_]=h; dG[e_]=(christoffel(g,x+e)-christoffel(g,x-e))/(2*h)
    R=np.zeros((4,4))
    for b in range(4):
        for c in range(4):
            R[b,c]=sum(dG[a][a,b,c]-dG[c][a,b,a] for a in range(4))+sum(G[a,a,d]*G[d,b,c]-G[a,c,d]*G[d,b,a] for a in range(4) for d in range(4))
    return R
def null_vectors(g,x,rng,n=12):
    gx=g(x); out=[]
    for _ in range(n):
        v=rng.normal(size=3); v/=np.linalg.norm(v)
        k=np.array([1/np.sqrt(-gx[0,0]),*(v/np.sqrt(np.diag(gx)[1:]))]); out.append(k)
    return out
def Rkk(g,x,rng):
    R=ricci(g,x); return max(abs(k@R@k) for k in null_vectors(g,x,rng)), R
# metrics in (t, r, theta, phi), diagonal
def diag(f): return lambda x: np.diag(f(x))
schw=lambda M: diag(lambda x: [-(1-2*M/x[1]),1/(1-2*M/x[1]),x[1]**2,x[1]**2*np.sin(x[2])**2])
rn=lambda M,Q2: diag(lambda x: [-(1-2*M/x[1]+Q2/x[1]**2),1/(1-2*M/x[1]+Q2/x[1]**2),x[1]**2,x[1]**2*np.sin(x[2])**2])
dsit=lambda L: diag(lambda x: [-(1-x[1]**2/L**2),1/(1-x[1]**2/L**2),x[1]**2,x[1]**2*np.sin(x[2])**2])
# flat FRW dust in (t, x, y, z): a = t^(2/3)
frw=diag(lambda x: [-1,x[0]**(4/3),x[0]**(4/3),x[0]**(4/3)])
# ---- path 2: ambitwistor incidence in flat space (complexified), Z = (omega, pi), W = (lam, nu)
def amb(x,lam,pi): return 1j*x@pi, -1j*x.T@lam
# ---- path 6: contour field from a twistor function on the overlap of two patches
def field(F,al,be,x):
    a0=1j*(al[0]*x[0,0]+al[1]*x[1,0])+al[2]; a1=1j*(al[0]*x[0,1]+al[1]*x[1,1])+al[3]
    b0=1j*(be[0]*x[0,0]+be[1]*x[1,0])+be[2]; b1=1j*(be[0]*x[0,1]+be[1]*x[1,1])+be[3]
    za=-a0/a1; zb=-b0/b1; rho=abs(za-zb)/2; th=2*np.pi*np.arange(256)/256; z=za+rho*np.exp(1j*th); dz=1j*rho*np.exp(1j*th)*(2*np.pi/256)
    om0=1j*(x[0,0]+x[0,1]*z); om1=1j*(x[1,0]+x[1,1]*z); Z=(om0,om1,np.ones_like(z),z)
    f=F(Z); return np.array([np.sum(z**k*f*dz)/(2j*np.pi) for k in range(5)])
dot=lambda v,Z: v[0]*Z[0]+v[1]*Z[1]+v[2]*Z[2]+v[3]*Z[3]
