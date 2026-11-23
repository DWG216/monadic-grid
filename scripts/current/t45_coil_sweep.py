import numpy as np
exec(open('t44_sequence_shift.py').read().split('A=wire_seq(0,a)')[0])
A=wire_seq(0,a); Ltot=np.sum(np.linalg.norm(np.diff(A,axis=0),axis=1))
Bs=[wire_seq(k,a+0.0005) for k in range(3)]
fr=np.linspace(0.3,2.0,35)    # wavelength as a fraction of wire length
rows=[]
for x in fr:
    lam=Ltot*x; M=[abs(mutual_c(A,B,lam)) for B in Bs]
    rows.append((x,M[1]/M[0],M[2]/M[0],M[0]))
rows=np.array(rows)
best=rows[np.argmin((rows[:,1]-0.5)**2+(rows[:,2]-0.25)**2)]
print('wire length (m):',round(Ltot,3))
for r in rows[::3]: print(f'lambda/L={r[0]:.2f}  ratios 1 : {r[1]:.3f} : {r[2]:.3f}')
print(f'closest to 1:0.5:0.25 at lambda/L={best[0]:.2f}: 1 : {best[1]:.3f} : {best[2]:.3f}')
# control: same loops, random visiting order
rng=np.random.default_rng(0)
def wire_order(o,aa):
    slots=[9*b+r for b in range(4) for r in o]; pts=[]; prev=None
    for s in slots:
        phi=2*np.pi*(s%S)/S
        if prev is not None:
            d=((phi-prev+np.pi)%(2*np.pi))-np.pi
            pts.append(run(prev,prev+d,aa) if d>=0 else run(prev+d,prev,aa)[::-1])
        pts.append(loop(phi,aa)); prev=phi
    return np.concatenate(pts)
lam=Ltot*best[0]
for t in range(2):
    o=list(rng.permutation(order)); Ac=wire_order(o,a)
    Mc=[abs(mutual_c(Ac,wire_order(o[k:]+o[:k],a+0.0005),lam)) for k in range(3)]
    print('control random order',o,': ratios 1 :',round(Mc[1]/Mc[0],3),':',round(Mc[2]/Mc[0],3))
