import os

def bid_winner(bids):
    highest = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > highest:
            highest = bids[bidder]
            winner = bidder
    print(f"The highest bid is {highest} and winner of the bid is {winner}.")

bids = {}
is_bidding_finished = False

while not is_bidding_finished:
    bidder = input("Enter the name of a bidder: ")
    price = int(input("Enter the bidding price: $"))

    bids[bidder] = price
    #print(bids)

    response = input("Type 'yes' if there are more bidder else type `no`: ").lower()
    if response == 'yes':
        os.system('cls')
    elif response == 'no':
        is_bidding_finished = True
    else:
        print("Invalid command, considering the bidding is completed.")
        is_bidding_finished = True

bid_winner(bids)