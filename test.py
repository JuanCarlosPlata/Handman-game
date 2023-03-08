from time import sleep
import sys
from os import system, name
import random
import pandas

def words():
    words = ["laptop", "umbrella", "radiator", "kitchen", "smartphone"]
    word = random.choice(words)
    return word


word =  words()
print (f"{word}\n{len(word)}")


# reading the CSV file
csvFile = pandas.read_csv('Giants.csv')

# displaying the contents of the CSV file
print(csvFile)