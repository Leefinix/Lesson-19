import random
print("RoPaSi")
print("Your going to play Rock Paper Scissors with a computer.")
options = ["Rock", "Paper", "Scissors"]
user_choice = input("Enter Rock, Paper, or Scissors!\n")
computer_choice = random.choice(options)

print("You chose:", user_choice)
print("The Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a Tie!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("You Win! Rock smashes Scissors.")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You Win! Paper covers Rock.")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("You Win! Scissors cuts Paper.")
else:
    print("You Lose!")