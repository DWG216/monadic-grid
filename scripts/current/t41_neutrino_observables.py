import numpy as np
from scipy.optimize import brentq
def Q(x): x=np.array(x); return np.sum(x**2)/np.sum(x)**2
def solve(d21,d31):
    f=lambda l: Q([-np.sqrt(l),np.sqrt(np.sqrt(l*l+d21)),np.sqrt(np.sqrt(l*l+d31))])-2/3
    g=np.linspace(1e-7,0.02,4001); v=[f(t) for t in g]
    for i in range(len(g)-1):
        if np.sign(v[i])!=np.sign(v[i+1]): return brentq(f,g[i],g[i+1])
rng=np.random.default_rng(2); out=[]
for _ in range(3000):
    d21=rng.normal(7.50e-5,0.12e-5); d31=rng.normal(2.513e-3,0.020e-3); s12=rng.normal(0.3092,0.0087); s13=rng.normal(0.0220,0.0007)
    m1=solve(d21,d31); m=[m1,np.sqrt(m1**2+d21),np.sqrt(m1**2+d31)]
    U=[(1-s12)*(1-s13),s12*(1-s13),s13]
    a=rng.uniform(0,2*np.pi); b=rng.uniform(0,2*np.pi)
    mbb_any=abs(U[0]*m[0]+U[1]*m[1]*np.exp(1j*a)+U[2]*m[2]*np.exp(1j*b))
    mbb_pi=[abs(-U[0]*m[0]+U[1]*m[1]+U[2]*m[2]*np.exp(1j*b)) for b in (0,np.pi)]
    out.append((sum(m),m1,mbb_any,mbb_pi[0],mbb_pi[1],U[0]*m[0]+U[1]*m[1]+U[2]*m[2]))
o=np.array(out)*1e3
print('sum (meV): %.2f +- %.2f'%(o[:,0].mean(),o[:,0].std()))
print('m_bb, Majorana phases free (meV): min %.2f  median %.2f  max %.2f'%(o[:,2].min(),np.median(o[:,2]),o[:,2].max()))
print('m_bb with nu1 phase = pi (the negative root), beta = 0 or pi (meV): %.2f to %.2f'%(o[:,4].mean(),o[:,3].mean()))
print('absolute ceiling sum|U|^2 m (meV): %.2f'%o[:,5].max())
