import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("350x600")
ventana.title("Hangman Game")


def next_level():
    for button in [button_A, button_B, button_C, button_D, button_E, button_F, button_G, button_H, button_I, button_J, button_K, button_L, button_M, button_N, button_O, button_P, button_Q, button_R, button_S, button_T, button_U, button_V, button_W, button_X, button_Y, button_Z]:
        button["state"] = "active"


def imagen_hangman():
    imagenes = [
        "Hangman images/Hangman-07.png",
        "Hangman images/Hangman-06.png",
        "Hangman images/Hangman-05.png",
        "Hangman images/Hangman-04.png",
        "Hangman images/Hangman-03.png",
        "Hangman images/Hangman-02.png",
        "Hangman images/Hangman-01.png",
    ]
    global photo, lifes
    image = Image.open(imagenes[lifes - 1])
    image = image.resize((300, 300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    return photo


def choice_word(level=1):
    filenames = {
        1: "easy_words.txt",
        2: "medium_words.txt",
        3: "hard_words.txt",
    }
    with open(filenames[level], "r") as f:
        words = f.read().split("\n")
    return random.choice(words)


word = choice_word().lower()
level = int(1)
lifes = 7
# Utilizamos una lista de compresión para crear una lista de guiones bajos del tamaño de la palabra escogida
secret_word = [" _" for _ in range(len(word))]
used_words = set()  # Creamos un conjunto vacío para almacenar las letras usadas


def check_user_input_letter(letter, boton):
    global secret_word, label_2, lifes, word, level
    if letter in word:
        for i, character in enumerate(word):
            if character == letter:
                secret_word[i] = letter
    else:
        lifes -= 1
        label_1.config(image=imagen_hangman())
        if lifes == 1:
            messagebox.showinfo("Game Over  ", f"The word was {word}")
            ventana.quit()
    boton.config(state="disabled")
    label_2.config(text=" ".join(secret_word))
    if " _" not in secret_word:
        level += 1
        if level == 4:
            messagebox.showinfo(
                "You Win!", "Congratulations you are incredible!")
            ventana.quit()
        else:
            lifes = 7
            word = choice_word(level)
            secret_word = [" _" for _ in range(len(word))]
            label_2.config(text=" ".join(secret_word))
            label_1.config(image=imagen_hangman())
            messagebox.showinfo("GOOD JOB", f"Now go to level {level}!")
            next_level()


Label(ventana,
      text="Hangman",
      font="normal 20 bold",
      fg="blue").grid(row=0, column=0, columnspan=1, pady=10)

label_1 = Label(ventana, image=imagen_hangman())
label_2 = Label(ventana, text="".join(secret_word), font="normal 20")
label_1.grid(row=1, column=0)
label_2.grid(row=2, column=0, pady=10)

frame1 = Frame(ventana)
frame2 = Frame(ventana)
frame3 = Frame(ventana)
frame4 = Frame(ventana)
frame5 = Frame(ventana)
frame1.grid(row=3, column=0, columnspan=5)
frame2.grid(row=4, column=0, columnspan=5)
frame3.grid(row=5, column=0, columnspan=5)
frame4.grid(row=6, column=0, columnspan=5)
frame5.grid(row=7, column=0, columnspan=5)

button_A = Button(frame1, text="A", font=10, padx=10, command=lambda: check_user_input_letter("a", button_A))
button_B = Button(frame1, text="B", font=10, width=1, command=lambda: check_user_input_letter("b", button_B))
button_C = Button(frame1, text="C", font=10, width=1, command=lambda: check_user_input_letter("c", button_C))
button_D = Button(frame1, text="D", font=10, width=1, command=lambda: check_user_input_letter("d", button_D))
button_E = Button(frame1, text="E", font=10, width=1, command=lambda: check_user_input_letter("e", button_E))
button_F = Button(frame2, text="F", font=10, width=1, command=lambda: check_user_input_letter("f", button_F))
button_G = Button(frame2, text="G", font=10, width=1, command=lambda: check_user_input_letter("g", button_G))
button_H = Button(frame2, text="H", font=10, width=1, command=lambda: check_user_input_letter("h", button_H))
button_I = Button(frame2, text="I", font=10, width=1, command=lambda: check_user_input_letter("i", button_I))
button_J = Button(frame2, text="J", font=10, width=1, command=lambda: check_user_input_letter("j", button_J))
button_K = Button(frame3, text="K", font=10, width=1, command=lambda: check_user_input_letter("k", button_K))
button_L = Button(frame3, text="L", font=10, width=1, command=lambda: check_user_input_letter("l", button_L))
button_M = Button(frame3, text="M", font=10, width=1, command=lambda: check_user_input_letter("m", button_M))
button_N = Button(frame3, text="N", font=10, width=1, command=lambda: check_user_input_letter("n", button_N))
button_O = Button(frame3, text="O", font=10, width=1, command=lambda: check_user_input_letter("o", button_O))
button_P = Button(frame4, text="P", font=10, width=1, command=lambda: check_user_input_letter("p", button_P))
button_Q = Button(frame4, text="Q", font=10, width=1, command=lambda: check_user_input_letter("q", button_Q))
button_R = Button(frame4, text="R", font=10, width=1, command=lambda: check_user_input_letter("r", button_R))
button_S = Button(frame4, text="S", font=10, width=1, command=lambda: check_user_input_letter("s", button_S))
button_T = Button(frame4, text="T", font=10, width=1, command=lambda: check_user_input_letter("t", button_T))
button_U = Button(frame5, text="U", font=10, width=1, command=lambda: check_user_input_letter("u", button_U))
button_V = Button(frame5, text="V", font=10, width=1, command=lambda: check_user_input_letter("v", button_V))
button_W = Button(frame5, text="W", font=10, width=1, command=lambda: check_user_input_letter("w", button_W))
button_X = Button(frame5, text="X", font=10, width=1, command=lambda: check_user_input_letter("x", button_X))
button_Y = Button(frame5, text="Y", font=10, width=1, command=lambda: check_user_input_letter("y", button_Y))
button_Z = Button(frame5, text="Z", font=10, width=1, command=lambda: check_user_input_letter("z", button_Z))

button_A.pack(side=LEFT, padx=5)
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

ventana.mainloop()
