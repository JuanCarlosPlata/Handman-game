# Importamos las librerías necesarias
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Creamos una ventana
ventana_principal = Tk()



# Establecemos la geometría de la ventana y su título
ventana_principal.attributes('-alpha', True)
ventana_principal.geometry("350x600")
ventana_principal.title("Hangman Game")

# Creamos una imagen de fondo
fondo = Image.open("Hangman images/fondo.jpg")
fondo = fondo.resize((350, 600), Image.ANTIALIAS)
fondo = ImageTk.PhotoImage(fondo)

# Creamos una etiqueta de imagen y establecemos la imagen de fondo en ella
label_fondo = Label(ventana_principal, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Definimos una función que activa todos los botones
def enable_all_buttons():
    # Recorremos la lista de botones y los activamos
    for button in [button_A, button_B, button_C, button_D, button_E, button_F, button_G, button_H, button_I, button_J, button_K, button_L, button_M, button_N, button_O, button_P, button_Q, button_R, button_S, button_T, button_U, button_V, button_W, button_X, button_Y, button_Z]:
        button["state"] = "active"

# Definimos una función que carga la imagen correspondiente al número de vidas que quedan
def update_hangman_image():
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
    global hangman_image, lifes
    image = Image.open(imagenes[lifes - 1])
    image = image.resize((300, 300), Image.ANTIALIAS)
    hangman_image = ImageTk.PhotoImage(image)
    return hangman_image

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

# Escogemos una palabra al azar para empezar el juego y establecemos el nivel y las vidas iniciales
secret_word = get_random_word().lower()
level = int(1)
lifes = 7
# Creamos una lista de guiones bajos del tamaño de la palabra escogida
hidden_word = [" _" for _ in range(len(secret_word))]

# Definimos una función que verifica si la letra escogida por el usuario está en la palabra secreta
def check_user_input_letter(letter, boton):
    global hidden_word, label_hidden_word, lifes, secret_word, level
    # Si la letra está en la palabra secreta, reemplazamos los guiones bajos correspondientes por la letra
    if letter in secret_word:
        for i, character in enumerate(secret_word):
            if character == letter:
                hidden_word[i] = letter
    else:
        # Si la letra no está en la palabra secreta, disminuimos el número de vidas restantes y mostramos la imagen correspondiente
        lifes -= 1
        label_hangman.config(image=update_hangman_image())
        # Si el usuario se queda sin vidas, se muestra un mensaje indicando que el juego ha terminado
        if lifes == 1:
            messagebox.showinfo("Game Over  ", f"The word was {secret_word}")
            ventana_principal.quit()
    # Desactivamos el botón correspondiente a la letra seleccionada
    boton.config(state="disabled")
    # Actualizamos la etiqueta que muestra la palabra secreta con los guiones bajos y las letras adivinadas
    label_hidden_word.config(text=" ".join(hidden_word))
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
            lifes = 7
            secret_word = get_random_word(level)
            hidden_word = [" _" for _ in range(len(secret_word))]
            label_hidden_word.config(text=" ".join(hidden_word))
            label_hangman.config(image=update_hangman_image())
            messagebox.showinfo("GOOD JOB", f"Now go to level {level}!")
            # Se activan todos los botones para la siguiente palabra
            enable_all_buttons()


Label(ventana_principal,
      text="Hangman",
      font="normal 20 bold",
      fg="blue").grid(row=0, column=0, columnspan=1, pady=10)


label_hangman = Label(ventana_principal, image=update_hangman_image())
label_hidden_word = Label(ventana_principal, text="".join(hidden_word), font="normal 20")
label_hangman.grid(row=1, column=0)
label_hidden_word.grid(row=2, column=0, pady=10)

frame_buttons_1 = Frame(ventana_principal)
frame_buttons_2 = Frame(ventana_principal)
frame_buttons_3 = Frame(ventana_principal)
frame_buttons_4 = Frame(ventana_principal)
frame_buttons_5 = Frame(ventana_principal)
frame_buttons_1.grid(row=3, column=0, columnspan=5)
frame_buttons_2.grid(row=4, column=0, columnspan=5)
frame_buttons_3.grid(row=5, column=0, columnspan=5)
frame_buttons_4.grid(row=6, column=0, columnspan=5)
frame_buttons_5.grid(row=7, column=0, columnspan=5)

button_A = Button(frame_buttons_1, text="A", font=10, width=1, command=lambda: check_user_input_letter("a", button_A))
button_B = Button(frame_buttons_1, text="B", font=10, width=1, command=lambda: check_user_input_letter("b", button_B))
button_C = Button(frame_buttons_1, text="C", font=10, width=1, command=lambda: check_user_input_letter("c", button_C))
button_D = Button(frame_buttons_1, text="D", font=10, width=1, command=lambda: check_user_input_letter("d", button_D))
button_E = Button(frame_buttons_1, text="E", font=10, width=1, command=lambda: check_user_input_letter("e", button_E))
button_F = Button(frame_buttons_2, text="F", font=10, width=1, command=lambda: check_user_input_letter("f", button_F))
button_G = Button(frame_buttons_2, text="G", font=10, width=1, command=lambda: check_user_input_letter("g", button_G))
button_H = Button(frame_buttons_2, text="H", font=10, width=1, command=lambda: check_user_input_letter("h", button_H))
button_I = Button(frame_buttons_2, text="I", font=10, width=1, command=lambda: check_user_input_letter("i", button_I))
button_J = Button(frame_buttons_2, text="J", font=10, width=1, command=lambda: check_user_input_letter("j", button_J))
button_K = Button(frame_buttons_3, text="K", font=10, width=1, command=lambda: check_user_input_letter("k", button_K))
button_L = Button(frame_buttons_3, text="L", font=10, width=1, command=lambda: check_user_input_letter("l", button_L))
button_M = Button(frame_buttons_3, text="M", font=10, width=1, command=lambda: check_user_input_letter("m", button_M))
button_N = Button(frame_buttons_3, text="N", font=10, width=1, command=lambda: check_user_input_letter("n", button_N))
button_O = Button(frame_buttons_3, text="O", font=10, width=1, command=lambda: check_user_input_letter("o", button_O))
button_P = Button(frame_buttons_4, text="P", font=10, width=1, command=lambda: check_user_input_letter("p", button_P))
button_Q = Button(frame_buttons_4, text="Q", font=10, width=1, command=lambda: check_user_input_letter("q", button_Q))
button_R = Button(frame_buttons_4, text="R", font=10, width=1, command=lambda: check_user_input_letter("r", button_R))
button_S = Button(frame_buttons_4, text="S", font=10, width=1, command=lambda: check_user_input_letter("s", button_S))
button_T = Button(frame_buttons_4, text="T", font=10, width=1, command=lambda: check_user_input_letter("t", button_T))
button_U = Button(frame_buttons_5, text="U", font=10, width=1, command=lambda: check_user_input_letter("u", button_U))
button_V = Button(frame_buttons_5, text="V", font=10, width=1, command=lambda: check_user_input_letter("v", button_V))
button_W = Button(frame_buttons_5, text="W", font=10, width=1, command=lambda: check_user_input_letter("w", button_W))
button_X = Button(frame_buttons_5, text="X", font=10, width=1, command=lambda: check_user_input_letter("x", button_X))
button_Y = Button(frame_buttons_5, text="Y", font=10, width=1, command=lambda: check_user_input_letter("y", button_Y))
button_Z = Button(frame_buttons_5, text="Z", font=10, width=1, command=lambda: check_user_input_letter("z", button_Z))

button_A.pack(side=LEFT, padx=5,)
button_B.pack(side=LEFT, padx=5)
button_C.pack(side=LEFT, padx=5)
button_D.pack(side=LEFT, padx=5)
button_E.pack(side=LEFT, padx=5)
button_F.pack(side=LEFT, padx=5)
button_G.pack(side=LEFT, padx=5)
button_H.pack(side=LEFT, padx=5)
button_I.pack(side=LEFT, padx=5)
button_J.pack(side=LEFT, padx=5)
button_K.pack(side=LEFT, padx=5)
button_L.pack(side=LEFT, padx=5)
button_M.pack(side=LEFT, padx=5)
button_N.pack(side=LEFT, padx=5)
button_O.pack(side=LEFT, padx=5)
button_P.pack(side=LEFT, padx=5)
button_Q.pack(side=LEFT, padx=5)
button_R.pack(side=LEFT, padx=5)
button_S.pack(side=LEFT, padx=5)
button_T.pack(side=LEFT, padx=5)
button_U.pack(side=LEFT, padx=5)
button_V.pack(side=LEFT, padx=5)
button_W.pack(side=LEFT, padx=5)
button_X.pack(side=LEFT, padx=5)
button_Y.pack(side=LEFT, padx=5)
button_Z.pack(side=LEFT, padx=7)

ventana_principal.mainloop()
