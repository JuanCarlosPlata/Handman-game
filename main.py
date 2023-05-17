import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

# Funciones auxiliares

def bind_keyboard_buttons():
    # Asigna eventos de teclado para cada letra del alfabeto
    for key in "abcdefghijklmnopqrstuvwxyz":
        # Asocia la pulsación de una tecla a la función check_user_input_letter
        ventana_principal.bind(key, lambda event, key=key: check_user_input_letter(key))

def set_canvas_background():
    # Carga y redimensiona la imagen de fondo del lienzo
    img = Image.open("images/background.jpg")
    img = img.resize((350, 600), Image.LANCZOS)
    background = ImageTk.PhotoImage(img)
    return background

def update_hangman_image(lifes):
    global hangman_image
    # Actualiza la imagen del ahorcado según las vidas restantes
    image_path = f"images/Hangman-0{8 - lifes}.png"
    image = Image.open(image_path)
    image = image.resize((300, 300), Image.LANCZOS)
    hangman_image = ImageTk.PhotoImage(image)

def get_random_word():
    # Obtiene una palabra aleatoria del archivo words.txt
    with open("doc/words.txt", "r") as file:
        words = file.read().split("\n")
    return random.choice(words)

def check_user_input_letter(letter):
    global hidden_word, lifes, secret_word, pressed_keys, ronda, name

    if letter in pressed_keys:
        return

    pressed_keys.append(letter)
    pressed_keys.sort()
    # Actualiza el texto de las letras utilizadas en el lienzo
    canvas.itemconfigure("used_letters", text="".join(pressed_keys).upper())

    if letter in secret_word:
        for i, character in enumerate(secret_word):
            if character == letter:
                # Revela las letras acertadas en la palabra oculta
                hidden_word[i] = letter
    else:
        lifes -= 1
        # Actualiza la imagen del ahorcado
        update_hangman_image(lifes)
        canvas.itemconfigure("hangman_imagen", image=hangman_image)

        if lifes == 1:
            # Guarda la puntuación y muestra un mensaje de finalización del juego
            save_top_scores(name, ronda)
            messagebox.showinfo("Game Over", f"You completed {ronda} rounds!\nThe word was {secret_word.upper()}")
            ventana_principal.quit()

    # Actualiza el texto de la palabra oculta en el lienzo
    canvas.itemconfigure("secret_word", text="".join(hidden_word).upper())

    if " _" not in hidden_word:
        # Si se han revelado todas las letras, muestra un mensaje de éxito y avanza a la siguiente ronda
        messagebox.showinfo("GOOD JOB", "Now go for another word!")
        ronda += 1
        pressed_keys = []
        lifes = 7
        # Obtiene una nueva palabra aleatoria para la siguiente ronda
        secret_word = get_random_word()
        hidden_word = [" _" for _ in range(len(secret_word))]
        canvas.itemconfigure("secret_word", text="".join(hidden_word).upper())
        update_hangman_image(lifes)
        canvas.itemconfigure("hangman_imagen", image=hangman_image)
        canvas.itemconfigure("used_letters", text="".join(pressed_keys).upper())

def save_top_scores(name, round_num):
    scores = []

    # Lee las puntuaciones existentes desde el archivo ranking.txt
    with open("doc/ranking.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                scores.append((parts[0], int(parts[1])))

    scores.append((name, round_num))
    # Ordena las puntuaciones de mayor a menor y toma las cinco primeras
    scores.sort(key=lambda x: x[1], reverse=True)
    scores = scores[:5]

    # Guarda las puntuaciones actualizadas en el archivo ranking.txt
    with open("doc/ranking.txt", "w") as file:
        for score in scores:
            file.write(f"{score[0]} {score[1]}\n")

def update_top_scores():
    # Actualiza el texto de las mejores puntuaciones en el lienzo
    with open("doc/ranking.txt", "r") as file:
        scores = file.readlines()
        scores = [line.strip() for line in scores]
        top_scores = scores[:5]
        top_scores_text = "\n".join(top_scores)
        canvas.itemconfigure("ranking", text=top_scores_text)


# Código principal

# Inicialización de variables
secret_word = get_random_word().lower()
ronda = 1
lifes = 7
hidden_word = [" _" for _ in range(len(secret_word))]
pressed_keys = []

# Configuración de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Hangman Game")
ventana_principal.tk.call('wm', 'iconphoto', ventana_principal._w, tk.PhotoImage(file="images/hangman-game.png"))

# Configuración del lienzo
canvas = tk.Canvas(ventana_principal, bg="white", width=350, height=600)
fondo = set_canvas_background()
canvas_fondo = canvas.create_image(0, 0, image=fondo, anchor="nw", tags="fondo")
update_hangman_image(lifes)
canvas_hangman = canvas.create_image(20, 150, image=hangman_image, anchor="nw", tags="hangman_imagen")
canvas.create_text(50, 2, text="Top 5", font=("Arial", 8, "bold"), anchor="nw", fill="black")
canvas.create_text(40, 15, text="", font=("Arial", 8, "bold"), anchor="nw", fill="black", tags="ranking")
canvas.create_text(80, 425, text="".join(hidden_word).upper(), font=("Arial", 18, "bold"), anchor="nw", fill="black", tags="secret_word")
canvas.create_text(90, 145, text="".join(pressed_keys), font=("Arial", 13, "bold"), anchor="nw", fill="black", tags="used_letters")
canvas.pack()

# Asociación de eventos de teclado
bind_keyboard_buttons()

# Obtención del nombre del jugador
name = simpledialog.askstring("Hangman Game", "Ingrese su nombre:").capitalize()

# Actualización de las mejores puntuaciones
update_top_scores()

# Bucle principal del juego
if __name__ == "__main__":
    ventana_principal.mainloop()
