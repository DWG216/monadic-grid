# SANITY RUN (not a test): one Kerr case and one Schwarzschild case; checks frame, vacuum, angles, order-4 fits.
exec(open('kerr_lib.py').read()); import time; t0=time.time()
lams=np.linspace(0.05,1.2,24); x0=np.array([0.,4.5,1.0,0.3]); a,b=1.1,0.7
g=kerr(1,0.9); k,s1,s2=frame(g,x0,a,b); gx=g(x0); print("frame checks: k.k",f"{k@gx@k:.1e}","s1.s1",f"{s1@gx@s1:.4f}","k.s1",f"{k@gx@s1:.1e}")
t_d,w_d=direct(g,x0,a,b); print("Kerr direct R_kk",f"{t_d:.1e}","w",f"{w_d:.5f}")
F=cone2(g,x0,a,b,lams,+1); P=cone2(g,x0,a,b,lams,-1)
for nm,i in (("area",0),("shape",1)):
    cf=fitd(lams,F[i]); cp=fitd(lams,P[i]); print(f"{nm}: c2 F/P {cf[1]:.6f}/{cp[1]:.6f}; c3 {cf[2]:+.6f}/{cp[2]:+.6f}; c4 {cf[3]:+.6f}/{cp[3]:+.6f}")
af=angle_fit(lams,F[2],F[2][0]); ap=angle_fit(lams,P[2],P[2][0]); print("angle intercepts F/P",np.round(af[0],4),np.round(ap[0],4),"sum mod pi",round(np.mod(af[0]+ap[0]+np.pi/2,np.pi)-np.pi/2,4),"; slopes",np.round(af[1],4),np.round(ap[1],4))
print(f"{time.time()-t0:.0f}s")
