# POST HOC (labelled, not pre-registered): why did P3 fail? Eigen sums only (identical to the entries readout to 1e-10).
exec(open('t10_lib.py').read())
PL=[(n,lam(n)) for n in range(2,51) if lam(n)>0]
wpr=np.abs(sum(l*n**(-0.5-1j*g) for n,l in PL))**2
Sw=lambda w,u: np.array([np.sum(w*np.cos(g*x))/w.sum() for x in np.atleast_1d(u)])
one=np.ones(len(g))
for nm,u0 in (('ln2',np.log(2)),('ln3',np.log(3)),('ln3/2',np.log(1.5))):
    print(f"{nm}: S_primes(u0) {Sw(wpr,u0)[0]:+.3f}; zeros' own S_uniform(u0) {Sw(one,u0)[0]:+.3f}; |S_primes| window median {np.median(np.abs(Sw(wpr,np.linspace(u0-.5,u0+.5,201)))):.3f}")
# how many planted frequencies ln(n/m) fall within +-0.5 of ln2?
fr=sorted({abs(np.log(n/m)) for n,_ in PL for m,_ in PL if n!=m}); print("distinct planted frequencies ln(n/m) within ln2 +- 0.5:",sum(abs(f-np.log(2))<0.5 for f in fr))
# the cleaner plant: a few primes only (2,3), one term each
w23=np.abs(1+2**(-0.5-1j*g)+3**(-0.5-1j*g))**2
for nm,u0 in (('ln2',np.log(2)),('ln3',np.log(3)),('ln3/2',np.log(1.5))): print(f"plant 1+2^-s+3^-s, {nm}: peak {peak(lambda u: Sw(w23,u),u0):.2f}")
