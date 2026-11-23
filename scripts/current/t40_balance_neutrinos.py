import numpy as np
from scipy.optimize import brentq
def Q(x): x=np.array(x,float); return np.sum(x**2)/np.sum(x)**2   # x = signed square roots
res={}
me,mmu,mt=0.51099895,105.6583755,1776.93
x=np.sqrt([me,mmu,mt]); X=np.fft.fft(x)
res['B1 P(+-1)/P(0)']=float((abs(X[1])**2+abs(X[2])**2)/abs(X[0])**2)
res['B2 angle to (1,1,1) deg']=float(np.degrees(np.arccos(x.sum()/np.sqrt(3)/np.linalg.norm(x))))
res['B3 Q pole']=Q(x); res['B3 Q running (M_Z)']=Q(np.sqrt([0.4866,102.72,1746.2]))
res['B4 Q(c,b,t)']=Q(np.sqrt([1.67,4.78,172.57])); res['B4 Q(-s,c,b)']=Q([-np.sqrt(0.0935),np.sqrt(1.273),np.sqrt(4.183)]); res['B4 triples tried']=4
def solve(d21,dA,order,neg):
    # order NO: m1 lightest, m2^2 = m1^2+d21, m3^2 = m1^2+d31 ; IO: m3 lightest, m1^2 = m3^2+|d32|-d21, m2^2 = m3^2+|d32|
    def ms(l):
        if order=='NO': return [l,np.sqrt(l*l+d21),np.sqrt(l*l+dA)]
        return [np.sqrt(l*l+dA-d21),np.sqrt(l*l+dA),l]
    def f(l):
        m=ms(l); s=[np.sqrt(v)*(-1 if i==neg else 1) for i,v in enumerate(m)]; return Q(s)-2/3
    g=np.linspace(1e-7,0.3,30001); v=np.array([f(t) for t in g]); out=[]
    for i in np.where(np.sign(v[:-1])!=np.sign(v[1:]))[0]:
        l=brentq(f,g[i],g[i+1]); out.append((l,ms(l)))
    return out
for order,dA in [('NO',2.513e-3),('IO',2.484e-3)]:
    for neg in [None,0,1,2]:
        sols=solve(7.50e-5,dA,order,neg)
        res[f'N1 {order} negative root {neg}']=[(round(l*1e3,4),round(sum(m)*1e3,3)) for l,m in sols] if sols else 'none'
rng=np.random.default_rng(1); S=[];L=[];MB=[]
for _ in range(4000):
    d21=rng.normal(7.50e-5,0.12e-5); d31=rng.normal(2.513e-3,0.020e-3); s12=rng.normal(0.3092,0.0087); s13=rng.normal(0.0220,0.0007)
    sols=solve(d21,d31,'NO',0)
    if not sols: continue
    l,m=sols[0]; S.append(sum(m)); L.append(l)
    U2=[(1-s12)*(1-s13),s12*(1-s13),s13]; MB.append(np.sqrt(sum(u*mm*mm for u,mm in zip(U2,m))))
S,L,MB=map(np.array,(S,L,MB))
res['N2 runs with a solution']=len(S)
res['N2 sum m_nu (meV) mean, sd']=(round(S.mean()*1e3,3),round(S.std()*1e3,3))
res['N2 lightest (meV) mean, sd']=(round(L.mean()*1e3,4),round(L.std()*1e3,4))
res['N2 m_beta (meV) mean, sd']=(round(MB.mean()*1e3,3),round(MB.std()*1e3,3))
l,m=solve(7.50e-5,2.513e-3,'NO',0)[0]; xs=np.array([-np.sqrt(m[0]),np.sqrt(m[1]),np.sqrt(m[2])]); a=xs.mean()
# fit delta: x_k = a(1+sqrt2 cos(delta+2pi k/3)) up to relabelling; take the phase of the k=1 Fourier coefficient
c1=np.fft.fft(xs)[1]; dnu=float(np.angle(c1))
cands=[(s*dnu+2*np.pi*j/3)%(2*np.pi) for s in (1,-1) for j in range(3)]
target=2/9+np.pi/12; dbest=min(cands,key=lambda c:abs(c-target))
res['N3 delta_nu nearest Brannen']=(round(dbest,5),round(target,5))
for k,v in res.items(): print(k,v)
