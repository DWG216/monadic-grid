import numpy as np
L=3; nq=2*L*L
def h(x,y): return (x%L)+L*(y%L)          # horizontal edge from (x,y) to (x+1,y)
def v(x,y): return L*L+(x%L)+L*(y%L)      # vertical edge from (x,y) to (x,y+1)
def star(x,y): return [h(x,y),h(x-1,y),v(x,y),v(x,y-1)]
def plaq(x,y): return [h(x,y),h(x,y+1),v(x,y),v(x+1,y)]   # plaquette with lower-left corner (x,y)
idx=np.arange(2**nq,dtype=np.int64)
def mask(qs):
    m=0
    for q in qs: m^=(1<<q)
    return m
def applyX(psi,qs): return psi[idx^mask(qs)]
def applyZ(psi,qs):
    m=mask(qs); par=np.zeros_like(idx)
    t=idx&m
    while t.any(): par^=(t&1); t>>=1
    return psi*(1-2*par)
def pauli(psi,X=(),Z=()):  # apply Z first then X (operator X..Z.. acting: we use fixed order consistently)
    return applyX(applyZ(psi,list(Z)),list(X))
psi=np.zeros(2**nq); psi[0]=1.0
for x in range(L):
    for y in range(L):
        psi=(psi+applyX(psi,star(x,y)))/2
psi/=np.linalg.norm(psi)
res={}
res['F0 max |<A_v>-1|, |<B_p>-1|']=(max(abs(psi@applyX(psi,star(x,y))-1) for x in range(L) for y in range(L)),
                                    max(abs(psi@applyZ(psi,plaq(x,y))-1) for x in range(L) for y in range(L)))
# F1: m pair by X on vertical edge v(1,1) -> flips plaquettes (0,1) and (1,1)
pm=applyX(psi,[v(1,1)])
loop=plaq(1,1)
res['F1 Z-loop with m inside']=float(pm@applyZ(pm,loop)); res['F1 Z-loop without']=float(psi@applyZ(psi,loop))
# F2 T-junction around centre vertex (1,1), eps = e at vertex + m at plaquette NE of vertex
x0,y0=1,1
hops={'e':[((),[h(x0-1,y0)]),((),[h(x0,y0)]),((),[v(x0,y0)])],
      'm':[([v(x0,y0)],()),([v(x0+1,y0)],()),([h(x0,y0+1)],())],
      'eps':[([v(x0,y0)],[h(x0-1,y0)]),([v(x0+1,y0)],[h(x0,y0)]),([h(x0,y0+1)],[v(x0,y0)])]}
for name,(t1,t2,t3) in hops.items():
    # start from a state with the particle present on leg 1 end (create by a string from far away): use psi with an excitation
    start=pauli(psi,X=t1[0],Z=t1[1])  # any state works for the operator identity; use an excited state
    A=pauli(pauli(pauli(start,*t2),*t3),*t1)   # t1 t3 t2 |start>
    B=pauli(pauli(pauli(start,*t1),*t3),*t2)   # t2 t3 t1 |start>
    res['F2 overlap '+name]=float(np.vdot(A,B).real/np.linalg.norm(A)/np.linalg.norm(B))
rng=np.random.default_rng(0); sg=[]
for _ in range(20):
    ts=[(list(rng.choice(nq,2,replace=False)),list(rng.choice(nq,2,replace=False))) for _ in range(3)]
    A=pauli(pauli(pauli(psi,*ts[1]),*ts[2]),*ts[0]); B=pauli(pauli(pauli(psi,*ts[0]),*ts[2]),*ts[1])
    sg.append(round(float(np.vdot(A,B).real),3))
res['F3 null random overlaps']=sg
for k,val in res.items(): print(k,val)
