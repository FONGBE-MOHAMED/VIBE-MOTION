# Contrôle du storyboard « Pas pour moi » (avant d'animer)

Grille en 15 points de `patterns/STORYBOARD-CRAFT.md` § 5, puis grille de contrôle et règles maison du skill
`motion-design`. ✓ = conforme ; ⚠ = conforme sous réserve, la réserve est écrite.

## Grille en 15 points

1. ✓ En-tête : monde par acte (stations de la frise en x 960, 2220, 3480 ; papier ; carte de fin), fonds texturés, couleurs de rôle, 2 signatures datées (post-it 2.12, 5.50, 11.55, 38.30 ; horloge 15.80 à 37.23), registres de texte.
2. ✓ Chaque plan a une piste caméra (dérive chiffrée + gestes datés avec cible) ; la caméra n'est jamais à l'arrêt hors silence écrit (le pivot pousse très lentement).
3. ✓ Aucun trou de plus de 1 s dans les étapes ; accroche à 0,2 à 0,4 s d'écart. La tenue finale (43.40 à 45.30) a ses événements (43.70, 44.30, 44.90).
4. ✓ Apparitions de 0,06 à 0,2 s ; dérives sur toute la durée du plan ; zone 0,3 à 0,9 s réservée aux gestes de caméra et au curseur (power3, expo).
5. ✓ Chaque tenue nomme sa couche vivante (caret, fumée de la tasse, aiguilles, halo du bouton, frise qui glisse).
6. ✓ Chaque jonction nomme son objet-pont ou son vecteur, recopié en handoff_in. Pas de dédoublement : les trois post-its de P5 sont trois objets distincts (un par appareil) et les deux colonnes de P10 sont un partage voulu.
7. ✓ Transitions « effet » : 1 (le flash de lumière de 24.80).
8. ✓ Coupe franche : 1, à 22.90, « Pas », changement d'acte, sous l'impact grave.
9. ✓ Chaque entrée principale a un état de départ (×1,15 à ×1,6 + flou, ou depuis la caméra) ; aucun fondu à taille finale.
10. ⚠ Écarts écrits, mais l'avance des mots-images est courte : post-it 0,09 à 0,11 s avant « Pas », fenêtre 0,07 s avant « Un » (la loi demande 0,1 à 0,6 s). À régler sur le minutage Whisper : viser 0,15 à 0,25 s. Chaque silence de plus de 0,4 s est un plan avec son action (liste VOIX de l'en-tête).
11. ✓ Verbes joués par un objet : « prend » (l'horloge avale), « n'a pas attendu » (les autres filent), « rédige », « résume », « calcule », « expliques » (la frappe), « fait le travail » (les diapos), « récupères » (les horloges à rebours), « Apprends » (le clic).
12. ✓ 13 plans sur 22 à 3 niveaux (avant-plan flou) ; parallaxe dans l'acte 1 (P3, P6) et l'acte 2 (P15).
13. ✓ Couches animées : régime 2, pic 3 à 4 (P6, P15), un seul élément actif à la fois.
14. ✓ Rimes : post-it 2.12 = 38.30 ; champ du gag 9.40 = 28.40 ; horloges 15 à 20 = 35 à 37 ; tasse 6.40 = 21.56 ; « L'intelligence artificielle ? » 8.02 = 38.12 ; frise du début = filet de la carte de fin.
15. ✓ Fin : le post-it se replie en bouton (le geste qui rassemble), curseur en une courbe, clic direct en 3 tons et onde, 2,6 s de tenue vivante, iris.

## Grille de contrôle et règles maison

- ⚠ La première image est le premier mot (« Deux mille » : l'écran de 2000), jamais un logo ; mais le premier mot nomme une date, pas la cible : c'est le choix du script (version B, accroche datée).
- ✓ Chaque phrase a sa composition ; sous-titre en bas au centre, mot par mot, morceaux de 45 caractères au plus.
- ✓ Un mot surligné par phrase (15 surlignages) ; 4 traits de pic ; aucun mot géant.
- ✓ Une chose à regarder à la fois ; côte à côte aux marges égales (horloge / appli, Toi / D'autres, trois cartes, trois tuiles).
- ⚠ La douleur est montrée dans des outils que la cible reconnaît (diapos, messagerie, tableur), mais ce sont des interfaces génériques sans marque, dessinées : pas de capture d'écran récente fournie.
- ✓ Pivot explicite (phrase sur le noir, 1,5 s de silence) et le sol change avec lui.
- ✓ Pas de logo (pas de marque).
- ✓ Coupes au quota (1), aucun aller-retour de caméra : la frise se longe toujours vers la droite.
- ✓ Les nombres roulent (87 → 94, total 0 → 1 066,08 €, horloges) ; aucun posé en fondu.
- ✓ Le produit est montré par des gestes (frappe, envoi, clic), pas par une capture statique.
- ✓ Un élément de l'accroche revient avant la fin (le post-it, la frise).
- ✓ Carte de fin : un seul bouton, curseur qui clique directement, tenue vivante, iris.
- ✓ Lisible sans le son, gag compris (la suggestion « moi. » se lit).
- ⚠ Rythme : la douleur (0 à 22.90) compte 4,4 plans / 10 s, sous les références (6 à 9) ; les événements toutes les 0,2 à 0,5 s compensent. Si le film paraît lent à l'aperçu, couper P7 et P10 en deux plans.

## Réserves à lever avant d'animer

1. Minutage : les débuts de phrase sont mesurés sur le son, les mots à l'intérieur des phrases sont estimés (±0,15 s). Recaler avec Whisper (`mots.py` puis `onsets.py`) dès que `openaipublic.azureedge.net` est autorisé, puis régénérer les Word cues (`tools/gen_sb.py`).
2. GSAP se charge depuis `cdn.jsdelivr.net`, bloqué dans cet environnement : l'autoriser, ou servir GSAP en local depuis le paquet npm.
