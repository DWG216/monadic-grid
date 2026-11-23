import numpy as np, itertools, cmath, math
# --- B1: the 5-qubit code as a perfect tensor ("the whole in every part") ---
I=np.eye(2);X=np.array([[0,1],[1,0]]);Z=np.diag([1,-1])
def kron(*m):
    r=np.array([[1.]])
    for a in m: r=np.kron(r,a)
    return r
P={'I':I,'X':X,'Z':Z}
stabs=[kron(*[P[c] for c in s]) for s in ['XZZXI','IXZZX','XIXZZ','ZXIXZ']]
proj=np.eye(32)
for S in stabs: proj=proj@(np.eye(32)+S)/2
vals,vecs=np.linalg.eigh(proj); code=vecs[:,vals>0.5]           # 2-dim code space
L0,L1=code[:,0],code[:,1]
T=np.stack([L0,L1]).reshape(2,2,2,2,2,2)                        # 6 legs: logical + 5 physical
perfect=True
for A in itertools.combinations(range(6),3):
    B=[k for k in range(6) if k not in A]
    M=np.transpose(T,list(A)+B).reshape(8,8)
    U=M/np.sqrt(np.trace(M.conj().T@M).real/8)
    perfect&=np.allclose(U.conj().T@U,np.eye(8),atol=1e-9)
print('5-qubit code tensor (6 legs) is perfect: every 3 legs map unitarily to the other 3 ->',perfect)
# --- B2: count tiles layer by layer in hyperbolic {p,3} tilings (Poincare disk) ---
def tiling_layers(p,q,layers):
    rv=math.sqrt(math.cos(math.pi/p+math.pi/q)/math.cos(math.pi/p-math.pi/q))
    V0=[rv*cmath.exp(2j*math.pi*k/p) for k in range(p)]
    def reflect(z,a,b):
        # circle orthogonal to unit circle through a,b:  |a|^2 - 2 Re(a conj c) + 1 = 0 (same for b)
        M=np.array([[2*a.real,2*a.imag],[2*b.real,2*b.imag]]); rhs=np.array([abs(a)**2+1,abs(b)**2+1])
        cx,cy=np.linalg.solve(M,rhs); c=complex(cx,cy); R2=abs(c)**2-1
        return c+R2/np.conj(z-c)
    key=lambda poly: (round(np.mean(poly).real,7),round(np.mean(poly).imag,7))
    seen={key(V0)}; frontier=[V0]; counts=[1]
    for _ in range(layers):
        new=[]
        for poly in frontier:
            for k in range(p):
                a,b=poly[k],poly[(k+1)%p]
                img=[reflect(z,a,b) for z in poly]
                kk=key(img)
                if kk not in seen: seen.add(kk); new.append(img)
        counts.append(len(new)); frontier=new
    return counts
c73=tiling_layers(7,3,5); c54=tiling_layers(5,4,4)
F=[0,1]
for _ in range(20): F.append(F[-1]+F[-2])
print('{7,3} heptagon tiling, tiles per layer:',c73,' vs 7*F(2n):',[1]+[7*F[2*n] for n in range(1,6)])
print('   growth ratios:',[round(c73[k+1]/c73[k],4) for k in range(1,len(c73)-1)],' phi^2 =',round(((1+5**.5)/2)**2,4))
print('{5,4} pentagon tiling (HaPPY code), tiles per layer:',c54,' ratios',[round(c54[k+1]/c54[k],3) for k in range(1,len(c54)-1)],' 2+sqrt3 =',round(2+3**.5,3))
