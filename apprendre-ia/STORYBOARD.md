---
format: 1920x1080
duration: "45.80s"
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

**VOIX** : minutage de onsets.json (débuts de phrase mesurés sur l'énergie du son ; mots à l'intérieur des phrases estimés, ±0,15 s, à recaler avec Whisper avant d'animer). Silences de plus de 0,4 s, chacun écrit comme un plan avec son action : 0.59 à 1.02 (la fenêtre s'ouvre) · 1.84 à 2.21 (le post-it arrive) · 2.74 à 3.22 (whip) · 3.94 à 4.39 (le téléphone s'éveille) · 5.15 à 5.61 (le post-it arrive) · 6.12 à 6.62 (whip) · 7.53 à 8.02 (l'accueil de l'IA) · 9.18 à 11.60 (LE GAG) · 12.18 à 12.63 (la frise se met à glisser) · 14.62 à 15.08 (poussée dans l'écran) · 16.69 à 17.06 (whip) · 18.28 à 18.72 (whip) · 20.13 à 20.60 (recul au partage) · 22.48 à 22.99 (coupe au noir) · 23.48 à 24.96 (LE PIVOT : le post-it tombe, le point s'embrase) · 28.00 à 28.44 (cran vers le champ) · 29.69 à 30.11 (envoi, clic) · 30.91 à 31.36 (whip, la carte de code) · 34.23 à 34.69 (les tuiles se posent) · 37.64 à 38.12 (recul vers le portable) · 39.27 à 39.70 (poussée sur le post-it) · 40.27 à 40.59 (le feutre barre « Pas ») · 41.19 à 41.66 (le jaune devient bouton) · 43.17 à 45.80 (clic, tenue, iris).

**COUPES** (voix narrative, quota 0 à 4) : une seule, 22.90 · premier mot « Pas » (22.99) · changement d'acte (l'excuse → le tournant), la musique se coupe sur un impact grave. Plus le flash de lumière de 24.80 (la seule transition « effet »). Toutes les autres jonctions sont des coutures de caméra ou d'objet.

**RYTHME** : douleur (0 à 22.90) 10 plans = 4,4 plans / 10 s mais un événement toutes les 0,2 à 0,5 s (accroche) et 0,5 s (douleurs) ; pivot 1 plan ; solution et fin (24.80 à 45.80) 11 plans = 5,2 plans / 10 s, un événement toutes les 0,5 s.

