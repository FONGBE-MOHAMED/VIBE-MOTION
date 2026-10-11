"""Generate one styleframe per shot (key image) of « Pas pour moi » in <project>/styleframes/Pxx.html."""
import math, pathlib, sys

OUT = pathlib.Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------ helpers
def page(body, title):
    return f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="_kit.css"></head><body><div id="stage">{body}</div></body></html>"""

def ground(theme, hx=960, hy=470, hw=1500, hh=1000):
    g = "g-dark" if theme == "dark" else "g-light"
    return (f'<div class="{g}"><div class="dots"></div>'
            f'<div class="halo" style="left:{hx-hw/2}px;top:{hy-hh/2}px;width:{hw}px;height:{hh}px"></div></div>')

def finish(theme):
    return '<div class="grain"></div>' + (f'<div class="vignette{" light" if theme == "light" else ""}"></div>')

def sub(text, theme, hl=None, pk=None, upto=None):
    """Subtitle: words up to `upto` (index, exclusive) visible; hl/pk = exact substring to highlight / underline."""
    def wrap(seg):
        out = []
        for w in seg.split(" "):
            out.append(w)
        return out
    tokens, i = [], 0
    marks = []
    for kind, s in (("hl", hl), ("pk", pk)):
        if s:
            k = text.index(s)
            marks.append((k, k + len(s), kind))
    marks.sort()
    pos, pieces = 0, []
    for a, b, kind in marks:
        if a > pos:
            pieces.append(("t", text[pos:a]))
        pieces.append((kind, text[a:b]))
        pos = b
    if pos < len(text):
        pieces.append(("t", text[pos:]))
    html, n = [], 0
    for kind, seg in pieces:
        words = seg.split(" ")
        if kind == "t":
            for j, w in enumerate(words):
                if w == "":
                    html.append(" ")
                    continue
                cls = "w" + (" off" if upto is not None and n >= upto else "")
                html.append(f'<span class="{cls}">{w}</span>')
                n += 1
                if j < len(words) - 1:
                    html.append(" ")
        else:
            nwords = len([w for w in words if w])
            cls = "w" + (" off" if upto is not None and n >= upto else "")
            n += nwords
            if kind == "hl":
                html.append(f'<span class="{cls} hl">{seg}</span>')
            else:
                html.append(f'<span class="{cls} pk">{seg}{BRUSH}</span>')
    return f'<div class="sub {theme}">{"".join(html)}</div>'

BRUSH = ('<svg viewBox="0 0 400 30" preserveAspectRatio="none"><path d="M6 22 C 70 16, 150 13, 230 11 C 300 9, 360 6, 396 3 '
         'C 398 6, 396 9, 392 10 C 330 15, 250 19, 170 22 C 110 24, 50 27, 10 28 C 2 28, 1 23, 6 22 Z" fill="#f7d038"/></svg>')

def postit(x, y, rot=-5, scale=1.0, blur=0, text="Pas pour<br>moi", extra="", strike=False, opacity=1):
    f = f"filter:blur({blur}px);" if blur else ""
    s = ""
    if strike:
        s = ('<svg class="strike" style="left:24px;top:84px;width:150px;height:60px" viewBox="0 0 150 60">'
             '<path d="M4 34 C 30 30, 60 27, 90 26 C 112 25, 132 22, 146 18" stroke="#17181c" stroke-width="7" fill="none" stroke-linecap="round"/></svg>')
    return (f'<div class="postit" style="left:{x}px;top:{y}px;transform:rotate({rot}deg) scale({scale});{f}opacity:{opacity};{extra}">'
            f'<div class="band"></div><div class="hw">{text}</div>{s}<div class="curl"></div></div>')

def clock(cx, cy, h, m, d=260, theme="dark", digital=None, label=None, arc=None, blur=0):
    r = d / 2
    ticks = []
    for k in range(12):
        a = math.radians(k * 30)
        r1, r2 = r - 18, r - (40 if k % 3 == 0 else 30)
        ticks.append(f'<line x1="{r + r1*math.sin(a):.1f}" y1="{r - r1*math.cos(a):.1f}" x2="{r + r2*math.sin(a):.1f}" '
                     f'y2="{r - r2*math.cos(a):.1f}" stroke="#17181c" stroke-width="{6 if k % 3 == 0 else 3}" stroke-linecap="round"/>')
    ha = math.radians(((h % 12) + m / 60) * 30)
    ma = math.radians(m * 6)
    sa = math.radians(((m * 7) % 60) * 6)
    arcsvg = ""
    if arc:  # (from_minutes_angle_deg, to_deg) yellow sector = time given back
        a0, a1 = [math.radians(v) for v in arc]
        large = 1 if (arc[1] - arc[0]) % 360 > 180 else 0
        x0, y0 = r + (r - 26) * math.sin(a0), r - (r - 26) * math.cos(a0)
        x1, y1 = r + (r - 26) * math.sin(a1), r - (r - 26) * math.cos(a1)
        arcsvg = (f'<path d="M{r} {r} L{x0:.1f} {y0:.1f} A{r-26} {r-26} 0 {large} 1 {x1:.1f} {y1:.1f} Z" fill="#f7d038" opacity=".55"/>')
    lab = (f'<text x="{r}" y="{r + r*0.42:.1f}" text-anchor="middle" font-family="Space Mono" font-weight="700" '
           f'font-size="{d*0.075:.0f}" letter-spacing="3" fill="#55565c">{label}</text>') if label else ""
    svg = (f'<svg width="{d}" height="{d}" viewBox="0 0 {d} {d}" style="overflow:visible">'
           f'<circle cx="{r}" cy="{r}" r="{r-4}" fill="#fffdf8" stroke="#17181c" stroke-width="8"/>'
           f'{arcsvg}{"".join(ticks)}{lab}'
           f'<line x1="{r}" y1="{r}" x2="{r + (r*0.5)*math.sin(ha):.1f}" y2="{r - (r*0.5)*math.cos(ha):.1f}" stroke="#17181c" stroke-width="10" stroke-linecap="round"/>'
           f'<line x1="{r}" y1="{r}" x2="{r + (r*0.74)*math.sin(ma):.1f}" y2="{r - (r*0.74)*math.cos(ma):.1f}" stroke="#17181c" stroke-width="6" stroke-linecap="round"/>'
           f'<line x1="{r - (r*0.15)*math.sin(sa):.1f}" y1="{r + (r*0.15)*math.cos(sa):.1f}" x2="{r + (r*0.8)*math.sin(sa):.1f}" y2="{r - (r*0.8)*math.cos(sa):.1f}" stroke="#f7d038" stroke-width="3" stroke-linecap="round"/>'
           f'<circle cx="{r}" cy="{r}" r="8" fill="#17181c"/></svg>')
    f = f"filter:blur({blur}px);" if blur else ""
    dig = (f'<div class="clock-digit{" light" if theme == "light" else ""}" style="left:{cx}px;top:{cy + r + 26}px">{digital}</div>') if digital else ""
    shadow = f'<div class="abs" style="left:{cx-r}px;top:{cy-r}px;width:{d}px;height:{d}px;border-radius:50%;box-shadow:0 30px 60px rgba(0,0,0,{.45 if theme=="dark" else .16})"></div>'
    return f'{shadow}<div class="clock" style="left:{cx-r}px;top:{cy-r}px;{f}">{svg}</div>{dig}'

def frise(y, theme="dark", years=(), ghost=()):
    t = "" if theme == "dark" else " light"
    h = f'<div class="frise{t}" style="top:{y}px"></div>'
    for x, label in years:
        h += f'<div class="tick{t}" style="left:{x-1}px;top:{y+2}px"></div><div class="year{t}" style="left:{x}px;top:{y+34}px">{label}</div>'
    for x, label, b in ghost:
        h += f'<div class="year ghost" style="left:{x}px;top:{y+34}px;filter:blur({b}px);color:rgba(201,198,191,.6)">{label}</div>'
    return h

def crt(x, y, scale=1.0, popup=True, extra=""):
    pop = ""
    if popup:
        pop = ('<div class="w98" style="left:64px;top:84px"><div class="w98-title">Assistant</div><div class="w98-body">'
               'Créer votre site internet ?<div class="w98-btns"><span class="w98-btn">Oui</span><span class="w98-btn">Plus tard</span></div></div></div>')
    return (f'<div class="crt" style="left:{x}px;top:{y}px;transform:scale({scale});transform-origin:50% 100%;{extra}">'
            f'<div class="crt-body"><div class="crt-screen">{pop}</div><div class="crt-led"></div></div>'
            f'<div class="crt-neck"></div><div class="crt-foot"></div></div>')

def phone10(x, y, scale=1.0, extra=""):
    apps = "".join("<i></i>" for _ in range(8))
    return (f'<div class="phone10" style="left:{x}px;top:{y}px;transform:scale({scale});transform-origin:50% 100%;{extra}">'
            f'<div class="phone10-ear"></div><div class="phone10-screen"><div class="app-grid">{apps}</div>'
            f'<div class="notif10">Rejoins tes amis sur le réseau<br><span class="btn">S’inscrire</span></div></div>'
            f'<div class="phone10-home"></div></div>')

ARROW = ('<svg width="30" height="30" viewBox="0 0 30 30"><path d="M15 24 V7 M8 13 L15 6 L22 13" stroke="#17181c" stroke-width="3.6" '
         'fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def ai_screen(theme="dark", hello="Bonjour. Que veux-tu faire aujourd’hui ?", field="Écris ta demande…", field_color=None, caret=True, body=""):
    t = "" if theme == "dark" else " light"
    fc = f"color:{field_color};" if field_color else ""
    car = '<span class="caret" style="height:36px;margin-left:4px"></span>' if caret else ""
    return (f'<div class="ai{t}"><div class="ai-head"><span class="ai-dot"></span>Assistant IA</div>'
            f'<div class="ai-hello">{hello}</div>{body}'
            f'<div class="ai-field" style="{fc}">{field}{car}<div class="send" style="right:16px;top:15px">{ARROW}</div></div></div>')

def laptop(x, y, scale=1.0, theme="dark", screen="", extra=""):
    t = "" if theme == "dark" else " light"
    return (f'<div class="laptop{t}" style="left:{x}px;top:{y}px;transform:scale({scale});{extra}">'
            f'<div class="laptop-lid"><div class="laptop-screen">{screen}</div></div>'
            f'<div class="laptop-base"></div><div class="laptop-notch"></div></div>')

def contact(cx, y, w, theme="dark"):
    return f'<div class="contact{"" if theme == "dark" else " light"}" style="left:{cx-w/2}px;top:{y-13}px;width:{w}px"></div>'

def cursor(x, y, scale=1.0, blur=0):
    f = f"filter:blur({blur}px);" if blur else ""
    return (f'<svg class="abs" style="left:{x}px;top:{y}px;transform:scale({scale});transform-origin:0 0;{f}" width="48" height="64" viewBox="0 0 48 64">'
            '<path d="M4 3 L4 50 L16 39 L24 58 L32 54 L24 36 L40 36 Z" fill="#fff" stroke="#17181c" stroke-width="3" stroke-linejoin="round" '
            'style="filter:drop-shadow(0 6px 8px rgba(0,0,0,.45))"/></svg>')

def mug(x, y, scale=1.0, blur=0, theme="dark"):
    f = f"filter:blur({blur}px);" if blur else ""
    body = "#e9e4d8" if theme == "dark" else "#fffdf8"
    return (f'<svg class="abs" style="left:{x}px;top:{y}px;transform:scale({scale});transform-origin:50% 100%;{f}" width="260" height="300" viewBox="0 0 260 300">'
            '<path d="M70 20 C 60 45, 92 60, 80 90 M115 10 C 105 40, 138 55, 125 92 M160 22 C 150 47, 182 62, 170 92" stroke="rgba(243,241,236,.45)" stroke-width="8" fill="none" stroke-linecap="round"/>'
            f'<path d="M40 110 H200 V240 C200 270, 180 288, 150 288 H90 C60 288, 40 270, 40 240 Z" fill="{body}" stroke="#17181c" stroke-width="6"/>'
            '<path d="M200 140 C 250 140, 250 220, 200 220" stroke="#17181c" stroke-width="12" fill="none"/>'
            '<ellipse cx="120" cy="112" rx="80" ry="12" fill="#3b2a1e"/></svg>')

CHECK = ('<svg width="30" height="30" viewBox="0 0 30 30"><path d="M6 16 L12 22 L24 8" stroke="#17181c" stroke-width="4.2" fill="none" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')

def win(x, y, w, h, title, inner, theme="dark", extra=""):
    t = " light" if theme == "light" else ""
    return (f'<div class="win{t}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}"><div class="win-bar"><i></i><i></i><i></i>'
            f'<span>{title}</span></div><div class="abs" style="left:0;top:52px;right:0;bottom:0">{inner}</div></div>')

def slides_ui(w, h):
    thumbs = "".join(f'<div style="height:74px;border-radius:6px;background:#fff;border:{"3px solid #17181c" if k == 0 else "1px solid #e1dccf"}"></div>' for k in range(5))
    cw, ch = w - 250, h - 52 - 110
    return (f'<div class="abs" style="left:24px;top:24px;width:150px;display:grid;gap:14px">{thumbs}</div>'
            f'<div class="abs" style="left:200px;top:24px;width:{cw}px;height:{ch}px;background:#fff;border:1px solid #e1dccf;border-radius:6px">'
            f'<div class="abs" style="left:60px;right:60px;top:{ch*0.32:.0f}px;height:120px;border:3px dashed #c9c3b6;border-radius:8px;display:flex;align-items:center;justify-content:center;'
            f'font:500 40px/1 Instrument Sans;color:#a19c90">Cliquez pour ajouter un titre</div></div>'
            f'<div class="abs micro" style="left:200px;bottom:34px">Diapo 1 / 20</div>')

def inbox_ui(w, n=7):
    names = ["Service client", "Comptabilité", "Équipe projet", "Fournisseur", "Banque", "Newsletter", "Rendez-vous", "Facturation"]
    subj = ["Relance : votre commande", "Pièces manquantes", "Re: Re: point de lundi", "Devis à valider", "Votre relevé", "Les nouveautés", "Confirmation demandée", "Facture n° 2026-118"]
    rows = "".join(
        f'<div style="display:flex;align-items:center;gap:18px;height:70px;border-bottom:1px solid #ece7dc;padding:0 26px">'
        f'<span style="width:12px;height:12px;border-radius:50%;background:#17181c"></span>'
        f'<span class="ui" style="font-weight:700;width:250px">{names[k]}</span><span class="ui" style="color:#55565c">{subj[k]}</span></div>'
        for k in range(n))
    return (f'<div style="display:flex;align-items:baseline;gap:20px;padding:24px 26px 18px"><span style="font:600 34px/1 Instrument Sans;color:#17181c">Boîte de réception</span>'
            f'<span class="micro" style="color:#17181c">87 non lus</span></div>{rows}')

def sheet_ui(w, rows=8, total=None):
    data = [("02/03", "Fournitures", "84,20"), ("05/03", "Abonnement", "29,00"), ("09/03", "Déplacement", "146,50"), ("12/03", "Logiciel", "59,99"),
            ("16/03", "Repas client", "72,40"), ("21/03", "Téléphone", "34,99"), ("24/03", "Formation", "390,00"), ("28/03", "Matériel", "249,00")]
    cols = [140, 360, 200]
    head = "".join(f'<div style="width:{c}px;padding:0 16px" class="micro">{t}</div>' for c, t in zip(cols, ["Date", "Libellé", "Montant"]))
    body = ""
    for k in range(rows):
        d = data[k]
        body += ('<div style="display:flex;height:58px;align-items:center;border-bottom:1px solid #ece7dc">' +
                 "".join(f'<div class="ui" style="width:{c}px;padding:0 16px;font-family:{"Space Mono" if j != 1 else "Instrument Sans"};font-size:{22 if j != 1 else 24}px">{v}</div>'
                         for j, (c, v) in enumerate(zip(cols, d))) + '</div>')
    tot = ""
    if total:
        tot = (f'<div style="display:flex;height:66px;align-items:center;background:#fff7d6;border-top:2px solid #17181c">'
               f'<div style="width:500px;padding:0 16px;font:700 24px/1 Instrument Sans">Total</div>'
               f'<div style="font:700 28px/1 Space Mono">{total}</div></div>')
    grid = ''.join(f'<div class="abs" style="left:{sum(cols[:k+1])}px;top:0;bottom:0;width:1px;background:#ece7dc"></div>' for k in range(2))
    return (f'<div class="abs" style="left:26px;top:26px;width:{sum(cols)}px"><div style="display:flex;height:46px;align-items:center;background:#f3efe6">{head}</div>'
            f'{body}{tot}{grid}</div>')

# ------------------------------------------------------------------ shots
S = {}

# P1 · 2000
S["P01"] = ("dark", lambda: ground("dark", 960, 470, 1400, 1000) + frise(770, years=[(960, "2000")])
    + contact(960, 772, 620) + crt(660, 248)
    + postit(905, 300, rot=-7, scale=1.03, blur=0.6)
    + '<div class="abs fg-blur" style="left:-160px;top:560px;width:420px;height:240px;border-radius:18px;background:linear-gradient(180deg,#d9d2c3,#a9a190);transform:rotate(-8deg)"></div>'
    + sub("Deux mille. Un site internet ? Pas pour moi.", "dark", hl="site internet"))

# P2 · 2010
S["P02"] = ("dark", lambda: ground("dark", 960, 470, 1400, 1000) + frise(770, years=[(960, "2010")])
    + '<div class="abs" style="left:-420px;top:248px;opacity:.5;filter:blur(18px)">' + crt(0, 0) + '</div>'
    + contact(960, 772, 340) + phone10(810, 210)
    + postit(800, 300, rot=6, scale=1.02, blur=0.5)
    + sub("Les réseaux sociaux ? Pas pour moi.", "dark", hl="réseaux sociaux"))

# P3 · 2026
S["P03"] = ("dark", lambda: ground("dark", 960, 430, 1500, 1000) + frise(770, years=[(960, "2026")])
    + contact(960, 772, 760) + laptop(360, 40, 0.98, "dark", ai_screen("dark"), "transform-origin:50% 100%;top:30px")
    + mug(-60, 540, 1.1, blur=12)
    + sub("L’intelligence artificielle ?", "dark", hl="L’intelligence artificielle"))

# P4 · gag (silent)
S["P04"] = ("dark", lambda: ground("dark", 960, 420, 1700, 1000)
    + '<div class="abs mid-blur" style="left:0;right:0;top:120px;text-align:center;font:600 64px/1.2 Instrument Sans;color:#f3f1ec;opacity:.55">Bonjour. Que veux-tu faire aujourd’hui ?</div>'
    + '<div class="abs" style="left:160px;top:330px;width:1600px;height:250px;border-radius:40px;background:#1f232c;border:2px solid rgba(255,255,255,.14);'
      'box-shadow:0 50px 120px rgba(0,0,0,.6);display:flex;align-items:center;padding:0 70px;font:600 100px/1 Instrument Sans;color:#f3f1ec;letter-spacing:-.02em">'
      'Pas pour<span class="caret" style="height:110px;width:7px;margin:0 6px 0 22px"></span><span style="color:rgba(243,241,236,.32)">moi.</span>'
      '<span class="abs" style="left:880px;top:176px;padding:8px 16px;border:2px solid rgba(243,241,236,.3);border-radius:10px;font:700 24px/1 Space Mono;color:rgba(243,241,236,.55);letter-spacing:.1em">TAB</span>'
      '<div class="send" style="right:40px;top:65px;width:120px;height:120px;border-radius:28px"><svg width="56" height="56" viewBox="0 0 30 30"><path d="M15 24 V7 M8 13 L15 6 L22 13" stroke="#17181c" stroke-width="3.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div>'
    + '<div class="abs fg-blur" style="left:-60px;top:-60px;width:2040px;height:110px;background:#2a2d33"></div>'
    + '<div class="abs fg-blur" style="left:-60px;top:-40px;width:120px;height:1200px;background:#2a2d33"></div>'
    + '<div class="abs fg-blur" style="right:-60px;top:-40px;width:120px;height:1200px;background:#2a2d33"></div>')

# P5 · Le problème ? (wide: three eras, three post-its)
def p5():
    h = ground("dark", 960, 470, 1900, 900) + frise(700, years=[(330, "2000"), (960, "2010"), (1590, "2026")])
    h += contact(330, 702, 280) + crt(30, 180, 0.5) + postit(245, 330, rot=-7, scale=0.5)
    h += contact(960, 702, 170) + phone10(810, 142, 0.5) + postit(810, 330, rot=6, scale=0.5)
    h += contact(1590, 702, 380) + laptop(990, -38, 0.5, "dark", ai_screen("dark"), "transform-origin:50% 100%")
    h += postit(1450, 300, rot=-12, scale=0.62, blur=3)
    h += sub("Le problème ?", "dark", hl="problème")
    return h
S["P05"] = ("dark", p5)

# P6 · Le monde, lui, n'a pas attendu.
def p6():
    h = ground("dark", 700, 470, 1700, 900)
    h += '<div class="frise" style="top:700px"></div>'
    for k in range(14):  # streaks of the moving line
        h += f'<div class="abs" style="left:{820 + k*90}px;top:{600 + (k*37) % 170}px;width:{160 + (k*53) % 220}px;height:2px;background:rgba(201,198,191,{.10 + (k%4)*.05:.2f});filter:blur(1px)"></div>'
    h += frise(700, years=[(330, "2026")], ghost=[(1000, "2027", 3), (1330, "2028", 5), (1660, "2029", 8)])
    h += contact(330, 702, 380) + laptop(-270, -38, 0.5, "dark", ai_screen("dark"), "transform-origin:50% 100%")
    h += postit(250, 330, rot=-5, scale=0.5)
    for k, (x, s, b) in enumerate([(930, 0.3, 2), (1250, 0.26, 4), (1560, 0.22, 7)]):
        glow = ai_screen("dark", hello="", field="", caret=False, body='<div class="abs" style="inset:0;background:radial-gradient(closest-side,rgba(255,233,138,.95),rgba(247,208,56,.35))"></div>')
        for g in (3, 2, 1):
            h += f'<div class="abs" style="left:{x - g*60}px;top:{700 - 740*s - 36}px;opacity:{0.12*g:.2f};filter:blur({b+4}px)">' + laptop(0, 0, s, "dark", "", "transform-origin:0 0") + '</div>'
        h += f'<div class="abs" style="left:{x}px;top:{700 - 740*s - 36}px;filter:blur({b}px)">' + laptop(0, 0, s, "dark", glow, "transform-origin:0 0") + '</div>'
    h += sub("Le monde, lui, n’a pas attendu.", "dark", hl="n’a pas attendu")
    return h
S["P06"] = ("dark", p6)

# P7-P9 · the three pains: clock left, app window right (equal margins 165)
def pain(clock_args, title, inner, halo, subtitle, hl):
    h = ground("dark", 960, 470, 1800, 1000).replace("rgba(52,66,102,.55)", halo)
    h += win(575, 110, 1180, 720, title, inner)
    h += clock(315, 430, *clock_args)
    return h + sub(subtitle, "dark", hl=hl)
S["P07"] = ("dark", lambda: pain((22, 47, 300, "dark", "22:47"), "Présentation", slides_ui(1180, 720), "rgba(52,66,102,.6)",
                                  "Ta présentation te prend une soirée.", "une soirée"))
S["P08"] = ("dark", lambda: pain((12, 0, 300, "dark", "12:00"), "Messagerie", inbox_ui(1180), "rgba(120,104,60,.45)",
                                  "Tes mails, ta matinée.", "ta matinée"))
S["P09"] = ("dark", lambda: pain((18, 30, 300, "dark", "18:30", "DIM."), "Compta 2026", sheet_ui(1180), "rgba(70,74,86,.5)",
                                  "Ta compta, ton dimanche.", "ton dimanche"))

# P10 · Pour d'autres, c'est réglé avant le café. (split)
def p10():
    h = ground("dark", 960, 450, 1900, 900)
    h += '<div class="abs micro" style="left:180px;top:116px;color:#c9c6bf;font-size:22px">Toi</div><div class="abs micro" style="left:1040px;top:116px;color:#c9c6bf;font-size:22px">D’autres</div>'
    tasks = [("Présentation", 22, 47, "22:47", None), ("Mails", 12, 0, "12:00", None), ("Compta", 18, 30, "DIM.", "DIM.")]
    for k, (t, hh, mm, dig, lab) in enumerate(tasks):
        y = 170 + k * 210
        h += f'<div class="card dark" style="left:180px;top:{y}px;width:700px;height:170px"></div>'
        h += f'<div class="abs" style="left:220px;top:{y+60}px;font:600 40px/1 Instrument Sans;color:#f3f1ec">{t}</div>'
        h += clock(800, y + 85, hh, mm, 120, "dark", None, None)
        h += f'<div class="abs" style="left:560px;top:{y+66}px;font:700 30px/1 Space Mono;color:#c9c6bf">{dig}</div>'
        h += f'<div class="card dark" style="left:1040px;top:{y}px;width:700px;height:170px"></div>'
        h += f'<div class="abs" style="left:1080px;top:{y+60}px;font:600 40px/1 Instrument Sans;color:#f3f1ec">{t}</div>'
        h += f'<div class="check" style="left:{1640}px;top:{y+57}px">{CHECK}</div>'
    h += mug(1300, 560, 0.85, blur=0)
    return h + sub("Pour d’autres, c’est réglé avant le café.", "dark", hl="avant le café")
S["P10"] = ("dark", p10)

# P11 · pivot on black
def p11():
    h = '<div class="g-dark" style="background:#0a0b0f"></div>'
    for g in (4, 3, 2, 1):
        h += postit(810, 60 - g * 34, rot=18, scale=1, blur=6, opacity=0.10 * (5 - g))
    h += postit(810, 60, rot=18, scale=1, blur=2.5)
    h += ('<div class="type" style="top:560px">Pas <span class="pk">cette fois.' + BRUSH.replace('<svg ', '<svg style="bottom:-.16em;height:.26em" ') + '</span></div>')
    return h
S["P11"] = ("dark", p11)

# P12 · Aujourd'hui, l'IA (light, flash residue)
def p12():
    h = ground("light", 960, 460, 1700, 1000)
    h += '<div class="abs" style="left:360px;top:60px;width:1200px;height:800px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,255,255,.95),rgba(255,251,230,.55) 45%,rgba(255,251,230,0))"></div>'
    body = ('<div class="abs" style="left:150px;top:300px;width:720px;padding:26px 30px;border-radius:20px;background:#f3efe6">'
            '<div class="line" style="width:92%;margin-bottom:16px"></div><div class="line" style="width:78%;margin-bottom:16px"></div><div class="line" style="width:40%"></div></div>')
    h += contact(960, 812, 800, "light")
    h += laptop(360, 80, 0.98, "light", ai_screen("light", hello="Bonjour. Que veux-tu faire aujourd’hui ?", body=body), "transform-origin:50% 100%;filter:blur(1.2px)")
    return h + sub("Aujourd’hui, l’IA rédige, résume, calcule.", "light", hl="l’IA", upto=2)
S["P12"] = ("light", p12)

# P13 · rédige, résume, calcule (triptych, margins 140)
def p13():
    h = ground("light", 960, 470, 1900, 900)
    xs = [140, 710, 1280]
    # rédige
    doc = ('<div class="micro" style="color:#55565c;margin-bottom:22px">Présentation de lundi</div>'
           '<div style="font:600 34px/1.15 Instrument Sans;color:#17181c;margin-bottom:24px">1. Où en est le projet</div>'
           + "".join(f'<div class="line" style="width:{w}%;margin-bottom:16px"></div>' for w in (96, 88, 92, 70))
           + '<div style="font:600 34px/1.15 Instrument Sans;color:#17181c;margin:26px 0 24px">2. Ce qui chan<span class="caret" style="height:34px;margin-left:3px"></span></div>')
    h += f'<div class="card" style="left:{xs[0]}px;top:180px;width:500px;height:600px;padding:40px 40px;opacity:.9;filter:blur(1.2px)">{doc}</div>'
    # résume
    stack = "".join(f'<div class="abs" style="left:{40 + k*8}px;top:{90 + k*12}px;width:{420 - k*16}px;height:70px;border-radius:12px;background:#fff;border:1px solid #e1dccf;opacity:{.35 + k*.08:.2f}"></div>' for k in range(5))
    summ = ('<div class="abs" style="left:40px;top:250px;width:420px;padding:26px;border-radius:16px;background:#fff7d6;border:2px solid #17181c">'
            '<div class="micro" style="color:#17181c;margin-bottom:18px">Résumé · 3 points</div>'
            + "".join(f'<div style="display:flex;gap:12px;align-items:center;margin-bottom:14px"><span style="width:10px;height:10px;border-radius:50%;background:#17181c"></span><div class="line" style="width:{w}%;background:#e8dfc0"></div></div>' for w in (86, 72, 64)) + '</div>')
    h += (f'<div class="card" style="left:{xs[1]}px;top:180px;width:500px;height:600px;opacity:.9;filter:blur(1.2px)">'
          f'<div class="abs micro" style="left:40px;top:40px;color:#55565c">12 messages</div>{stack}{summ}</div>')
    # calcule (active)
    h += f'<div class="card" style="left:{xs[2]}px;top:180px;width:500px;height:600px;overflow:hidden">' + \
         '<div class="abs micro" style="left:40px;top:40px;color:#55565c">Compta 2026</div>' + \
         '<div class="abs" style="left:-6px;top:70px;transform:scale(.72);transform-origin:0 0">' + sheet_ui(700, 7, "1 066,08 €") + '</div></div>'
    return h + sub("Aujourd’hui, l’IA rédige, résume, calcule.", "light", hl="l’IA")
S["P13"] = ("light", p13)

# P14 · Tu lui expliques avec tes mots... (prompt field, light, rhyme of P4)
S["P14"] = ("light", lambda: ground("light", 960, 420, 1700, 1000)
    + '<div class="abs mid-blur" style="left:0;right:0;top:120px;text-align:center;font:600 64px/1.2 Instrument Sans;color:#17181c;opacity:.4">Bonjour. Que veux-tu faire aujourd’hui ?</div>'
    + '<div class="abs" style="left:160px;top:330px;width:1600px;height:250px;border-radius:40px;background:#fff;border:2px solid rgba(23,24,28,.12);'
      'box-shadow:0 40px 100px rgba(60,45,20,.16);display:flex;align-items:center;padding:0 200px 0 70px;font:600 46px/1.2 Instrument Sans;color:#17181c;letter-spacing:-.015em">'
      '<span>Prépare ma présentation de lundi à partir de mes notes.<span class="caret" style="height:60px;width:6px;margin-left:8px"></span></span>'
      '<div class="send" style="right:40px;top:65px;width:120px;height:120px;border-radius:28px"><svg width="56" height="56" viewBox="0 0 30 30"><path d="M15 24 V7 M8 13 L15 6 L22 13" stroke="#17181c" stroke-width="3.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div></div>'
    + '<div class="abs fg-blur" style="left:-60px;top:-60px;width:2040px;height:110px;background:#c9ccd2"></div>'
    + '<div class="abs fg-blur" style="left:-60px;top:-40px;width:120px;height:1200px;background:#c9ccd2"></div>'
    + '<div class="abs fg-blur" style="right:-60px;top:-40px;width:120px;height:1200px;background:#c9ccd2"></div>'
    + sub("Tu lui expliques avec tes mots…", "light", hl="avec tes mots"))

# P15 · elle fait le travail. (deck builds itself)
def p15():
    h = ground("light", 960, 450, 1900, 900)
    h += ('<div class="abs" style="left:460px;top:70px;width:1000px;height:96px;border-radius:24px;background:#fff;border:2px solid rgba(23,24,28,.12);'
          'box-shadow:0 20px 50px rgba(60,45,20,.12);display:flex;align-items:center;padding:0 30px;font:600 28px/1 Instrument Sans;color:#55565c">'
          'Prépare ma présentation de lundi à partir de mes notes.</div>')
    h += '<div class="abs" style="left:1352px;top:52px;width:132px;height:132px;border-radius:50%;border:4px solid #f7d038;opacity:.8"></div>'
    h += '<div class="send" style="left:1388px;top:88px;width:60px;height:60px;transform:scale(.9)">' + ARROW + '</div>'
    h += cursor(1420, 120)
    for k in range(10):
        r, c = divmod(k, 5)
        x, y = 150 + c * 330, 260 + r * 230
        late = k >= 8
        st = f"transform:scale({1.35 if late else 1}) translate({ -30 if late else 0}px,{-40 if late else 0}px);filter:blur({8 if late else 0}px);opacity:{.7 if late else 1}"
        content = (f'<div class="abs" style="left:22px;top:22px;width:{120 + (k*29)%110}px;height:18px;border-radius:5px;background:#17181c"></div>'
                   + ("".join(f'<div class="abs line" style="left:22px;top:{60 + j*24}px;width:{200 - j*40 - (k*13)%40}px;height:10px"></div>' for j in range(3)) if k % 3 else
                      "".join(f'<div class="abs" style="left:{36 + j*52}px;bottom:24px;width:34px;height:{30 + (j*k*17)%70}px;border-radius:4px;background:{"#f7d038" if j == 3 else "#d8d2c4"}"></div>' for j in range(4))))
        h += f'<div class="card" style="left:{x}px;top:{y}px;width:300px;height:169px;border-radius:10px;{st}">{content}</div>'
    return h + sub("elle fait le travail.", "light", pk="le travail")
S["P15"] = ("light", p15)

# P16 · Pas besoin d'être technique : (code card falls)
def p16():
    h = ground("light", 960, 450, 1900, 900)
    h += ('<div class="abs" style="left:700px;top:300px;width:1100px;height:150px;border-radius:32px;background:#fff;border:2px solid rgba(23,24,28,.12);'
          'box-shadow:0 30px 80px rgba(60,45,20,.14);display:flex;align-items:center;padding:0 40px;font:600 36px/1.2 Instrument Sans;color:#17181c">'
          'Prépare ma présentation de lundi à partir de mes notes.</div>')
    code = ('<b>import</b> pandas <b>as</b> pd\n<b>def</b> build_deck(notes, n=10):\n    df = pd.read_csv(notes)\n    slides = [s <b>for</b> s <b>in</b> df.groupby(<b>"theme"</b>)]\n'
            '    <b>return</b> render(slides[:n])\n<b>if</b> __name__ == <b>"__main__"</b>:\n    build_deck(<b>"notes.csv"</b>)')
    for g in (2, 1):
        h += f'<div class="card dark" style="left:{60 - g*20}px;top:{470 - g*70}px;width:760px;height:380px;transform:rotate({-16 + g*2}deg);opacity:{.12*g:.2f};filter:blur(10px)"></div>'
    h += (f'<div class="card dark" style="left:60px;top:470px;width:760px;height:380px;padding:38px 40px;transform:rotate(-16deg);filter:blur(2.5px)">'
          f'<div class="code">{code}</div></div>')
    return h + sub("Pas besoin d’être technique :", "light", hl="technique")
S["P16"] = ("light", p16)

# P17 · il faut juste apprendre à lui parler. (chat)
def p17():
    h = ground("light", 960, 450, 1900, 900)
    h += '<div class="card" style="left:360px;top:90px;width:1200px;height:740px"></div>'
    h += '<div class="abs" style="left:360px;top:90px;width:1200px;height:70px;display:flex;align-items:center;gap:12px;padding:0 32px;border-bottom:1px solid #ece7dc;font:600 24px/1 Instrument Sans;color:#17181c"><span class="ai-dot"></span>Assistant IA</div>'
    bubbles = [("r", "Prépare ma présentation de lundi.", 200), ("l", "Voici 10 diapos. Je les raccourcis ?", 330), ("r", "Oui, et ajoute un graphique.", 460)]
    for side, txt, y in bubbles:
        if side == "r":
            h += f'<div class="abs" style="right:{1920-1510}px;top:{y}px;padding:24px 30px;border-radius:26px 26px 6px 26px;background:#efebe2;font:500 32px/1.2 Instrument Sans;color:#17181c">{txt}</div>'
        else:
            h += f'<div class="abs" style="left:410px;top:{y}px;padding:24px 30px;border-radius:26px 26px 26px 6px;background:#fff;border:1px solid #e1dccf;font:500 32px/1.2 Instrument Sans;color:#17181c;display:flex;gap:14px;align-items:center"><span class="ai-dot"></span>{txt}</div>'
    h += ('<div class="abs" style="left:410px;top:610px;width:1100px;height:110px;border-radius:24px;background:#fff;border:2px solid rgba(23,24,28,.14);display:flex;align-items:center;padding:0 30px;'
          'font:500 30px/1 Instrument Sans;color:#8d8a84">Écris ta demande…<span class="caret" style="height:36px;margin-left:6px"></span>'
          '<div class="send" style="right:24px;top:24px">' + ARROW + '</div></div>')
    return h + sub("il faut juste apprendre à lui parler.", "light", pk="apprendre à lui parler")
S["P17"] = ("light", p17)

# P18 · tu récupères ta soirée, ta matinée, ton dimanche (three tiles, margins 160)
def p18():
    h = ground("light", 960, 450, 1900, 900)
    tiles = [("Soirée", 18, 0, "18:00", None, (0, 167)), ("Matinée", 8, 30, "08:30", None, (180, 360)), ("Dimanche", 10, 0, "DIM.", "DIM.", (0, 359))]
    for k, (t, hh, mm, dig, lab, arc) in enumerate(tiles):
        x = 160 + k * 560
        h += f'<div class="card" style="left:{x}px;top:140px;width:480px;height:640px"></div>'
        h += clock(x + 240, 360, hh, mm, 280, "light", None, lab, arc=arc)
        h += f'<div class="abs" style="left:{x}px;width:480px;top:560px;text-align:center;font:600 46px/1 Instrument Sans;color:#17181c">{t}</div>'
        h += f'<div class="abs" style="left:{x}px;width:480px;top:640px;text-align:center"><span class="pill" style="background:#f7d038;color:#17181c;font-size:22px">Libre</span></div>'
        h += f'<div class="abs" style="left:{x}px;width:480px;top:600px;text-align:center;font:700 26px/1 Space Mono;color:#55565c;letter-spacing:.06em;display:none">{dig}</div>'
    return h + sub("ta matinée, ton dimanche.", "light")
S["P18"] = ("light", p18)

# P19 · L'intelligence artificielle ? (rhyme: laptop on the paper frise, the post-it lands again)
S["P19"] = ("light", lambda: ground("light", 960, 430, 1500, 1000) + frise(770, "light", years=[(960, "2026")])
    + contact(960, 772, 760, "light") + laptop(360, 30, 0.98, "light", ai_screen("light"), "transform-origin:50% 100%")
    + postit(870, 230, rot=-14, scale=1.25, blur=5, opacity=.9)
    + sub("L’intelligence artificielle ?", "light", hl="L’intelligence artificielle"))

# P20 · Cette fois... c'est pour toi. (strike "Pas")
def p20():
    h = ground("light", 960, 430, 1500, 1000)
    h += '<div class="abs mid-blur" style="left:260px;top:-40px;width:1400px;height:900px;border-radius:30px;background:#c9ccd2;opacity:.55"></div>'
    h += postit(810, 210, rot=-5, scale=2.15, strike=True, extra="transform-origin:50% 0")
    h += ('<svg class="abs" style="left:1210px;top:300px;transform:rotate(28deg)" width="60" height="420" viewBox="0 0 60 420">'
          '<rect x="12" y="40" width="36" height="360" rx="8" fill="#17181c"/><path d="M12 40 L30 0 L48 40 Z" fill="#e9e4d8"/><path d="M24 14 L30 0 L36 14 Z" fill="#17181c"/></svg>')
    return h + sub("Cette fois… c’est pour toi.", "light", pk="pour toi")
S["P20"] = ("light", p20)

# P21 · Apprends l'IA dès aujourd'hui. (end card, post-it folded into the button)
def button(x, y, pressed=False):
    fill = "#e9bf22" if pressed else "#f7d038"
    sc = .96 if pressed else 1
    return (f'<div class="abs" style="left:{x-120}px;top:{y-140}px;width:960px;height:440px;border-radius:50%;background:radial-gradient(closest-side,rgba(247,208,56,.28),rgba(247,208,56,0))"></div>'
            f'<div class="abs" style="left:{x}px;top:{y}px;width:720px;height:160px;border-radius:16px;background:linear-gradient(180deg,#ffe066,{fill} 40%);'
            f'box-shadow:0 30px 70px rgba(0,0,0,.5),inset 0 -6px 0 rgba(201,154,6,.5);display:flex;align-items:center;justify-content:center;transform:scale({sc})">'
            f'<span class="cta">Apprendre l’IA</span>'
            f'<div class="abs" style="right:0;top:0;width:54px;height:54px;border-radius:0 16px 0 0;background:linear-gradient(225deg,#0d0f14 50%,#fff3b0 51%,#e9bf22 100%)"></div></div>')
def p21():
    h = ground("dark", 960, 470, 1500, 900)
    h += '<div class="abs" style="inset:0;opacity:.6">' + frise(660, years=[(560, "2000"), (960, "2010"), (1360, "2026")]) + '</div>'
    h += button(600, 360)
    h += cursor(1480, 700, 1.3, blur=3)
    return h + sub("Apprends l’IA dès aujourd’hui.", "dark", hl="Apprends l’IA")
S["P21"] = ("dark", p21)

def p22():
    h = ground("dark", 960, 470, 1500, 900)
    h += '<div class="abs" style="inset:0;opacity:.6">' + frise(660, years=[(560, "2000"), (960, "2010"), (1360, "2026")]) + '</div>'
    h += '<div class="abs" style="left:440px;top:200px;width:1040px;height:480px;border-radius:50%;border:5px solid rgba(247,208,56,.55)"></div>'
    h += '<div class="abs" style="left:540px;top:260px;width:840px;height:360px;border-radius:50%;border:3px solid rgba(247,208,56,.3)"></div>'
    h += button(600, 360, pressed=True)
    h += cursor(1190, 450, 1.3)
    return h
S["P22"] = ("dark", p22)

for name, (theme, fn) in S.items():
    (OUT / f"{name}.html").write_text(page(fn() + finish(theme), name), encoding="utf-8")
print(len(S), "styleframes in", OUT)
