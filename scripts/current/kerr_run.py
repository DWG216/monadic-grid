exec(open('kerr_lib.py').read()); rng=np.random.default_rng(20261122); lams=np.linspace(0.05,1.2,24)
k1=True; k2=True; nf=0; k3=True; k4=True; k5=True; rows=[]
for nm,g,N in (("Kerr",kerr(1,0.9),6),("Schwarzschild",schw(1),4)):
    for _ in range(N):
        x0=np.array([0.,rng.uniform(3.5,7),rng.uniform(0.5,2.6),rng.uniform(0,6.2)]); a=rng.uniform(0.2,2.9); b=rng.uniform(0,6.2)
        F=cone2(g,x0,a,b,lams,+1); P=cone2(g,x0,a,b,lams,-1); sf=fitd(lams,F[1]); sp=fitd(lams,P[1]); arf=fitd(lams,F[0])
        line=f"{nm} r={x0[1]:.2f}: shape c2 {sf[1]:.5f}/{sp[1]:.5f}; c3 {sf[2]:+.5f}/{sp[2]:+.5f}; c4 {sf[3]:+.6f}/{sp[3]:+.6f}"
        if abs(sf[3])>5e-5: k5&=abs(sp[3]/sf[3]-1)<0.10
        if nm=="Kerr":
            t_d,w_d=direct(g,x0,a,b); k1&=abs(6*arf[1])<0.03*w_d and abs(1.5*sf[1]/w_d-1)<0.03
            af=angle_fit(lams,F[2],F[2][0]); ap=angle_fit(lams,P[2],P[2][0]); s=abs(np.mod(af[0]+ap[0]+np.pi/2,np.pi)-np.pi/2); k2&=s<0.02
            off=abs(np.mod(ap[0]-0.6+np.pi/2,np.pi)-np.pi/2); nf+=off>0.03
            if abs(af[1])>0.01: k3&=np.sign(af[1])==np.sign(ap[1]) and abs(af[1]-ap[1])<0.2*abs(af[1])
            if abs(sf[2])>1e-3: k4&=np.sign(sf[2])!=np.sign(sp[2]) and abs(sf[2]+sp[2])<0.15*abs(sf[2])
            line+=f"; w direct {w_d:.5f} est {1.5*sf[1]:.5f}; area {6*arf[1]:.1e}; angle0 {af[0]:.4f}/{ap[0]:.4f} (sum {s:.4f}, off-rotation {off:.3f}); slopes {af[1]:+.4f}/{ap[1]:+.4f}"
        print(line,flush=True); rows.append(line)
print("K1 Kerr vacuum:",'PASS' if k1 else 'FAIL'); print("K2 conjugate shear:",'PASS' if k2 and nf>=4 else 'FAIL',f"(not forced in {nf} of 6)"); print("K3 equal rotation:",'PASS' if k3 else 'FAIL'); print("K4 order 3 odd:",'PASS' if k4 else 'FAIL'); print("K5 order 4 even:",'PASS' if k5 else 'FAIL')
