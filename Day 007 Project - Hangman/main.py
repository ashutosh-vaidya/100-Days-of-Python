import random
from hangman_words import word_list
from hangman_art import logo, stages

game_over = False
lives = 6

#Print the hangman logo
print(logo)

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list);
chosen_word__length = len(chosen_word)

#Show the blanks equal to length of the chosen worlda
display = []
for _ in range(chosen_word__length):
    display += "_"
#print(display)
print(f"{' '.join(display)}")


while not game_over:
    print()
    #Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess the letter: ").lower();
    #Check if user have entered alreadyed gusessed letter
    if guess in display:
        print(f"You have already guessed the letter {guess}")

    #Check if the letter the user guessed (guess) is one of the letters in the chosen_word. And if it is a match then replace the "_" with letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")    

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Congrats, You have guseed the correct Word. You win!!!")

    #if used guessed incorrectly than dock one life
    if guess not in chosen_word:
        lives -= 1        
        print(f"Your guessed letter {guess} is not in the word. You lose a life. Lives remaining {lives}")
        if lives == 0:       
            print("-"*10)     
            print("All lives used, you lose.")
            print(f"The word was = {chosen_word}")
            print("GAME OVER")
            game_over = True

    #print hangman        
    print(stages[lives])