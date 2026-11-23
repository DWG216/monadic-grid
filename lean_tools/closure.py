import sys,collections,pickle,time; sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from tree2 import idx, deps
roots={'A Win (vwin_of_row)':'UpperTheory.One.vwin_of_row',
'B Galois reps from theta lift (Row0b)':'UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter',
'C Local Langlands (recTExists)':'UpperTheory.Zero.LLC.recTExists',
'D Character -> zero-free (theta integrals, covolume)':'UpperTheory.Lit.every_character_of_theta_integrals_local_matching',
'E Reflection (rh_of_right)':'Formalism.VW.rh_of_right'}
memo={}
def D(n):
    if n not in memo: memo[n]=deps(n)
    return memo[n]
res={}
for lab,r in roots.items():
    t=time.time(); seen={r}; q=[r]
    while q and len(seen)<400000:
        n=q.pop()
        for c in D(n):
            if c not in seen: seen.add(c); q.append(c)
    files=collections.Counter(idx[n][0] for n in seen)
    dirs=collections.Counter('/'.join(idx[n][0].split('/')[:3]) for n in seen)
    res[lab]=(len(seen),len(files),dirs.most_common(8))
    print(lab,'decls',len(seen),'files',len(files),f'{time.time()-t:.0f}s')
    for d,c in dirs.most_common(8): print('   ',c,d)
pickle.dump(res,open('closure.pkl','wb'))
everything=set()
