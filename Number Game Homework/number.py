import random
number= random.randint(1, 50)
print("Welcome to The Number Guessing Game!")
print("I have chose a number between 1 to 50. You have 5 chances to guess it!")
guess=int(input("Enter a number: "))
lives=5
while guess != number:
    guess=int(input("Enter a number: "))
    if guess != number:
        if guess < number:
            print("🧊 ice cold! You are really far.")
        elif guess > number:
            print("🥶 cold! Just a little far.")
        else:
            print("🔥 warm! Really close!")
        lives-=1
        print("Lives Left: ", end="")
        print("💗"*lives)
    if lives==0:
            print("You Lost! The Correct number is "+ str(number) +"!")
    if guess == number:
        print("Well Done! You have guessed the number!")


