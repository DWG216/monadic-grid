import itertools, cmath
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
def order(M):
    X=M;k=1
    while X!=I: X=mul(X,M);k+=1
    return k
Q=((0,1),(1,1)); U=((1,1),(0,1)); Q2=mul(Q,Q)
G=sorted(gen([Q2,U]))
# w: SL(2,3) -> Z3 via abelianization; build as homomorphism by BFS from generators: w(U)=1 (exponent), w(Q2)=?
comm=gen([mul(mul(a,b),mul(inv(a),inv(b))) for a in G for b in G])   # commutator subgroup (Q8)
cos=[]
for g in G:
    if not any(g in c for c in cos): cos.append({mul(g,k) for k in comm})
idxU=[i for i,c in enumerate(cos) if U in c][0]; idxI=[i for i,c in enumerate(cos) if I in c][0]
w={}
for g in G:
    c=[i for i,cc in enumerate(cos) if g in cc][0]
    # exponent: g in coset U^e comm
    for e in range(3):
        Ue=I
        for _ in range(e): Ue=mul(Ue,U)
        if mul(inv(Ue),g) in comm: w[g]=e
W=cmath.exp(2j*cmath.pi/3)
res={}
o3=[g for g in G if order(g)==3]
cls=[]
for g in o3:
    if not any(g in c for c in cls): cls.append({mul(mul(h,g),inv(h)) for h in G})
res['C1']=(len(o3),[len(c) for c in cls], any(U in c and inv(U) not in c for c in cls), sorted({w[g] for g in cls[0]}),sorted({w[g] for g in cls[1]}))
ad=lambda X,g: mul(mul(X,g),inv(X))
res['C2']=(all(w[ad(Q,g)]==(2*w[g])%3 for g in G), all(w[ad(Q2,g)]==w[g] for g in G))
Qi=inv(Q); res['C3']=all(w[ad(Qi,g)]==(2*w[g])%3 for g in G)
res['C4']=abs((W**1).conjugate()-W**2)<1e-12
res['C5']=all((W**w[ad(Q,g)]).conjugate()==W**w[g] or abs((W**w[ad(Q,g)]).conjugate()-W**w[g])<1e-12 for g in G)
for k,v in res.items(): print(k,v)
