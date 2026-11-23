import numpy as np
from scipy.optimize import brentq, least_squares
Q=lambda m,s=(1,1,1): sum(m)/sum(si*np.sqrt(mi) for si,mi in zip(s,m))**2
me,mmu,mtau,dtau=0.51099895,105.6583755,1776.93,0.09
res={}
q=Q([me,mmu,mtau]); res['K1 Q leptons']=q; res['K1 |Q-2/3|']=abs(q-2/3)
r=np.sqrt([me,mmu,mtau])
def resid(p):
    A,d=p; return [A*(1+np.sqrt(2)*np.cos(d+2*np.pi*k/3))-r[k] for k in (1,2,0)]  # assign k so that tau is largest
fit=least_squares(resid,[r.sum()/3,0.2]); A,d=fit.x
# delta modulo 2pi/3 symmetry: report the representative nearest 2/9
reps=[(d+2*np.pi*j/3)%(2*np.pi) for j in range(3)]+[(-d+2*np.pi*j/3)%(2*np.pi) for j in range(3)]
dbest=min(reps,key=lambda x:min(abs(x-2/9),abs(x-2/9-2*np.pi)))
res['K2 delta (rad)']=dbest; res['K2 |delta-2/9|']=abs(dbest-2/9); res['K2 fit residual max']=float(np.abs(fit.fun).max())
mt=brentq(lambda x: Q([me,mmu,x])-2/3,1000,3000); res['K3 predicted m_tau']=mt; res['K3 sigma away']=abs(mt-mtau)/dtau
mu,mc,mt_=2.16,1273.0,172570.0; md,ms,mb=4.70,93.5,4183.0
res['K4 Q(u,c,t)']=Q([mu,mc,mt_]); res['K4 Q(d,s,b)']=Q([md,ms,mb])
rng=np.random.default_rng(0); M=10**rng.uniform(-1,4,size=(1000000,3))
qs=M.sum(1)/np.sqrt(M).sum(1)**2; res['K5 null fraction']=float(np.mean(np.abs(qs-2/3)<=abs(q-2/3)))
d21,d31=7.49e-5,2.513e-3
def masses(m1): return [m1,np.sqrt(m1**2+d21),np.sqrt(m1**2+d31)]
grid=np.linspace(0,0.3,300001)
for name,s in [('all roots +',(1,1,1)),('m1 root -',(-1,1,1))]:
    vals=np.array([Q(masses(x),s)-2/3 for x in grid[::100]])
    idx=np.where(np.sign(vals[:-1])!=np.sign(vals[1:]))[0]
    sols=[brentq(lambda x: Q(masses(x),s)-2/3,grid[::100][i],grid[::100][i+1]) for i in idx]
    res['K6 '+name]=[(round(x,6),round(sum(masses(x)),5)) for x in sols] if sols else 'no solution in m1 in [0, 0.3] eV'
for k,v in res.items(): print(k,v)
