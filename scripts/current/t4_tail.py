# post hoc (labelled): is the 4b gap the missing zeros above t = 400?
import numpy as np
xs=np.arange(-2.6,2.6,0.0005); u=xs/0.5; f=np.zeros_like(xs); m=np.abs(u)<1; f[m]=np.exp(-1/(1-u[m]**2))
t=np.arange(400,4000,0.05); F2=np.empty(len(t))
for s in range(0,len(t),1500):
    F2[s:s+1500]=np.abs(np.exp(1j*np.outer(t[s:s+1500],xs))@f*0.0005)**2
dens=np.log(t/(2*np.pi))/(2*np.pi)
tail=2*np.trapezoid(F2*dens,t)
print(f"expected contribution of zeros above t=400 to each diagonal entry: {tail:.4e}; |F(400)|^2 = {F2[0]:.3e}")
