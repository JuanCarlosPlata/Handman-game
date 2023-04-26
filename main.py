from time import sleep
import sys
from os import system, name
import random
from stickman import stickman

# Funcion para limpiar la pantalla
def clear_screen():
    if name == 'nt': # Si el sistema operativo es Windows
        _ = system('cls')
    else: # Si el sistema operativo es Mac o Linux
        _ = system('clear')

# Funcion para escribir letra por letra
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.02)  # Tiempo de espera estre cada letra

# Funcion para validar que solo se ingresen letras en el input del usuario
def validate_user_input_text(text): # text indica el mensaje que se mostrar junto con el input
    while True:
        delay_print(text)
        letter = str(input("\n=> "))
        if len(letter) == 1 and letter.isalpha(): # Si lo ingresado es solo 1 letra y no es nada distinto a letras el programa continua de los contrario lanza un error y vuelve a preguntar
            return letter
        delay_print(f"Invalid option\nPlease only enter 1 letter (A-Z)\n") # Mostrar mensaje de error y volver a preguntar
        sleep(1)
        continue

# Funcion que escoge una palabra de forma aleatoria del archivo palabras.txt
def choice_word(level=1):
    filenames = {
        1: "easy_words.txt",
        2: "medium_words.txt",
        3: "hard_words.txt",
    }
    with open(filenames[level]) as f:
        words = f.read().split("\n")
        return random.choice(words)

# Funcion que verifica si una letra ingresada por el usuario esta en la palabra seleccionada
def check_user_input_letter(letter):
    for i, character in enumerate(word):
        if character == letter:
            secret_word[i] = letter
    return secret_word

# Función para comprobar si una letra ya ha sido utilizada
def letter_already_used(letter):
    global used_words
    if letter in used_words:
        return True
    letter = letter
    used_words.add(letter)
    return False

# variables de la palabra escogida y la palabra secreta
word = choice_word().lower()
level = int(1)
secret_word = ["_" for _ in range(len(word))]  # Utilizamos una lista de compresión para crear una lista de guiones bajos del tamaño de la palabra escogida
used_words = set()  # Creamos un conjunto vacío para almacenar las letras usadas

# Nucleo del juego
def run():
    global level,used_words,secret_word,word
    lifes = 8
    delay_print("Welcome to Hangman!\n")
    sleep(1)
    while lifes > 0:
        print(stickman[(8-lifes)])
        print("".join(secret_word))  # Unimos los caracteres de la lista secreta en una sola cadena para imprimir
        print("Used letters:", "-".join(sorted(used_words)))  # Imprimimos las letras usadas ordenadas alfabéticamente
        valid_word = validate_user_input_text("Please enter one letter (A-Z)")
        if letter_already_used(valid_word):
            delay_print("You've already used that letter\n")
            sleep(1)
            clear_screen()
            continue
        if valid_word in word:
            delay_print("Good job!\n")
            sleep(1)
            check_user_input_letter(valid_word)
        else:
            delay_print("Wrong letter\n")
            sleep(1)
            lifes -= 1
        clear_screen()
        if "_" not in secret_word:
            delay_print(f"You Win! The word was {word}\n")
            sleep(1)
            level += 1
            if level == 4:
                delay_print("Congratulations you are incredible!!!\n")
                break
            word = choice_word(level).lower()
            secret_word = ["_" for _ in range(len(word))]
            used_words.clear()
            lifes = 8
            delay_print(f"\nNext word (level {level})\n")
            sleep(1)
    if lifes == 0:
        print(stickman[(8-lifes)])
        delay_print(f"You lose! The word was {word}\n")
        sleep(1)

if __name__ == "__main__":
    run()