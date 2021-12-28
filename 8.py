import random
x=random.randrange(1,100)
trial=0
print("Hello, I thought a number from 1 to 100, your task is to guess the number.\n Good luck")
while(1):
    a=input("Trial "+str(trial)+".Your number:")
    a=int(a)
    if a<x:
        print("Your number is smaller than mine, try again.")
    elif a>x:
        print("Your number is bigger than mine, try again.")
    else:
        break
    trial+=1
print("You guessed the number with "+str(trial)+" trial.")
print("Thanks for playing!!")