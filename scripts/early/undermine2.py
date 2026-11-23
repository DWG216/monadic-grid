exec(open('undermine.py').read().split('hits=[]')[0])
def braid4(k,j):
    qn,adm,F,R=mk(k)
    trees=[(e1,e2,Y) for e1 in range(2*k+1) for e2 in range(2*k+1) for Y in range(2*k+1) if adm(j,j,e1) and adm(e1,j,e2) and adm(e2,j,Y)]
    ix={t:i for i,t in enumerate(trees)}; N=len(trees)
    s1=np.diag([R(j,t[0]) for t in trees]).astype(complex)
    s2=np.zeros((N,N),complex); s3=np.zeros((N,N),complex)
    for (e1,e2,Y) in trees:
        # sigma2 on strands 2,3 inside ((j j)e1 j)e2: F^{j j j}_{e2}
        E,Fs,M=F(j,j,j,e2)
        for e1b in E:
            amp=sum(M[E.index(e1),Fs.index(f)]*R(j,f)*M[E.index(e1b),Fs.index(f)] for f in Fs)
            s2[ix[(e1b,e2,Y)],ix[(e1,e2,Y)]]+=amp
        E,Fs,M=F(e1,j,j,Y)
        for e2b in E:
            amp=sum(M[E.index(e2),Fs.index(f)]*R(j,f)*M[E.index(e2b),Fs.index(f)] for f in Fs)
            s3[ix[(e1,e2b,Y)],ix[(e1,e2,Y)]]+=amp
    return [s1,s2,s3]
k,j=6,2
g=braid4(k,j); I=np.eye(len(g[0]))
print('U2 SU(2)_6 spin-1, 4 strands: dim',len(I),'| unitarity',max(np.linalg.norm(x@x.conj().T-I) for x in g),
      '| s1s2s1-s2s1s2 %.1e | s2s3s2-s3s2s3 %.1e | s1s3-s3s1 %.1e'%(np.linalg.norm(g[0]@g[1]@g[0]-g[1]@g[0]@g[1]),np.linalg.norm(g[1]@g[2]@g[1]-g[2]@g[1]@g[2]),np.linalg.norm(g[0]@g[2]-g[2]@g[0])))
def scan(gs,L=6):
    for l in range(1,L+1):
        for w in itertools.product(range(len(gs)),repeat=l):
            U=np.eye(len(gs[0]),dtype=complex)
            for i in w: U=gs[i]@U
            ev=np.linalg.eigvals(U)
            for x in ev[1:]:
                if order(x/ev[0],500) is None: return 'INFINITE-ORDER word '+''.join('s%d'%(i+1) for i in w)
    return 'all words <=%d finite order'%L
print('   3-strand part <s1,s2>:',scan(g[:2]),'| full <s1,s2,s3>:',scan(g))
