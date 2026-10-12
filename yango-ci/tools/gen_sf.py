"""Styleframes of the Yango film « On dit combien ? »: one key image per shot, <project>/styleframes/Pxx.html.
Street scenes are flat SVG illustrations; subtitles, bubbles and the (generic, provisional) app are HTML/CSS."""
import math, pathlib, sys

OUT = pathlib.Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
RED, TAXI, ROAD, WALK, INK = "#ff3b30", "#f28c28", "#3a3b42", "#d8c3a0", "#17181c"
SKIN = ["#6b3f26", "#8a5a3b", "#4a2a19"]

def page(body, title):
    return (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{title}</title><link rel="stylesheet" href="_kit.css"></head>'
            f'<body><div id="stage">{body}<div class="grain"></div><div class="vignette"></div></div></body></html>')

def svg(inner, extra=""):
    return f'<svg class="scene" viewBox="0 0 1920 1080" style="{extra}">{DEFS}{inner}</svg>'

DEFS = ('<defs>'
        '<linearGradient id="dawn" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3c98f"/><stop offset=".55" stop-color="#f9e2bd"/><stop offset="1" stop-color="#fdf0dc"/></linearGradient>'
        '<linearGradient id="noon" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe9b8"/><stop offset="1" stop-color="#fff7e6"/></linearGradient>'
        '<linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f1c33"/><stop offset=".6" stop-color="#4a3554"/><stop offset="1" stop-color="#e3784c"/></linearGradient>'
        '<radialGradient id="sunglow"><stop offset="0" stop-color="#fff6d8"/><stop offset=".35" stop-color="#ffe2a0" stop-opacity=".8"/><stop offset="1" stop-color="#ffe2a0" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="lamp"><stop offset="0" stop-color="#ffd98a" stop-opacity=".75"/><stop offset="1" stop-color="#ffd98a" stop-opacity="0"/></radialGradient>'
        '<radialGradient id="redglow"><stop offset="0" stop-color="#ff8a80" stop-opacity=".9"/><stop offset=".4" stop-color="#ff3b30" stop-opacity=".35"/><stop offset="1" stop-color="#ff3b30" stop-opacity="0"/></radialGradient>'
        '<filter id="b4"><feGaussianBlur stdDeviation="4"/></filter><filter id="b10"><feGaussianBlur stdDeviation="10"/></filter>'
        '<filter id="b18"><feGaussianBlur stdDeviation="18"/></filter><filter id="mx"><feGaussianBlur stdDeviation="22 2"/></filter>'
        '</defs>')

# ------------------------------------------------------------------ street kit
def sky(kind):
    return f'<rect width="1920" height="1080" fill="url(#{kind})"/>'

def skyline(y=720, op=.32, col="#5d6a8a", seed=1):
    out = []
    x = -40
    k = seed
    while x < 1960:
        w = 70 + (k * 37) % 90; h = 120 + (k * 53) % 260
        out.append(f'<rect x="{x}" y="{y - h}" width="{w}" height="{h}" fill="{col}" opacity="{op}"/>')
        for wy in range(int(y - h + 18), y - 10, 26):
            out.append(f'<rect x="{x + 12}" y="{wy}" width="{w - 24}" height="6" fill="#fff" opacity="{op * .35:.2f}"/>')
        x += w + 18 + (k * 11) % 40; k += 1
    return "".join(out)

def palm(x, y, s=1, col="#2f6b46", trunk="#7a5a3a"):
    leaves = "".join(f'<path d="M0 -330 Q {120*math.cos(a):.0f} {-330 - 90*math.sin(a) - 40:.0f} {230*math.cos(a):.0f} {-330 + 60 - 120*math.sin(a):.0f} '
                     f'Q {110*math.cos(a):.0f} {-330 - 20*math.sin(a):.0f} 0 -330 Z" fill="{col}"/>'
                     for a in (0.25, 0.9, 1.6, 2.25, 2.9, 3.6))
    return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-10 0 Q 12 -170 -4 -335 L 10 -335 Q 30 -170 14 0 Z" fill="{trunk}"/>{leaves}</g>')

def street(walk_y=720, road_y=790, dashes=True, night=False):
    walk = "#c9b28f" if not night else "#4b4350"
    road = ROAD if not night else "#26262e"
    d = "".join(f'<rect x="{x}" y="{road_y + 62}" width="120" height="10" rx="5" fill="#f2efe6" opacity="{.8 if not night else .45}"/>' for x in range(-60, 1980, 240)) if dashes else ""
    return (f'<rect x="0" y="{walk_y}" width="1920" height="{road_y - walk_y}" fill="{walk}"/>'
            f'<rect x="0" y="{road_y - 8}" width="1920" height="10" fill="{"#efe4cf" if not night else "#6b6070"}"/>'
            f'<rect x="0" y="{road_y}" width="1920" height="{1080 - road_y}" fill="{road}"/>{d}')

