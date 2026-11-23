import itertools as it
def preserves(f,ar,R):
    for rows in it.product(R,repeat=ar):
        if tuple(f[tuple(r[i] for r in rows)] for i in range(len(rows[0]))) not in R: return False
    return True
def ops(ar):
    keys=list(it.product((0,1),repeat=ar))
    for vals in it.product((0,1),repeat=len(keys)): yield dict(zip(keys,vals)),vals
def pols(Rs,ar): return [v for f,v in ops(ar) if all(preserves(f,ar,R) for R in Rs)]
cube=list(it.product((0,1),repeat=3))
SAT3=[set(t for t in cube if any(t[i]!=s[i] for i in range(3))) for s in cube]   # clause forbidding one assignment s
TWO=[set(t for t in it.product((0,1),repeat=2) if t!=s) for s in it.product((0,1),repeat=2)]
XOR=[set(t for t in cube if sum(t)%2==b) for b in (0,1)]
HORN=[set(t for t in cube if not(t[0] and t[1]) or t[2]), {(0,),}, {(1,)}]
DHORN=[set(t for t in cube if (t[0] or t[1]) or not t[2]), {(0,)}, {(1,)}]
proj2=[tuple(k[i] for k in it.product((0,1),repeat=2)) for i in range(2)]
proj3=[tuple(k[i] for k in it.product((0,1),repeat=3)) for i in range(3)]
p2=pols(SAT3,2); p3=pols(SAT3,3)
print("Q1 3-SAT polymorphisms: binary",len(p2),"(projections:",sorted(p2)==sorted(proj2),") ternary",len(p3),"(projections:",sorted(p3)==sorted(proj3),")")
K3=list(it.product((0,1),repeat=3)); K2=list(it.product((0,1),repeat=2))
maj={k:int(sum(k)>=2) for k in K3}; mino={k:sum(k)%2 for k in K3}; AND={k:k[0]&k[1] for k in K2}; OR={k:k[0]|k[1] for k in K2}
c0={k:0 for k in K2}; c1={k:1 for k in K2}
ZERO=[set(t for t in cube if not all(t)) | {(0,0,0)}]   # a 0-valid relation example
for name,f,ar,Rs in (("2-SAT majority",maj,3,TWO),("3-XOR minority",mino,3,XOR),("Horn AND",AND,2,HORN),("dual Horn OR",OR,2,DHORN),("0-valid const 0",c0,2,[r for r in SAT3 if (0,0,0) in r]),("1-valid const 1",c1,2,[r for r in SAT3 if (1,1,1) in r])):
    print(f"Q2 {name}: preserves its class {all(preserves(f,ar,R) for R in Rs)}; Q3 preserves 3-SAT {all(preserves(f,ar,R) for R in SAT3)}")
