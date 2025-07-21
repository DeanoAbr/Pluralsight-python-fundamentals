import random

computer_choice = random.choice(["rock","paper","scissors"])
user_choice = input("Do you want rock, paper or scissors? ")

print("Computer Choice: ", computer_choice)

if computer_choice == user_choice:
   print ("It's a draw")
elif user_choice == "rock" and computer_choice == "scissors":
   print ("you win")
elif user_choice == "paper" and computer_choice == "rock":
   print ("you win")
elif user_choice == "scissors" and computer_choice == "paper":
   print ("you win")
else:
   print ("You lose, the computer wins")