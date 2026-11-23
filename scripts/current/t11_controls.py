# Round 6 positive controls P1-P3. Pre-registered: PREDICTIONS_round6_2026-11-22.md
exec(open('t11_lib.py').read())
G=zeros_to(600); s=0.5+1j*G; ND=100
wsp=np.abs(1+2**(-s)+3**(-s))**2; wfk=np.abs(1+2.37**(-s)+3.71**(-s))**2
U=(('ln2',np.log(2)),('ln3',np.log(3)),('ln3/2',np.log(1.5)))
ok1=ok2=True
for nm,w in (('P1 sparse',wsp),('P2 fake sparse',wfk)):
    for un,u0 in U:
        r=np.random.default_rng(20261122); v=Dpeak(G,w,u0); q=np.quantile([Dpeak(G,r.permutation(w),u0) for _ in range(ND)],0.95)
        if nm.startswith('P1'): ok1&=v>q
        else: ok2&=v<=q
        print(f"{nm} {un}: {v:.2f} vs null95 {q:.2f}",flush=True)
print("P1",'PASS' if ok1 else 'FAIL',"; P2",'PASS' if ok2 else 'FAIL')
ns=list(range(2,31)); J=op_jumps(G,(1-G/600)/(0.5+1j*G),ns); pp=[n for n in ns if lam(n)>0]
neg=sum(J[ns.index(n)]<0 for n in pp); ratio=np.median([abs(J[ns.index(n)]) for n in pp])/np.median([abs(J[ns.index(n)]) for n in ns if lam(n)==0])
print(f"P3 pipeline 1/rho: {neg}/{len(pp)} prime-power jumps negative, ratio {ratio:.2f}",'PASS' if neg==len(pp) and ratio>3 else 'FAIL')
