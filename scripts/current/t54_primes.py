from collections import Counter
def run(p):
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
    def order(M):
        X=M;k=1
        while X!=I: X=mul(X,M);k+=1
        return k
    def inv(M):
        X=M
        while mul(X,M)!=I: X=mul(X,M)
        return X
    def classes(G):
        G=list(G); seen=set(); c=0
        for g in G:
            if g in seen: continue
            c+=1
            for h in G: seen.add(mul(mul(h,g),inv(h)))
        return c
    Q=((0,1),(1,1)); U=((1,1),(0,1)); Q2=mul(Q,Q)
    G=gen([Q2,U]); return G,classes(G),dict(sorted(Counter(order(g) for g in G).items())),len(gen([Q2])),gen,mul,classes
for p in [2,3,5]:
    G,c,o,cyc,gen,mul,classes=run(p)
    irr=all((x*x-x-1)%p for x in range(p))
    print(f'p={p}: x^2-x-1 irreducible: {irr}; |<Q^2,U>|={len(G)}; classes={c}; element orders={o}; |<Q^2>|={cyc}')
    if p==3:
        Q=((0,1),(1,1)); s=((1,1),(0,2)); G2=gen([Q,s])
        det=lambda M:(M[0][0]*M[1][1]-M[0][1]*M[1][0])%3
        Q8=[g for g in G2 if det(g)==1]; print('   Q8 classes:',classes(Q8))
F=[0,1]
for i in range(300): F.append(F[-1]+F[-2])
print('P2 F(n) = n*3^(n-1) mod 5 for n=1..200:',all(F[n]%5==(n*pow(3,n-1,5))%5 for n in range(1,201)))
print('double root mod 5:',[x for x in range(5) if (x*x-x-1)%5==0])
