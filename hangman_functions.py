'''
Initialized answer with the amount of blanks ("_") equal to the length of the word
chosen fron the word bank.
@ Parameters:
hangmanWord (string): word chosen from the word bank
answer (list): an empty list
'''
def initialize_game(hangmanWord, answer):
   for char in hangmanWord:
      answer.append("_")

'''
Prints to console/terminal the blanks ("_") and guessed letter of hangmanWord
@ Parameters:
answer (list): a list containing the correct gueses from user and blanks ("_")
''' 
def print_display(answer):
   display = ""
   for letter in answer:
      display += letter + " "
   print(display + "\n")

'''
Checks whether the game has ended or not.
@ Parameters:
answer (list): a list containing the correct gueses from user and blanks ("_")
playerLives (int): the number of player's current available lives
'''
def is_end(answer, playerLives):
   # if there are blanks, and player still has available lives, game is still on!
   if "_" in answer and playerLives > 0:
      return False
   return True
'''
Checks if the string in an ASCII encoded letter
@ Parameters:
str (string): user input string
'''
def is_letter(str):
   return True if str.encode('ascii').isalpha() else False