def sign(x, y, text, s=1):
    w = 40 + len(text) * 24
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-7" y="-420" width="14" height="420" fill="#8b8f98"/>'
            f'<rect x="{-w/2}" y="-470" width="{w}" height="90" rx="10" fill="#1f6b4a" stroke="#fff" stroke-width="5"/>'
            f'<text x="0" y="-410" text-anchor="middle" font-family="Instrument Sans" font-weight="700" font-size="44" fill="#fff">{text}</text></g>')

def sun(x, y, r=70):
    return f'<circle cx="{x}" cy="{y}" r="{r*4}" fill="url(#sunglow)"/><circle cx="{x}" cy="{y}" r="{r}" fill="#fff4d0"/>'

def streetlight(x, y, h=520, on=True):
    glow = f'<ellipse cx="{x - 70}" cy="{y - 40}" rx="260" ry="90" fill="url(#lamp)"/><path d="M{x - 92} {y - h + 30} L {x - 260} {y} L {x + 80} {y} Z" fill="#ffd98a" opacity=".12"/>' if on else ""
    return (f'{glow}<rect x="{x - 6}" y="{y - h}" width="12" height="{h}" fill="#2a2a33"/>'
            f'<path d="M{x} {y - h} Q {x} {y - h - 30} {x - 90} {y - h - 24}" stroke="#2a2a33" stroke-width="10" fill="none"/>'
            f'<ellipse cx="{x - 92}" cy="{y - h - 16}" rx="30" ry="12" fill="{"#ffe7a8" if on else "#555"}"/>')

def person(x, y, s=1, skin=0, shirt="#f4f2ee", trousers="#2a2d3a", tie="#b8432f", hand_up=False, shoes="shoes",
           bag=None, lean=0, hair="#1a1410", dress=None, flip=False, eyes=True):
    sk = SKIN[skin]
    legs = (f'<rect x="-40" y="-200" width="34" height="200" rx="12" fill="{trousers}"/>'
            f'<rect x="6" y="-200" width="34" height="200" rx="12" fill="{trousers}"/>') if not dress else \
           (f'<path d="M-70 -230 L 70 -230 L 88 -10 L -88 -10 Z" fill="{dress}"/><rect x="-34" y="-12" width="22" height="12" fill="{sk}"/><rect x="12" y="-12" width="22" height="12" fill="{sk}"/>')
    if shoes == "shoes":
        feet = '<ellipse cx="-24" cy="-4" rx="30" ry="12" fill="#111"/><ellipse cx="24" cy="-4" rx="30" ry="12" fill="#111"/>'
    else:
        feet = (f'<ellipse cx="-24" cy="-6" rx="24" ry="10" fill="{sk}"/><ellipse cx="24" cy="-6" rx="24" ry="10" fill="{sk}"/>'
                '<rect x="-52" y="-2" width="56" height="7" rx="3" fill="#2f8de4"/><rect x="-4" y="-2" width="56" height="7" rx="3" fill="#2f8de4"/>'
                '<path d="M-36 -8 L -24 -14 L -12 -8" stroke="#2f8de4" stroke-width="5" fill="none"/><path d="M12 -8 L 24 -14 L 36 -8" stroke="#2f8de4" stroke-width="5" fill="none"/>')
    torso = f'<rect x="-68" y="-390" width="136" height="205" rx="46" fill="{shirt}"/>'
    tie_s = f'<path d="M-9 -372 L 9 -372 L 14 -260 L 0 -240 L -14 -260 Z" fill="{tie}"/>' if tie else ""
    arm_l = f'<rect x="-92" y="-376" width="32" height="170" rx="16" fill="{shirt}"/><circle cx="-76" cy="-200" r="17" fill="{sk}"/>'
    if hand_up:
        arm_r = f'<g transform="rotate(-158 70 -360)"><rect x="56" y="-376" width="32" height="170" rx="16" fill="{shirt}"/><circle cx="72" cy="-200" r="18" fill="{sk}"/></g>'
    else:
        arm_r = f'<rect x="60" y="-376" width="32" height="170" rx="16" fill="{shirt}"/><circle cx="76" cy="-200" r="17" fill="{sk}"/>'
    bag_s = ""
    if bag == "case":
        bag_s = '<rect x="-112" y="-206" width="76" height="58" rx="8" fill="#5a3a22"/><rect x="-88" y="-216" width="28" height="12" rx="5" fill="none" stroke="#5a3a22" stroke-width="5"/>'
    elif bag == "back":
        bag_s = '<rect x="-96" y="-380" width="40" height="150" rx="16" fill="#2f6bd4"/>'
    neck = f'<rect x="-14" y="-412" width="28" height="30" fill="{sk}"/>'
    head = f'<circle cx="0" cy="-458" r="50" fill="{sk}"/><path d="M-50 -470 Q -48 -520 0 -514 Q 48 -520 50 -470 Q 40 -496 0 -494 Q -40 -496 -50 -470 Z" fill="{hair}"/>'
    ey = '<circle cx="-16" cy="-456" r="5" fill="#1a1410"/><circle cx="16" cy="-456" r="5" fill="#1a1410"/>' if eyes else ""
    tr = f'translate({x} {y}) scale({-s if flip else s} {s}) rotate({lean})'
    return f'<g transform="{tr}">{bag_s}{legs}{feet}{arm_l}{torso}{tie_s}{arm_r}{neck}{head}{ey}</g>'

