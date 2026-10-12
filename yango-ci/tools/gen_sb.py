"""Write <project>/STORYBOARD.md from sb_data.py (global times ‹t› → frame-local) and the word timings of onsets.json."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sb_data import FRAMES, SHOTS, HEAD, TOTAL

proj = pathlib.Path(sys.argv[1])
W = json.load(open(proj / "onsets.json", encoding="utf-8"))["words"]

def loc(text, start):
    return re.sub(r"‹([\d.]+)›", lambda m: f"{float(m.group(1)) - start:.2f}", text)

def glob(text):
    return re.sub(r"‹([\d.]+)›", lambda m: m.group(1), text)

def cues(f):
    ws = [w for w in W if f["start"] - 1e-6 <= w["s"] < f["end"]]
    out, prev_e = [], None
    for w in ws:
        tok = re.sub(r"[.,;:!?…«»\"()]+", "", w["w"]).replace("'", "’")
        if prev_e is not None and w["s"] - prev_e > 0.4:
            out.append(f"(silence de {prev_e - f['start']:.2f} à {w['s'] - f['start']:.2f})")
        out.append(f"{tok}@{w['s'] - f['start']:.2f}")
        prev_e = w["e"]
    tail = f["end"] - (ws[-1]["e"] if ws else f["start"])
    if ws and tail > 0.4:
        out.append(f"(silence de {ws[-1]['e'] - f['start']:.2f} à {f['end'] - f['start']:.2f})")
    return " ".join(out) if out else f"(silence : aucune voix de 0.00 à {f['end'] - f['start']:.2f})"


def block(f):
    shots = [s for s in SHOTS if s["frame"] == f["n"]]
    d = f["end"] - f["start"]
    prev = next((p for p in FRAMES if p["n"] == f["n"] - 1), None)
    if "handoff_in" in f:
        hin = f["handoff_in"]
    else:
        hin = f"à 0.00 : {prev['handoff_out']}"
    hout = f["handoff_out"] if f["handoff_out"].startswith("aucun") else f"à {d:.2f} : {f['handoff_out']}"
    out = [f"## Frame {f['n']} : {f['title']} · {f['start']:.2f} → {f['end']:.2f}", "",
           f"- scene: {f['scene']}",
           f"- duration: {d:.2f}s",
           "- transition_in: cut",
           "- status: outline",
           f"- src: compositions/frames/{f['n']:02d}-{f['slug']}.html",
           f"- voiceover: \"{f['voice'].replace(chr(39), '’')}\"",
           f"- type: {f['type']}",
           f"- blueprint: {f['blueprint']} (Adapt)",
           f"- focal: {f['focal']}",
           f"- rules: {f['rules']}",
           f"- world: {f['world']}",
           f"- handoff_in: {hin}",
           f"- handoff_out: {hout}", "",
           f"Word cues: {cues(f)}", ""]
    for k, s in enumerate(shots, 1):
        a, b = s["a"] - f["start"], s["b"] - f["start"]
        L = lambda t: loc(t, f["start"])
        out += [f"Scene {k} ({a:.2f} à {b:.2f} s) : {s['id']}, {s['name']}",
                f"  TEXTE ÉCRAN : {L(s['text'])}",
                f"  IMAGE DE DÉPART : {L(s['start'])}",
                f"  ÉTAPES : {L(s['steps'])}",
                f"  PISTE CAMÉRA : {L(s['camtrack'])}",
                f"  COUCHES ET PROFONDEUR : {L(s['layers'])}",
                f"  OBJET-PONT ET VECTEUR : {glob(s['bridgelong'])}",
                f"  SON : {L(s['sound'])}",
                f"  IMAGE CLÉ : {s['key'] - f['start']:.2f} : {s['keyimg']} (styleframes/png/{s['id']}.png)", ""]
    return "\n".join(out)

doc = HEAD + "\n" + "\n".join(block(f) for f in FRAMES)
(proj / "STORYBOARD.md").write_text(doc, encoding="utf-8")
total = sum(f["end"] - f["start"] for f in FRAMES)
print(f"STORYBOARD.md written, {len(FRAMES)} frames, {len(SHOTS)} shots, sum {total:.2f} s")
