import itertools, networkx as nx
E=[(1,2),(1,3),(1,6),(2,3),(2,4),(2,6),(3,5),(3,6),(4,5),(4,6),(4,7),(5,6),(5,8),(6,7),(6,8),(6,9),(7,8),(7,9),(7,10),(8,9),(8,10),(9,10)]
G=nx.Graph(E); print("nodes",G.number_of_nodes(),"edges",G.number_of_edges())
GM=nx.algorithms.isomorphism.GraphMatcher(G,G); auts=list(GM.isomorphisms_iter())
print("K1 |Aut| =",len(auts)); 
for a in auts:
    if any(a[k]!=k for k in a): print("   non-trivial:",{k:v for k,v in a.items() if k!=v},"fixed:",sorted(k for k in a if a[k]==k))
deg=dict(G.degree()); print("K2 degrees",deg)
short=[p for p in nx.all_simple_paths(G,1,10,cutoff=3)]
print("K2 paths 1->10 of length<=3:",len(short),"all through 6:",all(6 in p for p in short), short)
pl,_=nx.check_planarity(G); print("K3 planar:",pl, "faces:",22-10+2 if pl else None)
S={3,4,5,6,7,8,9,12,13,20,24,28,52,60,91,108,120,216,364}
f=len([n for n in range(1,31) if n in S])/30; print(f"K4 null fraction {f:.3f}, triple-hit prob {f**3:.3f}")
