# Calculation 2: one-layer network of perfect tensors on a {5,4} patch (centre pentagon + 5 neighbours, 20 boundary qubits)
import numpy as np, itertools
exec(open('holenmer.py').read().split('# --- B2')[0])
T=T/np.linalg.norm(T)
def S_bits(psi,A,n):
    B=[k for k in range(n) if k not in A]
    M=np.transpose(psi.reshape([2]*n),list(A)+B).reshape(2**len(A),-1)
    s=np.linalg.svd(M,compute_uv=False)**2; s=s[s>1e-14]; return float(-(s*np.log2(s)).sum())
def build(bond=None,ref=False):
    # bond: 2x2 matrix inserted on the centre-neighbour-1 link (deformation of that link)
    C=T if ref else T[0]                       # centre: bulk leg kept as reference qubit, or fixed to |0>
    psi=C
    off=1 if ref else 0
    for k in range(5):
        N=T[0]                                  # neighbour: bulk leg fixed to |0>; legs: (link, b1..b4)
        if k==0 and bond is not None: N=np.tensordot(bond,N,axes=([1],[0]))
        psi=np.tensordot(psi,N,axes=([off],[0]))  # contract the next link leg (always at position off)
    psi=psi.reshape(-1); return psi/np.linalg.norm(psi)
n=20; psi=build()
def mincut(A,bond_cost=1.0):
    best=1e9
    for side in itertools.product([0,1],repeat=6):   # side[0]=centre, side[1..5]=neighbours; 1 = grouped with A
        c=0
        for k in range(5):
            if side[0]!=side[k+1]: c+= bond_cost if k==0 else 1
            for j in range(4):
                q=4*k+j; c+= (q in A)!=(side[k+1]==1)
        best=min(best,c)
    return best
print('Contiguous boundary arcs: entropy vs minimal cut through the network (Ryu-Takayanagi)')
for L in range(1,11):
    A=list(range(L)); print('  arc of %2d qubits: S = %.3f bits   min-cut = %d'%(L,S_bits(psi,A,n),mincut(A)))
print('Same size, different shape (10 qubits):')
for name,A in [('one arc',list(range(10))),('every other qubit',list(range(0,20,2))),('two arcs of 5',list(range(5))+list(range(10,15)))]:
    print('  %-18s S = %.3f   min-cut = %d'%(name,S_bits(psi,A,n),mincut(A)))
# holenmerism: where does the centre's bulk qubit live on the boundary?
pr=build(ref=True); m=21
print('Centre bulk qubit R vs boundary region A: mutual information I(R:A) (2 = fully recoverable from A)')
for L in [4,8,10,12,16]:
    A=[q+1 for q in range(L)]; I=S_bits(pr,[0],m)+S_bits(pr,A,m)-S_bits(pr,[0]+A,m)
    print('  arc of %2d of 20: I = %.3f'%(L,I))
Asc=[q+1 for q in range(0,20,2)]; print('  every other qubit (10): I = %.3f'%(S_bits(pr,[0],m)+S_bits(pr,Asc,m)-S_bits(pr,[0]+Asc,m)))
# deformation: weaken ONE link (centre-neighbour 1) from maximal entanglement toward a product
print('Deforming one link (theta: pi/4 = undeformed). Change in S for regions whose cut does / does not cross it')
for th in [np.pi/4,0.6,0.4,0.2]:
    bond=np.diag([np.cos(th),np.sin(th)])*np.sqrt(2); p=build(bond)
    lam=np.array([np.cos(th)**2,np.sin(th)**2]); h=float(-(lam*np.log2(lam)).sum())
    out=[]
    for A in [list(range(4)),list(range(4,8)),list(range(12)),list(range(4,16))]:
        out.append(S_bits(p,A,n)-S_bits(psi,A,n))
    print('  theta=%.2f link entropy=%.3f | dS: nbr-1 tile %.3f, nbr-2 tile %.3f, arc incl. nbr1 (12) %.3f, arc excl. nbr1 (12) %.3f'%(th,h,*out))
