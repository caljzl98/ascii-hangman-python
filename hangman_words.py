'''
reads each line of a text file, and adds contents of each line into a list

Parameters:
filename (string): directory to text file
list (list): a list to append the contents of 'filename'
'''
def read_append(filename, list):
   with open(filename, "r") as file:
      for line in file:
         list.append(line.lower().strip())

animal_list = []
read_append("word_bank/animals.txt", animal_list)

fruit_list = []
read_append("word_bank/fruits.txt", fruit_list)

vegetable_list = []
read_append("word_bank/vegetables.txt", vegetable_list)

all_list = fruit_list + vegetable_list + animal_list