# SANITY RUN (not a test; seed 1, few points)
exec(open('g_lib.py').read()); rng=np.random.default_rng(1)
x=np.array([0.,4.,1.1,0.3])
for nm,g in (("Schwarzschild",schw(1)),("RN Q2=0.1",rn(1,0.1)),("de Sitter L=10",dsit(10))):
    v,R=Rkk(g,x,rng); print(nm,"max|R_kk|",f"{v:.2e}","max|R_ab|",f"{abs(R).max():.2e}")
v,R=Rkk(frw,np.array([1.,0.3,0.2,0.1]),rng); print("FRW dust max|R_kk|",f"{v:.2e}")
lam=rng.normal(size=2)+1j*rng.normal(size=2); pi=rng.normal(size=2)+1j*rng.normal(size=2); x=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
om,nu=amb(x,lam,pi); print("Z.W at a point:",abs(om@lam+pi@nu))
al=rng.normal(size=4)+1j*rng.normal(size=4); be=rng.normal(size=4)+1j*rng.normal(size=4); ga=rng.normal(size=4)+1j*rng.normal(size=4)
f=lambda Z: 1/(dot(al,Z)**3*dot(be,Z)**3); h0=lambda Z: dot(ga,Z)**2/dot(al,Z)**8
print("field change from a coboundary:",np.abs(field(lambda Z: f(Z)+h0(Z),al,be,x)-field(f,al,be,x)).max(),"; field size",np.abs(field(f,al,be,x)).max())
