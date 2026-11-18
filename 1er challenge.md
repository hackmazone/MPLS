# TP - Créer Matrix avec l'IA et Python

**Durée :** 45 minutes à 1 heure

## Objectif

Découvrir les bases de Python et de l'intelligence artificielle générative en demandant à une IA de créer une animation inspirée du film *The Matrix*.

À la fin du TP, vous aurez :

- installé Python ;
- utilisé une IA pour générer du code ;
- créé un programme Python ;
- exécuté votre programme ;
- personnalisé le résultat ;
- publié votre travail sur GitHub.

---

# Étape 1 - Installer Python

Télécharger Python :

https://www.python.org/downloads/

Pendant l'installation, cocher :

☑ Add Python to PATH

Puis cliquer sur :

Plain Text
Install Now

# Étape 2 - Vérifier l'installation

Ouvrir l'invite de commandes.

Exécuter :

BAT
python --version

Résultat attendu :

Plain Text
Python 3.x.x

Faire une capture d'écran.

Nom du fichier :

Plain Text
capture_installation.png
Étape 3 - Demander à une IA de générer le programme

Ouvrir ChatGPT, Copilot ou un autre assistant IA.

Copier-coller le prompt suivant :

Plain Text
Crée un programme Python utilisant tkinter qui reproduit un effet Matrix.
 
Le programme doit :
 
- être en plein écran ;
- afficher une pluie de caractères verts ;
- afficher successivement les messages :
- Wake up Neo...
- The Matrix has you...
- Follow the white rabbit.
- Knock, knock, Neo.
- produire un son continu ;
- comporter un effet glitch ;
- permettre de quitter avec la barre ESPACE.
 
Le programme doit être complet et directement exécutable.
Étape 4 - Créer le fichier Python

Créer un fichier nommé :

Plain Text
matrix_v4.py

Copier-coller dans ce fichier le code généré par l'IA.

Enregistrer le fichier.

Étape 5 - Exécuter le programme

Ouvrir une invite de commandes dans le dossier contenant :

Plain Text
matrix_v4.py

Exécuter :

BAT
python matrix_v4.py

Le programme doit afficher l'animation Matrix.

Pour quitter :

Plain Text
Appuyer sur la barre ESPACE

Faire une capture d'écran.

Nom du fichier :

Plain Text
capture_matrix.png
Étape 6 - Personnaliser le programme

Modifier les messages affichés.

Exemple :

Python
messages = [
"Bienvenue",
"Université de Guyane",
"Licence Informatique",
"Découvrons Python"
]

Ou créer votre propre version.

Exemples :

Python
messages = [
"Cyberdéfense",
"Projet ACAI",
"Intelligence Artificielle",
"Bienvenue"
]

ou

Python
messages = [
"Hello World",
"Je découvre Python",
"Je découvre l'IA",
"Je sais programmer"
]

Faire une nouvelle capture d'écran après modification.

Questions
Question 1

Quelle commande permet de vérifier que Python est correctement installé ?

Question 2

Quel prompt avez-vous utilisé avec l'IA ?

Question 3

Quelle touche permet de quitter l'application ?

Question 4

Quelle modification avez-vous réalisée dans le programme ?

Question 5

Quel est l'intérêt d'utiliser une IA pour développer un programme ?

Travail à rendre sur GitHub

Créer un dépôt GitHub contenant :

Plain Text
tp-matrix-ia/
│
├── README.md
├── matrix_v4.py
├── capture_installation.png
├── capture_matrix.png
└── reponses.md
Contenu de reponses.md

Répondre aux 5 questions du TP.

Barème
Critère	Points
Installation de Python	4
Utilisation de l'IA	4
Programme exécuté	4
Personnalisation	4
Réponses aux questions	4

Total : 20 points

Bonus (+2 points)

Demander à l'IA d'ajouter une nouvelle fonctionnalité parmi :

changement de couleur ;
ajout d'un logo ;
ajout d'un fond d'écran ;
ajout d'un nouveau message ;
ajout d'un compteur ;
ajout d'un effet visuel supplémentaire.

Inclure une capture d'écran du résultat.
