import random
playing = True
number = str(random.randint(1, 20))

print("I will generate a number between 1 to 20, and you have to guess the number!")
print("The game ends when u guess correctly.")

while playing:
    guess = input("Give me your best guess!\n")
    if number == guess:
        print("Wow!, You guessed correctly.")
        print("The number was ", number)
        break
    else:
        print("Your guess is wrong!, Try again")