**SON** (verrouillé sur l'image, temps globaux) : musique de tension de 0 à 22.90, montée (riser) de 19.90 à 22.90, coupée net par un impact grave à 22.90, silence ; la musique d'élan revient avec son attaque sur « Aujourd'hui » (24.96), respire sous la voix, s'éteint en fondu sur la carte de fin. Bruitages : whoosh court 0.05 · clic doux 0.30 · pop 0.95 · pop 2.12 (post-it) · whoosh court 2.82 · clic doux 3.22 · notification 4.30 · pop 5.50 (post-it) · whoosh court 6.10 · whoosh court 6.40 · clic doux 6.62 · scintillement 7.00 · frappe 9.45 · ping 10.30 (le gag) · whoosh 11.22 · pop 11.55 (post-it) · whoosh cinématique 12.70 · whoosh courts 13.10, 13.50, 14.60 · whoosh court 14.90 · clic 15.50 · clics doux 15.85, 16.05, 16.25 · notifications 17.10, 17.22, 17.34 · clic doux 17.55 · whoosh courts 18.32, 18.52 · frappe 19.20 · clic doux 19.55 · whoosh 20.30 · pops 21.19, 21.35, 21.50 · impact grave 22.90 · whoosh court 23.80 · scintillement 24.40 · whoosh cinématique 24.70 · scintillement 25.30 · frappe 26.30 · pop 26.80 · frappe 27.50 · carillon 27.95 · whoosh court 28.24 · frappe 28.45 · clic 30.08 · pops 30.20, 30.50 · whoosh courts 30.98, 31.15 · pop 31.30 · glitch 32.16 · pops 32.80, 33.20, 33.60 · whoosh 34.28 · carillons 35.70, 36.35, 37.25 · whoosh 37.72 · whoosh court 37.90 · pop 38.30 (post-it) · clic doux 40.30 · NOTIFICATION À DEUX TONS 40.60 (la signature : « c'est pour toi ») · whoosh cinématique 41.20 · whoosh court 41.42 · pop 41.70 · clic 43.20 · whoosh 45.30.

## Frame 1 : Deux mille, deux mille dix · 0.00 → 6.37

- scene: Sur la frise du bureau de nuit, l'écran cathodique de 2000 propose « Créer votre site internet ? » et un post-it « Pas pour moi » s'y colle ; whip vers 2010, le smartphone invite à « Rejoindre le réseau » et le même post-it s'y colle
- duration: 6.37s
- transition_in: cut
- status: animated
- src: compositions/frames/01-annees.html
- voiceover: "Deux mille. Un site internet ? Pas pour moi. Deux mille dix. Les réseaux sociaux ? Pas pour moi."
- type: hook
- blueprint: spatial-pan-stations (Adapt)
- focal: l'écran de 2000 puis le smartphone de 2010, chacun couvert du post-it
- rules: depth-of-field-blur, motion-blur-streak
- world: dark
- handoff_in: aucun (ouverture du film) ; première image = la frise du bureau de nuit (ligne en y 770, graduation et « 2000 » sous le centre) et l'écran cathodique qui arrive sur la ligne, ×1,15 et flou 8 px
- handoff_out: à 6.37 : cam2 en plein whip vers la droite (+9000 px/s), flou 16 px, entre la station 2010 (sortie par la gauche) et la station 2026 (pas encore entrée) ; la ligne de la frise en y 770, filée ; aucun appareil net ; sous-titre sorti ; bureau de nuit, trame de points, grain 5 %

Word cues: Deux@0.05 mille@0.32 (silence de 0.59 à 1.02) Un@1.02 site@1.20 internet@1.38 Pas@2.21 pour@2.39 moi@2.56 (silence de 2.74 à 3.22) Deux@3.22 mille@3.46 dix@3.70 (silence de 3.94 à 4.39) Les@4.39 réseaux@4.56 sociaux@4.85 (silence de 5.15 à 5.61) Pas@5.61 pour@5.78 moi@5.95

Scene 1 (0.00 à 2.98 s) : P01, 2000
  TEXTE ÉCRAN : sous-titre « Deux mille. Un [boîte : site internet] ? Pas pour moi. » ; boîte tracée à 1.18 ; écart synchro
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 l'écran cathodique (frame.md device-crt) arrive sur la ligne au-dessus de « 2000 » (×1,15, flou 8 → net en 0,12 s expo.out, ombre de contact) ; 0.30 l'écran s'allume (lueur 0,1 s, lignes de balayage) ; 0.70 le pointeur d'époque traverse l'écran ; 0.95 la fenêtre « Assistant » s'ouvre (×0,9 → 1 en 0,1 s) : « Créer votre site internet ? » et les boutons « Oui » / « Plus tard », 0,07 s avant « Un » ; 1.40 le bouton « Oui » clignote une fois ; 1.80 le pointeur se pose sur « Oui » ; 2.12 LE POST-IT arrive de la caméra (×1,6, flou 10, rotation -14° → -7°) et se colle sur l'écran en couvrant la fenêtre (claquement 0,97 → 1), 0,09 s avant « Pas » ; 2.56 « moi » : son coin bas droit se soulève de 3° (vie) ; 2.78 départ du whip.
  PISTE CAMÉRA : dérive x +18 px/s et poussée 2 %/s autour de cam2(960, 500, 1) ; 2.78 à 2.98 whip vers la droite (power2.in, flou 0 → 14 px).
  COUCHES ET PROFONDEUR : avant-plan : le clavier beige flou coupé par le bord gauche ; sujet : l'écran et le post-it ; fond : frise, trame de points, halo bleu-gris ; couches animées 2 à 3.
  OBJET-PONT ET VECTEUR : le post-it : il se recollera sur le smartphone (5.50), sur le portable (11.55) et à la fin (38.30) ; vecteur : whip vers la droite.
  SON : whoosh court 0.05 (l'écran se pose) ; clic doux 0.30 ; pop 0.95 (la fenêtre) ; pop 2.12 (le post-it, le son du post-it) ; whoosh court 2.82.
  IMAGE CLÉ : 2.40 : l'écran cathodique posé sur la frise au-dessus de « 2000 », sa fenêtre « Créer votre site internet ? » à moitié cachée par le post-it jaune « Pas pour moi ». (styleframes/png/P01.png)

Scene 2 (2.98 à 6.37 s) : P02, 2010
  TEXTE ÉCRAN : sous-titre « Deux mille dix. » puis « Les [boîte : réseaux sociaux] ? Pas pour moi. » ; boîte tracée à 4.54
  IMAGE DE DÉPART : sommet du whip : la frise filée, l'écran de 2000 sort par la gauche, flou.
  ÉTAPES : 2.98 à 3.14 le whip se pose (expo.out, flou 14 → 0) sur le smartphone de 2010, déjà sur la ligne ; 3.22 « Deux mille dix » : « 2010 » s'allume (gris → blanc, 0,1 s) ; 3.60 l'écran du téléphone s'éveille (grille d'icônes) ; 4.30 la notification « Rejoins tes amis sur le réseau » et son bouton « S’inscrire » tombent du haut de l'écran (y -40 → 0, 0,12 s), 0,09 s avant « Les » ; 4.85 « sociaux » : le bouton pulse une fois ; 5.50 le post-it arrive de la caméra et se colle sur le téléphone, plus large que lui (rotation 14° → 6°), 0,11 s avant « Pas » ; 5.98 le sous-titre sort ; 6.05 départ du whip.
  PISTE CAMÉRA : 2.98 à 3.14 atterrissage expo.out sur cam2(2220, 500, 1) ; dérive x +18 px/s ; 6.05 à 6.37 whip vers la droite (power2.in, flou 0 → 16 px).
  COUCHES ET PROFONDEUR : avant-plan : l'écran de 2000 flou qui sort à gauche ; sujet : le smartphone et le post-it ; fond : frise et sol ; couches 2 à 3.
  OBJET-PONT ET VECTEUR : vecteur : le whip vers la droite, repris par la séquence 2.
  SON : clic doux 3.22 (l'année) ; notification 4.30 ; pop 5.50 (le post-it) ; whoosh court 6.10.
  IMAGE CLÉ : 5.80 : le smartphone de 2010 posé sur la frise au-dessus de « 2010 », sa notification couverte par le post-it qui déborde des deux côtés. (styleframes/png/P02.png)

## Frame 2 : Deux mille vingt-six, le gag · 6.37 → 11.40

- scene: Le whip se pose sur le portable de 2026 : l'assistant IA attend « Écris ta demande… » ; cran dans le champ : il tape « Pas pour » et l'IA complète en gris « moi. » ; il se fige
- duration: 5.03s
- transition_in: cut
- status: animated
- src: compositions/frames/02-ia.html
- voiceover: "Deux mille vingt-six. L’intelligence artificielle ?"
- type: hook
- blueprint: prompt-type-submit-generate (Adapt)
- focal: le champ de saisie de l'assistant IA
- rules: coordinate-target-zoom, discrete-text-sequence
- world: dark
- handoff_in: à 0.00 : cam2 en plein whip vers la droite (+9000 px/s), flou 16 px, entre la station 2010 (sortie par la gauche) et la station 2026 (pas encore entrée) ; la ligne de la frise en y 770, filée ; aucun appareil net ; sous-titre sorti ; bureau de nuit, trame de points, grain 5 %
- handoff_out: à 5.03 : recul en cours (power2.in) depuis le champ de saisie, échelle ×1,2, flou 14 px ; au centre « Pas pour » et « moi. » en gris ; le portable, la frise et « 2026 » flous ; aucun sous-titre ; bureau de nuit

Word cues: Deux@0.25 mille@0.49 vingt-six@0.73 (silence de 1.16 à 1.65) L’intelligence@1.65 artificielle@2.23 (silence de 2.81 à 5.03)

Scene 1 (0.00 à 2.81 s) : P03, 2026
  TEXTE ÉCRAN : sous-titre « Deux mille vingt-six. » puis « [boîte : L’intelligence artificielle] ? » ; boîte tracée à 1.63
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.18 le whip se pose (expo.out) sur le portable de 2026, posé sur la ligne ; la tasse traverse l'avant-plan gauche, floue (parallaxe ×2,5) ; 0.25 « 2026 » s'allume ; 0.63 l'écran s'éveille : « Assistant IA » et son point jaune ; 1.03 « Bonjour. Que veux-tu faire aujourd’hui ? » monte (y 10 → 0, 0,12 s) ; 1.53 le caret jaune clignote dans le champ « Écris ta demande… » (pas finis) ; 1.65 « L’intelligence artificielle » ; 2.23 la poussée continue.
  PISTE CAMÉRA : 0.00 à 0.18 atterrissage expo.out sur cam2(3480, 500, 1) ; poussée linéaire ×1 → ×1,08 vers l'écran jusqu'à 2.81.
  COUCHES ET PROFONDEUR : avant-plan : la tasse floue coupée par le bord gauche ; sujet : le portable ; fond : frise et sol ; couches 3.
  OBJET-PONT ET VECTEUR : le champ de saisie devient le gros plan du gag ; la tasse reviendra en 21.56.
  SON : whoosh court 0.03 ; clic doux 0.25 ; scintillement 0.63 (l'écran IA).
  IMAGE CLÉ : 2.23 : le portable de 2026 posé sur la frise au-dessus de « 2026 », l'assistant IA allumé, la tasse floue à gauche. (styleframes/png/P03.png)

Scene 2 (2.81 à 5.03 s) : P04, le gag (muet)
  TEXTE ÉCRAN : aucun texte de sous-titre (silence écrit : le gag).
  IMAGE DE DÉPART : le champ de saisie au centre du cadre, l'accueil au-dessus.
  ÉTAPES : 2.81 à 3.03 cran dans le champ ; 2.93 le sous-titre sort ; 3.08 « Pas pour » se tape, une lettre toutes les 0,07 s (jusqu'à 3.57) ; 3.68 le caret clignote ; 3.93 la suggestion « moi. » apparaît en gris (opacité 0 → 0,32 en 0,08 s) avec la touche « TAB » ; 4.03 il se fige : le caret s'arrête (le temps comique), la suggestion respire à peine (0,32 ↔ 0,26) ; 4.53 le caret clignote une fois ; 4.83 départ du recul.
  PISTE CAMÉRA : 2.81 à 3.03 cran ×1,08 → ×2,4 sur le champ (expo.inOut, flou 8 au sommet) ; dérive x -10 px/s ; 3.93 à 4.05 micro-cran ×1,05 vers « moi. » ; 4.83 à 5.03 recul ×2,4 → ×1,2 (power2.in, flou 0 → 14 px).
  COUCHES ET PROFONDEUR : avant-plan : les bords du portable flous ; sujet : le champ ; fond : l'accueil flou ; couches 2.
  OBJET-PONT ET VECTEUR : le champ de saisie reviendra au même cadrage en 28.40 ; vecteur : recul.
  SON : frappe 3.08 ; ping 3.93 (la suggestion, le temps comique) ; whoosh 4.85.
  IMAGE CLÉ : 4.23 : le champ plein cadre : « Pas pour » tapé, « moi. » en gris proposé par l'IA, la touche TAB, le caret jaune figé. (styleframes/png/P04.png)

## Frame 3 : Le monde n'a pas attendu · 11.40 → 14.85

- scene: Recul : les trois bureaux sur la frise, trois post-its ; la caméra longe la frise vers la droite pendant que les portables des autres, écrans allumés, filent devant et disparaissent ; le nôtre reste seul avec son post-it
- duration: 3.45s
- transition_in: cut
- status: animated
- src: compositions/frames/03-monde.html
- voiceover: "Le problème ? Le monde, lui, n’a pas attendu."
- type: problem
- blueprint: zoom-out-workspace-reveal (Adapt)
- focal: notre portable couvert du post-it, seul, pendant que les autres filent
- rules: motion-blur-streak, multi-phase-camera
- world: dark
- handoff_in: à 0.00 : recul en cours (power2.in) depuis le champ de saisie, échelle ×1,2, flou 14 px ; au centre « Pas pour » et « moi. » en gris ; le portable, la frise et « 2026 » flous ; aucun sous-titre ; bureau de nuit
- handoff_out: à 3.45 : poussée en cours (power2.in) dans l'écran du portable 2026, échelle ×1,6, flou 14 px ; l'écran remplit 80 % du cadre, son contenu flou ; le post-it sort par le haut à gauche, flou ; aucun sous-titre ; bureau de nuit

Word cues: Le@0.20 problème@0.41 (silence de 0.78 à 1.23) Le@1.23 monde@1.49 lui@1.86 n’a@2.02 pas@2.34 attendu@2.60

Scene 1 (0.00 à 1.20 s) : P05, Le problème ?
  TEXTE ÉCRAN : sous-titre « Le [boîte : problème] ? » ; boîte tracée à 0.39
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.40 le recul continue jusqu'au plan large : les trois bureaux posés sur la frise, l'écran et le téléphone couverts de leur post-it ; 0.15 le troisième post-it arrive de la caméra et se colle sur l'écran du portable, 0,05 s avant « Le » ; 0.41 « problème » ; 0.60 les trois post-its frémissent l'un après l'autre (±2°, décalage 0,05 s) ; 0.90 la ligne commence à glisser.
  PISTE CAMÉRA : 0.00 à 0.40 recul expo.out jusqu'à cam2(2220, 450, 0,5) ; dérive x +20 px/s.
  COUCHES ET PROFONDEUR : avant-plan : le post-it qui arrive, flou ; sujet : les trois bureaux ; fond : frise et sol ; couches 3.
  OBJET-PONT ET VECTEUR : la ligne de la frise : elle se met à défiler en P6.
  SON : pop 0.15 (le post-it).
  IMAGE CLÉ : 0.60 : les trois bureaux sur la frise, 2000, 2010, 2026, trois post-its « Pas pour moi », le dernier en train de se coller. (styleframes/png/P05.png)

Scene 2 (1.20 à 3.45 s) : P06, Le monde n'a pas attendu
  TEXTE ÉCRAN : sous-titre « Le monde, lui, [boîte : n’a pas attendu]. » ; boîte tracée à 2.00
  IMAGE DE DÉPART : le plan large de P5.
  ÉTAPES : 1.20 la caméra part vers la droite ; l'écran de 2000 et le téléphone sortent par la gauche ; 1.30 « monde » : un premier portable allumé (écran jaune pâle) file le long de la ligne avec sa traînée ; 1.70 un deuxième ; 2.02 « n’a pas attendu » ; 2.10 un troisième ; sous la ligne, « 2027 », « 2028 », « 2029 » défilent, filées ; 2.60 « attendu » : le dernier sort par la droite ; notre portable reste seul à gauche, son écran baisse un peu ; 3.10 départ de la poussée.
  PISTE CAMÉRA : 1.20 à 1.60 travelling expo.inOut jusqu'à cam2(4740, 450, 0,5) ; dérive x +30 px/s ; 3.10 à 3.45 poussée ×0,5 → ×1,6 dans notre écran (power2.in, flou 0 → 14 px).
  COUCHES ET PROFONDEUR : avant-plan : traînées rapides ; milieu : les portables des autres, flous ; sujet : notre portable net ; fond : sol ; parallaxe 3:1 ; couches 3 à 4.
  OBJET-PONT ET VECTEUR : notre écran devient la fenêtre « Présentation » de la séquence 4.
  SON : whoosh cinématique 1.30 (le monde file) ; whoosh courts 1.70 et 2.10 ; whoosh court 3.20.
  IMAGE CLÉ : 2.40 : notre portable couvert du post-it, net à gauche ; à droite la ligne filée, trois portables allumés qui s'éloignent, « 2027 2028 2029 » flous. (styleframes/png/P06.png)

## Frame 4 : Ta soirée, ta matinée · 14.85 → 18.50

- scene: L'horloge murale à gauche, les applis à droite : la présentation vide (Diapo 1 / 20) pendant que l'horloge file jusqu'à 22:47 ; whip, la boîte de réception (87 non lus) pendant qu'elle file jusqu'à 12:00
- duration: 3.65s
- transition_in: cut
- status: animated
- src: compositions/frames/04-soiree.html
- voiceover: "Ta présentation te prend une soirée. Tes mails, ta matinée."
- type: pain_point
- blueprint: fixed-anchor-cycle (Adapt)
- focal: l'horloge qui avale le temps, puis l'appli
- rules: counting-dynamic-scale, coordinate-target-zoom
- world: dark
- handoff_in: à 0.00 : poussée en cours (power2.in) dans l'écran du portable 2026, échelle ×1,6, flou 14 px ; l'écran remplit 80 % du cadre, son contenu flou ; le post-it sort par le haut à gauche, flou ; aucun sous-titre ; bureau de nuit
- handoff_out: à 3.65 : whip vers la droite en cours (flou 14 px) : la fenêtre « Messagerie » sort par la gauche, filée ; l'horloge reste à sa place (Ø 300, centre (315, 430)), nette, à 12:00 ; sous-titre sorti ; bureau de nuit, halo chaud

Word cues: Ta@0.23 présentation@0.41 te@0.95 prend@1.17 une@1.32 soirée@1.53 Tes@2.21 mails@2.45 ta@2.92 matinée@3.06

Scene 1 (0.00 à 2.10 s) : P07, Ta soirée
  TEXTE ÉCRAN : sous-titre « Ta présentation te prend [boîte : une soirée]. » ; boîte tracée à 1.30
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.15 la poussée se pose : l'écran devient la fenêtre « Présentation » à droite ; l'horloge murale arrive de la caméra à gauche (×1,4, flou 10 → net en 0,14 s), à 18:00 ; 0.23 « Ta présentation » : diapo 1 sélectionnée, « Cliquez pour ajouter un titre », « DIAPO 1 / 20 » ; 0.65 le curseur clique dans le titre, le caret clignote, rien ne s'écrit ; 0.95 « te prend » : les aiguilles font deux tours (0,8 s power2.inOut) jusqu'à 22:47, l'heure numérique défile, le halo vire au bleu nuit ; 1.53 « soirée » ; 1.75 le titre est toujours vide ; 1.95 départ du whip.
  PISTE CAMÉRA : atterrissage 0.00 à 0.15 expo.out ; dérive x -12 px/s et poussée 1,5 %/s ; 1.95 à 2.10 whip vers la droite (expo.inOut, flou 10 px) sur la fenêtre seulement, l'horloge reste.
  COUCHES ET PROFONDEUR : sujet : l'horloge (nette quand elle tourne) puis la fenêtre ; fond : sol et halo ; couches 2 à 3.
  OBJET-PONT ET VECTEUR : l'horloge reste à sa place (l'ancre), seules les applis changent.
  SON : whoosh court 0.05 ; clic 0.65 ; clics doux 1.00, 1.20, 1.40 (les aiguilles).
  IMAGE CLÉ : 1.65 : l'horloge à 22:47 à gauche, l'éditeur de diapos vide à droite, « DIAPO 1 / 20 ». (styleframes/png/P07.png)

Scene 2 (2.10 à 3.65 s) : P08, Ta matinée
  TEXTE ÉCRAN : sous-titre « Tes mails, [boîte : ta matinée]. » ; boîte tracée à 2.90
  IMAGE DE DÉPART : sommet du whip : la fenêtre « Messagerie » entre par la droite, filée ; l'horloge en place.
  ÉTAPES : 2.10 la boîte de réception se pose (expo.out) : « Boîte de réception », « 87 NON LUS » ; 2.21 « Tes mails » : sept lignes de mails montent du bas (décalage 0,04 s) ; 2.45 le compteur roule de 87 à 94 ; 2.65 l'horloge file de 08:30 à 12:00 (0,6 s), le halo devient chaud ; 3.06 « matinée » ; 3.35 le sous-titre sort ; 3.45 départ du whip.
  PISTE CAMÉRA : dérive x -12 px/s ; 3.45 à 3.65 whip vers la droite (power2.in, flou 0 → 14 px).
  COUCHES ET PROFONDEUR : sujet : la boîte de réception, puis l'horloge ; fond : sol, halo chaud ; couches 2 à 3.
  OBJET-PONT ET VECTEUR : l'horloge reste (l'ancre).
  SON : notifications 2.25, 2.37, 2.49 ; clic doux 2.70 ; whoosh court 3.47.
  IMAGE CLÉ : 3.15 : l'horloge à 12:00 à gauche, la boîte de réception pleine à droite, « 87 NON LUS ». (styleframes/png/P08.png)

## Frame 5 : Ton dimanche, avant le café · 18.50 → 22.90

- scene: Le tableur de la compta pendant que l'horloge marque DIM. ; recul : les trois tâches à gauche (« Toi »), les mêmes cochées à droite (« D'autres »), la tasse de café fumante devant
- duration: 4.40s
- transition_in: cut
- status: animated
- src: compositions/frames/05-cafe.html
- voiceover: "Ta compta, ton dimanche. Pour d’autres, c’est réglé avant le café."
- type: pain_point
- blueprint: comparison-split (Adapt)
- focal: le tableur, puis le partage Toi / D'autres et la tasse
- rules: waterfall-entry, depth-of-field-blur
- world: dark
- handoff_in: à 0.00 : whip vers la droite en cours (flou 14 px) : la fenêtre « Messagerie » sort par la gauche, filée ; l'horloge reste à sa place (Ø 300, centre (315, 430)), nette, à 12:00 ; sous-titre sorti ; bureau de nuit, halo chaud
- handoff_out: à 4.40 : coupe franche voulue : dernière image = le partage « Toi » / « D'autres » complet, trois coches jaunes, la tasse fumante devant à droite, sous-titre sorti ; aucun raccord de caméra

Word cues: Ta@0.22 compta@0.35 ton@1.03 dimanche@1.25 (silence de 1.63 à 2.10) Pour@2.10 d’autres@2.30 c’est@2.46 réglé@2.69 avant@3.06 le@3.42 café@3.62 (silence de 3.98 à 4.40)

Scene 1 (0.00 à 1.90 s) : P09, Ton dimanche
  TEXTE ÉCRAN : sous-titre « Ta compta, [boîte : ton dimanche]. » ; boîte tracée à 1.01
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.16 le tableur « Compta 2026 » se pose ; 0.22 « Ta compta » : les lignes se remplissent une à une (0,05 s), dates, libellés, montants ; 0.70 le curseur tape dans une cellule ; 1.03 « ton dimanche » : « DIM. » s'imprime dans le cadran, les aiguilles filent de 10:00 à 18:30, le halo devient gris ; 1.60 pas de total ; 1.75 départ du recul.
  PISTE CAMÉRA : dérive x -12 px/s ; 1.75 à 2.10 recul expo.out vers le partage.
  COUCHES ET PROFONDEUR : sujet : le tableur, puis l'horloge ; fond : sol, halo gris ; couches 2.
  OBJET-PONT ET VECTEUR : la fenêtre rétrécit et devient la carte « Compta » de P10.
  SON : whoosh court 0.02 ; frappe 0.70 ; clic doux 1.05.
  IMAGE CLÉ : 1.40 : l'horloge « DIM. » à 18:30 à gauche, le tableur de la compta à droite. (styleframes/png/P09.png)

Scene 2 (1.90 à 4.40 s) : P10, Avant le café
  TEXTE ÉCRAN : sous-titre « Pour d’autres, c’est réglé [boîte : avant le café]. » ; boîte tracée à 3.04
  IMAGE DE DÉPART : la fenêtre du tableur qui rétrécit en carte.
  ÉTAPES : 1.90 à 2.20 la fenêtre rétrécit dans la carte « Compta » de la colonne « Toi », « Présentation · 22:47 » et « Mails · 12:00 » se posent au-dessus (décalage 0,05 s), chacune avec sa petite horloge ; 2.10 « Pour d’autres » : la colonne « D’autres » glisse depuis la droite, les mêmes trois cartes ; 2.69, 2.85, 3.00 « c’est réglé » : trois coches jaunes ; 3.06 « avant le café » : la tasse de P3 arrive devant, fumée vivante ; 3.80 les petites horloges de gauche tournent encore ; 3.98 le sous-titre sort.
  PISTE CAMÉRA : poussée lente ×1 → ×1,03 ; 2.10 cran léger vers la colonne de droite (0,1 s).
  COUCHES ET PROFONDEUR : avant-plan : la tasse (sujet final) ; milieu : les cartes ; fond : sol ; couches 3.
  OBJET-PONT ET VECTEUR : aucun : coupe franche à 22.90 sur « Pas » (changement d'acte : l'excuse → le tournant).
  SON : pops 2.69, 2.85, 3.00 (les coches) ; la montée de la musique de tension de 1.40 à 4.40 ; impact grave 4.40.
  IMAGE CLÉ : 3.30 : à gauche « Toi » et trois tâches avec leurs horloges (22:47, 12:00, DIM.), à droite « D’autres » et les mêmes tâches cochées en jaune, la tasse fumante devant. (styleframes/png/P10.png)

## Frame 6 : Pas cette fois · 22.90 → 24.80

- scene: Coupe au noir : « Pas cette fois. » centré ; le post-it se décolle et tombe dans le noir ; à sa place, un point de lumière s'embrase
- duration: 1.90s
- transition_in: cut
- status: animated
- src: compositions/frames/06-pivot.html
- voiceover: "Pas cette fois."
- type: problem
- blueprint: video-text-pivot (Adapt)
- focal: « Pas cette fois. » et le post-it qui tombe
- rules: svg-path-draw, motion-blur-streak
- world: dark
- handoff_in: aucun raccord de caméra (coupe franche voulue) ; première image : noir #0a0b0f plein cadre, grain sombre ; le post-it « Pas pour moi » seul en haut au centre (810, 60), rotation -5°, net
- handoff_out: à 1.90 : noir ; point de lumière en (960, 210) embrasé, cœur 40 px, halos 160 et 520 px, en train de grossir ; aucun texte ; grain sombre (départ du flash de lumière d'assemble.sh, LEAK 960, 210)

Word cues: Pas@0.09 cette@0.25 fois@0.42 (silence de 0.58 à 1.90)

Scene 1 (0.00 à 1.90 s) : P11, Pas cette fois.
  TEXTE ÉCRAN : moment typographique sur le noir : « Pas [trait : cette fois.] » centré sur y 560, 84 px, #f3f1ec (Pas 0.09, cette 0.25, fois. 0.42 ; le trait jaune se dessine de 0.30 à 0.70) ; pas de sous-titre en bas.
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 noir ; le post-it seul en haut au centre ; 0.09 « Pas », 0.25 « cette », 0.42 « fois. » ; 0.30 à 0.70 le trait jaune ; 0.70 le coin du post-it se décolle (rotation -5° → 18°, 0,2 s power2.in) ; 0.90 il tombe (y +900 en 0,35 s power2.in, flou vertical 8 px) et sort par le bas ; 1.30 la phrase s'efface (flou 0 → 8, opacité → 0, 0,2 s) ; 1.50 un point de lumière naît là où était le post-it ; 1.80 il s'embrase.
  PISTE CAMÉRA : poussée très lente ×1 → ×1,03 vers (960, 210).
  COUCHES ET PROFONDEUR : sujet : la phrase, puis le post-it qui tombe ; fond : noir et grain ; couches 2.
  OBJET-PONT ET VECTEUR : le point de lumière devient le flash de lumière qui ouvre le papier (assemble.sh).
  SON : impact grave 0.00 (la musique se coupe net, silence) ; whoosh court 0.90 (la chute) ; scintillement 1.50 ; whoosh cinématique 1.80.
  IMAGE CLÉ : 0.80 : sur le noir, « Pas cette fois. » souligné d'un trait de pinceau jaune, le post-it qui tombe au-dessus, incliné et filé. (styleframes/png/P11.png)

## Frame 7 : L'IA rédige, résume, calcule · 24.80 → 28.22

- scene: Le flash ouvre le papier : le portable clair se pose, l'assistant IA répond ; sa réponse se partage en trois cartes, une par verbe : le document s'écrit, les 12 mails se résument en 3 points, le total se calcule
- duration: 3.42s
- transition_in: cut
- status: animated
- src: compositions/frames/07-aujourdhui.html
- voiceover: "Aujourd’hui, l’IA rédige, résume, calcule."
- type: product_intro
- blueprint: grid-card-assemble (Adapt)
- focal: l'assistant IA, puis la carte du verbe dit
- rules: counting-dynamic-scale, discrete-text-sequence
- world: light
- handoff_in: à 0.00 : noir ; point de lumière en (960, 210) embrasé, cœur 40 px, halos 160 et 520 px, en train de grossir ; aucun texte ; grain sombre (départ du flash de lumière d'assemble.sh, LEAK 960, 210)
- handoff_out: à 3.42 : cran vers le bas en cours (flou 10 px) : les trois cartes sortent par le haut, filées ; le champ de saisie clair monte du bas, flou, à l'échelle ×1,8 ; sous-titre sorti ; papier, grain 3 %

Word cues: Aujourd’hui@0.16 l’IA@0.82 rédige@1.46 résume@1.93 calcule@2.68

Scene 1 (0.00 à 1.40 s) : P12, Aujourd'hui, l'IA
  TEXTE ÉCRAN : sous-titre « Aujourd’hui, [boîte : l’IA] rédige, résume, calcule. » ; boîte tracée à 0.80
  IMAGE DE DÉPART : le flash de lumière d'assemble.sh blanchit le cadre ; dessous, le papier.
  ÉTAPES : 0.00 à 0.30 le flash retombe sur le papier ; le portable clair se pose au centre (×1,15, flou 8 → net en 0,16 s) ; 0.16 « Aujourd’hui » ; 0.50 « Assistant IA » s'allume ; 0.82 « l’IA » ; 0.90 une réponse s'écrit dans une bulle (lignes qui poussent) ; 1.20 départ du recul.
  PISTE CAMÉRA : atterrissage 0.00 à 0.30 ; poussée 2 %/s ; 1.20 à 1.50 recul expo.out vers les trois cartes.
  COUCHES ET PROFONDEUR : sujet : le portable ; fond : papier, halo jaune doux, trame de points ; couches 2.
  OBJET-PONT ET VECTEUR : la bulle de réponse se partage en trois cartes (P13).
  SON : whoosh cinématique 0.00 (le flash ; la musique d'élan attaque sur « Aujourd’hui » 0.16) ; scintillement 0.50.
  IMAGE CLÉ : 0.70 : sur le papier inondé de lumière, le portable clair au centre, l'assistant IA qui commence à répondre. (styleframes/png/P12.png)

Scene 2 (1.40 à 3.42 s) : P13, rédige, résume, calcule
  TEXTE ÉCRAN : sous-titre (suite) « … rédige, résume, calcule. »
  IMAGE DE DÉPART : la bulle de réponse au centre.
  ÉTAPES : 1.40 à 1.60 trois cartes sortent de la bulle et se posent côte à côte (marges égales) ; 1.46 « rédige » : la carte 1 est nette (les autres à 85 %, flou 1 px) : « Présentation de lundi », « 1. Où en est le projet », les lignes s'écrivent, caret ; 1.93 « résume » : la carte 2 : la pile « 12 messages » se replie dans « Résumé · 3 points » (0,2 s power3.in) ; 2.68 « calcule » : la carte 3 : la ligne « Total » arrive, le montant roule de 0 à 1 066,08 € (0,5 s) ; 3.10 les trois cartes nettes ; 3.20 elles partent vers le haut.
  PISTE CAMÉRA : dérive x +12 px/s ; crans de 0,1 s vers la carte active (1.44, 1.91, 2.66) ; 3.20 à 3.42 cran vers le bas ×1 → ×1,8 (expo.inOut, flou 10 px).
  COUCHES ET PROFONDEUR : sujet : la carte du verbe ; milieu : les deux autres, atténuées ; fond : papier ; couches 2 à 3.
  OBJET-PONT ET VECTEUR : vecteur vers le bas : le champ de saisie de la séquence 8 monte du bas.
  SON : frappe 1.50 ; pop 2.00 ; frappe 2.70 ; carillon 3.15 (le total).
  IMAGE CLÉ : 3.00 : trois cartes côte à côte : le document qui s'écrit, le résumé en 3 points, le tableur et son total, la troisième nette. (styleframes/png/P13.png)

## Frame 8 : Avec tes mots · 28.22 → 31.13

- scene: Le même champ que le gag, sur le papier : une demande en français se tape ; envoi ; dix diapos arrivent de la caméra et se rangent
- duration: 2.91s
- transition_in: cut
- status: animated
- src: compositions/frames/08-mots.html
- voiceover: "Tu lui expliques avec tes mots... elle fait le travail."
- type: benefit_highlight
- blueprint: prompt-type-submit-generate (Adapt)
- focal: le champ de saisie, puis la grille de diapos
- rules: cursor-click-ripple, waterfall-entry
- world: light
- handoff_in: à 0.00 : cran vers le bas en cours (flou 10 px) : les trois cartes sortent par le haut, filées ; le champ de saisie clair monte du bas, flou, à l'échelle ×1,8 ; sous-titre sorti ; papier, grain 3 %
- handoff_out: à 2.91 : whip vers la gauche en cours (flou 12 px) : la grille des dix diapos sort par la droite, filée ; le champ de saisie avec la phrase tapée entre par la gauche, flou ; sous-titre sorti ; papier

Word cues: Tu@0.22 lui@0.39 expliques@0.65 avec@0.85 tes@1.06 mots@1.30 (silence de 1.47 à 1.89) elle@1.89 fait@2.06 le@2.23 travail@2.39

Scene 1 (0.00 à 1.58 s) : P14, Avec tes mots
  TEXTE ÉCRAN : sous-titre « Tu lui expliques [boîte : avec tes mots]… » ; boîte tracée à 0.83
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.18 le cran se pose : le champ plein cadre, même cadrage que le gag (la rime) ; 0.22 « Tu lui expliques » : « Prépare ma présentation de lundi à partir de mes notes. » se tape, 0,025 s par lettre (0.23 à 1.53) ; 0.85 « avec tes mots » ; 1.38 le caret clignote ; 1.53 départ du recul.
  PISTE CAMÉRA : atterrissage 0.00 à 0.18 ; dérive x +12 px/s.
  COUCHES ET PROFONDEUR : avant-plan : bords du portable clair, flous ; sujet : le champ ; fond : l'accueil flou ; couches 2.
  OBJET-PONT ET VECTEUR : le champ rétrécit en haut de P15 (même objet).
  SON : whoosh court 0.02 ; frappe 0.23.
  IMAGE CLÉ : 1.18 : le champ plein cadre sur le papier, la demande tapée en français, le caret jaune, le bouton d'envoi jaune. (styleframes/png/P14.png)

Scene 2 (1.58 à 2.91 s) : P15, Elle fait le travail
  TEXTE ÉCRAN : sous-titre « elle fait [trait : le travail]. » ; trait jaune de 2.23 à 2.63
  IMAGE DE DÉPART : le champ plein cadre.
  ÉTAPES : 1.58 à 1.83 recul : le champ rétrécit en haut ; 1.78 le curseur arrive d'un seul mouvement courbe sur le bouton d'envoi ; 1.86 clic direct (pression, onde jaune) ; 1.89 « elle fait le travail » : dix diapos arrivent de la caméra (×1,35, flou 8 → net, décalage 0,06 s, 1.93 à 2.48) en grille 5 × 2 ; 2.23 à 2.63 le trait jaune ; 2.73 départ du whip.
  PISTE CAMÉRA : 1.58 à 1.83 recul expo.out ; dérive ; 2.73 à 2.91 whip vers la gauche (expo.inOut, flou 12 px).
  COUCHES ET PROFONDEUR : avant-plan : les dernières diapos qui arrivent, floues ; sujet : la grille ; fond : papier ; couches 3.
  OBJET-PONT ET VECTEUR : vecteur vers la gauche, repris par la séquence 9.
  SON : clic 1.86 ; pops 1.98 et 2.28 ; whoosh court 2.76.
  IMAGE CLÉ : 2.38 : le champ en haut, l'onde jaune du clic sur Envoyer, la grille de dix diapos dont les dernières arrivent encore, floues. (styleframes/png/P15.png)

## Frame 9 : Pas besoin d'être technique · 31.13 → 34.46

- scene: Une carte de code se pose devant la demande en français, bascule et tombe hors champ ; recul : la conversation, trois bulles, on apprend à lui parler
- duration: 3.33s
- transition_in: cut
- status: animated
- src: compositions/frames/09-technique.html
- voiceover: "Pas besoin d’être technique : il faut juste apprendre à lui parler."
- type: benefit_highlight
- blueprint: transcript-scroll-artifact-reveal (Adapt)
- focal: la carte de code qui tombe, puis la conversation
- rules: motion-blur-streak, svg-path-draw
- world: light
- handoff_in: à 0.00 : whip vers la gauche en cours (flou 12 px) : la grille des dix diapos sort par la droite, filée ; le champ de saisie avec la phrase tapée entre par la gauche, flou ; sous-titre sorti ; papier
- handoff_out: à 3.33 : recul en cours (power2.in, flou 12 px) : la fenêtre de conversation rétrécit au centre (×0,6), floue ; sous-titre sorti ; papier, grain 3 %

Word cues: Pas@0.23 besoin@0.43 d’être@0.78 technique@1.03 il@1.61 faut@1.77 juste@1.96 apprendre@2.23 à@2.38 lui@2.62 parler@2.79

Scene 1 (0.00 à 1.57 s) : P16, Pas besoin d'être technique
  TEXTE ÉCRAN : sous-titre « Pas besoin d’être [boîte : technique] : » ; boîte tracée à 1.01
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.17 le whip se pose : le champ et sa phrase en français à droite ; 0.17 une carte de code sombre (7 lignes, Space Mono) arrive de la caméra à gauche (×1,3, flou 10 → net en 0,14 s), par-dessus ; 0.23 « Pas besoin » ; 1.03 « technique » : la carte bascule (0° → -16°, 0,15 s power2.in) et tombe hors champ en bas à gauche (y +700 en 0,35 s, flou vertical) ; 1.37 la phrase en français reste seule ; 1.42 départ du recul.
  PISTE CAMÉRA : atterrissage 0.00 à 0.17 ; dérive ; 1.42 à 1.67 recul expo.out.
  COUCHES ET PROFONDEUR : avant-plan : la carte de code ; sujet : le champ en français ; fond : papier ; couches 2 à 3.
  OBJET-PONT ET VECTEUR : le champ devient celui de la conversation (P17).
  SON : whoosh court 0.02 ; pop 0.17 ; glitch 1.03 (le code tombe).
  IMAGE CLÉ : 1.12 : la carte de code qui bascule et tombe, floue, en bas à gauche ; la demande en français nette à droite. (styleframes/png/P16.png)

Scene 2 (1.57 à 3.33 s) : P17, Apprendre à lui parler
  TEXTE ÉCRAN : sous-titre « il faut juste [trait : apprendre à lui parler]. » ; trait jaune de 2.23 à 2.63
  IMAGE DE DÉPART : le champ qui devient celui de la fenêtre de conversation.
  ÉTAPES : 1.57 le recul révèle la fenêtre « Assistant IA » ; 1.67 bulle 1 (toi) « Prépare ma présentation de lundi. » monte (y 20 → 0, 0,12 s) ; 2.07 bulle 2 (l'IA) « Voici 10 diapos. Je les raccourcis ? » ; 2.23 « apprendre » : le trait jaune ; 2.47 bulle 3 (toi) « Oui, et ajoute un graphique. » ; 2.87 le point de l'IA pulse ; 3.07 le sous-titre sort ; 3.12 départ du recul.
  PISTE CAMÉRA : poussée 2 %/s ; 3.12 à 3.33 recul (power2.in, flou 0 → 12 px).
  COUCHES ET PROFONDEUR : sujet : la dernière bulle ; milieu : la fenêtre ; fond : papier ; couches 2.
  OBJET-PONT ET VECTEUR : vecteur : recul, repris par la séquence 10.
  SON : pops 1.67, 2.07, 2.47 (les bulles) ; whoosh 3.15.
  IMAGE CLÉ : 2.77 : la fenêtre de conversation, trois bulles, le champ en bas ; « apprendre à lui parler » souligné de jaune. (styleframes/png/P17.png)

## Frame 10 : Tu récupères ton temps · 34.46 → 37.88

- scene: Trois tuiles côte à côte, les horloges de la douleur : chacune tourne à rebours sur son mot (soirée, matinée, dimanche), un secteur jaune dessine le temps rendu, « Libre »
- duration: 3.42s
- transition_in: cut
- status: animated
- src: compositions/frames/10-recuperes.html
- voiceover: "Et tu récupères ta soirée, ta matinée, ton dimanche."
- type: benefit_highlight
- blueprint: grid-card-assemble (Adapt)
- focal: la tuile du mot dit
- rules: svg-path-draw, counting-dynamic-scale
- world: light
- handoff_in: à 0.00 : recul en cours (power2.in, flou 12 px) : la fenêtre de conversation rétrécit au centre (×0,6), floue ; sous-titre sorti ; papier, grain 3 %
- handoff_out: à 3.42 : recul en cours (flou 12 px) : les trois tuiles rétrécissent au centre ; sous-titre sorti ; papier

Word cues: Et@0.23 tu@0.41 récupères@0.59 ta@1.04 soirée@1.22 ta@1.68 matinée@1.87 ton@2.54 dimanche@2.77

Scene 1 (0.00 à 3.42 s) : P18, Tu récupères
  TEXTE ÉCRAN : sous-titre « Et [boîte : tu récupères] ta soirée, » puis « ta matinée, ton dimanche. » ; boîte tracée à 0.39
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.24 la conversation se résorbe et les trois tuiles se posent côte à côte (marges égales), chacune avec l'horloge de sa douleur (22:47, 12:00, DIM.) ; 0.41 « tu récupères » ; 1.22 « soirée » : tuile 1, les aiguilles tournent à rebours de 22:47 à 18:00 (0,6 s power2.inOut), le secteur jaune se dessine, « Soirée » et la pastille « Libre » ; 1.54 le second morceau du sous-titre remplace le premier ; 1.87 « matinée » : tuile 2, de 12:00 à 08:30 ; 2.77 « dimanche » : tuile 3, « DIM. », tout le cadran se remplit de jaune ; 3.04 les trois tuiles respirent ; 3.18 le sous-titre sort ; 3.24 départ du recul.
  PISTE CAMÉRA : poussée 2 %/s, cran de 0,1 s vers la tuile active (1.14, 1.79, 2.69) ; 3.24 à 3.42 recul (power2.in, flou 0 → 12 px).
  COUCHES ET PROFONDEUR : sujet : la tuile active ; milieu : les deux autres ; fond : papier ; couches 2 à 3.
  OBJET-PONT ET VECTEUR : vecteur : recul, repris par la séquence 11.
  SON : carillons 1.24, 1.89, 2.79 (chaque temps rendu) ; whoosh 3.26.
  IMAGE CLÉ : 2.84 : trois tuiles « Soirée », « Matinée », « Dimanche », les horloges remontées, les secteurs jaunes, trois pastilles « Libre ». (styleframes/png/P18.png)

## Frame 11 : Cette fois, c'est pour toi · 37.88 → 41.42

- scene: Le portable sur la frise du papier, « 2026 » : le post-it revient et se colle (la rime) ; gros plan : un feutre barre « Pas », il reste « pour moi » ; poussée dans le jaune
- duration: 3.54s
- transition_in: cut
- status: animated
- src: compositions/frames/11-pour-toi.html
- voiceover: "L’intelligence artificielle ? Cette fois... c’est pour toi."
- type: benefit_highlight
- blueprint: device-surface-showcase (Adapt)
- focal: le post-it, puis « Pas » barré
- rules: svg-path-draw, depth-of-field-blur
- world: light
- handoff_in: à 0.00 : recul en cours (flou 12 px) : les trois tuiles rétrécissent au centre ; sous-titre sorti ; papier
- handoff_out: à 3.54 : le jaune du post-it remplit tout le cadre (poussée ×6, flou 6 px), l'écriture sortie par les bords ; aucun texte ; aucun sous-titre

Word cues: L’intelligence@0.24 artificielle@0.82 (silence de 1.39 à 1.82) Cette@1.82 fois@2.10 c’est@2.71 pour@2.94 toi@3.11

Scene 1 (0.00 à 1.62 s) : P19, L'intelligence artificielle ?
  TEXTE ÉCRAN : sous-titre « [boîte : L’intelligence artificielle] ? » ; boîte tracée à 0.22 (comme à 8.00 en temps global)
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.22 les tuiles rentrent dans l'écran : le portable clair posé sur la frise du papier, « 2026 » dessous (la rime de P3) ; 0.24 « L’intelligence artificielle » ; 0.42 le post-it arrive de la caméra et se colle sur l'écran, avec le même geste qu'en P1 ; 1.32 départ de la poussée.
  PISTE CAMÉRA : atterrissage 0.00 à 0.22 ; dérive ; 1.32 à 1.62 poussée ×1 → ×2,1 sur le post-it (expo.inOut).
  COUCHES ET PROFONDEUR : avant-plan : le post-it qui arrive ; sujet : le portable ; fond : frise et papier ; couches 3.
  OBJET-PONT ET VECTEUR : le post-it devient le gros plan de P20.
  SON : whoosh court 0.02 ; pop 0.42 (le son du post-it).
  IMAGE CLÉ : 0.52 : le portable clair sur la frise au-dessus de « 2026 », le post-it qui se colle sur l'écran, encore flou. (styleframes/png/P19.png)

Scene 2 (1.62 à 3.54 s) : P20, C'est pour toi
  TEXTE ÉCRAN : sous-titre « Cette fois… c’est [trait : pour toi]. » ; trait jaune de 2.92 à 3.32
  IMAGE DE DÉPART : le post-it au centre, ×2,15.
  ÉTAPES : 1.62 le post-it occupe le centre ; 1.82 « Cette fois » : un feutre noir entre par la droite ; 2.42 il barre « Pas » (le trait se dessine en 0,25 s power2.out) : il reste « pour moi » ; 2.71 « c’est pour toi » ; 2.92 à 3.32 le trait jaune sous « pour toi » ; 3.12 le feutre sort ; 3.27 départ de la poussée.
  PISTE CAMÉRA : poussée 1,5 %/s ; 3.27 à 3.54 poussée ×2,15 → ×6 dans le post-it (power2.in), le jaune remplit le cadre.
  COUCHES ET PROFONDEUR : avant-plan : le feutre ; sujet : le post-it ; fond : l'écran flou ; couches 2.
  OBJET-PONT ET VECTEUR : le post-it devient le bouton de la carte de fin.
  SON : clic doux 2.42 (le feutre) ; notification à deux tons 2.72 (LE son signature) ; whoosh cinématique 3.32.
  IMAGE CLÉ : 3.12 : le post-it en gros plan, « Pas » barré au feutre noir, « pour moi » qui reste, le feutre encore posé. (styleframes/png/P20.png)

## Frame 12 : Apprends l'IA · 41.42 → 45.80

- scene: Le jaune se replie en bouton « APPRENDRE L'IA » sur le bureau de nuit, la frise du début passe derrière ; un curseur arrive et clique directement ; onde jaune, tenue vivante, iris
- duration: 4.38s
- transition_in: cut
- status: animated
- src: compositions/frames/12-fin.html
- voiceover: "Apprends l’IA dès aujourd’hui."
- type: cta
- blueprint: cta-morph-press (Adapt)
- focal: le bouton, puis le clic
- rules: cursor-click-ripple, press-release-spring
- world: dark
- handoff_in: à 0.00 : le jaune du post-it remplit tout le cadre (poussée ×6, flou 6 px), l'écriture sortie par les bords ; aucun texte ; aucun sous-titre
- handoff_out: aucun (fin du film, iris noir de 45.30 à 45.80 centré sur le bouton)

Word cues: Apprends@0.24 l’IA@0.62 dès@0.99 aujourd’hui@1.21 (silence de 1.75 à 4.38)

Scene 1 (0.00 à 1.78 s) : P21, Apprends l'IA
  TEXTE ÉCRAN : sous-titre « [boîte : Apprends l’IA] dès aujourd’hui. » ; boîte tracée à 0.22
  IMAGE DE DÉPART : handoff_in.
  ÉTAPES : 0.00 à 0.28 le jaune rétrécit vite (0,28 s power3.in) jusqu'au bouton « APPRENDRE L’IA » (720 × 160, centre (960, 440)), son coin plié rappelle le post-it ; le bureau de nuit apparaît autour ; la frise du début passe derrière en filet, « 2000 · 2010 · 2026 » ; 0.24 « Apprends l’IA » ; 0.58 le halo du bouton respire ; 1.21 « aujourd’hui » ; 1.28 le curseur arrive d'un seul mouvement courbe depuis le bas à droite (0,45 s power3.out).
  PISTE CAMÉRA : dérive x +10 px/s, poussée 1,5 %/s.
  COUCHES ET PROFONDEUR : avant-plan : le curseur ; sujet : le bouton ; fond : frise en filet, sol ; couches 3.
  OBJET-PONT ET VECTEUR : le curseur clique en P22.
  SON : whoosh court 0.00 ; pop 0.28 (le bouton se pose).
  IMAGE CLÉ : 1.18 : sur le bureau de nuit, le bouton jaune « APPRENDRE L’IA » au coin plié, la frise des années en filet derrière, le curseur qui arrive. (styleframes/png/P21.png)

Scene 2 (1.78 à 4.38 s) : P22, Le clic
  TEXTE ÉCRAN : aucun sous-titre après 1.88 (la voix est finie).
  IMAGE DE DÉPART : le bouton, le curseur posé dessus.
  ÉTAPES : 1.73 le curseur touche le bouton ; 1.78 clic direct : pression (×0,96 en 0,06 s), jaune pâle → blanc → jaune (3 tons), ondes jaunes qui s'ouvrent ; 1.88 le sous-titre sort ; 1.98 à 3.88 tenue vivante : la frise glisse vers la gauche (12 px/s), le halo du bouton respire (période 1,2 s, pas finis) ; 2.28 la seconde onde s'efface ; 2.88 la graduation « 2026 » passe sous le bouton et s'allume en jaune ; 3.48 le bouton revient à son jaune plein, le curseur s'écarte de 12 px ; 3.88 à 4.38 iris noir centré sur le bouton.
  PISTE CAMÉRA : dérive x +10 px/s ; aucune coupe.
  COUCHES ET PROFONDEUR : sujet : le bouton ; milieu : les ondes ; fond : frise et sol ; couches 2 à 3.
  OBJET-PONT ET VECTEUR : aucun (fin du film).
  SON : clic 1.78 ; whoosh 3.88 (l'iris).
  IMAGE CLÉ : 2.78 : le bouton enfoncé, le curseur dessus, deux ondes jaunes ouvertes, la frise des années derrière. (styleframes/png/P22.png)
