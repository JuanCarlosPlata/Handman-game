from time import sleep
import sys
from os import system, name
import random

# Funcion para limpiar la pantalla
def clear_screen():
    # Si el sistema operativo es Windows
    if name == 'nt':
        _ = system('cls')
    # Si el sistema operativo es Mac o Linux
    else:
        _ = system('clear')

# Funcion para escribir letra por letra
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.02)  # Tiempo de espera estre cada letra

# Funcion para validar que solo se ingresen letras en el input del usuario
def validate_user_input_text(text):
    while True:
        # text indica el mensaje que se mostrar junto con el input
        delay_print(text)
        valor = str(input("\n=> "))
        # Si lo ingresado es solo 1 letra y no es nada distinto a letras el programa continua de los contrario lanza un error y vuelve a preguntar
        if len(valor) == 1 and valor.isalpha():
            return valor
        # Mostrar mensaje de error y volver a preguntar
        delay_print(f"Invalid option\nPlease only enter 1 letter (A-Z)\n")
        sleep(1)
        continue

# Funcion que escoge una palabra de forma aleatoria del archivo palabras.txt
def choice_word():
    with open('palabras.txt') as f:
        words = f.read().split(",")
        my_pick = random.choice(words)
    return my_pick

# Funcion que verifica si una letra ingresada por el usuario esta en la palabra seleccionada
def check_user_input_letter(letra):
    global secret_word
    for i, caracter in enumerate(word):
        if caracter == letra:
            secret_word[i] = letra
    return letra

# variables de la palabra escogida y la palabra secreta
word = choice_word()
secret_word = ["_" for _ in range(len(word))]  # Utilizamos una lista de compresión para crear una lista de guiones bajos del tamaño de la palabra escogida
used_words = set()  # Creamos un conjunto vacío para almacenar las letras usadas


# Representaciones del stickman según las vidas restantes
stickman="""
   ________
    |/         
    |        
    |                 
    |             
    |              
    |               
    |___           ""","""
   ________
    |/   |     
    |        
    |                 
    |             
    |              
    |               
    |___           ""","""
   ________
    |/   |     
    |   🐷    
    |                 
    |             
    |              
    |               
    |___           ""","""
   ________
    |/   |     
    |   🐷    
    |    |            
    |             
    |              
    |               
    |___           ""","""
   ________
    |/   |     
    |   🐷    
    |   /|            
    |             
    |              
    |               
    |___           ""","""
   ________
    |/   |     
    |   🐷    
    |   /|\           
    |             
    |              
    |               
    |___           ""","""
   ________
    |/   |     
    |   🐷    
    |   /|\           
    |    |        
    |              
    |               
    |___           ""","""
   ________
    |/   |     
    |   🐷    
    |   /|\           
    |    |        
    |   /          
    |               
    |___           ""","""
    _______
    |/   |     
    |   🐷    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           """

# Función para comprobar si una letra ya ha sido utilizada
def letter_already_used(letra):
    global used_words
    if letra in used_words:
        return True
    used_words.add(letra)
    return False

# Nucleo del juego
def run():
    global used_words
    lifes = 8
    while lifes > 0:
        print(stickman[(8-lifes)])
        print("".join(secret_word))  # Unimos los caracteres de la lista secreta en una sola cadena para imprimir
        print("Used letters:", ", ".join(sorted(used_words)))  # Imprimimos las letras usadas ordenadas alfabéticamente
        valid_word = validate_user_input_text("Please enter one letter (A-Z)")
        if letter_already_used(valid_word):
            delay_print("You've already used that letter\n")
            sleep(1)
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
            delay_print("You win!\n")
            sleep(1)
            break
    else:
        delay_print(f"You lose! The word was {word}\n")

if __name__ == "__main__":
    run()