---
version: 1
name: "Apprendre l'IA · « Pas pour moi » · charte"
description: >
  Charte du film « Pas pour moi » (45,80 s, 1920×1080, 30 i/s), sur la voix assets/audio/voix-montage.wav.
  Direction « La frise des excuses » : une frise du temps (2000, 2010, 2026) porte trois bureaux, et sur chaque écran
  le même post-it jaune « Pas pour moi ». Le post-it est l'objet du film : il se colle (accroche), tombe (pivot) et
  devient le bouton de fin. Deux mondes : la DOUBLE PEINE (l'excuse, puis le temps perdu) dans le bureau de nuit,
  bleu-noir ; la SOLUTION sur le papier clair. La carte de fin revient au bureau de nuit. Un seul accent, le jaune
  post-it, réservé au post-it, à la boîte du mot clé (comme un surligneur) et à 4 traits de pic.
unit: 1920×1080
principle: "lisible sans le son · une seule chose à regarder · un accent jaune, un seul mécanisme de mise en valeur · la voix déclenche chaque révélation"
reference: "styleframes/_kit.css (sol, frise, post-it, horloge, appareils, interfaces, sous-titre, boîte, trait) : source unique du dessin, que chaque séquence recopie"

colors:
  canvas: "#0d0f14"            # bureau de nuit (accroche, douleur, pivot, carte de fin)
  canvas-2: "#161a22"          # surfaces sombres, cartes du monde sombre
  paper: "#f5f2ea"             # monde clair (solution)
  paper-2: "#ece7dc"
  card-light: "#fffdf8"        # cartes et fenêtres du monde clair
  ink: "#f3f1ec"               # texte sur le sombre
  ink-soft: "#c9c6bf"
  ink-mute: "#8d8a84"
  ink-dark: "#17181c"          # texte sur le clair, texte DANS la boîte jaune, écriture du post-it
  ink-dark-soft: "#55565c"
  hairline-light: "#e1dccf"
  accent: "#f7d038"            # LE jaune post-it : post-it, boîte du mot clé, traits de pic, bouton de fin, coches
  accent-light: "#ffe066"
  accent-deep: "#c99a06"       # ombre du post-it, bord du bouton
  accent-glow: "#ffe98a"       # halo de l'écran IA, point de lumière du pivot

# Fichiers woff2 locaux uniquement (Google Fonts, SIL Open Font License), jamais d'@import réseau.
fonts:
  Instrument Sans: { files: ["assets/fonts/InstrumentSans-400.woff2 (400)", "assets/fonts/InstrumentSans-500.woff2 (500)", "assets/fonts/InstrumentSans-600.woff2 (600)", "assets/fonts/InstrumentSans-700.woff2 (700)"] }
  Space Mono: { files: ["assets/fonts/SpaceMono-400.woff2 (400)", "assets/fonts/SpaceMono-700.woff2 (700)"] }
  Big Shoulders: { files: ["assets/fonts/BigShoulders-800.woff2 (800)"] }
  Caveat: { files: ["assets/fonts/Caveat-700.woff2 (700)"], note: "UNIQUEMENT l'écriture à la main sur le post-it" }

typography:
  subtitle:   { fontFamily: "Instrument Sans", px: 62, weight: 600, lineHeight: 74, tracking: "-0.015em", note: "la phrase de la voix EN BAS AU CENTRE (haut à y 896, dans la bande y 890 à 980 qui ne porte rien d'autre), 45 caractères au plus par morceau, mot par mot sur son horodatage ; #f3f1ec sur le sombre, #17181c sur le clair, ombre légère. Jamais en haut à gauche" }
  type:       { fontFamily: "Instrument Sans", px: 84, weight: 600, lineHeight: 1.12, tracking: "-0.025em", note: "UN seul moment typographique : le pivot « Pas cette fois. », centré, sans sous-titre en bas" }
  postit:     { fontFamily: "Caveat", px: 76, weight: 700, lineHeight: 0.95, note: "« Pas pour moi » écrit à la main, encre #17181c, deux lignes" }
  frise-year: { fontFamily: "Space Mono", px: 30, weight: 700, tracking: "0.18em", note: "années sous la ligne de la frise : « 2000 », « 2010 », « 2026 »" }
  ui:         { fontFamily: "Instrument Sans", px: 24, weight: 500, lineHeight: 1.35, note: "texte des interfaces" }
  ui-title:   { fontFamily: "Instrument Sans", px: 34, weight: 600, lineHeight: 1.15 }
  clock:      { fontFamily: "Space Mono", px: 30, weight: 700, tabularNums: true, note: "heure numérique sous le cadran (« 22:47 »)" }
  micro:      { fontFamily: "Space Mono", px: 16, weight: 400, tracking: "0.2em", upper: true, note: "étiquettes (« DIAPO 1 / 20 », « NON LUS »)" }
  code:       { fontFamily: "Space Mono", px: 22, weight: 400, lineHeight: 1.5, note: "seulement la carte de code de la séquence 9" }
  cta:        { fontFamily: "Big Shoulders", px: 56, weight: 800, upper: true, tracking: "0.04em", note: "le bouton « APPRENDRE L'IA »" }

components:
  ground-dark:
    background: "#0d0f14 plein + un halo radial bleu-gris (#26304a à 35 %, flou 140 px) derrière le sujet + trame de points (2 px, pas de 36 px, blanc à 6 %) qui rend la dérive visible + grain 5 %. Couche class=\"clip\" sur toute la durée, jamais sur #root."
  ground-light:
    background: "#f5f2ea plein + halo radial jaune très doux (#f7d038 à 8 %) derrière le sujet + trame de points (encre à 5 %) + grain 3 %. Couche class=\"clip\"."
  frise:
    look: "LA frise du film : une ligne fine (2 px, #8d8a84 sur le sombre, #17181c à 40 % sur le clair) à y 770 dans le monde A ; une graduation de 18 px sous chaque station et l'année dessous en Space Mono 700 30 px (« 2000 », « 2010 », « 2026 ») ; les appareils sont POSÉS sur la ligne, ombre de contact douce. Stations du monde A (x monde, ligne en y 770) : 2000 à x 960, 2010 à x 2220, 2026 à x 3480 (1260 px d’écart). La caméra la longe toujours de gauche à droite."
  postit:
    look: "carré de 300 × 300 px, #f7d038 avec un dégradé vers #ffe066 en haut, bande adhésive en haut un peu plus foncée (#e9bf22, 54 px), coin bas droit légèrement décollé (ombre interne), ombre portée 0 18px 30px rgba(0,0,0,.35) ; « Pas pour / moi » en Caveat 700 76 px #17181c, rotation propre -5°. Le MÊME dessin à chaque apparition."
    motion: "« se colle » : arrive de la caméra ×1,6 et flou 10 px, rotation -14° → -5°, posé en 0,12 s expo.out, petit tassement 0,97 → 1 en 0,08 s (claquement). « tombe » : le coin haut gauche se décolle (rotation -5° → 18°, 0,2 s power2.in) puis chute y +900 en 0,35 s power2.in avec flou vertical 8 px."
  clock:
    look: "horloge murale ronde Ø 260 px : cadran #fffdf8, bord #17181c 8 px, 12 index, aiguilles #17181c, trotteuse jaune #f7d038 ; heure numérique Space Mono sous le cadran ; sur le dimanche, « DIM. » en micro dans le cadran."
    motion: "« le temps avalé » : les aiguilles tournent vite vers l'heure tardive (2 tours en 0,8 s, power2.inOut), l'heure numérique défile ; « le temps rendu » : elles tournent à rebours, un arc jaune montre le temps rendu."
  device-crt:
    look: "écran cathodique 2000 : boîtier beige #d9d2c3 (rayon 18, profondeur suggérée par un dégradé), dalle bombée vert-gris sombre avec reflet, petit pied ; à l'écran une fenêtre d'assistant d'époque (barre de titre bleue en dégradé, bouton « Oui » / « Plus tard »)."
  device-phone2010:
    look: "smartphone de 2010 : dalle noire 300 × 560, rayon 40, bouton rond en bas, écran à icônes carrées ; une notification « Rejoins tes amis sur le réseau » et un bouton « S'inscrire »."
  device-laptop:
    look: "ordinateur portable d'aujourd'hui : bords fins gris sidéral #2a2d33, écran 1060 × 660, base fine ; à l'écran l'assistant IA (thème sombre dans le monde A, clair dans le monde B). Le MÊME portable de 2026 jusqu'à la fin."
  ai-window:
    look: "fenêtre d'assistant IA générique, sans marque : en-tête « Assistant IA » avec un petit point jaune, message d'accueil « Bonjour. Que veux-tu faire aujourd'hui ? », champ de saisie en bas (rayon 18) avec caret jaune et bouton d'envoi carré jaune à flèche. Ce champ est le MÊME objet au gag (séquence 2) et à la solution (séquence 8)."
  apps:
    look: "interfaces génériques, épurées, sans marque : éditeur de diapos (colonne de vignettes, « Cliquez pour ajouter un titre », « DIAPO 1 / 20 ») ; boîte de réception (« Boîte de réception », « 87 NON LUS », expéditeurs génériques) ; tableur (colonnes Date, Libellé, Montant ; ligne « Total »)."
  word-by-word:
    rule: "chaque mot du sous-titre apparaît SUR son horodatage, gris (encre à 35 %) : fromTo {opacity:0, y:8, filter:blur(6px)} → {opacity:1, y:0, blur(0)} en 0,14 s, immediateRender:false, puis passe à l'encre pleine en 0,2 s. Avant une couture, le sous-titre sort : opacité 1 → 0 et flou 0 → 6 px en 0,14 s."
  key-word-box (LE mécanisme de mise en valeur, un par phrase):
    look: "un surligneur : rectangle jaune #f7d038, angles nets (rayon 3 px), qui déborde du mot de 0,14 em de chaque côté ; le mot reste en encre #17181c dedans (sur le sombre aussi). Jamais une boîte noire."
    motion: "le surligneur se trace depuis la gauche (scaleX 0 → 1, origine à gauche, 0,16 s power3.out), 0 à 2 images avant le mot ; sur le sombre, le mot passe de #f3f1ec à #17181c au passage du jaune (0,1 s)."
  peak-stroke (les 4 pics):
    look: "trait de pinceau effilé jaune #f7d038 (attaque ronde, sortie fine, légère courbe montante), 10 px d'épaisseur max, SOUS le mot clé seulement."
    motion: "se dessine de gauche à droite (scaleX 0 → 1, 0,4 s power2.out) pendant que le mot est dit."
  cursor:
    description: "flèche blanche à contour sombre + ombre ; arrive d'un seul mouvement courbe (0,4 à 0,5 s power3.out) et clique directement : pression (scale .85, 0,06 s) + onde jaune qui s'ouvre et s'efface. Jamais d'hésitation."
  light-point:
    description: "point blanc-chaud (radial #fffbe6 → #ffe98a → transparent), là où le post-it a disparu au pivot : départ du flash de lumière."
  end-card:
    description: "bureau de nuit ; le post-it se replie en bouton : « APPRENDRE L'IA » (Big Shoulders 800 56 px, #17181c sur #f7d038, rayon 14, coin plié en haut à droite qui rappelle le post-it, halo jaune doux) ; la frise du début passe derrière, en filet, avec « 2000 · 2010 · 2026 » ; un curseur arrive et clique ; 2 à 3 s de tenue vivante, puis iris."

negative:
  - "Un seul mécanisme de mise en valeur : le surligneur jaune, une fois par phrase ; les 4 traits de pic. Aucun texte coloré, aucun texte lumineux."
  - "Pas de grande phrase : sous-titre 60 à 64 px, moment typographique 84 px au plus ; aucun mot géant, aucune grosse boîte. Rien d'autre que le sous-titre dans la bande y 890 à 980."
  - "Une seule chose à regarder à la fois ; mises en page côte à côte aux marges égales."
  - "Jamais d'aller-retour de caméra : la frise se longe de gauche à droite. Aucun curseur qui hésite."
  - "Aucun décor sans sens, aucune ligne du décor qui traverse une phrase."
  - "Aucune autre teinte que le jaune, sauf le bleu de la barre de titre de 2000 (époque) et le gris-bleu du halo du bureau de nuit."
  - "Aucune marque, aucun logo réel : l'assistant IA, les diapos, la messagerie et le tableur sont génériques."
  - "Pas d'Inter, Space Grotesk, Geist, system-ui. Pas d'emoji. Caveat seulement sur le post-it."
  - "Pas d'ease rebondissante ou élastique, pas de repeat:-1, jamais de tween de letterSpacing."
  - "Aucun texte visible qui ne figure pas dans les lignes Scene de la séquence (les libellés de composants ci-dessus sont permis)."
---

# « Pas pour moi » : charte

Le film a deux mondes. **La double peine** se joue dans le bureau de nuit, bleu-noir : une frise du temps porte trois
bureaux (2000, 2010, 2026), et sur chaque écran le même post-it jaune « Pas pour moi » ; puis le temps perdu, compté par
une horloge (la soirée, la matinée, le dimanche). Le **pivot** « Pas cette fois. » est le seul moment typographique : le
post-it se décolle et tombe dans le noir, un point de lumière reste. La lumière inonde l'écran et l'on arrive sur **la
solution**, sur le papier clair : l'assistant IA rédige, résume, calcule ; on lui parle avec ses mots ; les horloges
tournent à rebours. Le post-it revient, « Pas » se barre, et il se replie en bouton sur la **carte de fin**, dans le
bureau de nuit.

Tout ce qu'on lit est en Instrument Sans : la phrase de la voix en sous-titre en bas au centre, mot par mot, avec un mot
clé par phrase surligné en jaune. Un trait de pinceau jaune marque les 4 pics. Les années, les heures et les étiquettes
sont en Space Mono ; le bouton en Big Shoulders ; seul le post-it est écrit à la main (Caveat).