def car(x, y, s=1, color=TAXI, taxi=True, driver=True, flip=False, stripe=False, blur=False, open_door=False, night=False):
    win = "#253042" if not night else "#151a24"
    drv = ('<g><circle cx="-60" cy="-230" r="30" fill="#4a2a19"/><path d="M-92 -240 Q -60 -282 -28 -240 Z" fill="#20263a"/>'
           '<rect x="-96" y="-206" width="72" height="20" rx="8" fill="#3c4a63"/></g>') if driver else ""
    roof = ('<rect x="-60" y="-326" width="110" height="34" rx="8" fill="#fff6e0" stroke="#17181c" stroke-width="3"/>'
            '<text x="-5" y="-301" text-anchor="middle" font-family="Instrument Sans" font-weight="700" font-size="22" fill="#17181c">TAXI</text>') if taxi else ""
    stripe_s = f'<rect x="-300" y="-118" width="600" height="14" fill="{RED}"/>' if stripe else ""
    door = ('<path d="M-30 -186 L 130 -186 L 130 -70 L -30 -70 Z" fill="#000" opacity=".25"/>'
            f'<path d="M130 -186 L 230 -230 L 230 -110 L 130 -70 Z" fill="{color}" stroke="#00000022" stroke-width="2"/>') if open_door else ""
    body = (f'<path d="M-310 -70 Q -318 -150 -270 -178 L -170 -196 L -110 -286 Q -96 -300 -70 -300 L 150 -300 Q 180 -300 200 -280 L 260 -196 '
            f'L 300 -186 Q 330 -176 326 -120 L 322 -70 Z" fill="{color}"/>'
            f'<path d="M-160 -196 L -104 -278 L 30 -278 L 30 -196 Z" fill="{win}"/>'
            f'<path d="M48 -196 L 48 -278 L 146 -278 Q 162 -278 176 -262 L 228 -196 Z" fill="{win}"/>'
            f'{drv}{stripe_s}<rect x="-318" y="-92" width="30" height="16" rx="6" fill="#fff3c4"/><rect x="300" y="-96" width="24" height="18" rx="6" fill="#c33"/>'
            f'<circle cx="-185" cy="-62" r="58" fill="#15161a"/><circle cx="-185" cy="-62" r="26" fill="#9aa0aa"/>'
            f'<circle cx="190" cy="-62" r="58" fill="#15161a"/><circle cx="190" cy="-62" r="26" fill="#9aa0aa"/>'
            f'<ellipse cx="0" cy="-2" rx="330" ry="14" fill="#000" opacity=".25"/>{roof}{door}')
    f = ' filter="url(#mx)"' if blur else ""
    return f'<g transform="translate({x} {y}) scale({-s if flip else s} {s})"{f}>{body}</g>'

def price_tag(x, y, text, rot=-6, s=1, blur=False):
    f = ' filter="url(#b4)"' if blur else ""
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"{f}><path d="M0 -150 L 0 -80" stroke="#8a7a60" stroke-width="3"/>'
            f'<rect x="-185" y="-80" width="370" height="110" rx="22" fill="#fff" stroke="#17181c" stroke-width="5"/>'
            f'<circle cx="-155" cy="-25" r="11" fill="none" stroke="#17181c" stroke-width="5"/>'
            f'<text x="22" y="-6" text-anchor="middle" font-family="Space Mono" font-weight="700" font-size="50" fill="#17181c">{text}</text></g>')

def headlights(y, n=5, night=True):
    out = []
    for k in range(n):
        x = 100 + k * 400 + (k * 37) % 120
        out.append(f'<rect x="{x}" y="{y + (k % 2) * 40}" width="{300 + (k*61) % 200}" height="10" rx="5" fill="#fff2c2" opacity=".55" filter="url(#b4)"/>')
        out.append(f'<rect x="{x + 80}" y="{y + 70 + (k % 2) * 40}" width="{200 + (k*43) % 160}" height="8" rx="4" fill="#ff5a4a" opacity=".45" filter="url(#b4)"/>')
    return "".join(out)

