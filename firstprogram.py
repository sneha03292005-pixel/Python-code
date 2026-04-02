print("welcom to the ticket center")
height=int(input("enter the number"))

if height>=120:
    print("you can go to the next step")
    age=int(input("what is your age"))
    if age>=18:
        print("you can play the game")
    else:
        print("Sorry your below 18 you can't play the game ")
else:
    print(" Sorry you can't play the game")