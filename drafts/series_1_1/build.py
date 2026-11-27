"""Build series 1.1's 20 posts from the series template in Ember, render each to PNG (canvas/render1.py) and report fit."""
import html, os, subprocess, sys
from content import P
import re
def E(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'bar\{([^}]*)\}', r'<span style="text-decoration: overline">\1</span>', s)
    s = re.sub(r'_\{([^}]*)\}', r'<sub style="font-size: 0.7em">\1</sub>', s)
    s = re.sub(r'\^\{([^}]*)\}', r'<sup style="font-size: 0.7em">\1</sup>', s)
    return s
EMBER = {'#0F1A2B':'#3E1F18','#15233A':'#512A20','#16344A':'#6A3122','#2A3B57':'#7A4434','#A9B8CC':'#EBCDB8','#EEF2F7':'#FFF6EE','#7FD4E8':'#F2B441','#5CC8E0':'#F2B441','#B5E6F2':'#FFD98A','#9C8CF0':'#FF7A52'}  # golden red (2026-11-26); was Ember #1E1410
HEAD = open('/home/claude/canvas/CobaltE8.dc.html').read().split('<div data-gl="1" aria-hidden="true" style="flex: 1 1 0px; min-height: 0; margin-top: -21px"></div>')[0]
TAIL = '''<div data-gl="1" aria-hidden="true" style="flex: 1.618 1 0px; min-height: 0; margin-top: -21px"></div>
<div style="margin-top: 0; display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #2A3B57; padding-top: 21px; font-size: 16px; color: #A9B8CC">
<span></span>
<span style="font-family: 'Space Grotesk', sans-serif">The Monadic Grid</span>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1080,"height":1350}}'>
class Component extends DCLogic {
renderVals() {
return {};
}
}
</script>
</body>
</html>'''
GAP = '<div data-gl="1" aria-hidden="true" style="flex: 1 1 0px; min-height: 0; margin-top: -21px; max-height: 13px"></div>'
def card(head, text, color):
    return (f'<div style="background: #15233A; border-radius: 21px; padding: 26px; display: flex; flex-direction: column; gap: 13px">\n'
            f'<div style="font-family: \'Space Grotesk\', sans-serif; font-size: 26px; font-weight: 600; color: {color}">{E(head)}</div>\n'
            f'<p style="margin: 0; font-size: 19px; line-height: 1.5; color: #EEF2F7">{E(text)}</p>\n</div>')
def found(head, text):
    return (f'<div style="border: 1px solid #2A3B57; border-radius: 21px; padding: 21px 26px; display: flex; flex-direction: column; gap: 8px">\n'
            f'<div style="font-family: \'Space Grotesk\', sans-serif; font-size: 18px; font-weight: 500; color: #A9B8CC">{E(head)}</div>\n'
            f'<p style="margin: 0; font-size: 18px; line-height: 1.5; color: #EEF2F7">{E(text)}</p>\n</div>')
def credit(p):
    if 'credit' not in p: return ''
    k, a = p['credit']
    return (GAP + '\n<div style="border-top: 1px solid #2A3B57; padding-top: 13px; font-size: 16px; line-height: 1.45; color: #A9B8CC">'
            f'<span style="color: #B5E6F2; font-weight: 600">Prior work</span> {E(k)} <br><span style="color: #B5E6F2; font-weight: 600">The grid adds</span> {E(a)}</div>\n')
def page(p):
    h, eq, tx = p['main']
    body = ('<div data-gl="1" aria-hidden="true" style="flex: 1 1 0px; min-height: 0; margin-top: -21px"></div>\n'
      '<div style="display: flex; flex-direction: column; gap: 13px">\n'
      f'<h1 style="margin: 0; font-family: \'Space Grotesk\', sans-serif; font-size: 55px; line-height: 1.1; font-weight: 600">{E(p["title"])}</h1>\n'
      f'<div style="background: #16344A; border-radius: 21px; padding: 21px 26px; display: flex; flex-direction: column; gap: 8px"><div style="font-family: \'Space Grotesk\', sans-serif; font-size: 18px; font-weight: 500; color: #B5E6F2">What this solves</div><p style="margin: 0; font-size: 21px; line-height: 1.5; color: #EEF2F7; font-weight: 500">{E(p["solves"])}</p></div>\n</div>\n'
      + GAP + '\n<div style="background: #15233A; border-radius: 21px; padding: 26px; display: flex; flex-direction: column; gap: 13px">\n'
      f'<div style="font-family: \'Space Grotesk\', sans-serif; font-size: 26px; font-weight: 600; color: #5CC8E0">{E(h)}</div><div style="font-family: \'STIX Two Text\', serif; font-size: 26px; color: #EEF2F7">{E(eq)}</div>\n'
      f'<p style="margin: 0; font-size: 19px; line-height: 1.5; color: #EEF2F7">{E(tx)}</p>\n</div>' + GAP + '\n'
      '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 21px">' + card(*p['left'], '#5CC8E0') + card(*p['right'], '#9C8CF0') + '</div>' + GAP + '\n'
      '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 21px">' + found(*p['f1']) + found(*p['f2']) + '</div>\n' + credit(p))
    s = HEAD.replace('<title>One record, two readings</title>', '<title>Since the drop</title>') + body + TAIL
    for a, b in EMBER.items(): s = s.replace(a, b).replace(a.lower(), b)
    return s
os.makedirs('html', exist_ok=True); out = '/home/claude/launch/series_1_1'; os.makedirs(out, exist_ok=True)
only = [int(x) for x in sys.argv[1:]] or range(1, 21)
for i in only:
    p = P[i - 1]; fn = f'html/post_{i:02d}.dc.html'; open(fn, 'w').write(page(p))
    png = f'{out}/1.1 post {i:02d} - {p["title"]}.png'
    r = subprocess.run(['python3', '/home/claude/canvas/render1.py', fn, png], capture_output=True, text=True, timeout=180)
    fit = int(r.stdout.strip().split()[-1]) if r.stdout.strip() else -1
    print(i, 'fit', fit, 'OVERFLOW' if fit > 1295 or fit < 0 else 'ok', p['title'])
