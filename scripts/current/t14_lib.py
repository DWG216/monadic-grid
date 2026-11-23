# Step 5 library: the pairing measure (Karchmer-Wigderson game on a slice, spectral Khrapchenko bound).
exec(open('t13_lib.py').read()); from scipy.sparse.linalg import svds
def pairing(f,A,pts):
    """K(f) = B^2 / (sigma^2 |X||Y|): lower bound on the leaves of any monotone formula separating yes from no on the slice.
    B = yes/no pairs one swap apart; sigma = top singular value of the pairs whose swapped-out edge is edge 0 (all edges equivalent for graph properties)."""
    f=np.asarray(f); X=np.where(f==1)[0]; Y=np.where(f==0)[0]
    N=A[X][:,Y]; B=N.sum()
    x0=np.array([pts[i]&1 for i in X],dtype=float); y0=np.array([1-(pts[i]&1) for i in Y],dtype=float)
    N0=sp.diags(x0)@N@sp.diags(y0)
    if N0.nnz==0: return 0.0,B,0.0
    sig=svds(N0.asfptype(),k=1,return_singular_vectors=False)[0] if min(N0.shape)>2 else np.linalg.svd(N0.toarray(),compute_uv=False)[0]
    return float(B*B/(sig*sig*len(X)*len(Y))),float(B),float(sig)
