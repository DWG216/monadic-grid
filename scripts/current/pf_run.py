exec(open('pastfuture_lib.py').read()); rng=np.random.default_rng(20261122); lams=np.linspace(0.1,1.0,10)
ok1=ok2=ok3=ok4=True; rows=[]
for nm,g in (("Schwarzschild",schw(1)),("Reissner-Nordstrom",rn(1,0.5))):
    for _ in range(4):
        x0=np.array([0.,rng.uniform(3.5,7),rng.uniform(0.5,2.6),rng.uniform(0,6.2)]); a=rng.uniform(0.2,2.9); b=rng.uniform(0,6.2)
        F=cone2(g,x0,a,b,lams,+1); P=cone2(g,x0,a,b,lams,-1)
        sf=fit(lams,F[1]); sp=fit(lams,P[1]); af=fit(lams,F[0]); ap=fit(lams,P[0])
        e2=abs(sp[1]/sf[1]-1); ok1&=e2<0.03
        th=angdiff(F[2][2],-P[2][2]); ok2&=th<0.02
        if abs(sf[2])>1e-3: ok3&=np.sign(sf[2])!=np.sign(sp[2]) and abs(sf[2]+sp[2])<0.15*abs(sf[2])
        if nm.startswith('R'): ea=abs(ap[1]/af[1]-1); ok4&=af[1]>0 and ap[1]>0 and ea<0.05; ok1&=ea<0.05
        else: ea=float('nan')
        rows.append((nm,x0[1],sf[1],sp[1],sf[2],sp[2],F[2][2],P[2][2],af[1],ap[1]))
        print(f"{nm} r={x0[1]:.2f}: shape c2 F/P {sf[1]:.5f}/{sp[1]:.5f} (err {e2:.3f}); c3 F/P {sf[2]:+.5f}/{sp[2]:+.5f}; angle F/P {F[2][2]:.3f}/{P[2][2]:.3f} (miss {th:.4f}); area c2 F/P {af[1]:.6f}/{ap[1]:.6f}",flush=True)
print("P1 order 2 time-even:",'PASS' if ok1 else 'FAIL'); print("P2 conjugate shear:",'PASS' if ok2 else 'FAIL'); print("P3 order 3 time-odd:",'PASS' if ok3 else 'FAIL'); print("P4 matter time-symmetric:",'PASS' if ok4 else 'FAIL')
import json; json.dump(rows,open('pf_results.json','w'))
