import numpy as np
exec(open('ade_ladder.py').read().split("for name,gens in groups.items():")[0])
# rebuild 2I characters (copy of ade_ladder internals, 2I only)
src=open('ade_ladder.py').read().split("for name,gens in groups.items():")[1]
src=src.replace("    print('A2","    pass #").replace("        name,n,k","        #")
gens=groups['2I']; name='2I'
exec("if True:\n"+src.split("    # arm lengths")[0])
order_of=lambda M: next(m for m in range(1,121) if np.allclose(np.linalg.matrix_power(M,m),np.eye(2)))
cls_ord=[order_of(G[c[0]]) for c in cls]
chars=np.array(chars)
# label irreps by dim; identify the pairs by value on an order-5 class
dims=[int(round(np.real(c[e]))) for c in chars]
# Galois swap = power map g -> g^2 on classes (sends zeta5 -> zeta5^2, sqrt5 -> -sqrt5)
sq=[cid[idx[key(G[c[0]]@G[c[0]])]] for c in cls]
p2=[cid[idx[key(np.linalg.matrix_power(G[c[0]],2))]] for c in cls]
# better: Galois via g -> g^3 which is a bijection on classes of order dividing 10 for coprime power
p3=[cid[idx[key(np.linalg.matrix_power(G[c[0]],7))]] for c in cls]
swap={}
for i,c in enumerate(chars):
    cg=c[p3]
    j=[jj for jj,d in enumerate(chars) if np.allclose(d,cg,atol=1e-8)][0]; swap[i]=j
lab={}
for i,d in enumerate(dims):
    lab[i]=str(d)
for i,j in swap.items():
    if j!=i and dims[i]==dims[j] and lab[j]==str(dims[j]) and i<j: lab[j]=str(dims[j])+"'"
two=[i for i in range(len(dims)) if lab[i]=='2'][0]; twop=[i for i in range(len(dims)) if lab[i]=="2'"][0]
def mckay(v):
    return np.round([[np.real(np.sum(sizes*chars[v]*chars[i]*np.conj(chars[j]))/n) for j in range(k)] for i in range(k)]).astype(int)
A2=mckay(two); A2p=mckay(twop)
P=np.zeros((k,k),int)
for i,j in swap.items(): P[j,i]=1
print('M1 Galois swap on irreps:',{lab[i]:lab[j] for i,j in swap.items()})
print('   graph(tensor 2\') == swap(graph(tensor 2)):',np.array_equal(A2p,P@A2@P.T),'| both have Perron eigenvalue 2 and degree sequence',sorted(A2.sum(1))==sorted(A2p.sum(1)))
