import os
import random

list_word = []
list_result = []
hangman_pics = ['''  +---+
  |   |
      |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def clear_screen(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def screen_clean(a):
    menu = """
         ¡Bienvenido al juego del Ahorcado!
Adivina la palabra antes de que se ahorque el hombresito

"""
    clear_screen()
    print(menu)
    print(hangman_pics[a] + "\n")
    print(" ".join(list_result) + "\n")

def read():
    word = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            word.append(line.strip())
    return word


def run():
    word = random.choice(read())
    raw_word = word.maketrans('áéíóú', 'aeiou')
    word = word.translate(raw_word)
    counter = 0

    # Inicialiso listas
    for letter in word:
        list_word.append(letter)
        list_result.append("_")

    screen_clean(counter)
    letter_user = input("Escribe una letra: ")
    

    # Actualizo el resultado con las letras que da el usuario
    while list_result != list_word and counter < 6:
        if letter_user in list_word:
            for index, letter in enumerate(list_word):
                if letter == letter_user:
                    list_result[index] = letter_user
            if list_result != list_word:
                screen_clean(counter)
                letter_user = input("Bien! Elige otra letra: ")
            else:
                break
        else:
            counter += 1
            screen_clean(counter)
            if counter <= 5:
                letter_user = input("Ups! No estaba! Elige otra letra: ")
            
    if counter == 6:
        screen_clean(counter)
        print("Perdiste! el hombresito se ahorcó!")
    else:
        screen_clean(counter)
        print("Ganaste!")


if __name__ == "__main__":
    run()