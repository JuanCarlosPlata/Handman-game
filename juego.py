from time import sleep
import sys
from os import system, name
import random



def hangman(rope="",head="",chest="",right_arm=" ",left_arm="",cintura="",right_leg="",left_leg=""):
    stickman=f"""
   ________
    |/   {rope}     
    |   {head}    
    |   {right_arm}{chest}{left_arm}           
    |    {cintura}        
    |   {right_leg} {left_leg}        
    |               
    |___           
    """
    print(stickman)

# Funcion para limpiar la pantalla
def clear_screen():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Funcion para escribir letra por letra
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.02)  # Tiempo de espera estre cada letra

# Funcion para validadr que solo se ingresen letras en el input del usuario
def validate_user_input_text(text):
    while True:
        # text indica el mensaje que se mostrar junto con el input
        delay_print(text)
        valor = str(input("\n=> "))
        # Si lo ingresado es solo 1 letra y no es nada distinto a letras el programa continua de los contrario lanza un error y vuelve a preguntar
        if len(valor) == 1 and valor.isalpha():
            return valor
        delay_print(f"Invalid option\nPlease only enter 1 letter (A-Z)\n")
        sleep(1)
        continue

# Funcion que escoge una palabra de formar aleatoria del archivo palabras.txt
def choice_word():
    with open('palabras.txt') as f:
        words = f.read().split(",")
        my_pick = random.choice(words)
    return my_pick

# Funcion que mostrara en pantalla el juego
def visual_game(lives):
    print(hangman[lives])

# Funcionn para comprobar que la letrea ingresada se encuentre en la  palabra a adivinar
def check_user_input_letter(letra):
    for i, caracter in enumerate(word):
        if caracter == letra:
            secret_word[i] = letra
    return secret_word

# variables de la palabra escogida y la palbra secreta
word = choice_word()
list_word = list(word)
secret_word = ["_"]*len(word)

# nucleo del juego
def run():
    lifes = 7
    used_words;used_words = "".capitalize
    ronda;ronda=0
    while lifes < 0:
        hangman()
        validate_user_input_text("Please enter one letter (A-Z)")
        continue
        


if __name__ == "__main__":
    run()