# ------------------------------------------------------------------ html bits
def sub(text, theme="dark", hl=None, pk=None, upto=None):
    marks = []
    for kind, sx in (("hl", hl), ("pk", pk)):
        if sx:
            k = text.index(sx); marks.append((k, k + len(sx), kind))
    marks.sort(); pos, pieces = 0, []
    for a, b, kind in marks:
        if a > pos: pieces.append(("t", text[pos:a]))
        pieces.append((kind, text[a:b])); pos = b
    if pos < len(text): pieces.append(("t", text[pos:]))
    html, n = [], 0
    for kind, seg in pieces:
        if kind == "t":
            for j, w in enumerate(seg.split(" ")):
                if w == "": html.append(" "); continue
                html.append(f'<span class="w{" off" if upto is not None and n >= upto else ""}">{w}</span>'); n += 1
                if j < len(seg.split(" ")) - 1: html.append(" ")
        else:
            cls = "w" + (" off" if upto is not None and n >= upto else "")
            n += len([w for w in seg.split(" ") if w])
            html.append(f'<span class="{cls} hl">{seg}</span>' if kind == "hl" else f'<span class="{cls} pk">{seg}{BRUSH}</span>')
    return f'<div class="sub {theme}">{"".join(html)}</div>'

BRUSH = ('<svg viewBox="0 0 400 30" preserveAspectRatio="none"><path d="M6 22 C 70 16, 150 13, 230 11 C 300 9, 360 6, 396 3 '
         'C 398 6, 396 9, 392 10 C 330 15, 250 19, 170 22 C 110 24, 50 27, 10 28 C 2 28, 1 23, 6 22 Z" fill="#ff3b30"/></svg>')

def bubble(x, y, text, tail="tl", mono=False, extra=""):
    return f'<div class="bubble {tail}{" mono" if mono else ""}" style="left:{x}px;top:{y}px;{extra}">{text}</div>'

def mapsvg(w=390, h=844, route=True, car_at=None, pin=(250, 520), night=False):
    roads = ("".join(f'<path d="{d}" stroke="#ffffff" stroke-width="{sw}" fill="none" stroke-linecap="round"/>' for d, sw in
             [("M-20 300 L 420 260", 16), ("M120 -20 L 170 880", 14), ("M-20 620 Q 200 560 420 640", 16), ("M300 -20 L 260 880", 10), ("M-20 450 L 420 470", 10)]))
    water = '<path d="M-20 720 Q 140 690 420 760 L 420 880 L -20 880 Z" fill="#cfe3f2"/>'
    parks = '<rect x="190" y="320" width="60" height="110" rx="14" fill="#d9ecd6"/><rect x="20" y="480" width="80" height="90" rx="14" fill="#d9ecd6"/>'
    r = ""
    if route:
        r = f'<path d="M170 140 L 155 300 Q 150 360 200 400 L {pin[0]} {pin[1]}" stroke="{RED}" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
    p = (f'<circle cx="{pin[0]}" cy="{pin[1]}" r="34" fill="{RED}" opacity=".18"/><circle cx="{pin[0]}" cy="{pin[1]}" r="14" fill="{RED}" stroke="#fff" stroke-width="5"/>')
    c = ""
    if car_at:
        cx, cy = car_at
        c = (f'<g transform="translate({cx} {cy}) rotate(80)"><rect x="-24" y="-13" width="48" height="26" rx="9" fill="#fff" stroke="#17181c" stroke-width="3"/>'
             f'<rect x="-10" y="-13" width="6" height="26" fill="{RED}"/></g>')
    return f'<svg width="{w}" height="{h}" viewBox="0 0 390 844" style="position:absolute;left:0;top:0"><rect width="390" height="844" fill="#eceff2"/>{water}{parks}{roads}{r}{p}{c}</svg>'

def phone(x, y, screen, s=1, rot=0, extra=""):
    if y == 98 and s == 1: y, s = -10, .82
    return (f'<div class="phone" style="left:{x}px;top:{y}px;transform:rotate({rot}deg) scale({s});transform-origin:50% 50%;{extra}">'
            f'<div class="phone-screen">{screen}</div><div class="phone-island"></div></div>')

def light_bg(hx=960, hy=470):
    return (f'<div class="abs" style="inset:0;background:#f6f5f2"></div>'
            f'<div class="abs" style="left:{hx-800}px;top:{hy-520}px;width:1600px;height:1040px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,59,48,.10),rgba(255,59,48,0))"></div>'
            '<div class="abs" style="inset:-40px;background-image:radial-gradient(rgba(23,24,28,.06) 1.3px,transparent 1.8px);background-size:36px 36px"></div>')

TAP = lambda x, y: (f'<div class="abs" style="left:{x-60}px;top:{y-60}px;width:120px;height:120px;border-radius:50%;border:5px solid {RED};opacity:.7"></div>'
                    f'<div class="abs" style="left:{x-30}px;top:{y-30}px;width:60px;height:60px;border-radius:50%;background:rgba(255,255,255,.85);border:4px solid #17181c"></div>')

# ------------------------------------------------------------------ shots
S = {}
DAWN = lambda: sky("dawn") + sun(1500, 330, 60) + skyline(720, .30, "#7d7f9a", 3)

S["P01"] = lambda: svg(DAWN() + palm(250, 720, 1.1) + palm(1700, 720, .9) + street() + sign(1260, 720, "Riviera 2")
                       + person(760, 760, 1.0, bag="case")
                       + '<text x="560" y="250" font-family="Space Mono" font-weight="700" font-size="120" fill="#17181c" opacity=".85">07:00</text>') \
    + sub("Lundi, sept heures. Carrefour Riviera Deux.", "dark", hl="Riviera Deux")

