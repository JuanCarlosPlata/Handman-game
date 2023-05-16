import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

def bind_keyboard_buttons():
    for key in "abcdefghijklmnopqrstuvwxyz":
        ventana_principal.bind(key, lambda event, key=key: check_user_input_letter(key))

def set_canvas_background():
    img = Image.open("images/background.jpg")
    img = img.resize((350, 600), Image.LANCZOS)
    background = ImageTk.PhotoImage(img)
    return background

def update_hangman_image(lifes):
    global hangman_image
    image_path = f"images/Hangman-0{8 - lifes}.png"
    image = Image.open(image_path)
    image = image.resize((300, 300), Image.LANCZOS)
    hangman_image = ImageTk.PhotoImage(image)

def get_random_word():
    with open("doc/words.txt", "r") as file:
        words = file.read().split("\n")
    return random.choice(words)

def check_user_input_letter(letter):
    global hidden_word, lifes, secret_word, pressed_keys, ronda, name
    if letter in pressed_keys:
        return
    pressed_keys.append(letter)
    pressed_keys.sort()
    canvas.itemconfigure("used_letters", text="".join(pressed_keys).upper())
    if letter in secret_word:
        for i, character in enumerate(secret_word):
            if character == letter:
                hidden_word[i] = letter
    else:
        lifes -= 1
        update_hangman_image(lifes)
        canvas.itemconfigure("hangman_imagen", image=hangman_image)
        if lifes == 1:
            save_top_scores(name, ronda)
            messagebox.showinfo("Game Over", f"You completed {ronda} rounds!\nThe word was {secret_word.upper()}")
            ventana_principal.quit()
    canvas.itemconfigure("secret_word", text="".join(hidden_word).upper())
    if " _" not in hidden_word:
        messagebox.showinfo("GOOD JOB", "Now go for another word!")
        ronda += 1
        pressed_keys = []
        lifes = 7
        secret_word = get_random_word()
        hidden_word = [" _" for _ in range(len(secret_word))]
        canvas.itemconfigure("secret_word", text="".join(hidden_word).upper())
        update_hangman_image(lifes)
        canvas.itemconfigure("hangman_imagen", image=hangman_image)
        canvas.itemconfigure("used_letters", text="".join(pressed_keys).upper())

def save_top_scores(name, round_num):
    # Leer el contenido actual del archivo y almacenarlo en una lista
    scores = []
    with open("doc/ranking.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split()
                scores.append((parts[0], int(parts[1])))
    # Agregar el nuevo registro a la lista
    scores.append((name, round_num))
    # Ordenar la lista en función del número de ronda en orden descendente
    scores.sort(key=lambda x: x[1], reverse=True)
    # Mantener solo los 5 mejores registros
    scores = scores[:5]
    # Guardar los registros en el archivo
    with open("doc/ranking.txt", "w") as file:
        for score in scores:
            file.write(f"{score[0]} {score[1]}\n")

def update_top_scores():
    with open("doc/ranking.txt", "r") as file:
        scores = file.readlines()
        scores = [line.strip() for line in scores]
        top_scores = scores[:5]
        top_scores_text = "\n".join(top_scores)
        canvas.itemconfigure("ranking", text=top_scores_text)

secret_word = get_random_word().lower()
ronda = 1
lifes = 7
hidden_word = [" _" for _ in range(len(secret_word))]
pressed_keys = []
ventana_principal = tk.Tk()
ventana_principal.resizable(False, False)
ventana_principal.title("Hangman Game")
ventana_principal.tk.call('wm', 'iconphoto', ventana_principal._w, tk.PhotoImage(file="images/hangman-game.png"))
canvas = tk.Canvas(ventana_principal, bg="white", width=350, height=600)
fondo = set_canvas_background()
canvas_fondo = canvas.create_image(0,0, image=fondo, anchor="nw",tags="fondo")
update_hangman_image(lifes)
canvas_hangman = canvas.create_image(20, 150, image=hangman_image, anchor="nw", tags="hangman_imagen")
canvas.create_text(50, 2, text="Top 5", font=("Arial", 8, "bold"), anchor="nw", fill="black")
canvas.create_text(40, 15, text="", font=("Arial", 8, "bold"), anchor="nw", fill="black", tags="ranking")
canvas.create_text(80, 425, text="".join(hidden_word).upper(), font=("Arial", 18, "bold"), anchor="nw", fill="black", tags="secret_word")
canvas.create_text(90, 145, text="".join(pressed_keys), font=("Arial", 13, "bold"), anchor="nw", fill="black", tags="used_letters")
canvas.pack()
bind_keyboard_buttons()
name = simpledialog.askstring("Hangman Game", "Ingrese su nombre:").capitalize()
update_top_scores()

if __name__ == "__main__":
    ventana_principal.mainloop()