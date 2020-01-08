from random import randint
player_wins = 0
comp_wins = 0

while player_wins < 2 and comp_wins < 2 :
    print("--------------------------------------------------")
    print("...rock...")
    print("...paper...")
    print("...scissor...")


    rand_num = randint(0,2)
    player2 = input("Enter your move ").lower()

    if rand_num == 0 :
        player1 = "rock"
    elif rand_num == 1 :
        player1 = "paper"
    else :
        player1 = "scissor"

    print(f"computer = {player1}")
    print(f"player = {player2}")

    if player1 != player2 and player1 and player2:
        if player1 == "scissor" and player2 == "paper" :
            print("computer is winner")
        elif player1 == "paper" and player2 == "rock" :
            print("computer is winner")
        elif player1 == "rock" and player2 == "scissor" :
            print("computer is winner")
        else :
            print("player is winner")
            player_wins += player_wins
        comp_wins += 1
    elif player1 == player2 :
        print("it is a tie")
    else :
        print("Something went wrong")

# tenary operator in case of python
print("Player is a winner") if player_wins>comp_wins else print("comp is winner")