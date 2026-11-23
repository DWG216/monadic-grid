import os,re,sys,pickle
root=sys.argv[1]
line=re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+|nonrec\s+)*(theorem|lemma|def|abbrev|structure|class|instance|inductive|opaque)\s+([^\s:({\[]+)|^\s*namespace\s+(\S+)|^\s*end\s+(\S+)|^\s*section\b',re.M)
idx={}
for dp,_,fs in os.walk(root):
    for f in fs:
        if not f.endswith('.lean'): continue
        p=os.path.join(dp,f); t=open(p,errors='ignore').read(); rel=os.path.relpath(p,root)
        ns=[]
        for m in line.finditer(t):
            if m.group(3): ns.append(m.group(3))
            elif m.group(4):
                if ns and ns[-1]==m.group(4): ns.pop()
            elif m.group(2):
                n=m.group(2).replace('_root_.','')
                full=n if m.group(2).startswith('_root_.') else '.'.join(ns+[n]) if ns else n
                idx.setdefault(full,(rel,m.start(),m.group(1)))
pickle.dump(idx,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'idx.pkl'),'wb')); print(len(idx))
