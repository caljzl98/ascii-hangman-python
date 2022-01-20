import random
from hangman_words import *
from hangman_art import *
from hangman_functions import *

# answer is a list that keeps track of user's answers
answer = []
# guessed is a set that keeps track of user's guesses
guessed = set()
playerLives = 6

# Simple ASCII UI
print(logo)
print("Welcome to the game of HANGMAN. Let us start the game.")
print('''
1. animals
2. fruits
3. asian vegetables
4. all of the above
''')

# prompt user input
category = input("Please type in the category number you wish to play: ")
# error guard for invalid inputs by user
while not category.isnumeric() or int(category) <= 0 or int(category) >= 5:
   category = input("Please type a positive integer number between 1 - 4: ")

# convert user string input to int
category = int(category)
if category == 1:
   hangmanWord = random.choice(animal_list)
elif category == 2:
   hangmanWord = random.choice(fruit_list)
elif category == 3:
   hangmanWord = random.choice(vegetable_list)
elif category == 4:
   hangmanWord = random.choice(all_list)


initialize_game(hangmanWord, answer)
print_display(answer)

# while game hasn't ended
while not is_end(answer, playerLives):
   # prompt user input
   while True:
      guess = input("Guess a letter: ").lower()
      # if guess is just an ASCII letter, move on
      if len(guess) == 1 and is_letter(guess):
         break

   # if user has guessed the letter before
   while guess in guessed:
      guess = input(f"You've guessed '{guess}' before. Guess another letter: ").lower()

   # guessed is a set that keep tracks of previously gueesed letters
   guessed.add(guess)

   # if guessed correctly
   for i in range(len(hangmanWord)):
      letter = hangmanWord[i]
      if letter == guess:
         answer[i] = guess

   # if guessed incorrectly
   if guess not in hangmanWord:
      playerLives -= 1

   print(playerStages[playerLives])
   print_display(answer)

# reached the end of game
if playerLives == 0:
   print(f"Game Over. The word is: {hangmanWord}")
else:
   print("Congrats! You have won the game.")