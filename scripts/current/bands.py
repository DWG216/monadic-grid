import itertools as it, random
rnd=random.Random(20261122)
def rand_circuit(n,s,t):
    gates=[]; nots=sorted(rnd.sample(range(3,s-1),t))
    for g in range(s):
        pool=n+g
        if g in nots: gates.append(('N',rnd.randrange(pool)))
        else: gates.append((rnd.choice('AO'),rnd.randrange(pool),rnd.randrange(pool)))
    return gates
def run(gates,n,x,force=None):
    v=[(x>>i)&1 for i in range(n)]; ys=[]; ins=[]; k=0
    for g in gates:
        if g[0]=='N':
            ins.append(v[g[1]]); o=(1-v[g[1]]) if force is None else force[k]; ys.append(o); v.append(o); k+=1
        else: v.append(v[g[1]]&v[g[2]] if g[0]=='A' else v[g[1]]|v[g[2]])
    return v[-1],tuple(ys),ins
def mono(tab,n): return all(tab[x]<=tab[x|(1<<i)] for x in range(1<<n) for i in range(n))
n=6; N=1<<n; ok=True; cells_hist={}
for trial in range(2000):
    t=1+trial%4; C=rand_circuit(n,30,t)
    f=[];Y=[]
    for x in range(N): o,y,_=run(C,n,x); f.append(o); Y.append(y)
    cells={}
    for x in range(N): cells.setdefault(Y[x],[]).append(x)
    cells_hist.setdefault(t,[]).append(len(cells)); ok&=len(cells)<=2**t
    recon=[0]*N
    for b,S in cells.items():
        Sset=set(S)
        # convex
        for x in S:
            for z in S:
                if x&z==x and x!=z:
                    d=z^x; w=x
                    sub=d
                    while True:
                        if (x|sub) not in Sset: ok=False
                        if sub==0: break
                        sub=(sub-1)&d
        G=[run(C,n,x,force=b) for x in range(N)]
        U=[int(all(G[x][2][i] for i in range(t) if b[i]==0)) for x in range(N)]
        V=[int(any(G[x][2][i] for i in range(t) if b[i]==1)) for x in range(N)]
        H=[G[x][0] for x in range(N)]
        ok&=mono(U,n) and mono(V,n) and mono(H,n)
        ok&=all((U[x] and not V[x])==(x in Sset) for x in range(N))
        ok&=all(H[x]==f[x] for x in S)
        for x in range(N): recon[x]|=U[x]&(1-V[x])&H[x]
    ok&=recon==f
print("B1 band lemma on 2000 random circuits:", "PASS" if ok else "FAIL")
print("B4 nonempty cells (mean, max) by t:",{t:(round(sum(v)/len(v),2),max(v),2**t) for t,v in sorted(cells_hist.items())})
# B2
n=8; ok2=all(((x>>i)&1)^1==int(bin(x&~(1<<i)).count('1')>=k) for k in range(n+1) for x in range(1<<n) if bin(x).count('1')==k for i in range(n))
n=7
def rand_dm(n,s):
    return [(rnd.choice('AO'),rnd.randrange(-n,n+g) ,rnd.randrange(-n,n+g)) for g in range(s)]   # negative index -j-1.. = negated literal j
def ev(D,n,x,k=None):
    def leaf(j):
        if j>=0: return None
        i=-j-1
        return (1-((x>>i)&1)) if k is None else int(bin(x&~(1<<i)).count('1')>=k)
    v=[(x>>i)&1 for i in range(n)]
    for op,a,b in D:
        A=leaf(a) if a<0 else v[a]; B=leaf(b) if b<0 else v[b]; v.append(A&B if op=='A' else A|B)
    return v[-1]
for _ in range(500):
    D=rand_dm(n,25); k=rnd.randrange(1,n)
    tab=[ev(D,n,x,k) for x in range(1<<n)]
    ok2&=mono(tab,n) and all(tab[x]==ev(D,n,x) for x in range(1<<n) if bin(x).count('1')==k)
print("B2 pseudo-complement identity and Berkowitz replacement:", "PASS" if ok2 else "FAIL")
# B3
E=list(it.combinations(range(5),2)); idx={e:i for i,e in enumerate(E)}
def tri(x): return int(any(all((x>>idx[p])&1 for p in it.combinations(T,2)) for T in it.combinations(range(5),3)))
pos=[sum(1<<idx[p] for p in it.combinations(T,2)) for T in it.combinations(range(5),3)]
neg=[]
for r in range(1,3):
    for A in it.combinations(range(5),r): neg.append(sum(1<<idx[(min(a,b),max(a,b))] for a in A for b in range(5) if b not in A))
wp=sorted({bin(x).count('1') for x in pos}); wn=sorted({bin(x).count('1') for x in neg})
by={}
for x in range(1<<10):
    w=bin(x).count('1'); a=by.setdefault(w,[0,0]); a[tri(x)]+=1
print("B3 positive-test weights",wp,"negative-test weights",wn,"shared slices:",sorted(set(wp)&set(wn)),"; all negatives triangle-free:",all(tri(x)==0 for x in neg))
print("B3 graphs by weight [triangle-free, with triangle]:",{w:by[w] for w in sorted(by)})
import json; json.dump({str(w):by[w] for w in by},open('bands_tri.json','w'))
