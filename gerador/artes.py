"""Gera as artes dos posts do @amigos.dieta (1080x1350, visual verde da marca)."""
import os, subprocess, sys, html
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOTOS = f"{REPO}/biblioteca"          # img(FOTOS + "/fotos/natal/p031-0.jpg")
FONTES = f"{REPO}/biblioteca/fontes"
OUT = os.environ.get("ARTES_OUT", "/tmp/artes-out")
os.makedirs(OUT, exist_ok=True)

CSS = f"""
@font-face{{font-family:'Baloo 2';font-weight:800;src:url('file://{FONTES}/baloo-2-latin-800-normal.woff2')}}
@font-face{{font-family:'Baloo 2';font-weight:700;src:url('file://{FONTES}/baloo-2-latin-700-normal.woff2')}}
@font-face{{font-family:'DM Sans';font-weight:400;src:url('file://{FONTES}/dm-sans-latin-400-normal.woff2')}}
@font-face{{font-family:'DM Sans';font-weight:500;src:url('file://{FONTES}/dm-sans-latin-500-normal.woff2')}}
@font-face{{font-family:'DM Sans';font-weight:700;src:url('file://{FONTES}/dm-sans-latin-700-normal.woff2')}}
:root{{--bg:#1f7a4d;--blob:#2b8a5c;--ink:#ffffff;--acc:#ffb45c;--acc2:#f28c28;--dark:#14432c;--soft:#e2f0d8}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{background:var(--bg);color:var(--ink);font-family:'DM Sans',sans-serif;position:relative}}
.blob{{position:absolute;border-radius:50%;background:var(--blob)}}
.b1{{width:760px;height:760px;right:-300px;top:-260px}}
.b2{{width:620px;height:620px;left:-320px;bottom:-300px}}
.top{{position:absolute;top:64px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center;z-index:2}}
.logo{{display:flex;align-items:center;gap:14px;font-family:'Baloo 2';font-weight:800;font-size:40px;letter-spacing:-.5px}}
.selo{{background:var(--acc);color:var(--dark);font-weight:700;font-size:26px;letter-spacing:3px;padding:10px 26px;border-radius:999px}}
.wrap{{position:absolute;left:72px;right:72px;top:170px;bottom:90px;display:flex;flex-direction:column;z-index:2}}
.kicker{{color:var(--acc);font-weight:700;font-size:28px;letter-spacing:5px;text-transform:uppercase;margin-bottom:14px}}
h1{{font-family:'Baloo 2';font-weight:800;line-height:.98;letter-spacing:-1.5px}}
h1 em{{font-style:normal;color:var(--acc)}}
h2{{font-family:'Baloo 2';font-weight:800;font-size:92px;line-height:1;letter-spacing:-1px;margin-bottom:28px}}
h2 em{{font-style:normal;color:var(--acc)}}
.sub{{font-size:40px;line-height:1.3;font-weight:500;margin-top:18px;max-width:880px}}
.pills{{display:flex;flex-wrap:wrap;gap:14px;margin-top:26px}}
.pill{{background:#fff;color:var(--bg);font-weight:700;font-size:26px;padding:10px 24px;border-radius:999px}}
.photo{{border-radius:40px;overflow:hidden;box-shadow:0 24px 50px rgba(0,0,0,.28);background:#fff}}
.photo img{{width:100%;height:100%;object-fit:cover;display:block}}
.foot{{position:absolute;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;align-items:center;font-weight:700;font-size:30px;z-index:2}}
.cta{{background:#fff;color:var(--bg);border-radius:28px;padding:26px 34px;font-family:'Baloo 2';font-weight:800;font-size:44px;line-height:1.1;display:flex;justify-content:space-between;align-items:center;gap:20px}}
.cta small{{font-family:'DM Sans';font-weight:700;font-size:26px;color:var(--dark);text-align:right;line-height:1.25}}
.card{{background:rgba(255,255,255,.09);border:2px solid rgba(255,255,255,.18);border-radius:32px;padding:34px 40px}}
ul.list{{list-style:none;display:flex;flex-direction:column;gap:18px}}
ul.list li{{font-size:40px;line-height:1.28;padding-left:46px;position:relative}}
ul.list li:before{{content:'';position:absolute;left:0;top:17px;width:20px;height:20px;border-radius:50%;background:var(--acc)}}
ol.steps{{list-style:none;display:flex;flex-direction:column;gap:34px;counter-reset:s}}
ol.steps li{{counter-increment:s;font-size:41px;line-height:1.3;padding-left:84px;position:relative}}
ol.steps li:before{{content:counter(s);position:absolute;left:0;top:0;width:60px;height:60px;border-radius:50%;background:var(--acc);color:var(--dark);font-family:'Baloo 2';font-weight:800;font-size:36px;display:flex;align-items:center;justify-content:center}}
.label{{color:var(--acc);font-weight:700;font-size:26px;letter-spacing:4px;text-transform:uppercase;margin-bottom:18px}}
.price{{font-family:'Baloo 2';font-weight:800;font-size:150px;line-height:.9;color:var(--acc)}}
.price small{{font-size:56px;margin-right:8px}}
"""

LEAF = """<svg width="58" height="58" viewBox="0 0 64 64" aria-hidden="true">
<path d="M10 54 C10 26 28 8 56 8 C56 36 38 54 10 54 Z" fill="#f28c28"/>
<path d="M14 50 C26 38 36 28 48 16" stroke="#ffffff" stroke-width="4" fill="none" stroke-linecap="round"/></svg>"""


def page(body, selo, contador=None, blobs=True, foot=""):
    s = f'<span class="selo">{html.escape(selo)}</span>' if selo else ""
    c = f'<span class="selo" style="background:transparent;color:#fff;border:2px solid rgba(255,255,255,.5)">{contador}</span>' if contador else ""
    right = s or c
    b = '<div class="blob b1"></div><div class="blob b2"></div>' if blobs else ""
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{b}
<div class="top"><div class="logo">{LEAF}<span>amigos da dieta</span></div>{right}</div>
{body}{foot}</body></html>"""


def img(path):
    return "file://" + path


def render(name, doc):
    hp = f"{OUT}/{name}.html"
    pp = f"{OUT}/{name}.png"
    open(hp, "w", encoding="utf-8").write(doc)
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--force-device-scale-factor=1",
                    "--window-size=1080,1350", "--virtual-time-budget=3000",
                    f"--screenshot={pp}", "file://" + hp], check=True, capture_output=True)
    Image.open(pp).convert("RGB").save(f"{OUT}/{name}.jpg", quality=90, optimize=True)
    os.remove(pp)
    return f"{OUT}/{name}.jpg"


def foot_swipe(txt="Arraste para o lado →"):
    return f'<div class="foot"><span></span><span>{txt}</span></div>'
