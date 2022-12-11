#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Explaination
#random.choices will return list of random elements from each list, 
#k specifies how many
#join will create a single string from the list, 
#appending each one gets us single easy level password.
easy_password = "".join(random.choices(letters, k = nr_letters)) + "".join(random.choices(symbols, k = nr_symbols)) + "".join(random.choices(numbers, k = nr_numbers))
print(f"Easy level password = {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Explaination
#Half of our work is already done in eariler steps so we will use easy_password directly
#First charcter of password should be always letter, hence we assign 0th element first
hard_password = easy_password[0]
split_password_list = []
#Then we will split the string from 1st element onwords and store in list
for i in range(1, len(easy_password)):
    split_password_list.append(easy_password[i])
#We will then use shuffle to change the order of element in the list
random.shuffle(split_password_list)
#and finally we will join the shuffled list and append it into hard_password
hard_password += "".join(split_password_list)
print(f"Hard level password = {hard_password}")