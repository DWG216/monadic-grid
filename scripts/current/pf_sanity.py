# SANITY RUN (not a test): one Schwarzschild case.
exec(open('pastfuture_lib.py').read()); lams=np.linspace(0.1,1.0,10); x0=np.array([0.,4.,1.2,0.5]); a,b=0.9,0.4
F=cone2(schw(1),x0,a,b,lams,+1); P=cone2(schw(1),x0,a,b,lams,-1)
for nm,i in (("area",0),("shape",1)):
    cf=fit(lams,F[i]); cp=fit(lams,P[i]); print(f"{nm}: future c2 {cf[1]:.6f} c3 {cf[2]:.6f}; past c2 {cp[1]:.6f} c3 {cp[2]:.6f}")
print("major-axis angle at lambda = 0.3: future",round(F[2][2],4),"past",round(P[2][2],4),"; future + past (mod pi)",round(np.mod(F[2][2]+P[2][2],np.pi),4))