S["P02"] = lambda: svg(DAWN() + palm(1650, 720, 1) + street() + sign(260, 720, "Riviera 2", .9)
                       + car(1240, 880, 1.05, blur=False) + person(560, 760, 1.05, hand_up=True, bag="case")
                       + '<g opacity=".5" filter="url(#mx)"><rect x="1560" y="830" width="360" height="12" fill="#fff"/><rect x="1600" y="900" width="300" height="8" fill="#fff"/></g>') \
    + sub("Tu lèves la main. Un taxi s'arrête.", "dark", hl="Un taxi")

S["P03"] = lambda: svg(DAWN() + street() + car(1180, 880, 1.45, driver=True)
                       + person(560, 860, 1.22, bag="case", lean=10)) \
    + bubble(820, 250, "Plateau ?", "tl") + sub("« Plateau ? »", "dark", hl="Plateau")

S["P04"] = lambda: svg(DAWN() + street() + person(960, 870, 1.32, bag="case")
                       + '<rect x="0" y="0" width="1920" height="1080" fill="#000" opacity=".08"/>'
                       + '<rect x="700" y="420" width="520" height="6" fill="#fffaf0" opacity=".85"/><rect x="700" y="420" width="520" height="120" fill="#fffaf0" opacity=".10"/>'
                       + '<path d="M0 0 L 520 0 Q 380 300 420 1080 L 0 1080 Z" fill="#253042" opacity=".9"/><path d="M1920 0 L 1400 0 Q 1540 300 1500 1080 L 1920 1080 Z" fill="#253042" opacity=".9"/>') \
    + sub("Le chauffeur te regarde… de la tête aux pieds.", "dark", hl="de la tête aux pieds")

S["P05"] = lambda: svg(DAWN() + street() + car(1400, 880, 1.05) + person(620, 760, 1.05, bag="case")
                       + price_tag(620, 230, "3 000 F", -5, 1.05)) \
    + bubble(1150, 420, "Trois mille.", "tl") + sub("« Trois mille. »", "dark", hl="Trois mille")

S["P06"] = lambda: svg(DAWN() + street()
                       + car(1500, 880, 1.0, blur=True)
                       + person(380, 760, .82, bag="case") + price_tag(380, 300, "3 000 F", -5, .8)
                       + person(820, 760, .82, tie=None) + price_tag(820, 300, "2 500 F", 4, .8)
                       + person(1250, 760, .82, tie=None, shoes="flip") + price_tag(1250, 300, "1 500 F", -3, .8)
                       + '<path d="M1700 760 q 40 -30 80 0 q 40 -30 80 0" stroke="#c9b28f" stroke-width="24" fill="none" opacity=".7" filter="url(#b10)"/>')

