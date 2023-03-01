import random 
import os
import art

def deal_card():
    '''
    Returns the random card from the deck.
    This mimics the card dealing by the dealer
    '''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] # Ace = 11, and Jack, Queen and King = 10
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''
    Takes a list of cards and returns the calculated score from the cards
    Step 1: Check if the cards contains the BlackJack
            BlackJack will have sum = 21 and no of cards = 2
            If hand contains BlackJack return 0
    Step 2: If hand contains Ace but total goes over 21 then count ace as 1 instead.
    '''

    #check the blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    #Hand contains Ace and sum is more than 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(player_score, computer_score):
    '''
    Compares the player and computer score and deterimines the winner
    1. If Computer and Player score are equal, its a draw
    2. If Computer has BlackJack (Score = 0), computer wins
    3. Else If Player has BlackJack (Score = 0), player wins
    4. If Player score is more than 21, player loses
    5. If Computer Score is more than 21, computer loses
    6. If niether of above condition is meet than player who has highest score wins
    '''

    #result = ""
    #Player and Computer has same score
    if player_score == computer_score:        
        return "Its a Draw!!!"
    
    #Player or Computer has BlackJack
    if computer_score == 0:
        return "Computer has a BlackJack. Computer Wins!!!"
    elif player_score == 0:
        return "Congratulations, you have a blackjack. You Win!!!"
    
    #Player or computer has score more than 21
    if computer_score > 21 and player_score < 21:
        return "Congratulations, Computer has exceeded the score. You Win!!!"
    elif player_score > 21:
        return "Your have exceeded the score. You Lose!!!"
    
    #Highest score wins
    if computer_score > player_score:
        return "Computer has a more score than you, Computer Wins!!!"
    else:
        return "Congratulations, you have more score than computer. You Win!!!"
    
def play_game():
    print(art.logo)
    player_cards = []
    computer_cards = []
    is_game_over = False

    #deal player and computer 2 cards from the dec
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        #Calculate the score
        player_score = calculate_score(player_cards)        
        print(f"Your cards: {player_cards}, Current Score: {player_score}")

        computer_score = calculate_score(computer_cards)        
        print(f"Computer's first cards: {computer_cards[0]}")

        #if computer has BlackJack or Player has BlackJack or Player's score exceeds 21 game ends
        if computer_score == 0 or player_score == 0 or player_score > 21:
            is_game_over = True
        else:
            #Ask player if he wants another card or else game ends
            player_wants_card = input("Type 'y' to get another card, 'n' to pass:  ").lower()
            if player_wants_card == 'y':
                player_cards.append(deal_card())
                player_score = calculate_score(player_cards)
            else:
                is_game_over = True

    #Once the player is done, let computer play until it has score less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    #Print the final hands and final score
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    #compare and print the result
    print(compare_score(player_score, computer_score))

#Starting pointy
while input("DO you want to play game of BlackJack? Type 'y' or 'n': ").lower() == 'y':
    os.system('cls') #Used to clear the console in VS Code, based on IDE it can be diff.
    play_game()







