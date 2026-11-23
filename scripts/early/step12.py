import numpy as np
from scipy.integrate import solve_ivp
print('=== STEP 1: propagate the two hands along a light ray (vacuum Sachs + Bianchi, principal ray) ===')
# along the ray: d rho/dr = rho^2 (focusing, shear-free), d Psi/dr = 3 rho Psi ; hand- uses its own rho~, Psi~
def run(q_plus, q_minus, M=(1.0+0.4j), r0=3.0, r1=30.0):
    y0=[-1/(r0-1j*q_plus), -M/(r0-1j*q_plus)**3, -1/(r0+1j*q_minus), -np.conj(M)/(r0+1j*q_minus)**3]
    f=lambda r,y:[y[0]**2, 3*y[0]*y[1], y[2]**2, 3*y[2]*y[3]]
    s=solve_ivp(f,(r0,r1),y0,rtol=1e-11,atol=1e-14,t_eval=np.linspace(r0,r1,6))
    return s.t, np.abs(s.y[3]-np.conj(s.y[1]))/np.abs(s.y[1])
for name,qp,qm in [('real ray (twist real, both hands see the same real ray)',0.7,0.7),
                   ('complexified ray (hand- sees a different twist)',0.7,0.7+0.3j)]:
    t,dev=run(qp,qm); print('  %-58s relative mismatch hand- vs conj(hand+) at r=%s: %s'%(name,np.round(t,1).tolist(),np.round(dev,6).tolist()))
print('\n=== STEP 2: light (shape) + hbar (size) -> Einstein, Jacobson-style ===')
rng=np.random.default_rng(2); g=np.diag([-1,1,1,1.])
def sym(): a=rng.normal(size=(4,4)); return a+a.T
basis=[];
for i in range(4):
    for j in range(i,4):
        E=np.zeros((4,4)); E[i,j]=E[j,i]=1; basis.append(E)
def rank_of(vectors):   # how many of the 10 components of X = Ric - 8piG T get fixed by X(k,k)=0 for these k
    Arow=np.array([[k@B@k for B in basis] for k in vectors]); s=np.linalg.svd(Arow,compute_uv=False); return int((s>1e-9*s[0]).sum())
null=[]
for _ in range(60):
    n=rng.normal(size=3); n/=np.linalg.norm(n); null.append(np.r_[1,n])
print('  focusing = heat flow along ALL light directions fixes %d of 10 components (remaining 1 = multiple of the metric -> cosmological constant)'%rank_of(null))
print('  energy balance for ONE observer (time direction only) fixes %d of 10'%rank_of([np.array([1,0,0,0.])]))
# check the leftover direction is the metric
Arow=np.array([[k@B@k for B in basis] for k in null]); _,s,vt=np.linalg.svd(Arow); X=sum(c*B for c,B in zip(vt[-1],basis))
print('  the undetermined direction is proportional to the metric:',np.allclose(X/X[1,1],g/g[1,1],atol=1e-8))
for hb in [1.0,1e-3,1e3]:
    kappa=0.37; dA=-2.1; G=1.0; lp2=hb*G
    T=hb*kappa/(2*np.pi); dS=dA/(4*lp2); print('  hbar=%-7g Unruh T=%.4g, entropy change=%.4g, heat T*dS=%.6f  (hbar-free)'%(hb,T,dS,T*dS))
