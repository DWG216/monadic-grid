import itertools, numpy as np
exec(open('da5.py').read().split('# Q2')[0])          # A5 group, classes, cyc, conj
C5=[c for c in cls if len(c)==12 and cyc(next(iter(c)))==(5,)][0]
cls5=[c for c in cls if len(c)==12]; A,B=cls5[0],cls5[1]
def chiA5(name,g):
    t=cyc(g)
    if t==(1,1,1,1,1): return {'1':1,'3':3,"3'":3,'4':4,'5':5}[name]
    if t==(2,2,1): return {'1':1,'3':-1,"3'":-1,'4':0,'5':1}[name]
    if t==(3,1,1): return {'1':1,'3':0,"3'":0,'4':1,'5':-1}[name]
    if name=='3': return phi if g in A else 1-phi
    if name=="3'": return 1-phi if g in A else phi
    return {'1':1,'4':-1,'5':0}[name]
def M2(a,b):
    n=np.hypot(a,b); a,b=a/n,b/n; x,z=2*a*b,a*a-b*b
    return -np.log2((1+x**4+z**4)/2),(x,z)
def run(Gr,cls_set,chi,names,label):
    Cl=sorted(cls_set); ci={h:i for i,h in enumerate(Cl)}; n=len(Cl)
    def pm(g):
        M=np.zeros((n,n))
        for h in Cl: M[ci[conj(g,h)],ci[h]]=1
        return M
    best=0; out=[]
    for name,d in names:
        P=sum(chi(name,g)*pm(g) for g in Gr)*d/len(Gr); v=P[:,0]; pout=v[0]
        if pout<1e-12: print('  %s charge %-2s: probability 0'%(label,name)); continue
        rows={}
        for y in range(1,n):
            m,(x,z)=M2(v[0],v[y]); key=(round(v[y]/v[0],6))
            rows.setdefault(key,[0,m,(round(x,4),round(z,4)),v[0]**2+v[y]**2]); rows[key][0]+=1
        print('  %s charge %-2s: P=%.4f'%(label,name,pout))
        for k,(cnt,m,bl,pj) in sorted(rows.items()):
            print('     ratio %+.6f x%-2d Bloch(x,z)=%s M2=%.4f joint p=%.4f'%(k,cnt,bl,m,pj))
            if m>1e-9: best+=0  # tallied below
        mags=[(pj,m) for k,(cnt,m,bl,pj) in rows.items() if m>1e-9]
        if mags: out.append((name,pout,max(p for p,_ in mags)))
    return out
print('D(A5), pair charge on 5-cycle class (12 states):')
o=run(G,C5,chiA5,[('1',1),('3',3),("3'",3),('4',4),('5',5)],'A5')
y=sum(pj for _,_,pj in o)   # best sort per outcome; joint probabilities add over outcomes
print('  expected magic states per charge measurement: %.4f -> %.2f measurements per magic state'%(y,1/y))
print('  break-even Mochon overhead vs tau60 (1.9e5 raw/rotation @1e-10): %.3g magic states per rotation'%(1.9e5*y))
# Control C1: A4 on one class of 3-cycles
G4=[g for g in G if g[4]==4]
c3=[g for g in G4 if cyc(g)==(3,1,1)]; c0=c3[0]; cl4=frozenset(conj(h,c0) for h in G4)
def chiA4(name,g):
    t=cyc(g); return {'1':1,'3':{(1,1,1,1,1):3,(2,2,1):-1}.get(t,0)}[name]
print('Control C1, D(A4), 3-cycle class (%d states):'%len(cl4)); run(G4,cl4,chiA4,[('1',1),('3',3)],'A4')
print('Control C2 (flux measurement): states |0>,|1> only, M2 =',M2(1,0)[0],M2(0,1)[0])
