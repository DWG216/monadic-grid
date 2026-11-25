"""Palette wheel: keep series 1's lightness and chroma for every role, rotate the hue by the golden angle."""
import numpy as np, json, sys
def srgb2lin(c): c = c/255; return np.where(c <= 0.04045, c/12.92, ((c+0.055)/1.055)**2.4)
def lin2srgb(c): c = np.clip(c, 0, 1); return np.where(c <= 0.0031308, 12.92*c, 1.055*c**(1/2.4) - 0.055)*255
M1 = np.array([[0.4122214708, 0.5363325363, 0.0514459929], [0.2119034982, 0.6806995451, 0.1073969566], [0.0883024619, 0.2817188376, 0.6299787005]])
M2 = np.array([[0.2104542553, 0.7936177850, -0.0040720468], [1.9779984951, -2.4285922050, 0.4505937099], [0.0259040371, 0.7827717662, -0.8086757660]])
def hex2oklch(h):
    rgb = srgb2lin(np.array([int(h[i:i+2], 16) for i in (1, 3, 5)], float)); L, a, b = M2 @ np.cbrt(M1 @ rgb)
    return L, np.hypot(a, b), np.degrees(np.arctan2(b, a)) % 360
def oklch2hex(L, C, H):
    while True:
        a, b = C*np.cos(np.radians(H)), C*np.sin(np.radians(H)); lms = np.linalg.solve(M2, [L, a, b])**3; rgb = np.linalg.solve(M1, lms)
        if np.all(rgb >= -1e-4) and np.all(rgb <= 1+1e-4) or C < 1e-3: break
        C *= 0.97
    return '#' + ''.join(f'{int(round(v)):02X}' for v in lin2srgb(rgb))
def lum(h): r = srgb2lin(np.array([int(h[i:i+2], 16) for i in (1, 3, 5)], float)); return 0.2126*r[0] + 0.7152*r[1] + 0.0722*r[2]
def contrast(a, b): x, y = sorted([lum(a), lum(b)]); return (y + 0.05)/(x + 0.05)
roles = ['#0F1A2B', '#15233A', '#16344A', '#2A3B57', '#A9B8CC', '#EEF2F7', '#7FD4E8', '#5CC8E0', '#B5E6F2', '#9C8CF0']
base = [hex2oklch(r) for r in roles]; h0 = base[6][2]
golden = 360*(1 - 1/((1+5**0.5)/2))   # 137.5 degrees
def palette(h):
    return {r: oklch2hex(L, C, (H - h0 + h) % 360) for r, (L, C, H) in zip(roles, base)}
if __name__ == '__main__':
    print('series 1 accent hue', round(h0, 1), 'golden angle', round(golden, 2))
    slots = {k: (h0 + k*golden) % 360 for k in range(8)}
    out = {}
    for k, h in slots.items():
        p = palette(h); out[k] = dict(hue=round(h, 1), map=p)
        print(k, round(h, 1), p['#0F1A2B'], p['#7FD4E8'], p['#9C8CF0'], 'text/bg', round(contrast(p['#EEF2F7'], p['#0F1A2B']), 1), 'accent/bg', round(contrast(p['#7FD4E8'], p['#0F1A2B']), 1))
    json.dump(out, open('slots.json', 'w'), indent=1)
