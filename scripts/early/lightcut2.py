import numpy as np
src=open('lightcut.py').read().split("kinds=[")[0]; exec(src)
R=Rr+0.5
def taper(width):   # flat middle, linear ramp to zero over 'width' sites at each edge
    return np.clip((R-np.abs(x))/width,0,1)
def diamond(beta):
    L=beta*v/np.pi; return L*np.sinh((R-x)/L)*np.sinh((R+x)/L)/np.sinh(2*R/L)
grid=np.linspace(-0.2,0.0,81)
for beta in [5.0,10.0,20.0]:
    C=corr(beta)[np.ix_(idx,idx)]; L=beta*v/np.pi
    cands={'light-cone diamond (thermal length %.1f)'%L:diamond(beta),
           'zero-temperature diamond (R^2-x^2)':(R**2-x**2)/(2*R),
           'triangle (R-|x|)':R-np.abs(x),
           'taper, right width (%.1f)'%L:taper(L),
           'taper, 1/3 width':taper(L/3),'taper, 3x width':taper(3*L),
           'Gaussian bump':np.exp(-(x/(R/2))**2)}
    print('beta=%.0f'%beta)
    for name,w in cands.items():
        ga=gen(Ha,w); res=[]
        for lp in grid:
            g=np.block([[ga,np.zeros_like(ga)],[np.zeros_like(ga),gen(h(-lp),w)]]); res.append(np.linalg.norm(g@C-C@g)/np.linalg.norm(g))
        res=np.array(res); k=np.argmin(res); s=slice(max(k-4,0),k+5); p=np.polyfit(grid[s],res[s]**2,2); xm=-p[1]/(2*p[0])
        print('   %-42s drift %.4f'%(name,abs(xm+lam)))
