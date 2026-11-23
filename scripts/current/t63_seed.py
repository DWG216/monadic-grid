from fractions import Fraction as Fr
def mm(A,B,m=None):
    R=[[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    return [[x%m for x in r] for r in R] if m else R
def mv(A,v,m=None):
    r=[A[0][0]*v[0]+A[0][1]*v[1],A[1][0]*v[0]+A[1][1]*v[1]]
    return [x%m for x in r] if m else r
Q=[[0,1],[1,1]]; U=[[1,1],[0,1]]; L=[[1,0],[1,1]]; Ui=[[1,-1],[0,1]]; Li=[[1,0],[-1,1]]
Q2=mm(Q,Q); Qm2=[[2,-1],[-1,1]]
res={}
# S1 uniqueness of unit-diagonal LU: L=[[1,0],[l,1]], U=[[a,b],[0,d]] -> a=M00,b=M01,l=M10/a,d=M11-l*b
def LU(M):
    a=Fr(M[0][0]); b=Fr(M[0][1]); l=Fr(M[1][0])/a; d=Fr(M[1][1])-l*b; return l,(a,b,d)
l,(a,b,d)=LU(Q2); res['S1']=(mm(L,U)==Q2, (l,a,b,d)==(1,1,1,1))
# S2 characters mod 3 (reuse t62 construction)
import itertools
p=3
def mul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%p for j in range(2)) for i in range(2))
I=((1,0),(0,1))
def gen(gs):
    G={I}; fr=[I]
    while fr:
        n=[]
        for g in fr:
            for h in gs:
                x=mul(g,h)
                if x not in G: G.add(x); n.append(x)
        fr=n
    return G
def inv(M):
    X=M
    while mul(X,M)!=I: X=mul(X,M)
    return X
T=lambda A: tuple(tuple(x%3 for x in r) for r in A)
G=sorted(gen([T(Q2),T(U)]))
comm=gen([mul(mul(a_,b_),mul(inv(a_),inv(b_))) for a_ in G for b_ in G])
def w(g):
    for e in range(3):
        Ue=I
        for _ in range(e): Ue=mul(Ue,T(U))
        if mul(inv(Ue),g) in comm: return e
res['S2']=(w(T(U)),w(T(L)),w(T(Q2)))
seed=[0,1]
res['S3']=(mv(L,seed)==seed, mv(Li,seed)==seed, mv(U,seed)!=seed, mv(Ui,seed)!=seed,
           sorted(g for g in G if [ (g[0][0]*0+g[0][1]*1)%3, (g[1][0]*0+g[1][1]*1)%3 ]==[0,1])==sorted(gen([T(L)])))
# S4 first mover in each factorization (rightmost factor acts first)
fwd=[L,U]; bwd=[Ui,Li]
def first_mover(fs):
    for f in reversed(fs):
        if mv(f,seed)!=seed: return f
res['S4']=(first_mover(fwd)==U, w(T(first_mover(fwd))), first_mover(bwd)==Ui, w(T(first_mover(bwd))), mm(Ui,Li)==Qm2, mm(Q2,Qm2)==[[1,0],[0,1]])
l2,_=LU(Qm2); res['S5']=(l2, l2.denominator!=1)
for k,v in res.items(): print(k,v)
