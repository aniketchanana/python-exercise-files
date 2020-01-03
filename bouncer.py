age = input("How old are you")

if age :
    age = int(age)
    if age >= 18 and age < 21 :
        print("Need a wrist band")
    elif age>=21 :
        print("you can enter and drink")
    else :
        print("too little to enter")
else :
    print("Input is empty")
