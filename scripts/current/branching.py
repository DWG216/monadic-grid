exec(open('branch_lib.py').read()); import json; out={}
ok1=ok2=ok3=True
for r in (3,4,5,6,7,8,10,12):
    c,w=branches(r,12); f=w[-1]/c[-1]; rat=[c[l]/c[l-1] for l in range(8,13)]; out[r]=c
    print(f"r={r}: branches L=0..12 {c}; ratios L=8..12 {[round(x,3) for x in rat]}; fungibility at L=12 {f:.1f}",flush=True)
    if r in (4,6,10): ok1&=len(set(c[8:]))==1 and c[12]=={4:24,6:12,10:60}[r]; ok3&=f>1e4
    if r in (5,7,8,12): ok2&=min(rat)>1.5; ok3&=f<50
print("B1 frame saturates at the group order:",'PASS' if ok1 else 'FAIL'); print("B2 fluid keeps branching:",'PASS' if ok2 else 'FAIL'); print("B3 fungibility separates frame from fluid:",'PASS' if ok3 else 'FAIL')
json.dump(out,open('branching.json','w'))
