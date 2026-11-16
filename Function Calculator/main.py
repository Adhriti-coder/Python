import math
def add(n1, n2):
    addition = n1 + n2
    return addition

def min(n1, n2):
    minus = n1 - n2
    return minus

def mult(n1, n2):
    multiply = n1 * n2
    return multiply

def div(n1, n2):
    divide = n1 / n2
    return divide

print("FUNCTION CALCULATOR")
operation = input("Enter the operation you want to use(+, -, *, /): ")
try:
    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))
    result_add = add(num1, num2)
except ValueError:
    print("Error - Please enter numbers only!")
    
except ZeroDivisionError:
    print("Error - Can't enter 0!")

if operation == "+":
    print("Answer: ", add(num1, num2))

elif operation == "-":

    print("Answer: ", min(num1, num2))
elif operation == "*":
    print("Answer: ", mult(num1, num2))
else:
    print("Answer: ", div(num1, num2))
    
