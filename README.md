# TP - Matrix en Python

**Durée :** 30 à 45 minutes

## Objectif

Créer et exécuter une animation inspirée du film *The Matrix*, puis la personnaliser.

---

# Étape 1 - Installer Python

Télécharger Python :

https://www.python.org/downloads/

Pendant l'installation, cocher :

```text
☑ Add Python to PATH
```

Puis cliquer sur :

```text
Install Now
```

---

# Étape 2 - Vérifier l'installation

Ouvrir l'invite de commandes.

Exécuter :

```cmd
python --version
```

Résultat attendu :

```text
Python 3.x.x
```

Faire une capture d'écran du résultat.

---

Étape 3 - Créer le programme

Créer un fichier nommé :

Plain Text
matrix_v4.py

Ouvrir le fichier avec le Bloc-notes, Visual Studio Code ou Notepad++.

Copier-coller intégralement le code suivant :

Python
import tkinter as tk
import random
import winsound
import threading
 
running_sound = True
 
def matrix_sound():
 
global running_sound
 
while running_sound:
 
winsound.Beep(
random.randint(80, 180),
40
)
 
if not running_sound:
return
 
winsound.Beep(
random.randint(250, 500),
20
)
 
threading.Thread(
target=matrix_sound,
daemon=True
).start()
 
root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")
 
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
 
canvas = tk.Canvas(
root,
bg="black",
highlightthickness=0
)
 
canvas.pack(
fill="both",
expand=True
)
 
flash = canvas.create_rectangle(
0,
0,
WIDTH,
HEIGHT,
fill="#00ff00",
outline=""
)
 
def remove_flash():
canvas.delete(flash)
 
root.after(
200,
remove_flash
)
 
symbols = (
"0123456789"
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"abcdefghijklmnopqrstuvwxyz"
"ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿ"
"ﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉ"
)
 
streams = []
 
for x in range(0, WIDTH, 16):
 
streams.append({
"x": x,
"y": random.randint(-5000, 0),
"length": random.randint(30, 90),
"speed": random.randint(8, 20)
})
 
messages = [
"Wake up Neo...",
"The Matrix has you...",
"Follow the white rabbit.",
"Knock, knock, Neo."
]
 
current_message = 0
current_text = ""
char_index = 0
 
message_text = canvas.create_text(
WIDTH // 2,
HEIGHT // 2,
text="",
fill="white",
font=("Consolas", 34, "bold")
)
 
def next_phrase():
 
global current_message
global current_text
global char_index
 
current_message += 1
 
if current_message >= len(messages):
return
 
current_text = ""
char_index = 0
 
canvas.itemconfig(
message_text,
text=""
)
 
root.after(
800,
typewriter
)
 
def typewriter():
 
global current_message
global current_text
global char_index
 
if current_message >= len(messages):
return
 
phrase = messages[current_message]
 
if char_index < len(phrase):
 
current_text += phrase[char_index]
 
canvas.itemconfig(
message_text,
text=current_text
)
 
char_index += 1
 
root.after(
110,
typewriter
)
 
else:
 
root.after(
2500,
next_phrase
)
 
typewriter()
 
def animate():
 
canvas.delete("matrix")
 
for stream in streams:
 
x = stream["x"]
 
for i in range(stream["length"]):
 
y = stream["y"] + i * 14
 
char = random.choice(symbols)
 
if i == 0:
color = "#FFFFFF"
 
elif i < 4:
color = "#CCFFCC"
 
elif i < 10:
color = "#66FF66"
 
else:
color = "#00AA00"
 
canvas.create_text(
x,
y,
text=char,
fill=color,
font=("Consolas", 12, "bold"),
tags="matrix"
)
 
stream["y"] += stream["speed"]
 
if stream["y"] > HEIGHT + 1500:
 
stream["y"] = random.randint(
-5000,
-500
)
 
stream["length"] = random.randint(
30,
90
)
 
stream["speed"] = random.randint(
8,
20
)
 
if random.random() < 0.08:
 
y = random.randint(
0,
HEIGHT
)
 
canvas.create_rectangle(
0,
y,
WIDTH,
y + random.randint(1, 4),
fill="#00FF00",
outline="",
tags="matrix"
)
 
for y in range(0, HEIGHT, 4):
 
canvas.create_line(
0,
y,
WIDTH,
y,
fill="#001100",
tags="matrix"
)
 
canvas.create_text(
WIDTH - 20,
HEIGHT - 20,
text="[SPACE]",
anchor="e",
fill="#003300",
font=("Consolas", 12),
tags="matrix"
)
 
root.after(
16,
animate
)
 
def quit_app(event):
 
global running_sound
 
running_sound = False
 
root.destroy()
 
root.bind(
"<space>",
quit_app
)
 
animate()
 
root.mainloop()

Enregistrer le fichier.

Étape 4 - Exécuter le programme

Dans le dossier contenant matrix_v4.py, exécuter :

BAT
python matrix_v4.py

L'animation Matrix doit apparaître.

Pour quitter :

Plain Text
Appuyer sur la barre ESPACE

Faire une capture d'écran du programme.




# Étape 5 - Personnalisation

Dans le fichier `matrix_v4.py`, rechercher :

```python
messages = [
    "Wake up Neo...",
    "The Matrix has you...",
    "Follow the white rabbit.",
    "Knock, knock, Neo."
]
```

Modifier ces messages avec votre propre version.

Exemple :

```python
messages = [
    "Bienvenue",
    "Université de Guyane",
    "Licence Informatique",
    "Découvrons Python"
]
```

Faire une nouvelle capture d'écran après modification.

---

# Questions

## Question 1

Quelle commande permet de vérifier que Python est correctement installé ?

## Question 2

À quoi sert la bibliothèque `tkinter` ?

## Question 3

Quelle touche permet de quitter l'application ?

## Question 4

Quelle modification avez-vous réalisée dans le programme ?

## Question 5

Quelle amélioration souhaiteriez-vous ajouter au projet ?

---

# Travail à rendre sur GitHub

Créer un dépôt GitHub contenant :

```text
tp-matrix-python/
│
├── README.md
├── matrix_v4.py
├── capture_installation.png
├── capture_matrix.png
└── reponses.md
```

## Contenu de `reponses.md`

Répondre aux 5 questions du TP.

---

# Barème

| Critère | Points |
|----------|---------:|
| Installation de Python | 4 |
| Exécution du programme | 4 |
| Personnalisation réalisée | 6 |
| Réponses aux questions | 6 |

**Total : 20 points**
