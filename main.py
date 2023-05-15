# Importamos las librerías necesarias
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#funciones

def bind_keyboard_buttons():
    # Creamos un diccionario que mapea las teclas del teclado con los botones correspondientes
    keyboard_buttons = {
        "a": button_A,
        "b": button_B,
        "c": button_C,
        "d": button_D,
        "e": button_E,
        "f": button_F,
        "g": button_G,
        "h": button_H,
        "i": button_I,
        "j": button_J,
        "k": button_K,
        "l": button_L,
        "m": button_M,
        "n": button_N,
        "o": button_O,
        "p": button_P,
        "q": button_Q,
        "r": button_R,
        "s": button_S,
        "t": button_T,
        "u": button_U,
        "v": button_V,
        "w": button_W,
        "x": button_X,
        "y": button_Y,
        "z": button_Z
    }
    # Asociamos las teclas del teclado a la función check_user_input_letter
    for key, button in keyboard_buttons.items():
        ventana_principal.bind(key, lambda event, btn=button: check_user_input_letter(event.char, btn))

def set_canvas_background():
    img = Image.open("Hangman images/fondo.jpg")
    img = img.resize((350, 600), Image.LANCZOS)
    background = ImageTk.PhotoImage(img)
    return background

# Definimos una función que activa todos los botones
def enable_all_buttons():
    # Recorremos la lista de botones y los activamos
    for button in [button_A, button_B, button_C, button_D, button_E, button_F, button_G, button_H, button_I, button_J, button_K, button_L, button_M, button_N, button_O, button_P, button_Q, button_R, button_S, button_T, button_U, button_V, button_W, button_X, button_Y, button_Z]:
        button["state"] = "active"

# Definimos una función que carga la imagen correspondiente al número de vidas que quedan
def update_hangman_image(lifes):
    global hangman_image  # Variable global para almacenar la imagen de ahorcado
    # Creamos una lista con las rutas de las imágenes de ahorcado
    imagenes = [
        "Hangman images/Hangman-07.png",
        "Hangman images/Hangman-06.png",
        "Hangman images/Hangman-05.png",
        "Hangman images/Hangman-04.png",
        "Hangman images/Hangman-03.png",
        "Hangman images/Hangman-02.png",
        "Hangman images/Hangman-01.png",
    ]
    # Accedemos a la variable global de vidas y cargamos la imagen correspondiente
    image = Image.open(imagenes[lifes - 1])
    image = image.resize((300, 300), Image.LANCZOS)
    hangman_image = ImageTk.PhotoImage(image)

# Definimos una función que escoge una palabra al azar del archivo correspondiente al nivel indicado
def get_random_word(level=1):
    # Creamos un diccionario con los nombres de los archivos de palabras para cada nivel
    filenames_word = {
        1: "easy_words.txt",
        2: "medium_words.txt",
        3: "hard_words.txt",
    }
    # Abrimos el archivo correspondiente al nivel y cargamos las palabras en una lista
    with open(filenames_word[level], "r") as file:
        words = file.read().split("\n")
    # Escogemos una palabra al azar de la lista y la convertimos a minúsculas
    return random.choice(words)

# Definimos una función que verifica si la letra escogida por el usuario está en la palabra secreta
def check_user_input_letter(letter, boton):
    global hidden_word, lifes, secret_word, level, pressed_keys
    # Verificamos si la tecla ya ha sido presionada anteriormente
    if letter in pressed_keys:
        return  # Salir de la función si la tecla ya ha sido presionada
    pressed_keys.add(letter)  # Agregar la tecla al conjunto de teclas presionadas
    # Si la letra está en la palabra secreta, reemplazamos los guiones bajos correspondientes por la letra
    if letter in secret_word:
        for i, character in enumerate(secret_word):
            if character == letter:
                hidden_word[i] = letter
    else:
        # Si la letra no está en la palabra secreta, disminuimos el número de vidas restantes y mostramos la imagen correspondiente
        lifes -= 1
        update_hangman_image(lifes)
        canvas.itemconfigure("hangman_imagen", image=hangman_image)
        # Si el usuario se queda sin vidas, se muestra un mensaje indicando que el juego ha terminado
        if lifes == 1:
            messagebox.showinfo("Game Over  ", f"The word was {secret_word}")
            ventana_principal.quit()
    # Desactivamos el botón correspondiente a la letra seleccionada
    boton.config(state="disabled")
    # Actualizamos la etiqueta que muestra la palabra secreta con los guiones bajos y las letras adivinadas
    canvas.itemconfigure("secret_word",text="".join(hidden_word))
    # Verificamos si el usuario ha adivinado todas las letras de la palabra secreta, en cuyo caso pasamos al siguiente nivel
    if " _" not in hidden_word:
        level += 1
        # Si el usuario ha pasado el nivel 3, se muestra un mensaje indicando que ha ganado el juego
        if level == 4:
            messagebox.showinfo(
                "You Win!", "Congratulations you are incredible!")
            ventana_principal.quit()
        # Si el usuario no ha pasado el nivel 3, se carga una nueva palabra y se reinicia el número de vidas restantes
        else:
            pressed_keys = set()
            lifes = 7
            secret_word = get_random_word(level)
            hidden_word = [" _" for _ in range(len(secret_word))]
            canvas.itemconfigure("secret_word",text="".join(hidden_word))
            update_hangman_image(lifes)
            canvas.itemconfigure("hangman_imagen",image=hangman_image)
            messagebox.showinfo("GOOD JOB", f"Now go to level {level}!")
            # Se activan todos los botones para la siguiente palabra
            enable_all_buttons()

    #variables