S["P07"] = lambda: (svg(sky("dawn")) + "".join(
    f'<div class="card" style="left:{120 + k*350}px;top:240px;width:310px;height:420px;overflow:hidden">'
    f'<svg viewBox="0 0 620 840" width="310" height="420"><rect width="620" height="840" fill="#f9e2bd"/>'
    f'<rect y="560" width="620" height="60" fill="#c9b28f"/><rect y="620" width="620" height="220" fill="{ROAD}"/>{person(300, 600, .9, hand_up=True, bag="case")}</svg>'
    f'<div class="abs micro" style="left:20px;top:20px;color:#17181c;font-size:20px">{d}</div></div>'
    for k, d in enumerate(["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]))) \
    + sub("Chaque jour, c'est la même histoire.", "light", hl="la même histoire")

S["P08"] = lambda: svg(DAWN() + street() + car(1380, 880, 1.05) + person(560, 760, 1.05, bag="case")) \
    + bubble(320, 150, "2 000 ?", "tr", True) + bubble(1150, 210, "3 000 !", "tl", True) + bubble(420, 330, "2 500 ?", "tr", True, "opacity:.9") \
    + bubble(1090, 380, "Non, 3 000.", "tl", True, "opacity:.85") \
    + sub("Le matin, tu discutes le prix. Encore.", "dark", hl="le prix")

NOON = lambda: sky("noon") + sun(960, 120, 80) + skyline(720, .22, "#9a8f86", 5)
S["P09"] = lambda: svg(NOON() + palm(1650, 720, 1) + street() + person(800, 760, 1.05, bag="case", hand_up=True)
                       + '<ellipse cx="800" cy="768" rx="70" ry="12" fill="#000" opacity=".35"/>'
                       + "".join(f'<path d="M{x} 690 q 10 -20 0 -40 q -10 -20 0 -40" stroke="#fff" stroke-width="4" fill="none" opacity=".45"/>' for x in (420, 620, 1080, 1280, 1460))) \
    + sub("À midi, on te répond :", "dark", hl="À midi")

S["P10"] = lambda: svg(NOON() + street() + sign(1580, 720, "Yopougon", .95)
                       + car(1060, 880, 1.1, driver=True) + person(480, 760, 1.0, bag="case")) \
    + bubble(860, 300, "Yopougon ? Non !", "tl") \
    + sub("Je ne vais pas là-bas.", "dark", hl="là-bas")

DUSK = lambda: sky("dusk") + skyline(720, .55, "#1d1a2c", 7) + "".join(f'<circle cx="{(k*197)%1920}" cy="{60 + (k*83)%300}" r="2" fill="#fff" opacity=".6"/>' for k in range(30))
S["P11"] = lambda: svg(DUSK() + street(night=True) + streetlight(1300, 760, 560) + streetlight(400, 760, 560, False)
                       + person(1180, 760, 1.0, bag="case", shirt="#d9d6cf")
                       + '<path d="M1180 770 L 1700 790 L 1700 830 Z" fill="#000" opacity=".35"/>'
                       + '<g transform="translate(1290 520) rotate(-8)"><rect x="-30" y="-56" width="60" height="112" rx="10" fill="#111"/><rect x="-24" y="-48" width="48" height="96" rx="6" fill="#ffd98a" opacity=".9"/>'
                         '<text x="0" y="6" text-anchor="middle" font-family="Space Mono" font-weight="700" font-size="14" fill="#17181c">19:42</text></g>') \
    + sub("tu attends au bord du goudron…", "dark", hl="au bord du goudron")

S["P12"] = lambda: svg(DUSK() + street(night=True) + streetlight(1300, 760, 560)
                       + person(760, 760, 1.0, bag="case", hand_up=True, shirt="#d9d6cf") + headlights(820, 5)
                       + car(1500, 880, 1.0, color="#2b2b33", taxi=False, driver=False, blur=True, night=True)) \
    + sub("sans savoir qui va s'arrêter.", "dark", hl="qui va s'arrêter")

S["P13"] = lambda: ('<div class="abs" style="inset:0;background:#0d0e12"></div>'
                    '<div class="abs" style="left:560px;top:180px;width:800px;height:800px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,59,48,.35),rgba(255,59,48,0))"></div>'
                    + bubble(820, 250, "2 500 ?", "tl", True, "opacity:.35;filter:blur(3px);transform:scale(.8)")
                    + '<div class="type" style="top:470px">Et si on <span class="pk">arrêtait de discuter ?' + BRUSH + '</span></div>')

APPHOME = lambda field="Où allez-vous ?", caret=False, sheet="": (
    mapsvg(route=False, pin=(200, 560)) + f'<div class="app-search"><span class="app-dot"></span>{field}{"<span style=&quot;display:inline-block;width:3px;height:30px;background:#ff3b30&quot;></span>" if caret else ""}</div>' + sheet)
S["P14"] = lambda: light_bg() + phone(745, 98, APPHOME(), extra="box-shadow:0 0 0 0 transparent, 0 60px 140px rgba(255,59,48,.25)") + sub("Avec Yango, tu choisis où tu vas,", "light", hl="Yango", upto=2)

SUGG = ('<div class="app-sheet" style="height:420px"><div class="micro" style="margin-bottom:18px">Suggestions</div>'
        + "".join(f'<div style="display:flex;gap:14px;align-items:center;height:70px;border-bottom:1px solid #eee;font:600 24px/1 Instrument Sans;color:#17181c">'
                  f'<span style="width:36px;height:36px;border-radius:50%;background:#f1f2f4"></span>{t}</div>' for t in ["Plateau", "Plateau, cité administrative", "Plateau, Indénié"]) + '</div>')
S["P15"] = lambda: light_bg() + phone(745, 98, APPHOME("Plateau", True, SUGG)) + \
    '<div class="card" style="left:300px;top:360px;width:330px;height:150px;padding:26px"><div class="micro">Départ</div><div style="font:700 34px/1.3 Instrument Sans;color:#17181c">Riviera 2</div></div>' \
    + sub("tu choisis où tu vas, depuis ton téléphone.", "light", hl="depuis ton téléphone")

PRICE = ('<div class="app-sheet" style="height:330px"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:22px">'
         '<div><div style="font:700 28px/1.2 Instrument Sans;color:#17181c">Riviera 2 → Plateau</div><div class="micro" style="margin-top:8px">Prix avant la course</div></div></div>'
         '<div class="app-price" style="margin-bottom:24px">2 500 F</div><div class="app-btn">Commander</div></div>')
S["P16"] = lambda: light_bg() + phone(745, 98, mapsvg(route=True, pin=(250, 520)) + PRICE) \
    + '<div class="card" style="left:1250px;top:520px;width:300px;height:110px;display:flex;align-items:center;justify-content:center;font:700 46px/1 Space Mono;color:#17181c;border:4px solid #17181c;transform:rotate(4deg)">2 500 F</div>' \
    + sub("Le prix s'affiche avant la course.", "light", hl="avant la course")

S["P17"] = lambda: light_bg() + phone(745, 98, mapsvg(route=True, pin=(250, 520)) + PRICE, extra="filter:blur(2px);opacity:.6") \
    + svg(person(1290, 820, .9, bag="case") + price_tag(1290, 300, "2 500 F", 0, .9), "pointer-events:none") \
    + sub("Pas de surprise.", "light", hl="Pas de surprise")

S["P18"] = lambda: light_bg() + phone(745, 98, mapsvg(route=True, pin=(250, 520), car_at=(160, 230))
                                     + '<div class="app-sheet" style="height:220px"><div style="font:700 30px/1.2 Instrument Sans;color:#17181c">Votre voiture arrive</div><div class="micro" style="margin-top:12px">vers Riviera 2</div></div>') \
    + sub("Une voiture vient te chercher là où tu es.", "light", hl="là où tu es")

DRIVER = ('<div class="app-sheet" style="height:300px"><div style="display:flex;gap:18px;align-items:center;margin-bottom:20px">'
          '<div style="width:84px;height:84px;border-radius:50%;background:#8a5a3b;position:relative;overflow:hidden"><div style="position:absolute;left:12px;top:-6px;width:60px;height:34px;border-radius:30px 30px 6px 6px;background:#1a1410"></div></div>'
          '<div><div style="font:700 32px/1.1 Instrument Sans;color:#17181c">Koffi</div><div style="font:500 22px/1.4 Instrument Sans;color:#55565c">Berline blanche · 4,9 ★</div></div></div>'
          '<span class="plate">1234 AB 01</span><div class="micro" style="margin-top:18px">Arrive dans 3 min</div></div>')
S["P19"] = lambda: light_bg() + phone(745, 98, mapsvg(route=True, pin=(250, 520), car_at=(205, 410))
                                     + '<div class="app-sheet" style="height:200px"><div style="font:700 30px/1.2 Instrument Sans;color:#17181c">Arrive dans 3 min</div></div>') \
    + sub("Tu vois ton chauffeur arriver sur la carte,", "light", hl="sur la carte")

S["P20"] = lambda: light_bg() + phone(745, 98, mapsvg(route=True, pin=(250, 520), car_at=(225, 470)) + DRIVER) \
    + '<div class="card" style="left:1250px;top:560px;width:330px;height:130px;padding:24px;display:flex;align-items:center;gap:16px;transform:rotate(3deg)"><span class="plate" style="font-size:34px">1234 AB 01</span></div>' \
    + sub("avec son nom et sa plaque.", "light", hl="son nom et sa plaque")

def mini(label, scene, k):
    return (f'<div class="card" style="left:{140 + k*560}px;top:170px;width:520px;height:620px;overflow:hidden">'
            f'<svg viewBox="0 0 520 520" width="520" height="520">{scene}</svg>'
            f'<div style="height:100px;display:flex;align-items:center;justify-content:center;font:700 40px/1 Instrument Sans;color:#17181c">{label}</div></div>')
MARKET = ('<rect width="520" height="520" fill="#fff3da"/><path d="M40 170 L 260 90 L 480 170 Z" fill="#ff3b30"/><path d="M40 170 L 480 170 L 480 190 L 40 190 Z" fill="#c22"/>'
          '<rect x="70" y="190" width="380" height="140" fill="#e8c38d"/>' + "".join(f'<circle cx="{100 + i*42}" cy="{215 + (i%2)*20}" r="18" fill="{c}"/>' for i, c in enumerate(["#f4a62a", "#e2522e", "#7cbf4a", "#f4a62a", "#e2522e", "#7cbf4a", "#f4a62a", "#e2522e"]))
          + '<rect y="380" width="520" height="140" fill="#3a3b42"/>' + person(130, 420, .55, skin=1, dress="#2f6bd4", tie=None, shirt="#f2a33a", eyes=False) + car(370, 500, .45, color="#f7f7f7", taxi=False, stripe=True, driver=False))
OFFICE = ('<rect width="520" height="520" fill="#e9eef4"/><rect x="150" y="40" width="220" height="340" fill="#7d8aa3"/>'
          + "".join(f'<rect x="{170 + (i%4)*50}" y="{60 + (i//4)*44}" width="30" height="26" fill="#cfe3f2"/>' for i in range(28))
          + '<rect y="380" width="520" height="140" fill="#3a3b42"/>' + person(120, 420, .55, skin=2, bag="back", tie=None, shirt="#f4f2ee", eyes=False) + car(370, 500, .45, color="#f7f7f7", taxi=False, stripe=True, driver=False))
MAQUIS = ('<rect width="520" height="520" fill="#2b2742"/>' + "".join(f'<circle cx="{30 + i*46}" cy="{80 + 14*math.sin(i)}" r="9" fill="#ffd98a"/>' for i in range(11))
          + '<path d="M10 80 Q 260 120 510 80" stroke="#555" stroke-width="2" fill="none"/>'
          + '<rect x="200" y="260" width="140" height="12" fill="#f2f2f2"/><rect x="214" y="272" width="10" height="90" fill="#f2f2f2"/><rect x="316" y="272" width="10" height="90" fill="#f2f2f2"/>'
          + '<path d="M120 270 L 170 270 L 170 360 M 120 270 L 120 360 M 120 310 L 170 310" stroke="#ff3b30" stroke-width="10" fill="none"/>'
          + '<rect y="380" width="520" height="140" fill="#26262e"/>' + person(420, 420, .55, skin=0, shirt="#7a3fa0", tie=None, eyes=False) + car(160, 500, .45, color="#f7f7f7", taxi=False, stripe=True, driver=False, flip=True))
S["P21"] = lambda: light_bg() + mini("Au marché", MARKET, 0) + mini("Au travail", OFFICE, 1) + mini("Au maquis", MAQUIS, 2) \
    + sub("Que tu ailles au marché, au travail ou au maquis…", "light", hl="au marché", upto=9)

S["P22"] = lambda: svg(sky("noon") + skyline(720, .25, "#7d7f9a", 9) + street()
                       + car(1150, 880, 1.05, color="#f7f7f7", taxi=False, stripe=True, driver=True)
                       + '<g opacity=".5" filter="url(#mx)"><rect x="1500" y="840" width="420" height="12" fill="#fff"/><rect x="1560" y="900" width="360" height="8" fill="#fff"/></g>') \
    + sub("tu montes, et tu pars.", "dark", pk="tu pars")

S["P23"] = lambda: svg(DAWN() + palm(250, 720, 1.1) + palm(1700, 720, .9) + street() + sign(1260, 720, "Riviera 2")
                       + person(760, 760, 1.0, bag="case")
                       + '<text x="560" y="250" font-family="Space Mono" font-weight="700" font-size="120" fill="#17181c" opacity=".85">07:00</text>') \
    + sub("Lundi, sept heures. Carrefour Riviera Deux.", "dark", hl="Riviera Deux")

S["P24"] = lambda: svg(DAWN() + palm(1700, 720, .9) + street() + sign(300, 720, "Riviera 2", .9)
                       + car(1120, 880, 1.05, color="#f7f7f7", taxi=False, stripe=True, driver=True, open_door=True)
                       + person(700, 760, 1.0, bag="case")) \
    + sub("Ta voiture est déjà là.", "dark", hl="déjà là")

S["P25"] = lambda: ('<div class="abs" style="inset:0;background:#ff3b30"></div>'
                    '<div class="abs" style="left:460px;top:120px;width:1000px;height:700px;border-radius:50%;background:radial-gradient(closest-side,rgba(255,138,128,.7),rgba(255,59,48,0))"></div>'
                    '<div class="abs" style="left:0;width:1920px;top:300px;text-align:center;font:700 170px/1 Instrument Sans;color:#fff;letter-spacing:-.03em">Yango</div>'
                    '<div class="abs micro" style="left:0;width:1920px;top:510px;text-align:center;color:#fff;opacity:.8">logo officiel à fournir</div>'
                    + sub("Yango.", "dark onred"))

S["P26"] = lambda: ('<div class="abs" style="inset:0;background:#ff3b30"></div>'
                    '<div class="abs" style="left:0;width:1920px;top:180px;text-align:center;font:700 130px/1 Instrument Sans;color:#fff;letter-spacing:-.03em">Yango</div>'
                    '<div class="cta-btn" style="left:560px;top:420px;width:800px">Télécharger l’application</div>' + TAP(1300, 480)
                    + svg('<rect x="0" y="760" width="1920" height="3" fill="#fff" opacity=".5"/>' + car(1300, 760, .32, color="#f7f7f7", taxi=False, stripe=False, driver=False), "")
                    + sub("Télécharge l'application, et bouge tranquille.", "dark onred", hl="Télécharge l'application", pk="bouge tranquille"))

S["P27"] = lambda: ('<div class="abs" style="inset:0;background:#ff3b30"></div>'
                    '<div class="abs" style="left:0;width:1920px;top:180px;text-align:center;font:700 130px/1 Instrument Sans;color:#fff;letter-spacing:-.03em">Yango</div>'
                    '<div class="abs" style="left:430px;top:330px;width:1060px;height:300px;border-radius:150px;border:5px solid rgba(255,255,255,.55)"></div>'
                    '<div class="abs" style="left:330px;top:280px;width:1260px;height:400px;border-radius:200px;border:3px solid rgba(255,255,255,.3)"></div>'
                    '<div class="cta-btn" style="left:560px;top:420px;width:800px;background:#ffe5e3;transform:scale(.97)">Télécharger l’application</div>'
                    + svg('<rect x="0" y="760" width="1920" height="3" fill="#fff" opacity=".5"/>' + car(1650, 760, .32, color="#f7f7f7", taxi=False, stripe=False, driver=False), ""))

for name, fn in S.items():
    (OUT / f"{name}.html").write_text(page(fn(), name), encoding="utf-8")
print(len(S), "styleframes")
