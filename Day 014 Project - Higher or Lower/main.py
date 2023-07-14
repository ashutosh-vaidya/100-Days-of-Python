#importing
from game_data import data
from art import logo,vs
import random
import os

# Generate a random account from the game data.
def get_random_account():
    return random.choice(data)

# Format account data into printable format.
def format_account(account):
    name = account["name"]
    description = account["description"]
    country = account["country"] 
    return f"{name}, {description}, from {country}"

# Ask user for a guess.
# def guess_answer(account_a, account_b):
    
#     return input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct.
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()
    
    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()
        
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_account(account_a)}.")
        print(vs)
        print(f"Against B: {format_account(account_b)}.")

        ## Get follower count.
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
    
        # Ask user for a guess.
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
        is_guess_correct = check_answer(guess, a_follower_count, b_follower_count)
    
        os.system('cls') #Used to clear the console in VS Code, based on IDE it can be diff.
    
        print(logo)
        if is_guess_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

#start
game()