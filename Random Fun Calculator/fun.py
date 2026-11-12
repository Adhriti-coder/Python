import random
import math
print("===== RANDOM FUN CALCULATOR =====")
lucky_number = random.randint(1, 10)
print()
print(f"Your lucky number is {lucky_number}!")
print()
fun_activity = ["Play a game","Draw something","Read a story","Solve a puzzle"]
random_activity = random.choice(fun_activity)
print(f"Random Activity For Today: {random_activity}")
print()
print("Guess the secret number from 1 to 5!")
num = random.randint(1, 5)
while True:
    guess = int(input("Enter your guess: "))
    if guess == num:
        print("Yay! You guessed the number!")
        break
    else:
        print("Wrong guess! Try again!")
print()
decimal = float(input("Enter a decimal number! "))
print(f"Ceilng value of {decimal}: {math.ceil(decimal)}")
print(f"Floor value of {decimal}: {math.floor(decimal)}")
print()
x= 10
y= -5
print(f"Copysign result: {math.copysign(x, y)}")
print()
negative_num= int(input("Enter a negative value: "))
print(f"Absolute Value: {math.fabs(negative_num)}")
print()
num1 = int(input("Enter the 1st number for GCD: "))
num2 = int(input("Enter the 2ns number for GCD: "))
print()
print(f"Greatest Common Divisor(GCD) of {num1} and {num2}: {math.gcd(num1, num2)}")
print()
print("===== FUN CALCULATOR SUMMARY! =====")
print("Lucky Number       :  ", lucky_number)
print("Random Activity    :  ", random_activity)
print("Secret Number      :  ", num)
print("===================================")