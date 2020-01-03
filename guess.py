from random import randint

random_number = randint(1,10)

guess = None

while(guess != random_number) :
    guess = int(input("Pick a number from 1 to 10: "))
    if guess == random_number :
        print("YOU WON !!")
        play_again = input("Do you want to play again ? (Y/N) ").lower()
        if play_again == "y" :
            random_number = randint(1,10)
            guess = None
            continue
        else :
            print("Thank you for playing")
            break
    elif guess < random_number :
        print("Too low !!")
    else :
        print("Too high!!")