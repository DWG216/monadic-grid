# SANITY RUN (not a test): window A, centres 9..46.
exec(open('t15_lib.py').read()); exec(open('t11_lib.py').read())
Z=zeros_to(600); s=1.5; cs=np.arange(9,46.1,1.5); PP=prime_powers(5000)
G,H=forms_from_primes(cs,s,PP); Gz,Hz=forms_from_zeros(cs,s,Z)
print("basis",len(cs),"; max |G_primes - G_zeros| / max G:",f"{np.abs(G-Gz).max()/np.abs(Gz).max():.2e}","; H:",f"{np.abs(H-Hz).max()/np.abs(Hz).max():.2e}")
print("min eigenvalue of G from primes / max:",f"{np.linalg.eigvalsh(G).min()/np.linalg.eigvalsh(G).max():.2e}")
for tol in (1e-5,1e-7,1e-9):
    rv,kk,e=ritz(G,H,tol); rz,kz,_=ritz(Gz,Hz,tol)
    print(f"tol {tol}: kept {kk} (zero side {kz}); Ritz from primes:",np.round(rv,3))
print("true zeros below 50:",np.round(Z[Z<50],3))
rng=np.random.default_rng(1); fake=[int(x) for x in rng.integers(2,5001,size=len(PP))]
Gf,Hf=forms_from_primes(cs,s,PP,fake=fake); ef=np.linalg.eigvalsh(Gf); print("fake primes: min/max eigenvalue of G:",f"{ef.min()/ef.max():.2e}")
