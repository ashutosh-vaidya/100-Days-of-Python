rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
compChoice = random.randint(0,2)

if userChoice == 0:
    print(f"You choose, {rock}")
    if compChoice == 0:
        print(f"Computer choose, {rock}")
        print("Its a draw!")
    elif compChoice == 1:
        print(f"Computer choose, {paper}")
        print("Winner is Computer!")
    else:
        print(f"Computer choose, {scissors}")
        print("You are a Wineer!")

elif userChoice == 1:
    print(f"You choose, {paper}")
    if compChoice == 0:
        print(f"Computer choose, {rock}")
        print("You are a Wineer!")
    elif compChoice == 1:
        print(f"Computer choose, {paper}")
        print("Its a draw!")
    else:
        print(f"Computer choose, {scissors}")
        print("Winner is Computer!")

elif userChoice == 2:
    print(f"You choose, {scissors}")
    if compChoice == 0:
        print(f"Computer choose, {rock}")        
        print("Winner is Computer!")
    elif compChoice == 1:
        print(f"Computer choose, {paper}")        
        print("You are a Wineer!")
    else:
        print(f"Computer choose, {scissors}")        
        print("Its a draw!")
else:
    print("Invalid Choice")



