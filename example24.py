# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player
# plays (using input), compare them, print out a message of
# congratulations to the winner, and ask if the players want to start a
# new game)

def is_play_valid(play):
    if play != 'rock' and play != 'paper' and play != 'scissors':
        return False
    else:
        return True

def play_game():
    p1 = input("Player 1, what are you playing?\n")
    while not is_play_valid(p1):
        p1 = input("Wrong play, please play again.\n")

    p2 = input("Player 2, what are you playing?\n")
    while not is_play_valid(p2):
        p2 = input("Wrong play, please play again.\n")

    # Game Logic
    if p1 == p2:
        print("Its a tie!")
    elif p1 == "rock":
        if p2 == 'scissors':
            print("Player 1 wins")
        else:
            print("Player 2 wins")
    elif p1 == "paper":
        if p2 == "rock":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
    else:
        if p2 == 'paper':
            print("Player 1 wins")
        else:
            print("Player 2 wins")

    ans = input("Do you want to start a new game?\n")
    if ans == 'yes':
        print("Starting a new game")
        play_game()

play_game()