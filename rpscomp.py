from random import randint

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
        print("player is winner")
    elif player1 == "paper" and player2 == "rock" :
        print("player is winner")
    elif player1 == "rock" and player2 == "scissor" :
        print("player is winner")
    else :
        print("Computer is winner")
elif player1 == player2 :
    print("it is a tie")
else :
    print("Something went wrong")
