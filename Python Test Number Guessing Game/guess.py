import random
secret = random.randint(1, 50)
print("WELCOME TO THE NUMBER GUESSING GAME! You have 5 chances to guess the number!")
lives=5
guess=int(input("Enter a number: "))
while guess != secret:
    guess=int(input("Enter a number: "))
    if guess == secret:
        print("Well Done! You guessed the number!")
    else:
        if guess < secret:
          print("🧊")
        elif guess > secret:
          print("🥶")
        elif guess <= secret:
          print("🌡️")
        else:
          print("🔥")
        print("Wrong! Try Again!")
        lives-=1
        print("Lives left: ", end="")
        print("💗"*lives)
    if lives == 0:
        print("You lost! The number was ", lives)

