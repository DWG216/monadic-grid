# Round 6 real tests L1-L5 (Liouville through the operator). Pre-registered: PREDICTIONS_round6_2026-11-22.md
exec(open('t11_lib.py').read())
G=zeros_to(600); rho=0.5+1j*G; zp=zeta_prime(G); z2=np.array([zeta_em(1+2j*t) for t in G])
c=(1-G/600)*z2/(rho*zp); ns=list(range(2,31)); ND=100
def liou(n):
    k=0; m=n; p=2
    while p*p<=m:
        while m%p==0: m//=p; k+=1
        p+=1
    return (-1)**(k+(m>1))
L=np.array([liou(n) for n in ns])
cnt=lambda J: int(np.sum(np.sign(J)==L)); med=lambda J: float(np.median(J*np.sqrt(ns)*L))
J1=op_jumps(G,c,ns)
print(f"L1 full operator: signs {cnt(J1)}/29, median jump*sqrt(n)*lambda {med(J1):.3f}, corr {np.corrcoef(np.abs(J1),1/np.sqrt(ns))[0,1]:.3f}",flush=True)
print("   n, lambda, jump*sqrt(n):",[(n,int(l),round(float(j*np.sqrt(n)),2)) for n,l,j in zip(ns,L,J1)],flush=True)
r=np.random.default_rng(20261122); NC=[];NM=[]
for _ in range(ND):
    Jn=op_jumps(shuffle_spacings(G,r),c,ns); NC.append(cnt(Jn)); NM.append(med(Jn))
print(f"L2 null (shuffled spacings): signs 95th {np.quantile(NC,0.95):.1f} (real {cnt(J1)}); median 95th {np.quantile(NM,0.95):.3f} (real {med(J1):.3f})",flush=True)
p=np.abs(c); a,b,_=jacobi(G,p); e1=np.zeros(len(G)); e1[0]=1
def jm(a,b):
    Sx=lambda x: 2*np.real(kpm(a,b,e1[:len(a)],np.array([x])))[0]
    return np.array([Sx(np.log(n)+0.012)-Sx(np.log(n)-0.012) for n in ns])
J3=jm(a,b); r=np.random.default_rng(20261122); N3=[cnt(jm(*jacobi(shuffle_spacings(G,r),p)[:2])) for _ in range(ND)]
print(f"L3 magnitudes only: signs {cnt(J3)}/29 vs null95 {np.quantile(N3,0.95):.1f} -> {'PASS (not carried)' if cnt(J3)<=np.quantile(N3,0.95) else 'FAIL'}",flush=True)
res=[]
for K in (43,85,128,170,255,341):
    JK=op_jumps(G,c,ns,K); res.append((K,cnt(JK),float(np.median(np.abs(JK/J1)))))
    print(f"L4/L5 K={K}: signs {cnt(JK)}/29, median |J_K/J_full| {res[-1][2]:.2f}",flush=True)
np.save('t11_locality.npy',np.array(res)); np.save('t11_J1.npy',J1)
