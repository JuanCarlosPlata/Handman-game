from time import sleep
import sys
from os import system, name
import random

def clear():
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
        try:
            delay_print(text)
            valor = int(input("\n=> "))
        except ValueError:
            delay_print(f"Invalid option\nPlease only enter letters (A-Z)\n")
            sleep(1.5)
            continue
        return valor

# Funcion que escoge una palbra de la lista
def words():
    words = ["laptop", "umbrella", "radiator", "kitchen", "smartphone"]
    word = random.choice(words)
    return word

# Funcion que mostrara en pantalla el juego
def visual_game():
    None

word =  words()
lifes = 6
# nucleo del juego
def run():
    while lifes < 0:


if __name__ == "__main__":
    run()