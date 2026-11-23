import itertools, numpy as np
p=3
def mul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%p for j in range(2)) for i in range(2))
def gen(gs):
    I=((1,0),(0,1)); G={I}; fr=[I]
    while fr:
        n=[]
        for g in fr:
            for h in gs:
                x=mul(g,h)
                if x not in G: G.add(x); n.append(x)
        fr=n
    return G
det=lambda M:(M[0][0]*M[1][1]-M[0][1]*M[1][0])%p
def order(M):
    I=((1,0),(0,1)); X=M; k=1
    while X!=I: X=mul(X,M); k+=1
    return k
Q=((0,1),(1,1)); s=((1,1),(0,2)); U=((1,1),(0,1)); Q2=mul(Q,Q)
print('irreducible x^2-x-1 mod 3:',all((x*x-x-1)%3 for x in range(3)))
G1=gen([Q]); G2=gen([Q,s]); S2=[g for g in G2 if det(g)==1]; G3=gen([Q2,U]); G4=gen([Q,U])
print('G1',len(G1),' G2',len(G2),' G2 in SL',len(S2),' orders there',sorted(order(g) for g in S2))
print('G3',len(G3),' all det 1:',all(det(g)==1 for g in G3),' G4',len(G4))
print('affine orders: 9*|G1|=',9*len(G1),' 9*|G3|=',9*len(G3),' 9*|G4|=',9*len(G4))
print('order of s:',order(s),' det s:',det(s),'  s Q s^-1 = Q^3 (Frobenius):',mul(mul(s,Q),s)==mul(Q2,Q))
ctrl=gen([Q2,mul(s,Q)]); print('control <Q^2, sQ>:',len(ctrl))
# 24-cell link: SL(2,3) ~ binary tetrahedral; element orders
from collections import Counter
print('element orders in G3:',dict(Counter(order(g) for g in G3)))
