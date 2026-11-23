exec(open('order4_lib.py').read()); rng=np.random.default_rng(20261122); lams=np.linspace(0.05,1.2,24); o1=o2=o3=True; rows=[]
for nm,g,N in (("Kerr",kerr(1,0.9),4),("Schwarzschild",schw(1),3),("Reissner-Nordstrom",rn(1,0.5),3)):
    for _ in range(N):
        x0=np.array([0.,rng.uniform(3.5,7),rng.uniform(0.5,2.6),rng.uniform(0,6.2)]); a=rng.uniform(0.2,2.9); b=rng.uniform(0,6.2)
        T0,T1,T2=tidal_series(g,x0,a,b); Ap,Bp,Cp=predicted(T0,T1,T2); Am,Bm,Cm=cone_matrix(g,x0,a,b,lams)
        eA,eB,eC=rel(Am,Ap),rel(Bm,Bp),rel(Cm,Cp); eN=rel(Cm,-T2/20); o1&=eA<1e-3 and eB<1e-2 and eC<0.02; o2&=eN>5*eC
        P=2/45*T0@T0; ev=np.linalg.eigvalsh(P); an=(ev[1]-ev[0])/abs(ev.mean()); o3&=(an<1e-3) if nm!="Reissner-Nordstrom" else (an>1e-2)
        share=np.linalg.norm(P)/np.linalg.norm(Cp)
        print(f"{nm} r={x0[1]:.2f}: rel diff A {eA:.1e}, B {eB:.1e}, C {eC:.1e}; C without T0^2 {eN:.1e}; T0^2 share of C {share:.2f}; anisotropy of T0^2 {an:.1e}",flush=True)
        rows.append((nm,x0[1],eA,eB,eC,eN,share,an))
print("O1 orders 2-4 predicted:",'PASS' if o1 else 'FAIL'); print("O2 meeting term needed:",'PASS' if o2 else 'FAIL'); print("O3 vacuum meeting term is pure area:",'PASS' if o3 else 'FAIL')
import json; json.dump(rows,open('o4_results.json','w'))
