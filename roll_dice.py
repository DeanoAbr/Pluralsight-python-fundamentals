import random

roll = random.randint(1,6)

print ("The computer rolled a " + str(roll))

guess = int(input("Guess the dice roll:\n"))

if roll == guess:
    print("Nice guess :D, they rolled a " + str(roll))
else:
    print("Unlucky, they rolled a " + str(roll) +  " try again")