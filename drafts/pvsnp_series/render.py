import asyncio, sys, glob, os
from playwright.async_api import async_playwright
FONTCSS = """@font-face{font-family:'Space Grotesk';src:local('Inter Display SemiBold'),local('InterDisplay-SemiBold');font-weight:600}
@font-face{font-family:'Space Grotesk';src:local('Inter Display Medium'),local('InterDisplay-Medium');font-weight:500}
@font-face{font-family:'STIX Two Text';src:local('Latin Modern Roman'),local('LMRoman10-Regular')}
"""
async def main(files):
    os.makedirs('png', exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        for src in files:
            html = open(src).read().replace('<script src="./support.js"></script>', '').replace('</style>', FONTCSS+'</style>', 1)
            open('/tmp/r1.html', 'w').write(html)
            await pg.goto('file:///tmp/r1.html'); await pg.wait_for_timeout(150)
            info = await pg.evaluate("()=>{const r=document.querySelector('x-dc > div');const k=[...r.children].filter(c=>getComputedStyle(c).position!='absolute');const f=k[k.length-1];return [Math.round(f.getBoundingClientRect().bottom), r.scrollHeight]}")
            el = await pg.query_selector('x-dc > div'); out = 'png/' + os.path.basename(src).replace('.html', '.png'); await el.screenshot(path=out)
            print(os.path.basename(src), info, 'OVER' if info[0] > 1295 or info[1] > 1350 else '')
        await b.close()
asyncio.run(main(sorted(sys.argv[1:])))
