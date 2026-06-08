FICHE DE SYNTHÈSE : EXPLICATION DU CODE SOURCE
**Projet :** Créateur de Constellations Interactif
Langage :** Python (Module Turtle)
## 1. Objectif Général du Programme
Le programme développé est un éditeur de constellations interactif. Au lieu d'afficher un dessin statique ou automatique, il permet à l'utilisateur de contrôler un curseur à l'écran pour concevoir sa propre carte du ciel.
L'utilisateur peut :
 * **Se déplacer** dans l'espace à l'aide des flèches directionnelles.
 * **Placer une étoile** brillante à sa position actuelle avec la barre *Espace*.
 * **Relier toutes les étoiles** entre elles avec la touche *Entrée* pour révéler la constellation.
 * **Réinitialiser l'écran** avec la touche *Suppr*.
## 2. Analyse Technique des Fonctions Exigées
Le code intègre rigoureusement les structures et commandes demandées dans les consignes du projet :
### A. La Structure de Données (La liste de tuples)
 * **etoiles = []** : Initialisation d'une liste vide globale. Elle sert de mémoire pour le programme.
 * **etoiles.append(position_actuelle)** : À chaque pression de la barre *Espace*, la position du curseur est récupérée sous forme de **tuple (x, y)** et ajoutée à la liste. Le choix du tuple garantit que les coordonnées enregistrées sont protégées et ne peuvent pas être modifiées par erreur.
### B. Le Parcours de la Liste (La boucle for)
Pour l'implémentation du tracé des lignes (le bonus), le programme effectue un parcours séquentiel de la liste de tuples :
```python
for pt in etoiles:
    lignes.goto(pt[0], pt[1])

```
 * **Mécanisme :** La boucle lit chaque point pt de la liste un par un. pt[0] représente la coordonnée X et pt[1] la coordonnée Y. La commande déplace le stylo de liaison pour connecter l'étoile précédente à la nouvelle.
### C. Les Commandes Graphiques Impératives
 * **turtle.goto()** : Utilisée pour modifier les coordonnées du curseur lors des déplacements (+20 ou -20 pixels) et pour guider le tracé des lignes de constellation.
 * **turtle.dot()** : Utilisée pour dessiner les étoiles. Pour obtenir un rendu esthétique et "lumineux", deux points sont superposés : un grand point orange (taille 16) pour le halo, et un petit point blanc (taille 6) pour le cœur de l'étoile.
 * **turtle.color()** : Permet de gérer l'identité visuelle de l'interface (blanc pour le viseur, orange/blanc pour les astres, et cyan pour les lignes de connexion).
## 3. Gestion des Événements (Clavier)
Pour rendre le script interactif, le programme utilise le gestionnaire d'écoute de la fenêtre graphique :
 * **ecran.listen()** : Active l'écoute des entrées du clavier par le système.
 * **ecran.onkey(fonction, "Touche")** : Associe chaque touche physique du clavier à une fonction spécifique du code (ex: "Up" pour monter, "space" pour l'étoile, "Return" pour l'application de la boucle de liaison).
## 4. Réponses aux Questions Potentielles de l'Oral
 * **Pourquoi y a-t-il une variable lignes = turtle.Turtle() ?**
   * *Réponse :* Pour séparer les rôles. Le turtle par défaut sert uniquement à déplacer le viseur et poser les étoiles. L'objet lignes est un second pinceau indépendant (et invisible) dédié uniquement au tracé des liaisons bleues sans perturber le curseur principal.
 * **Pourquoi avoir utilisé ecran.tracer(0) au début ?**
   * *Réponse :* Cela permet de désactiver l'animation pendant que le programme génère les 200 étoiles décoratives du fond de l'espace. Le décor s'affiche ainsi instantanément à l'ouverture, évitant au joueur d'attendre que le programme dessine chaque point un par un.
