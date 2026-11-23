# SANITY RUN (not a test): one Kerr case.
exec(open('order4_lib.py').read()); import time; t0=time.time()
lams=np.linspace(0.05,1.2,24); x0=np.array([0.,4.5,1.0,0.3]); a,b=1.1,0.7; g=kerr(1,0.9)
T0,T1,T2=tidal_series(g,x0,a,b); Ap,Bp,Cp=predicted(T0,T1,T2); Am,Bm,Cm=cone_matrix(g,x0,a,b,lams)
print("A pred/meas rel diff",f"{rel(Am,Ap):.2e}","; B",f"{rel(Bm,Bp):.2e}","; C",f"{rel(Cm,Cp):.2e}")
print("C measured",np.round(Cm,6).tolist(),"\nC predicted",np.round(Cp,6).tolist(),"\n  T0^2 part",np.round(2/45*T0@T0,6).tolist(),"  T2 part",np.round(-T2/20,6).tolist())
print("C without the T0^2 term: rel diff",f"{rel(Cm,-T2/20):.2e}",f"; {time.time()-t0:.0f}s")
