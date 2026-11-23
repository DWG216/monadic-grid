exec(open('t15_lib.py').read()); exec(open('t11_lib.py').read())
pub=np.array([48.005151,49.773832,52.970321,56.446248,59.347044,60.831779,65.112544,67.079811,69.546402,72.067158,75.704691,77.144840,79.337375])
s=1.5; cs=np.arange(47,80.6,1.5); PP=prime_powers(5000); inner=pub[(pub>=50)&(pub<=77)]
G,H=forms_from_primes(cs,s,PP); rv,kk,e=ritz(G,H)
print("Ritz values from the primes:",np.round(rv,4)); print("published zeros:           ",np.round(pub,4))
d=np.array([np.abs(rv-z).min() for z in inner]); print(f"T1 max distance for the {len(inner)} zeros in [50,77]: {d.max():.4f} ->",'PASS' if d.max()<0.01 else 'FAIL')
print(f"T2 kept directions: {kk} ->",'PASS' if kk in (12,13,14) else 'FAIL')
print(f"T3 min/max eigenvalue of G: {e.min()/e.max():.2e} ->",'PASS' if e.min()/e.max()>=-1e-10 else 'FAIL')
rng=np.random.default_rng(20261122); fake=[int(x) for x in rng.integers(2,5001,size=len(PP))]
Gf,Hf=forms_from_primes(cs,s,PP,fake=fake); rf,kf,ef=ritz(Gf,Hf); m=int(sum(np.abs(rf-z).min()<0.01 for z in inner))
print(f"T4 fake primes: kept {kf}, min/max eig {ef.min()/ef.max():.2e}, zeros matched {m}/11 ->",'PASS' if m<6 else 'FAIL'); print("   fake Ritz:",np.round(rf,3))
Z=zeros_to(600); Gz,Hz=forms_from_zeros(cs,s,Z); rz,kz,_=ritz(Gz,Hz)
dz=max(np.abs(rz-z).min() for z in rv) if kz else 9; print(f"C1 zero-side kept {kz}; max distance prime-side to zero-side Ritz: {dz:.4f} ->",'PASS' if dz<0.02 else 'FAIL')
np.save('t15_ritz.npy',rv)
