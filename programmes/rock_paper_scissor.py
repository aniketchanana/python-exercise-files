print("...rock...")
print("...paper...")
print("...scissor...")

player1 = input("Player 1 enter your move ")
player2 = input("Player 2 enter your move ")

if player1 != player2 and player1 and player2:
    if player1 == "scissor" and player2 == "paper" :
        print("player 1 is winner")
    elif player1 == "paper" and player2 == "rock" :
        print("player 1 is winner")
    elif player1 == "rock" and player2 == "scissor" :
        print("player 1 is winner")
    else :
        print("player 2 is winner")
elif player1 == player2 :
    print("it is a tie")
else :
    print("Something went wrong")