"""Storyboard board: one image per shot with its timing, voice, image, camera, bridge object and sound."""
import pathlib, sys, html
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sb_data import FRAMES, SHOTS, TITLE, META, LEGEND
proj = pathlib.Path(sys.argv[1]).resolve()
out = proj / "planche"; out.mkdir(exist_ok=True)
import subprocess
(out / "img").mkdir(exist_ok=True)
for s_ in SHOTS:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(proj / "styleframes/png" / f"{s_['id']}.png"), "-q:v", "3", str(out / "img" / f"{s_['id']}.jpg")], check=True)
fr = lambda t: f"{t:.2f}".replace(".", ",")
E = html.escape
CSS = """
@font-face{font-family:IS;font-weight:400;src:url(../assets/fonts/InstrumentSans-400.woff2)}
@font-face{font-family:IS;font-weight:600;src:url(../assets/fonts/InstrumentSans-600.woff2)}
@font-face{font-family:IS;font-weight:700;src:url(../assets/fonts/InstrumentSans-700.woff2)}
@font-face{font-family:SM;font-weight:400;src:url(../assets/fonts/SpaceMono-400.woff2)}
@font-face{font-family:SM;font-weight:700;src:url(../assets/fonts/SpaceMono-700.woff2)}
@font-face{font-family:CV;font-weight:700;src:url(../assets/fonts/Caveat-700.woff2)}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1920px;background:#f6f5f2;color:#17181c;font-family:IS}
.page{width:1920px;padding:56px 70px 60px}
.top{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #17181c;padding-bottom:18px;margin-bottom:36px}
.top h1{font:700 44px/1 IS;letter-spacing:-.02em}
.top h1 em{font:700 50px/1 CV;font-style:normal;background:#ff3b30;color:#fff;padding:0 12px;margin-left:6px}
.top .meta{font:400 18px/1.4 SM;letter-spacing:.08em;text-align:right;color:#55565c;text-transform:uppercase}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:44px 50px}
.cell img{width:865px;height:487px;display:block;border-radius:10px;box-shadow:0 18px 40px rgba(60,45,20,.18)}
.hd{display:flex;align-items:baseline;gap:16px;margin:18px 0 8px}
.id{font:700 26px/1 SM;background:#ff3b30;color:#fff;padding:6px 10px;border-radius:6px}
.tc{font:700 22px/1 SM;color:#17181c;white-space:nowrap}
.sq{font:400 16px/1 SM;letter-spacing:.1em;text-transform:uppercase;color:#8d8a84;margin-left:auto;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:400px}
.vo{font:600 27px/1.25 IS;margin:6px 0 12px}
.vo.muet{color:#8d8a84;font-style:italic}
.row{display:grid;grid-template-columns:118px 1fr;gap:12px;font:400 20px/1.36 IS;margin-bottom:7px;color:#2b2c31}
.row b{font:700 14px/1.9 SM;letter-spacing:.14em;text-transform:uppercase;color:#8d8a84}
.ov{display:grid;grid-template-columns:repeat(4,1fr);gap:26px 22px}
.ov .c img{width:100%;border-radius:8px;box-shadow:0 10px 24px rgba(60,45,20,.16);display:block}
.ov .c div{font:700 18px/1.3 SM;margin-top:9px}
.ov .c span{font:400 17px/1.3 IS;color:#55565c;display:block}
.legend{margin-top:34px;font:400 21px/1.5 IS;color:#2b2c31;columns:2;column-gap:60px}
.legend p{margin-bottom:10px;break-inside:avoid}
.legend b{font-weight:700}
"""
def head(title, sub):
    return (f'<div class="top"><h1>{E(TITLE)} <em>storyboard</em> · {E(title)}</h1>'
            f'<div class="meta">{E(META.replace(chr(39), '’'))}<br>{E(sub)}</div></div>')
def doc(body):
    return f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>'
pages = []
# page 0: overview
cells = "".join(f'<div class="c"><img src="img/{s["id"]}.jpg"><div>{s["id"]} · {fr(s["a"])} → {fr(s["b"])} s</div>'
                f'<span>{E(s["voice"].replace(chr(39), "’"))}</span></div>' for s in SHOTS)
legend = '<div class="legend">' + "".join(f"<p><b>{E(k)}</b> {E(v)}</p>" for k, v in LEGEND) + "</div>"
pages.append(head("vue d’ensemble", f"{len(SHOTS)} plans · {len(FRAMES)} séquences") + f'<div class="ov">{cells}</div>' + legend)
# detail pages, 6 shots each
seq = {f["n"]: f for f in FRAMES}
NP = (len(SHOTS) + 5) // 6
for p in range(0, len(SHOTS), 6):
    chunk = SHOTS[p:p + 6]
    cells = ""
    for s in chunk:
        f = seq[s["frame"]]
        muet = s["voice"].startswith("(")
        quoted = s["voice"].startswith("«")
        cells += (f'<div class="cell"><img src="img/{s["id"]}.jpg">'
                  f'<div class="hd"><span class="id">{s["id"]}</span><span class="tc">{fr(s["a"])} → {fr(s["b"])} s · {fr(s["b"] - s["a"])} s</span>'
                  f'<span class="sq">Séq. {f["n"]} · {E(f["title"].replace(chr(39), "’"))}</span></div>'
                  f'<div class="vo{" muet" if muet else ""}">{"" if muet or quoted else "« "}{E(s["voice"].replace(chr(39), "’"))}{"" if muet or quoted else " »"}</div>'
                  f'<div class="row"><b>À l’image</b><span>{E(s["see"])}</span></div>'
                  f'<div class="row"><b>Caméra</b><span>{E(s["cam"])}</span></div>'
                  f'<div class="row"><b>Pont</b><span>{E(s["bridge"])}</span></div>'
                  f'<div class="row"><b>Son</b><span>{E(s["sfx"])}</span></div></div>')
    pages.append(head(f"plans {chunk[0]['id'][1:]} à {chunk[-1]['id'][1:]}", f"planche {p // 6 + 1} / {NP}") + f'<div class="grid">{cells}</div>')
files = []
for k, body in enumerate(pages):
    f = out / f"planche-{k}.html"
    f.write_text(doc(f'<div class="page">{body}</div>'), encoding="utf-8")
    files.append(f)
(out / "planche.html").write_text(doc("".join(f'<div class="page" style="break-after:page">{b}</div>' for b in pages)), encoding="utf-8")
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1920, "height": 1200})
    for f in files:
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready.then(()=>true)"); pg.wait_for_timeout(300)
        pg.screenshot(path=str(f.with_suffix(".png")), full_page=True); print(f.with_suffix(".png"))
    pg.goto((out / "planche.html").as_uri()); pg.evaluate("document.fonts.ready.then(()=>true)"); pg.wait_for_timeout(300)
    h = pg.evaluate("Math.max(...[...document.querySelectorAll('.page')].map(e=>e.scrollHeight))")
    pg.pdf(path=str(out / "planche.pdf"), width="1920px", height=f"{h}px", print_background=True); print(out / "planche.pdf", h)
    b.close()
