# SANITY RUN (not a test): golden L-function L(s, chi_5), window 3..25; and zeta with truncated primes (window A).
exec(open('t16_lib.py').read())
PP=prime_powers(5000); s=1.5
Zd=zeros_chi5(1,27); print("L(s,chi5) zeros by direct computation:",np.round(Zd,4))
cs=np.arange(3,25.1,1.5); G,H=forms(cs,s,PP,q=5,chi=chi5,pole=False); rv,kk,e=ritz(G,H)
print("operator from chi5-twisted primes: kept",kk,"min/max eig",f"{e.min()/e.max():.1e}"); print("   Ritz:",np.round(rv,4))
