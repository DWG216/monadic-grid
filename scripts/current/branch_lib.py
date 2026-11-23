src=open('qc_frozen_fluid.py').read(); exec(src[src.index('def mul'):src.index('def image')])
import cmath, math
def gens(r):
    t=cmath.exp(2j*math.pi/r); g=[((-t,1),(0,1)),((1,0),(t,-t))]; out=list(g)
    for A in g:
        det=A[0][0]*A[1][1]-A[0][1]*A[1][0]; out.append(((A[1][1]/det,-A[0][1]/det),(-A[1][0]/det,A[0][0]/det)))
    return out
def branches(r,L):
    """distinct projective states reachable by histories (words) of length <= l, l = 0..L; and words counted"""
    G=gens(r); I=((1,0),(0,1)); seen={key(I)}; frontier=[I]; counts=[1]
    for l in range(1,L+1):
        nf=[]
        for A in frontier:
            for g in G:
                B=mul(A,g); k=key(B)
                if k not in seen: seen.add(k); nf.append(B)
        frontier=nf; counts.append(len(seen))
    words=[sum(4*3**(j-1) if j else 1 for j in range(l+1)) for l in range(L+1)]   # reduced words of length <= l
    return counts, words
