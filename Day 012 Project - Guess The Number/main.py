import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def set_difficulty():
    '''
    This function will ask the player to choose from easy or hard difficulty
    If player chose hard, they will have 5 turns to guess the correct number
    If player chose easy, they will have 10 turns to guess the correct number
    '''
    global turns
    difficulty = input(f"Choose your difficulty, 'easy' or 'hard': ").lower()
    print(f"You chose {difficulty} difficulty.")
    if difficulty == "easy":
        turns = EASY_LEVEL_TURNS
    else:
        turns = HARD_LEVEL_TURNS

def check_the_answer(guess, random_number, turns):
    '''
    Checks the random_number agains the guessed number.
    If player has guessed wrong reduced the turn by 1.
    Prints Too High or Too low based on comparision betwenn the numbers.
    '''
    if guess > random_number:
        print("Too High")
        return turns - 1
    elif guess < random_number:
        print("Too Low")
        return turns -1
    else:
        print("Congrats! You guessed correct number")

def start_game():
    global turns
    random_number = random.randint(1,100)
    guessed_number = 0
    
    set_difficulty() #This will set the global variable turns

    while guessed_number != random_number:
        print(f"You have {turns} attempts to guess the correct number.")
        guessed_number = int(input("Guess the number: "))
        # Check and reduce the turns by 1 if player gets wrong number
        turns = check_the_answer(guessed_number, random_number, turns)
        if turns == 0:
            print("You exhausted all the attempts. You lose.")
            return
        elif guessed_number != random_number:
            print("Guess Again: ")

#Starting point
start_game()


#old code
# difficulty = input(f"Choose your difficulty, 'easy' or 'hard': ").lower()
# if difficulty == "easy":
#     number_of_attempts = 10
# else:
#     number_of_attempts = 5
# print(f"You chose {difficulty} difficulty.")
# print(f"You have {number_of_attempts} to guess the correct number.")
# guessed_number = int(input("Guess the number: "))

# while number_of_attempts > 0:
#     if guessed_number == random_number:
#         print("Congrats! You guessed correct number")
#         break
#     elif guessed_number > random_number:
#         print("Too High")
#         number_of_attempts -= 1
#     elif guessed_number < random_number:
#         print("Too Low")
#         number_of_attempts -= 1

#     print(f"Number of attempts left {number_of_attempts}")
#     if number_of_attempts != 0:
#         guessed_number = int(input("Guess Again: "))
#     else:
#         print("You exhausted all the attempts. You lose.")
