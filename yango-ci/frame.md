---
version: 1
name: "Yango Côte d'Ivoire · « On dit combien ? » · charte"
description: >
  Charte du film « On dit combien ? » (60,00 s, 1920×1080, 30 i/s), sur la voix assets/audio/voix-montage.wav.
  Direction « Au bord du goudron » : une rue d'Abidjan en illustration plate (carrefour Riviera 2, le goudron, le
  trottoir, le panneau, les palmiers, les tours du Plateau au loin) que la caméra longe du matin au soir. Le problème
  vit dans la rue, avec le taxi orange et la discussion du prix ; le pivot est sur le noir ; la solution vit dans le
  téléphone (fond clair, rouge Yango) ; la rime ramène au même carrefour, où la voiture attend déjà ; la carte de fin
  est rouge Yango. Objets-ponts : la main levée, l'étiquette de prix (le gag), la bulle de la discussion, le téléphone.
  PROVISOIRE : le rouge, le mot-symbole « Yango » et les écrans de l'application sont des substituts génériques, à
  remplacer par le logo, les couleurs et des captures récentes fournis par la marque.
unit: 1920×1080
principle: "lisible sans le son · une seule chose à regarder · un accent rouge, un seul mécanisme de mise en valeur · la voix déclenche chaque révélation"
reference: "reference/rue.html (EXÉCUTABLE : le CSS et la fonction rueKit, à copier mot pour mot dans chaque séquence ; la rue, le héros, le taxi, la voiture blanche, l étiquette, la bulle, le sous-titre, le téléphone). Images de style : styleframes/P01.html à P27.html, une par plan."

colors:
  canvas: "#0d0e12"            # le noir du pivot
  sky-dawn: "#f7d9a8"          # matin (7 h), dégradé vers #fdf0dc
  sky-noon: "#fff3da"          # midi, lumière dure
  sky-dusk: "#2b2742"          # soir, dégradé vers #e3784c à l'horizon
  goudron: "#3a3b42"           # la route, pointillés #f2efe6
  trottoir: "#d8c3a0"
  paper: "#f6f5f2"             # monde de la solution (le téléphone), fond clair
  card-light: "#ffffff"
  ink: "#17181c"               # texte sur le clair
  ink-soft: "#55565c"
  ink-on-dark: "#f4f2ee"
  accent: "#ff3b30"            # rouge Yango PROVISOIRE : boîte du mot clé, traits de pic, éléments de l'appli, carte de fin
  accent-deep: "#d92b21"
  accent-glow: "#ff8a80"
  taxi: "#f28c28"              # le taxi orange d'Abidjan (objet du monde, pas un accent)
  skin-1: "#6b3f26"
  skin-2: "#8a5a3b"
  skin-3: "#4a2a19"

fonts:
  Instrument Sans: { files: ["assets/fonts/InstrumentSans-400.woff2 (400)", "assets/fonts/InstrumentSans-500.woff2 (500)", "assets/fonts/InstrumentSans-600.woff2 (600)", "assets/fonts/InstrumentSans-700.woff2 (700)"] }
  Space Mono: { files: ["assets/fonts/SpaceMono-400.woff2 (400)", "assets/fonts/SpaceMono-700.woff2 (700)"] }
  Big Shoulders: { files: ["assets/fonts/BigShoulders-800.woff2 (800)"] }

typography:
  subtitle:  { fontFamily: "Instrument Sans", px: 62, weight: 600, lineHeight: 74, tracking: "-0.015em", note: "la phrase de la voix EN BAS AU CENTRE (haut à y 896, bande y 890 à 980 libre de tout autre élément), 45 caractères au plus par morceau, mot par mot ; encre #17181c avec halo clair sur les scènes claires, #f4f2ee avec ombre sur les scènes sombres" }
  type:      { fontFamily: "Instrument Sans", px: 84, weight: 600, note: "UN seul moment typographique : le pivot « Et si on arrêtait de discuter ? »" }
  bubble:    { fontFamily: "Instrument Sans", px: 44, weight: 700, note: "bulles de dialogue (« Plateau ? », « 3 000 », « Yopougon ? Non ! »)" }
  price:     { fontFamily: "Space Mono", px: 40, weight: 700, tabularNums: true, note: "l'étiquette de prix « 3 000 F » et le prix de l'appli" }
  ui:        { fontFamily: "Instrument Sans", px: 26, weight: 500 }
  sign:      { fontFamily: "Instrument Sans", px: 40, weight: 700, note: "panneaux de rue (« Riviera 2 », « Yopougon »), blanc sur vert #1f6b4a" }
  wordmark:  { fontFamily: "Instrument Sans", px: 150, weight: 700, note: "« Yango » PROVISOIRE, blanc sur rouge, en attendant le logo officiel" }
  cta:       { fontFamily: "Instrument Sans", px: 40, weight: 700, note: "bouton « Télécharger l’application », rouge sur blanc" }

