exec(open('t16_lib.py').read()); import json
PP=prime_powers(5000); s=1.5; out={}
cs=np.arange(28,55.6,1.5); Zd=zeros_chi5(26,58); inner=Zd[(Zd>=30)&(Zd<=53)]
G,H=forms(cs,s,PP,q=5,chi=chi5,pole=False); rv,kk,e=ritz(G,H); d=np.array([np.abs(rv-z).min() for z in inner])
print("G1 direct zeros of L(s,chi5):",np.round(Zd,4)); print("   operator from the primes:  ",np.round(rv,4))
print(f"G1 {len(inner)} zeros in [30,53]: max distance {d.max():.5f}; positivity {e.min()/e.max():.1e} ->",'PASS' if d.max()<1e-3 and e.min()/e.max()>=-1e-10 else 'FAIL')
G2,H2=forms(cs,s,PP,q=5,chi=None,pole=False); r2,k2,_=ritz(G2,H2); m=int(sum(np.abs(r2-z).min()<0.01 for z in inner)); print(f"G2 null (no character): {m}/{len(inner)} matched ->",'PASS' if m<len(inner)/2 else 'FAIL')
out['chi5']=dict(direct=Zd.tolist(),ritz=rv.tolist())
pub=np.array([52.970321,56.446248,59.347044,60.831779,65.112544,67.079811,69.546402,72.067158,75.704691]); cz=np.arange(47,80.6,1.5); curve=[]
for X in (1,10,30,100,300,1000,5000):
    Gx,Hx=forms(cz,s,[p for p in PP if p[0]<=X]); rx,_,_=ritz(Gx,Hx); dx=np.array([np.abs(rx-z).min() for z in pub]); curve.append((X,int((dx<0.01).sum()),float(dx.max())))
    print(f"X1 primes up to {X}: {int((dx<0.01).sum())}/9 within 0.01; max distance {dx.max():.5f}")
c=dict((X,n) for X,n,_ in curve); print("X1 ->",'PASS' if c[100]==9 and c[10]<9 and c[1]<=2 else 'FAIL'); out['curve']=curve
ca=np.arange(9,46.1,1.5); Ga,Ha=forms(ca,s,PP); ra,_,_=ritz(Ga,Ha); Gb,Hb=forms(ca,s,PP,pole=False); rb,_,_=ritz(Gb,Hb)
dp=np.abs(ra-rb).max() if len(ra)==len(rb) else 9; print(f"A1 pole term dropped: max shift {dp:.2e} ->",'PASS' if dp<1e-4 else 'FAIL')
# D1 eigenvector for 59.347
Gz,Hz=forms(cz,s,PP); ee,U=np.linalg.eigh(Gz); keep=ee>1e-7*ee.max(); T=U[:,keep]/np.sqrt(ee[keep]); ev,W=np.linalg.eigh(T.T@Hz@T); k=np.argmin(np.abs(np.sqrt(np.abs(ev))-59.347)); coef=T@W[:,k]
r=np.arange(44,84,0.01); f=sum(a*phi(r,c,s) for a,c in zip(coef,cz)); f/=f[np.argmin(np.abs(r-59.347))]
allz=np.array([43.327073,48.005151,49.773832,52.970321,56.446248,59.347044,60.831779,65.112544,67.079811,69.546402,72.067158,75.704691,77.144840,79.337375,82.910381])
print("D1 eigenvector value at each zero:",np.round([f[np.argmin(np.abs(r-z))] for z in allz],3))
out['eig']=dict(r=r[::5].tolist(),f=f[::5].tolist(),zeros=allz.tolist()); json.dump(out,open('t16_results.json','w'))
