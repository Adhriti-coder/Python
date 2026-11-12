import random
num = random.randint(1, 20)
print("Guess the random number!")
user = 0
chances = 5
while user != num:
    try:
        user = int(input("Your guess: "))
    except ValueError:
        print("Error - Please enter numbers only!")
    if num == user:
        print("Well done! You have guessed the number!")
    else:
        print("Wrong number! Try again!")
        chances-=1
        print("Chances left: ", chances)
    if chances == 0:
        print("You lost! The number was ", num)