# SANITY RUN (not a test): Schwarzschild and RN at one vertex, coarse.
exec(open('cone_lib.py').read()); import time; t0=time.time()
x0=np.array([0.,4.,1.2,0.5]); a,b=0.9,0.4; lams=np.linspace(0.1,1.0,10)
for nm,g in (("Schwarzschild",schw(1)),("RN Q2=0.5",rn(1,0.5))):
    t_d,w_d=direct(g,x0,a,b); ar,sh=cone(g,x0,a,b,lams); ca=fit(lams,ar); cs=fit(lams,sh)
    print(f"{nm}: direct R_kk {t_d:.5f}, Weyl w {w_d:.5f}; cone: area order1 {ca[0]:.1e}, R_kk est {6*ca[1]:.5f}; shape order1 {cs[0]:.1e}, w est {1.5*cs[1]:.5f}; {time.time()-t0:.0f}s",flush=True)
