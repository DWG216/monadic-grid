"""Generate the P vs NP series (60 posts) in the series-1 template, with the chain strip (whole in every part) and the beef line."""
import html, json, sys, importlib.util, os
LEVELS = {1: '1 · No math', 2: '2 · Algebra', 3: '3 · Calculus', 4: '4 · Physics', 5: '5 · Grad math', 6: '6 · Research'}
CHAIN = ['Balanced pair', 'One record: QM × GR', 'Slice = fermions', 'Root √n', 'Meetings vs exclusion', 'Only a law wins', 'Laws live in dolls', '3-SAT: balanced, lawless']
E = html.escape
def card(head, text, color='#5CC8E0', formula=None):
    f = f'<div style="font-family: \'STIX Two Text\', serif; font-size: 25px; color: #EEF2F7">{E(formula)}</div>' if formula else ''
    return (f'<div style="background: #15233A; border-radius: 21px; padding: 24px 26px; display: flex; flex-direction: column; gap: 11px">'
            f'<div style="font-family: \'Space Grotesk\', sans-serif; font-size: 25px; font-weight: 600; color: {color}">{E(head)}</div>{f}'
            f'<p style="margin: 0; font-size: 19px; line-height: 1.48; color: #EEF2F7">{E(text)}</p></div>')
GAP = '<div data-gl="1" aria-hidden="true" style="flex: 1 1 0px; min-height: 0; margin-top: -21px; max-height: 13px"></div>'
def strip(step):
    pills = []
    for i, c in enumerate(CHAIN):
        on = i in (step if isinstance(step, (list, tuple)) else [step])
        st = ('background: #5CC8E0; color: #0F1A2B; font-weight: 600' if on else 'background: #16344A; color: #B5E6F2; font-weight: 500')
        pills.append(f'<span style="{st}; border-radius: 999px; padding: 6px 12px; font-size: 15px; font-family: \'Space Grotesk\', sans-serif; white-space: nowrap">{E(c)}</span>')
        if i < len(CHAIN) - 1: pills.append('<span style="color: #5CC8E0; font-size: 15px">→</span>')
    return ('<div style="border: 1px solid #2A3B57; border-radius: 21px; padding: 16px 20px; display: flex; flex-direction: column; gap: 10px">'
            '<div style="font-family: \'Space Grotesk\', sans-serif; font-size: 16px; font-weight: 500; color: #A9B8CC">The chain: P ≠ NP on the monadic grid (this post is the highlighted link)</div>'
            f'<div style="display: flex; flex-wrap: wrap; gap: 6px 6px; align-items: center">{"".join(pills)}</div></div>')
def page(p, slide=''):
    lvl = LEVELS[p['lvl']]
    num = f"{p['n']}{slide}"
    body = []
    body.append(f'<div style="display: flex; justify-content: space-between; font-family: \'Space Grotesk\', sans-serif; font-size: 17px; color: #A9B8CC"><span>P vs NP · {num} / 60</span><span>Level {E(lvl)}</span></div>')
    body.append(f'<div style="display: flex; flex-direction: column; gap: 13px"><h1 style="margin: 0; font-family: \'Space Grotesk\', sans-serif; font-size: {p.get("fs", 50)}px; line-height: 1.1; font-weight: 600">{E(p["title"])}</h1>'
                f'<div style="background: #16344A; border-radius: 21px; padding: 20px 26px; display: flex; flex-direction: column; gap: 8px"><div style="font-family: \'Space Grotesk\', sans-serif; font-size: 18px; font-weight: 500; color: #B5E6F2">What this solves</div>'
                f'<p style="margin: 0; font-size: 21px; line-height: 1.45; color: #EEF2F7; font-weight: 500">{E(p["solves"])}</p></div></div>')
    body.append(GAP)
    h, f, t = p['card']
    body.append(card(h, t, formula=f))
    body.append(GAP)
    body.append(f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 21px">{card(*p["left"])}{card(p["right"][0], p["right"][1], "#9C8CF0")}</div>')
    body.append(GAP)
    body.append(strip(p['step']))
    body.append(f'<div style="border: 1px solid #2A3B57; border-radius: 21px; padding: 16px 22px; display: flex; flex-direction: column; gap: 6px"><div style="font-family: \'Space Grotesk\', sans-serif; font-size: 16px; font-weight: 500; color: #A9B8CC">Where\'s the beef</div>'
                f'<p style="margin: 0; font-size: 18px; line-height: 1.45; color: #EEF2F7">{E(p["beef"])}</p></div>')
    inner = '\n'.join(body)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{E(p["title"])}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Space+Grotesk:wght@500;600&amp;family=STIX+Two+Text:ital,wght@0,400;1,400&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:#7FD4E8}}a:hover{{color:#B5E6F2}}
</style>
</helmet>
<div style="width: 1080px; height: 1350px; box-sizing: border-box; position: relative; overflow: hidden; background: #0F1A2B; color: #EEF2F7; font-family: Inter, system-ui, sans-serif; padding: 55px; display: flex; flex-direction: column; gap: 21px">
<svg aria-hidden="true" width="667" height="667" viewBox="0 0 667 667" style="position: absolute; right: -150px; top: -150px; opacity: 0.15">
<path d="M667 667 A667 667 0 0 0 0 0" fill="none" stroke="#7FD4E8" stroke-width="1.5"></path>
<path d="M0 0 A412 412 0 0 0 412 412" fill="none" stroke="#7FD4E8" stroke-width="1.5"></path>
<path d="M412 412 A255 255 0 0 0 667 157" fill="none" stroke="#7FD4E8" stroke-width="1.5"></path>
<path d="M667 157 A157 157 0 0 0 510 0" fill="none" stroke="#7FD4E8" stroke-width="1.5"></path>
<rect x="0.75" y="0.75" width="665.5" height="665.5" fill="none" stroke="#7FD4E8" stroke-width="1"></rect>
<line x1="412" y1="0" x2="412" y2="667" stroke="#7FD4E8" stroke-width="1"></line>
<line x1="412" y1="412" x2="667" y2="412" stroke="#7FD4E8" stroke-width="1"></line>
</svg>
{inner}
<div data-gl="1" aria-hidden="true" style="flex: 1.618 1 0px; min-height: 0; margin-top: -21px"></div>
<div style="margin-top: 0; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #2A3B57; padding-top: 21px; font-size: 16px; color: #A9B8CC">
<span>Deduced, not modelled · nothing in it is arbitrary</span>
<span style="font-family: 'Space Grotesk', sans-serif">The Monadic Grid</span>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
if __name__ == '__main__':
    posts = []
    for f in sys.argv[1:]:
        spec = importlib.util.spec_from_file_location('c', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); posts += m.POSTS
    os.makedirs('html', exist_ok=True)
    for p in posts:
        if 'b' in p:
            a = dict(p); a.pop('b'); open(f"html/post{p['n']:02d}a.html", 'w').write(page(a, 'a'))
            b = dict(p); b.update(p['b']); b.pop('b'); open(f"html/post{p['n']:02d}b.html", 'w').write(page(b, 'b'))
        else:
            open(f"html/post{p['n']:02d}.html", 'w').write(page(p))
    print(len(posts), 'posts')