components:
  street:
    look: "illustration plate, sans contours : ciel en dégradé selon l'heure, tours du Plateau en silhouette au loin (bleu-gris à 35 %), palmiers, trottoir #d8c3a0 en y 720 à 790, bordure claire, goudron #3a3b42 de y 790 à 1080 avec pointillés ; le panneau vert « Riviera 2 » sur poteau. La caméra longe la rue de gauche à droite."
  person:
    look: "personnage plat : tête ronde (peau brune, cheveux courts), PAS de visage détaillé (deux petits yeux au plus), corps en formes arrondies ; le héros porte chemise blanche, cravate rouge brique, pantalon sombre, chaussures noires (puis claquettes au gag). Le MÊME dessin dans tout le film. Passagers de la solution : une maman (pagne), un jeune employé (sac à dos), un commerçant (boubou)."
  taxi:
    look: "taxi orange #f28c28 vu de profil, vitres teintées, enseigne « TAXI » sur le toit, chauffeur en buste derrière la vitre (casquette) ; arrive flou et étiré (filé), freine avec une petite plongée du capot."
  yango-car:
    look: "berline blanche vue de profil, liseré rouge (PROVISOIRE, sans logo), même gabarit que le taxi ; elle remplace le taxi dans la solution et la rime."
  price-tag:
    look: "étiquette blanche arrondie, œillet et ficelle, prix en Space Mono 700 « 3 000 F » ; flotte au-dessus de la tête du héros, change de prix au gag (3 000 → 2 500 → 1 500), revient FIGÉE en solution."
  bubble:
    look: "bulle blanche à queue, ombre douce ; les prix de la discussion rebondissent d'une bulle à l'autre."
  phone:
    look: "téléphone d'aujourd'hui, bords fins noirs, écran 390 × 844 ; appli GÉNÉRIQUE PROVISOIRE : carte claire (routes grises, eau bleu pâle), champ « Où allez-vous ? », fiche de prix, voiture sur la carte, fiche du chauffeur (nom, voiture, plaque). Accent rouge seulement pour l'action."
  word-by-word: { rule: "chaque mot apparaît sur son horodatage, gris puis plein, flou → net en 0,14 s, immediateRender:false" }
  key-word-box: { look: "rectangle rouge #ff3b30, angles nets (3 px), déborde de 0,14 em ; le mot passe en blanc dedans", motion: "se trace depuis la gauche en 0,16 s power3.out" }
  peak-stroke: { look: "trait de pinceau effilé rouge sous LE mot clé", motion: "se dessine en 0,4 s power2.out" }
  cursor: { description: "un doigt-repère (cercle blanc à contour sombre) qui arrive d'un seul mouvement et tape directement : onde rouge" }
  end-card: { description: "fond rouge plein, « Yango » blanc qui s'assemble, bouton blanc « Télécharger l’application », tap, tenue vivante (la petite voiture blanche longe une route en filet), puis iris" }

negative:
  - "Un seul mécanisme de mise en valeur (boîte rouge) et 3 ou 4 traits de pic ; pas de texte coloré, pas de mot géant."
  - "Rien dans la bande du sous-titre (y 890 à 980) ; le goudron y passe mais sans objet ni texte."
  - "Aucun logo réel tant que la marque ne l'a pas fourni ; aucune autre marque (pas de logos de stores)."
  - "Pas de caricature : personnages simples, dignes, variés ; le chauffeur de taxi n'est pas ridiculisé (il hésite, il repart)."
  - "Pas de prix réel présenté comme un tarif Yango : les montants à l'écran sont des exemples à faire valider."
  - "Jamais d'aller-retour de caméra ; pas de repeat:-1 ; jamais de tween de letterSpacing."
---

# « On dit combien ? » : charte

La rue d'Abidjan est le lieu du film : le carrefour Riviera 2 au petit matin, la chaleur de midi, le soir au bord du
goudron. Le héros y lève la main, le taxi orange s'y arrête, la discussion du prix s'y joue chaque jour. Au pivot, tout
s'éteint : « Et si on arrêtait de discuter ? ». La lumière revient dans le téléphone, sur fond clair et rouge Yango :
la destination, le prix affiché, la voiture qui vient, le chauffeur et sa plaque. Puis, en rime, le même carrefour au
même moment, mais la voiture est déjà là. La carte de fin est rouge.
