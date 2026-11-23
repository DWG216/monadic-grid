# SANITY RUN 2 (not a test): plant detector D = S_w - S_uniform. 30 null draws, seed 2.
exec(open('t11_lib.py').read())
G=zeros_to(600); rng=np.random.default_rng(2); s=0.5+1j*G
wsp=np.abs(1+2**(-s)+3**(-s))**2; wfk=np.abs(1+2.37**(-s)+3.71**(-s))**2
for nm,w in (('sparse',wsp),('fake sparse',wfk)):
    for un,u0 in (('ln2',np.log(2)),('ln3',np.log(3)),('ln3/2',np.log(1.5))):
        v=Dpeak(G,w,u0); q=np.quantile([Dpeak(G,rng.permutation(w),u0) for _ in range(30)],0.95); print(f"{nm} {un}: {v:.2f} vs null95 {q:.2f}")
