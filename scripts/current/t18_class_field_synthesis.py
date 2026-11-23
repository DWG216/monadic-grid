from fractions import Fraction as F
# element: (a,b,c,d) = a + b s + i(c + d s), s = sqrt5, s^2=5
def m(x,y):
    a,b,c,d=x; e,f,g,h=y
    re=(a*e+5*b*f)-(c*g+5*d*h); res=(a*f+b*e)-(c*h+d*g)
    im=(a*g+5*b*h)+(c*e+5*d*f); ims=(a*h+b*g)+(c*f+d*e)
    return (re,res,im,ims)
def conj_s(x): a,b,c,d=x; return (a,-b,c,-d)
def conj_i(x): a,b,c,d=x; return (a,b,-c,-d)
half=F(1,2)
phi=(half,half,0,0); phim1=(-half,half,0,0)
alpha=(half,half,-half,half); beta=(half,half,half,-half)
one_p_i=(1,0,1,0); one_m_i=(1,0,-1,0)
sqrtm5=(0,0,0,1)  # i*sqrt5
r={}
r['H1 1+sqrt-5=(1+i)alpha']= m(one_p_i,alpha)==(1,0,0,1)
r['H1 1-sqrt-5=(1-i)beta']= m(one_m_i,beta)==(1,0,0,-1)
r['H1 2=(1+i)(1-i)']= m(one_p_i,one_m_i)==(2,0,0,0)
r['H1 3=alpha*beta']= m(alpha,beta)==(3,0,0,0)
def norm(x):
    p=x
    for y in (conj_s(x),conj_i(x),conj_i(conj_s(x))): p=m(p,y)
    return p
def charpoly(x):
    # product of (T - conjugates): coefficients via elementary symmetric functions
    cs=[x,conj_s(x),conj_i(x),conj_i(conj_s(x))]
    poly=[(1,0,0,0)]
    for c in cs:
        new=[(0,0,0,0)]*(len(poly)+1)
        for k,a in enumerate(poly):
            new[k]=tuple(p+q for p,q in zip(new[k],a))
            t=m(a,tuple(-v for v in c))
            new[k+1]=tuple(p+q for p,q in zip(new[k+1],t))
        poly=new
    return poly
for name,x in [('alpha',alpha),('beta',beta),('1+i',one_p_i),('1-i',one_m_i)]:
    cp=charpoly(x)
    rational=all(c[1]==0 and c[2]==0 and c[3]==0 for c in cp)
    integral=rational and all(c[0].denominator==1 if isinstance(c[0],F) else True for c in cp)
    n=norm(x)[0]
    r[f'H2 {name} integral, norm']=(integral, n, [c[0] for c in cp])
r['H3 same atoms']= m(m(one_p_i,one_m_i),m(alpha,beta))==m(m(one_p_i,alpha),m(one_m_i,beta))==(6,0,0,0)
alpha_bad=(half,-half,-(-half-half)+0,0)  # phi->phibar: phibar + i(phibar-1)
alpha_bad=(half,-half,-half,-half)
r['C1 conj phi fails']= m(one_p_i,alpha_bad)!=(1,0,0,1)
for k,v in r.items(): print(k,v)
