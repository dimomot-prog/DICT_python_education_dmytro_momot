print("HANGMAN")
print("The hame will be available soon.")

print("HANGMAN")
secret_word = "python"

user_guess =input("Guess the word: > ")

if user_guess == secret_word:
    print("You survived!")
else:
    print("You lost")
import random

print("HANGMAN")
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)

user_guess =input("Guess the word: > ")
if user_guess == secret_word:
    print("You survived!")
else:
   print("You lost")
import random
print("HANGMAN")
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)

hint = secret_word[:3] + '-' * (len(secret_word) - 3)

user_guess =input("Guess the word {hint}: > ")

if user_guess == secret_word:
    print("You survived!")
else:
    print("You lost")
import random

print("HANGMAN")

words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)

guessed_letters = set()
attempts = 8

while attempts > 0:
    display_word = "".join([letter if letter in guessed_letters else "-" for letter in secret_word])
    print(display_word)

    if "-" in display_word:
        break
letter = input("Input a letter: > ")

if letter in secret_word:
   if letter in guessed_letters:
         attempts -= 1
   else:
       guessed_letters.add(letter)
else:
    print("That letter doesn't appear in this word!")
    guessed_letters.add(letter)
    attempts -= 1

print("Thanks for playing!")
print("We'll see how well you did in the next stage")
import random

print("HANGMAN")
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)

guessed_letters = set()
attempts = 8

while attempts > 0:
    display_word = "".join([letter if letter in guessed_letters else "-" for letter in secret_word])
    print(display_word)

    if "-" not in display_word:
       print("You guessed the word!")
       print("You survived!")
       break
    letter = input("Input a letter: > ")

    if letter in secret_word:
        if letter in guessed_letters:
            print("No improvement")
            attempts -= 1
        else:
            guessed_letters.add(letter)
    else:
        print("That letter doesn't appear in this word!")
        attempts -= 1
if attempts == 0:
   print("You lost!")
import random

print("HANGMAN")

words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)

guessed_letters = set()
attempts = 8
while attempts > 0:
    display_word = "".join([letter if letter in guessed_letters else "-" for letter in secret_word])
    print(display_word)
    if "-" not in display_word:
        print(f"You guessed teh word {secret_word}")
        print("You survived!")
        break

    letter = input("Input a letter: > ")

    if len(letter) != 1:
       print("Please enter a lowercase English letter")
       continue
    if letter in secret_word:
       print("That letter doesn't appear in this word!")
       attempts -= 1
if attempts == 0:
   print("You lost!")

import random

def play_game():
    words = ['python', 'java', 'javascript', 'php']
    secret_word = random.choice(words)

    guessed_letters = set()
    attempts = 8

    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "-" for letter in secret_word])
        print(display_word)
        if "-" not in display_word:
            print(f"You guessed the word {secret_word}")
            print("You survived!")
            return
        letter = input("Input a letter: > ")
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if not (letter.isascii() and letter.islower() and letter.isalpha()):
            print("Please enter a lowercase English letter!")
            continue
        if letter in guessed_letters:
            print("You already guessed the letter")
            continue
        guessed_letters.add(letter)

        if letter in guessed_letters:
            print("That letter doesn't appear in the word!")
            attempts -= 1
    print("You lost!")

print("HANGMAN")
while True:
    action = input('Type "play" to play the game, "exit" to quit:>')
    if action == "play":
       print()
       play_game()
    elif action == "exit":
        break