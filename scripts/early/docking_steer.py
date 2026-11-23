import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
R=25.0; cap=lambda s:0.5*np.log2(1+(R**2/12)/s**2)
print('D1: one inter-spike interval carries: pessimistic %.2f | median %.2f | optimistic %.2f bits'%(cap(5),cap(2),cap(0.5)))
# D2: calibrate P(closer wins) = 1/2 + arctan(r)/pi = 0.764
r=np.tan((0.764-0.5)*np.pi); print('D2: sigma_asym/sigma_noise = %.2f'%r)
rng=np.random.default_rng(5); N=400000; sa=r; sn=1.0; comb=np.hypot(sa,sn)
A=rng.normal(0,sa,N); E=rng.normal(0,sn,N)
print('   control (no nudge): closer cluster extruded %.3f'%np.mean(np.sign(A+E)==np.sign(A)))
for k in [0.5,1.0,1.4,2.0,3.0]:
    nu=k*comb; win=np.mean(A+E+nu>0)   # nudge toward a chosen lot (here: '+' lot), independent of geometry
    print('   nudge = %.1f x combined spread -> chosen lot wins %.3f'%(k,win))
need84=norm.ppf(0.84); need99=norm.ppf(0.99); print('   analytic: 84%% needs %.2f x, 99%% needs %.2f x combined spread'%(need84,need99))
# D3: power for two-proportion test, equal groups, base reversal p0
p0=0.236
def n_per_group(OR,alpha=0.05,power=0.8):
    o1=p0/(1-p0)*OR; p1=o1/(1+o1); pb=(p0+p1)/2; za=norm.ppf(1-alpha/2); zb=norm.ppf(power)
    return ((za*np.sqrt(2*pb*(1-pb))+zb*np.sqrt(p0*(1-p0)+p1*(1-p1)))/(p1-p0))**2, p1
for OR in [3,2,1.5]:
    n,p1=n_per_group(OR); print('D3: odds ratio %.1f (reversal %.3f -> %.3f): %d eggs per group, %d total'%(OR,p0,p1,np.ceil(n),2*np.ceil(n)))
