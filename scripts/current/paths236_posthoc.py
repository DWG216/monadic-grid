# POST HOC (labelled): diagnose the three failures of paths236.py. Not upgraded to passes.
exec(open('g_lib.py').read()); rng=np.random.default_rng(7); C=lambda *s: rng.normal(size=s)+1j*rng.normal(size=s)
eps=np.array([[0,1],[-1,0]])
m=0
for _ in range(50):
    x=C(2,2); lam=C(2); pi=C(2); om,nu=amb(x,lam,pi); t=C(1)[0]
    om2,nu2=amb(x+t*np.outer(eps@lam,eps@pi),lam,pi); m=max(m,abs(om2-om).max(),abs(nu2-nu).max())
print(f"A1 with the spinor epsilon on both factors of the direction: change along the null line {m:.1e}")
P=[np.array([0.0,r,1.2,0.5]) for r in (3,4,5,6,7,8)]
for x in P:
    q=Rkk(rn(1,0.1),x,rng)[0]; s=Rkk(schw(1),x,rng)[0]; print(f"T3 r = {x[1]:.0f}: RN |R_kk| {q:.1e}, Schwarzschild {s:.1e}, ratio {q/max(s,1e-30):.0f}, Q^2/r^4 = {0.1/x[1]**4:.1e}")
src=open('g_lib.py').read()
for npts in (256,1024,4096):
    g={}; exec(src.replace('256',str(npts)),g); al=C(4); be=C(4); ga=C(4); de=C(4); d=g['dot']
    f=lambda Z: 1/(d(al,Z)**3*d(be,Z)**3); cob=lambda Z: f(Z)+d(ga,Z)**2/d(al,Z)**8+d(de,Z)**3/d(be,Z)**9
    r=max(np.abs(g['field'](cob,al,be,x)-g['field'](f,al,be,x)).max()/np.abs(g['field'](f,al,be,x)).max() for x in (C(2,2) for _ in range(20)))
    print(f"G1 contour points {npts}: max relative change from the coboundary {r:.1e}")
# G1, second look: is the coboundary's residual cancellation roundoff? Compare its integral with the integral of its absolute value.
g={}; exec(src,g); d=g['dot']; rng2=np.random.default_rng(11); C2=lambda *s: rng2.normal(size=s)+1j*rng2.normal(size=s)
worst=0
for _ in range(20):
    al=C2(4); be=C2(4); ga=C2(4); de=C2(4); x=C2(2,2)
    h=lambda Z: d(ga,Z)**2/d(al,Z)**8+d(de,Z)**3/d(be,Z)**9
    I=np.abs(g['field'](h,al,be,x)).max(); A=np.abs(g['field'](lambda Z: np.abs(h(Z)),al,be,x)).max()
    worst=max(worst,I/A)
print(f"G1 coboundary integral / integral of its absolute value: max {worst:.1e} (roundoff level ~1e-13)")
