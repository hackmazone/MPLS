import tkinter as tk
import random
import winsound
import threading

# ==========================
# ETAT GLOBAL
# ==========================

running_sound = True

# ==========================
# SON MATRIX CONTINU
# ==========================

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

# ==========================
# FENETRE
# ==========================

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

# ==========================
# FLASH VERT
# ==========================

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

# ==========================
# GLYPHES MATRIX
# ==========================

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

# ==========================
# MESSAGES
# ==========================

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

# ==========================
# ANIMATION
# ==========================

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

    # GLITCH

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

    # EFFET CRT

    for y in range(0, HEIGHT, 4):

        canvas.create_line(
            0,
            y,
            WIDTH,
            y,
            fill="#001100",
            tags="matrix"
        )

    # INDICATION KILL SWITCH

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

# ==========================
# KILL SWITCH
# ==========================

def quit_app(event):

    global running_sound

    running_sound = False

    root.destroy()

root.bind(
    "<space>",
    quit_app
)

# ==========================
# START
# ==========================

animate()

root.mainloop()