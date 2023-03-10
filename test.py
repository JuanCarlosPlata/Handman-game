from time import sleep
import sys
from os import system, name
import random
import pandas as pd

"""def words():
    words = ["laptop", "umbrella", "radiator", "kitchen", "smartphone"]
    word = random.choice(words)
    return word


word =  words()
print (f"{word}\n{len(word)}")
"""

# reading the CSV file
"""csvFile = pd.read_csv('palabras.csv')"""
"""word = random.choice(csvFile)"""

# displaying the contents of the CSV file
"""print(csvFile)"""
"""print(word)"""


"""with open('palabras.txt') as f:
    words = f.read().split(",")
    my_pick = random.choice(words)
    print (my_pick)"""




  
"""def word():
    with open('palabras.txt') as f:
        words = f.read().split(",")
        my_pick = random.choice(words)
    return my_pick

print (word())"""

def choice_word():
    with open('palabras.txt') as f:
        words = f.read().split(",")
        my_pick = random.choice(words)
    return my_pick

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.02)  # Tiempo de espera estre cada letra

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

"""print(validate_user_input_text("Ingrese una letra"))"""



word = choice_word()
list_word = list(word)
secret_word = ["_"]*len(word)

def check_user_input_letter(letra):
    for i, caracter in enumerate(word):
        if caracter == letra:
            secret_word[i] = letra
    return secret_word




def hangman(rope="",head="",chest="",right_arm=" ",left_arm="",cintura="",right_leg="",left_leg=""):
    stickman=f"""
   ________
    |/   {rope}     
    |   {head}    
    |   {right_arm}{chest}{left_arm}           
    |    {cintura}        
    |   {right_leg} {left_leg}        
    |               
    |___           """
    print(stickman)

hangman("|","🐷","|","/","\\","|","/","\\")

print(" "*10,"".join(check_user_input_letter("o")))
