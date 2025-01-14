import random
top_of_range=input("enter top the range number ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("please try enter number greater than zero next time ")
        quit()
else:
    print("type a number next time")
    quit()
random_number=random.randint(0,top_of_range)
guesses=0
while True:
    guesses+=1
    user_guess=input("make a guess!: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("try entering a number next time")
        continue
    if user_guess==random_number:
        print("you got it")
        break
    elif user_guess > random_number:
        print("you were above the number")
    else:
        print("you were below the number")
print("you get it in",guesses,"guesses")
