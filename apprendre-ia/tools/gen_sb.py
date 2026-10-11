"""Write <project>/STORYBOARD.md from sb_data.py (global times ‹t› → frame-local) and the word timings of onsets.json."""
import json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sb_data import FRAMES, SHOTS

proj = pathlib.Path(sys.argv[1])
W = json.load(open(proj / "onsets.json", encoding="utf-8"))["words"]
TOTAL = 45.80

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
    return " ".join(out)

HEAD = f"""---
format: 1920x1080
duration: "{TOTAL:.2f}s"
message: "Tu as dit « pas pour moi » à chaque révolution ; le monde, lui, n'a pas attendu. Cette fois, apprends l'IA : elle fait le travail, tu récupères ton temps."
arc: Hook (2000, 2010, 2026) → Gag → Problème → 3 douleurs → Pivot → Solution → Démo → Réassurance → Bénéfice → Rime → CTA
audience: "indépendants, entrepreneurs et petites équipes, non techniques, qui repoussent l'IA comme ils ont repoussé le site internet et les réseaux sociaux"
mode: autonomous
captions: disabled
music: "pré-mixée avec la voix et les bruitages dans assets/audio/mix.wav (montée à la racine par l'orchestrateur)"
direction: "La frise des excuses (direction unique, tirée du script choisi : le post-it « Pas pour moi » sur chaque écran)"
styleframes: "styleframes/png/P01.png à P22.png (une image clé par plan, temps dans chaque bloc)"
patterns: ../patterns/STORYBOARD-CRAFT.md, ../patterns/PATTERNS.md
---

## Video direction

- **Un seul objet porte le film** : le post-it jaune « Pas pour moi » (frame.md postit). Il se colle sur chaque écran (2000, 2010, 2026), tombe au pivot, revient et perd son « Pas », puis se replie en bouton. Deux mondes : le bureau de nuit (séquences 1 à 6, et la carte de fin 12) et le papier clair (séquences 7 à 11). Chaque séquence peint son propre sol plein cadre en couche `class="clip"`.
- **Coutures invisibles** : chaque séquence entre en `cut` ; chaque couture tombe au sommet du flou d'un geste de caméra et le `handoff_out` de la séquence N est recopié mot pour mot dans le `handoff_in` de N+1. Exceptions voulues : 22.90, coupe franche au noir sur « Pas » (changement d'acte) ; 24.80, flash de lumière d'assemble.sh depuis le point (960, 210) (l'unique transition « effet » du film).
- **Texte** (lisible sans le son) : chaque phrase de la voix est un sous-titre en bas au centre (bande y 890 à 980, rien d'autre dedans), MOT PAR MOT sur les horodatages de chaque séquence (`mot@secondes`, temps locaux). Exactement UN mot ou groupe par phrase dans le surligneur jaune (nommé [boîte : …]). Aucun autre texte coloré. Un seul moment typographique (la phrase EST l'image, centrée, 84 px) : « Pas cette fois. » (séquence 6).
- **Pics** : seulement les 4 pics nommés [trait : …] (« cette fois », « le travail », « apprendre à lui parler », « pour toi ») : un trait de pinceau jaune effilé sous LE mot clé. Aucun mot géant, aucune grosse boîte.
- **Une seule chose à regarder** : la caméra isole le sujet de la phrase ; la frise se longe toujours de gauche à droite, jamais d'aller-retour ; mises en page côte à côte aux marges égales (horloge / appli, Toi / D'autres, trois cartes, trois tuiles) ; aucun décor sans sens, aucune ligne qui traverse une phrase.
- **Interfaces** (frame.md apps et ai-window) : génériques, sans marque ni logo (assistant IA, diapos, messagerie, tableur), épurées ; le MÊME portable de 2026 jusqu'à la fin. Les appareils de 2000 et 2010 sont des appareils d'époque, dessinés.
- **Grammaire de mouvement** : deux vitesses, gestes de 1 à 6 images (expo.out) et dérives linéaires qui ne s'arrêtent jamais ; la zone 0,3 à 0,9 s est réservée à la caméra et au curseur (expo, power3 ou power4) ; les éléments arrivent trop grands et flous puis se posent, jamais en fondu à leur taille finale ; aucune tenue figée (chaque tenue nomme sa couche vivante).
- **Texte visible** : exactement le texte cité dans les lignes Scene, rien d'autre.
- **Négatifs** : diaporama (tout à t=0), écran de veille, objet dédoublé (UN seul post-it à l'écran sauf dans le plan large P5 et le partage P10), texte coloré au lieu du surligneur, grande phrase, mot géant, symbole abstrait, curseur qui hésite, plusieurs objets qui bougent pendant une couture, toute teinte autre que le jaune hors époque (barre de titre bleue de 2000).

**MONDE**
- Acte 1 (0.00 à 22.90), monde A, bureau de nuit #0d0f14, trame de points blancs à 7 %, halo bleu-gris : la frise (ligne en y 770, cam2 du monde) porte trois stations : 2000 en x 960 (écran cathodique), 2010 en x 2220 (smartphone), 2026 en x 3480 (portable) ; plus loin à droite, x 4000 à 6000 : la frise continue, années 2027 à 2029, où filent les portables des autres. Séquences 4 et 5 : dans l'écran du portable (horloge murale à gauche, appli à droite).
- Pivot (22.90 à 24.80) : noir #0a0b0f, la phrase, le post-it qui tombe, le point de lumière.
- Acte 2 (24.80 à 41.42), monde B, papier #f5f2ea, trame de points d'encre à 7 %, halo jaune doux : le portable clair et l'assistant IA ; les trois cartes ; le champ de saisie ; la conversation ; les trois tuiles ; puis la frise du papier avec « 2026 » (séquence 11).
- Acte 3 (41.42 à 45.80) : carte de fin sur le bureau de nuit, la frise en filet à y 660 (2000 · 2010 · 2026).
- Couleurs de rôle : jaune #f7d038 = le post-it, le surligneur, les 4 traits, les coches, le secteur du temps rendu, le bouton ; encre = le monde ; bleu de 2000 = l'époque seulement.

**SIGNATURES**
- Mécanisme 1 « le post-it qui se colle » (arrive de la caméra ×1,6 flou 10, rotation, claquement) : 2.12, 5.50, 11.55, 38.30 (4 fois) ; son inverse « le post-it qui tombe » : 23.80 ; « le post-it qui se replie en bouton » : 41.42.
- Mécanisme 2 « l'horloge qui avale / rend le temps » : 15.80 (22:47), 17.50 (12:00), 19.53 (DIM.), 22.30 (les trois petites), puis à rebours 35.68, 36.33, 37.23.
- Registres de texte : sous-titre mot par mot (flou → net, gris → plein) ; surligneur (se trace depuis la gauche, 0,16 s) ; trait de pic (se dessine, 0,4 s) ; moment typographique du pivot (mots qui paraissent sur le noir).
- Rimes : le post-it de 2.12 se recolle à 38.30 avec le même geste ; le champ du gag (9.40) revient au même cadrage à 28.40 ; les horloges de la douleur (15 à 20) tournent à rebours (35 à 37) ; la tasse de 6.40 revient « avant le café » (21.56) ; « [boîte : L'intelligence artificielle] ? » à 8.02 et 38.12 ; la frise du début devient le filet de la carte de fin (41.42).

**PARTITION CAMÉRA** (temps globaux) : 0.00 dérive sur 2000 · 2.78 whip → 2010 (sommet 2.98) · 6.05 whip → 2026 (couture 6.37) · 6.55 poussée lente sur l'écran · 9.18 cran ×2,4 dans le champ · 10.30 micro-cran vers « moi. » · 11.20 recul (couture 11.40) jusqu'au plan large (11.80) · 12.60 travelling vers la droite le long de la frise · 14.50 poussée dans notre écran (couture 14.85) · 16.80 whip de la fenêtre (horloge fixe) · 18.30 whip (couture 18.50) · 20.25 recul au partage · 22.90 coupe au noir · poussée lente sur le noir · 24.80 flash, atterrissage sur le papier · 26.00 recul aux trois cartes · 28.00 cran vers le bas (couture 28.22) · 29.80 recul · 30.95 whip vers la gauche (couture 31.13) · 32.55 recul à la conversation · 34.25 recul (couture 34.46) · crans par tuile 35.60, 36.25, 37.15 · 37.70 recul (couture 37.88) · 39.20 poussée sur le post-it · 41.15 poussée dans le jaune (couture 41.42) · 41.42 le jaune se replie en bouton · dérive jusqu'à l'iris 45.30.

**VOIX** : minutage de onsets.json (débuts de phrase mesurés sur l'énergie du son ; mots à l'intérieur des phrases estimés, ±0,15 s, à recaler avec Whisper avant d'animer). Silences de plus de 0,4 s, chacun écrit comme un plan avec son action : 0.59 à 1.02 (la fenêtre s'ouvre) · 1.84 à 2.21 (le post-it arrive) · 2.74 à 3.22 (whip) · 3.94 à 4.39 (le téléphone s'éveille) · 5.15 à 5.61 (le post-it arrive) · 6.12 à 6.62 (whip) · 7.53 à 8.02 (l'accueil de l'IA) · 9.18 à 11.60 (LE GAG) · 12.18 à 12.63 (la frise se met à glisser) · 14.62 à 15.08 (poussée dans l'écran) · 16.69 à 17.06 (whip) · 18.28 à 18.72 (whip) · 20.13 à 20.60 (recul au partage) · 22.48 à 22.99 (coupe au noir) · 23.48 à 24.96 (LE PIVOT : le post-it tombe, le point s'embrase) · 26.00 non · 28.00 à 28.44 (cran vers le champ) · 29.69 à 30.11 (envoi, clic) · 30.91 à 31.36 (whip, la carte de code) · 34.23 à 34.69 (les tuiles se posent) · 37.64 à 38.12 (recul vers le portable) · 39.27 à 39.70 (poussée sur le post-it) · 40.27 à 40.59 (le feutre barre « Pas ») · 41.19 à 41.66 (le jaune devient bouton) · 43.17 à 45.80 (clic, tenue, iris).

**COUPES** (voix narrative, quota 0 à 4) : une seule, 22.90 · premier mot « Pas » (22.99) · changement d'acte (l'excuse → le tournant), la musique se coupe sur un impact grave. Plus le flash de lumière de 24.80 (la seule transition « effet »). Toutes les autres jonctions sont des coutures de caméra ou d'objet.

**RYTHME** : douleur (0 à 22.90) 10 plans = 4,4 plans / 10 s mais un événement toutes les 0,2 à 0,5 s (accroche) et 0,5 s (douleurs) ; pivot 1 plan ; solution et fin (24.80 à 45.80) 11 plans = 5,2 plans / 10 s, un événement toutes les 0,5 s.

**SON** (verrouillé sur l'image, temps globaux) : musique de tension de 0 à 22.90, montée (riser) de 19.90 à 22.90, coupée net par un impact grave à 22.90, silence ; la musique d'élan revient avec son attaque sur « Aujourd'hui » (24.96), respire sous la voix, s'éteint en fondu sur la carte de fin. Bruitages : whoosh court 0.05 · clic doux 0.30 · pop 0.95 · pop 2.12 (post-it) · whoosh court 2.82 · clic doux 3.22 · notification 4.30 · pop 5.50 (post-it) · whoosh court 6.10 · whoosh court 6.40 · clic doux 6.62 · scintillement 7.00 · frappe 9.45 · ping 10.30 (le gag) · whoosh 11.22 · pop 11.55 (post-it) · whoosh cinématique 12.70 · whoosh courts 13.10, 13.50, 14.60 · whoosh court 14.90 · clic 15.50 · clics doux 15.85, 16.05, 16.25 · notifications 17.10, 17.22, 17.34 · clic doux 17.55 · whoosh courts 18.32, 18.52 · frappe 19.20 · clic doux 19.55 · whoosh 20.30 · pops 21.19, 21.35, 21.50 · impact grave 22.90 · whoosh court 23.80 · scintillement 24.40 · whoosh cinématique 24.70 · scintillement 25.30 · frappe 26.30 · pop 26.80 · frappe 27.50 · carillon 27.95 · whoosh court 28.24 · frappe 28.45 · clic 30.08 · pops 30.20, 30.50 · whoosh courts 30.98, 31.15 · pop 31.30 · glitch 32.16 · pops 32.80, 33.20, 33.60 · whoosh 34.28 · carillons 35.70, 36.35, 37.25 · whoosh 37.72 · whoosh court 37.90 · pop 38.30 (post-it) · clic doux 40.30 · NOTIFICATION À DEUX TONS 40.60 (la signature : « c'est pour toi ») · whoosh cinématique 41.20 · whoosh court 41.42 · pop 41.70 · clic 43.20 · whoosh 45.30.
"""

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

doc = HEAD.replace(" · 26.00 non", "") + "\n" + "\n".join(block(f) for f in FRAMES)
(proj / "STORYBOARD.md").write_text(doc, encoding="utf-8")
total = sum(f["end"] - f["start"] for f in FRAMES)
print(f"STORYBOARD.md written, {len(FRAMES)} frames, {len(SHOTS)} shots, sum {total:.2f} s")