secret_word = get_random_word().lower()
level = int(1)
lifes = 7
hidden_word = [" _" for _ in range(len(secret_word))]
pressed_keys = set()

# Creamos una ventana
ventana_principal = tk.Tk()

# Establecemos la geometría de la ventana y su título
canvas = tk.Canvas(ventana_principal, bg="white", width=350, height=600)
# Creamos una imagen de fondo
fondo = set_canvas_background()
# Creamos una etiqueta de imagen y establecemos la imagen de fondo en ella
canvas_fondo = canvas.create_image(0,0, image=fondo, anchor="nw",tags="fondo")
# Escogemos una palabra al azar para empezar el juego y establecemos el nivel y las vidas iniciales
update_hangman_image(lifes)
canvas_hangman = canvas.create_image(20, 150, image=hangman_image, anchor="nw", tags="hangman_imagen")
canvas.create_text(65, 10, text="HANGMAN", font=("Impact", 30), anchor="nw", fill="black")
canvas.create_text(130, 145, text="".join(hidden_word), font=("Arial", 18, "bold"), anchor="nw", fill="black", tags="secret_word")

button_A = tk.Button(command=lambda: check_user_input_letter("a", button_A))
button_B = tk.Button(command=lambda: check_user_input_letter("b", button_B))
button_C = tk.Button(command=lambda: check_user_input_letter("c", button_C))
button_D = tk.Button(command=lambda: check_user_input_letter("d", button_D))
button_E = tk.Button(command=lambda: check_user_input_letter("e", button_E))
button_F = tk.Button(command=lambda: check_user_input_letter("f", button_F))
button_G = tk.Button(command=lambda: check_user_input_letter("g", button_G))
button_H = tk.Button(command=lambda: check_user_input_letter("h", button_H))
button_I = tk.Button(command=lambda: check_user_input_letter("i", button_I))
button_J = tk.Button(command=lambda: check_user_input_letter("j", button_J))
button_K = tk.Button(command=lambda: check_user_input_letter("k", button_K))
button_L = tk.Button(command=lambda: check_user_input_letter("l", button_L))
button_M = tk.Button(command=lambda: check_user_input_letter("m", button_M))
button_N = tk.Button(command=lambda: check_user_input_letter("n", button_N))
button_O = tk.Button(command=lambda: check_user_input_letter("o", button_O))
button_P = tk.Button(command=lambda: check_user_input_letter("p", button_P))
button_Q = tk.Button(command=lambda: check_user_input_letter("q", button_Q))
button_R = tk.Button(command=lambda: check_user_input_letter("r", button_R))
button_S = tk.Button(command=lambda: check_user_input_letter("s", button_S))
button_T = tk.Button(command=lambda: check_user_input_letter("t", button_T))
button_U = tk.Button(command=lambda: check_user_input_letter("u", button_U))
button_V = tk.Button(command=lambda: check_user_input_letter("v", button_V))
button_W = tk.Button(command=lambda: check_user_input_letter("w", button_W))
button_X = tk.Button(command=lambda: check_user_input_letter("x", button_X))
button_Y = tk.Button(command=lambda: check_user_input_letter("y", button_Y))
button_Z = tk.Button(command=lambda: check_user_input_letter("z", button_Z))
canvas.pack()

bind_keyboard_buttons()
ventana_principal.mainloop()