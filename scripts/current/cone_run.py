exec(open('cone_lib.py').read()); rng=np.random.default_rng(20261122); lams=np.linspace(0.1,1.0,10); out={}
def cases(lo,hi): return [(np.array([0.,rng.uniform(lo,hi),rng.uniform(0.5,2.6),rng.uniform(0,6.2)]),rng.uniform(0.2,2.9),rng.uniform(0,6.2)) for _ in range(6)]
ok1=True; rows=[]
for nm,g,(lo,hi) in (("flat",schw(0),(3.5,7)),("Schwarzschild",schw(1),(3.5,7)),("Reissner-Nordstrom",rn(1,0.5),(3.5,7)),("de Sitter",dsit(10),(1,5))):
    R=[]
    for x0,a,b in cases(lo,hi):
        t_d,w_d=direct(g,x0,a,b); ar,sh=cone(g,x0,a,b,lams); ca=fit(lams,ar); cs=fit(lams,sh)
        ok1&=abs(ca[0])<1e-4 and abs(cs[0])<1e-4; R.append((t_d,w_d,6*ca[1],1.5*cs[1])); rows.append((nm,x0[1],t_d,w_d,6*ca[1],1.5*cs[1]))
    R=np.array(R); out[nm]=R
    print(f"{nm}: R_kk direct/est "+", ".join(f"{p:.5f}/{q:.5f}" for p,q in R[:,[0,2]])); print(f"   w direct/est "+", ".join(f"{p:.5f}/{q:.5f}" for p,q in R[:,[1,3]]),flush=True)
F,S,Q,D=out['flat'],out['Schwarzschild'],out['Reissner-Nordstrom'],out['de Sitter']
print("C0 flat:",'PASS' if np.abs(F[:,2:]).max()<1e-5 else 'FAIL',f"(max {np.abs(F[:,2:]).max():.1e})")
print("C1 order 1 vanishes:",'PASS' if ok1 else 'FAIL')
c2=np.all(np.abs(S[:,2])<0.03*S[:,1]) and np.all(np.abs(S[:,3]/S[:,1]-1)<0.03); print("C2 Schwarzschild:",'PASS' if c2 else 'FAIL',f"(max |R_kk est|/w {np.max(np.abs(S[:,2])/S[:,1]):.3f}; max w error {np.max(np.abs(S[:,3]/S[:,1]-1)):.3f})")
c3=np.all(np.abs(Q[:,2]/Q[:,0]-1)<0.05) and np.all(np.abs(Q[:,3]/Q[:,1]-1)<0.03); print("C3 Reissner-Nordstrom:",'PASS' if c3 else 'FAIL',f"(max R_kk error {np.max(np.abs(Q[:,2]/Q[:,0]-1)):.3f}; max w error {np.max(np.abs(Q[:,3]/Q[:,1]-1)):.3f})")
c4=np.abs(D[:,2:]).max()<1e-4; print("C4 de Sitter:",'PASS' if c4 else 'FAIL',f"(max {np.abs(D[:,2:]).max():.1e})")
import json; json.dump({k:v.tolist() for k,v in out.items()},open('cone_results.json','w'))
