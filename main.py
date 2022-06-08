#PassGenor Project

import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '_', '=', '~']

print("Welcome to the PassGenor! (v 1.0)")

optional = input("Would you like to include any names to your pass?\nType Y for yes or N for No (Please NOTE THAT THE NAME WILL BE SHUFFLED!)\n")
optional = optional.lower()

if optional == "y":
  password = input("Enter the name: ")
else:
  password = ""

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))


for char in range(1, num_letters + 1):
  
  rand_letter = random.choice(letters)
  password += rand_letter

for char in range(1, num_symbols + 1):
  rand_symbol = random.choice(symbols)
  password += rand_symbol

for char in range(1, num_numbers + 1):
  rand_number = random.choice(numbers)
  password += rand_number

visibility = input("Would you like to print each char individually? Y or N\n")
visibility = visibility.lower()

num_of_char = len(password) 
if visibility == "y":
  
  password = list(password)
  random.shuffle(password)
  print(f"{num_of_char} total chars")
  # print(len(f"{password}\n"))
  print(''.join(f"{password}\n"))
  print(''.join(password))
else:
  # print(len(f"{password}\n"))
  print(f"{num_of_char} total chars.")
  print(''.join(f"{password}\n"))


#AlanShami