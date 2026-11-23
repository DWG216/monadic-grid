exec(open('t11_lib.py').read())
G=zeros_to(600); zp=zeta_prime(G); c=np.abs(1/((0.5+1j*G)*zp))
def lead(N,w,q=5): a,b,_=jacobi(G[:N],w[:N]); return a[:q],b[:q]
for nm,w in (("O1 w = |1/(rho zeta')|",c),("O2 tempered, e^(-gamma/30)",c*np.exp(-G/30))):
    r={N:lead(N,w) for N in (100,200,341)}
    print(nm); [print(f"   N={N}: a = {np.round(r[N][0],4)}  b = {np.round(r[N][1],4)}") for N in r]
    da=np.abs(r[341][0]/r[200][0]-1).max(); db=np.abs(r[341][1]/r[200][1]-1).max(); d1=abs(r[341][0][0]/r[200][0][0]-1)
    print(f"   a_1 change 200->341: {100*d1:.2f}%; max change in a_1..5, b_1..5: {100*max(da,db):.4f}% ->", ('PASS' if d1>0.05 else 'FAIL') if nm.startswith('O1') else ('PASS' if max(da,db)<1e-3 else 'FAIL'))
