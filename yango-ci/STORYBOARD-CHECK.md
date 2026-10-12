# Contrôle du storyboard « On dit combien ? » (avant d'animer)

Grille en 15 points de `patterns/STORYBOARD-CRAFT.md` § 5, puis grille de contrôle et règles maison du skill
`motion-design`. ✓ = conforme ; ⚠ = conforme sous réserve, la réserve est écrite.

## Grille en 15 points

1. ✓ En-tête : monde par acte (la rue et ses stations Riviera 2, discussion, midi, soir ; le noir du pivot ; le téléphone sur fond clair ; la rue de la rime ; la carte rouge), ciel qui dit l'heure, couleurs de rôle (rouge = Yango, orange = le taxi, vert = les panneaux), 2 signatures datées (l'étiquette de prix 9.12, 10.55, 11.20, 32.87, 33.90 ; la main levée 3.25, 12.33, 17.47, 23.65, baissée à 49.71), registres de texte.
2. ✓ Chaque plan a une piste caméra (dérive chiffrée et gestes datés avec leur cible) ; la caméra n'est jamais à l'arrêt (le pivot pousse très lentement).
3. ✓ Aucun trou de plus de 1 s dans les étapes (vérifié par script sur les 27 plans) ; la tenue finale (55.30 à 60.00) a ses événements (tap, ondes à 56.60 et 57.40, la voiture qui sort à 58.40, iris).
4. ✓ Apparitions de 0,06 à 0,2 s ; dérives sur toute la durée du plan ; zone 0,3 à 0,9 s réservée aux gestes de caméra et au doigt (expo, power2, power3).
5. ✓ Chaque tenue nomme sa couche vivante (passants flous, soleil qui monte, chaleur qui tremble, phares, lueur rouge, voiture sur la carte, halo du bouton, petite voiture sur le filet de route).
6. ✓ Chaque jonction nomme son objet-pont ou son vecteur, recopié mot pour mot en handoff_in (généré, voir STORYBOARD.md). Pas de dédoublement : les trois héros du gag sont trois temps du même homme, posés côte à côte, qui se fondent en un seul avant le repli ; les cinq vignettes sont cinq jours.
7. ✓ Transitions « effet » : 2, celles de l'orchestrateur (le flash à 28.20, l'iris depuis la portière à 51.15).
8. ✓ Coupe franche : 1, à 25.45, sur « Et », changement d'acte (la rue → la question), sous l'impact grave.
9. ✓ Chaque entrée principale a un état de départ (×1,1 à ×1,6 et flou, ou filé depuis le bord) ; aucun fondu à taille finale.
10. ⚠ L'image précède le mot de 0,15 à 0,2 s (panneau 1.58 avant « Carrefour » 1.76, taxi 4.12 avant « Un taxi » 4.32, étiquette 9.12 avant « Trois » 9.32, « 07:00 » 46.40 avant « Lundi » 46.58, panneau 48.02 avant « Carrefour » 48.20), mais les mots à l'intérieur des phrases sont estimés : à revérifier sur le minutage Whisper. Chaque silence de plus de 0,4 s est un plan avec son action (liste VOIX de l'en-tête, 22 silences).
11. ✓ Verbes joués : « lèves » (le bras), « s'arrête » (le capot plonge), « regarde de la tête aux pieds » (le panoramique), « discutes » (les bulles qui rebondissent), « on te répond » (le doigt qui dit non), « attends » (les phares qui passent), « choisis » (la frappe), « s'affiche » (le prix qui roule), « vient te chercher » (la voiture sur la carte), « montes » (la portière), « pars » (le démarrage), « Télécharge » (le tap).
12. ✓ 15 plans sur 27 à 3 niveaux (avant-plan flou : passants, poteau, palmes) ; parallaxe dans la rue (P01, P02, P09) et dans la rime (P23).
13. ✓ Couches animées : régime 2, pic 3 (P06, P08, P12), un seul élément actif à la fois.
14. ✓ Rimes : le carrefour Riviera 2 à 7 h (0.00 = 46.05, même cadre, même dérive) ; le taxi orange (4.12) devient la voiture blanche au même endroit (49.71) ; l'étiquette qui change (9 à 12) revient figée (33.90) ; la main levée devient la main baissée.
15. ✓ Fin : « Yango » s'assemble, le bouton arrive, le doigt en une courbe, tap direct en 3 tons et deux ondes, 3,4 s de tenue vivante, iris noir sur le bouton.

## Grille de contrôle et règles maison

- ✓ La première image est le premier mot (« Lundi, sept heures » : le carrefour à 07:00), jamais un logo.
- ✓ Chaque phrase a sa composition ; sous-titre en bas au centre, mot par mot, morceaux de 45 caractères au plus ; rien dans la bande y 890 à 980 (voitures roues à y 880, pointillés à y 852, téléphone réduit).
- ⚠ Une boîte rouge par phrase (22 boîtes) et 3 traits de pic ; la phrase de midi en porte deux (« À midi » puis « là-bas »), parce que la réplique citée « Yopougon ? Je ne vais pas là-bas. » est traitée comme une phrase à part. Aucun mot géant.
- ✓ Une chose à regarder à la fois ; côte à côte aux marges égales (les cinq jours, les trois destinations).
- ⚠ La solution est montrée dans une appli GÉNÉRIQUE dessinée (champ, fiche de prix, carte, fiche du chauffeur) : à remplacer par des captures récentes de l'application Yango fournies par la marque.
- ✓ Pivot explicite (phrase sur le noir, 1,56 s de silence) et le sol change avec lui (rue → noir → fond clair).
- ⚠ Logo : « Yango » est écrit en Instrument Sans 700 sur rouge #ff3b30, en attendant le logo officiel et la charte de la marque.
- ✓ Coupes au quota (1), aucun aller-retour de caméra : la rue se longe toujours vers la droite (les whips vont tous vers la droite).
- ✓ Les nombres roulent (étiquette 3 000 → 2 500 → 1 500, prix de l'appli, « 3 min ») ; aucun posé en fondu.
- ✓ Le produit est montré par des gestes (frappe, prix qui roule, voiture qui avance, fiche qui monte), pas par une capture statique.
- ✓ Un élément de l'accroche revient avant la fin (le carrefour, le panneau, « 07:00 », le héros).
- ✓ Carte de fin : un seul bouton, doigt qui tape directement, tenue vivante, iris.
- ✓ Lisible sans le son, gag compris (les trois étiquettes 3 000 F, 2 500 F, 1 500 F se lisent).
- ✓ Personnages dignes, pas de caricature : le chauffeur hésite et repart, il n'est pas moqué.
- ⚠ Rythme : problème (0 à 25.45) 12 plans = 4,7 plans / 10 s, sous les références (6 à 9) ; un événement toutes les 0,3 à 0,6 s compense. Si le film paraît lent à l'aperçu, couper P08 et P11 en deux plans.

## Réserves à lever avant d'animer

1. Minutage : les débuts de phrase sont mesurés sur l'énergie du son, les mots à l'intérieur des phrases sont estimés (±0,15 s). Recaler avec Whisper (`mots.py` puis `onsets.py`) dès que `openaipublic.azureedge.net` est autorisé, puis régénérer les Word cues (`python3 -I yango-ci/tools/gen_sb.py yango-ci`).
2. Marque : logo, rouge officiel et captures de l'application à fournir ; tant qu'ils manquent, le film reste un brouillon de travail, à ne pas diffuser.
3. Promesses à confirmer avec l'offre réelle de Yango en Côte d'Ivoire : prix affiché avant la course, suivi du chauffeur sur la carte, nom et plaque, texte du bouton « Télécharger l’application ».
4. Valeurs d'exemple à valider : les prix 3 000 F, 2 500 F, 1 500 F (et 2 500 F dans l'appli), le prénom « Koffi », la plaque 1234 AB 01, « Arrive dans 3 min ».
5. Son : la musique est une piste CC0 à fournir. Les bruitages de rue marqués ★ (frein, démarrage, portière, claquettes, klaxon, grillons, ambiance) ne sont pas dans la bibliothèque locale : à fournir en CC0, sinon ils sont remplacés par le son indiqué (`assets/audio/sfx-events.json` contient déjà les remplacements, 73 événements).
