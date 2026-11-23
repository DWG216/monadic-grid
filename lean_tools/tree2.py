import re,sys,pickle,os,collections
import os as _o; root=_o.environ.get('R2R_LEAN_SRC','riemann-hypothesis-lean/src')
idx=pickle.load(open(_o.path.join(_o.path.dirname(_o.path.abspath(__file__)),'idx.pkl'),'rb'))
cache={}
def text(f):
    if f not in cache: cache[f]=open(os.path.join(root,f),errors='ignore').read()
    return cache[f]
decl=re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*(theorem|lemma|def|abbrev|structure|class|instance|inductive)\s',re.M)
tok=re.compile(r"[A-Za-z_][\w.'!?₀-₉]*")
openre=re.compile(r'^\s*open\s+([^\n]+)',re.M); nsre=re.compile(r'^\s*namespace\s+(\S+)',re.M)
def ctx(name):
    f,pos,_=idx[name]; t=text(f)[:pos]
    pre=[]; parts=name.split('.')[:-1]
    for i in range(len(parts),0,-1): pre.append('.'.join(parts[:i]))
    for m in nsre.finditer(t): pre.append(m.group(1))
    for m in openre.finditer(t):
        for w in m.group(1).split():
            if w[0].isupper(): pre.append(w)
    return list(dict.fromkeys(pre))
def body(name):
    f,pos,kind=idx[name]; t=text(f)
    m=decl.search(t,pos+1); return t[pos:m.start() if m else len(t)]
def deps(name):
    b=body(name); pre=ctx(name); out=[]
    skip=set(b.split('\n',1)[0].split()[:2])
    for t in tok.findall(b.replace("_root_.","")):
        r=None
        if '.' in t and t in idx: r=t
        else:
            for p in pre:
                c=p+'.'+t
                if c in idx: r=c; break
        if r and r!=name and r not in out: out.append(r)
    return out
if __name__=='__main__':
    seen=set()
    def show(name,d,maxd,maxc):
        f=idx[name][0]; print('  '*d+f"{name}  [{os.path.dirname(f)}]")
        if d>=maxd or name in seen: return
        seen.add(name)
        for c in deps(name)[:maxc]: show(c,d+1,maxd,maxc)
    show(sys.argv[1],0,int(sys.argv[2]),int(sys.argv[3]))
