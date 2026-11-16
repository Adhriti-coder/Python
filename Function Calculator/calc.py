import math
print("FUNCTION CALCULATOR")
print()
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
try:
    operation = input("Enter the operation(+, -, *, /): ")
    print()
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    print()
    if operation == "+":
        print("Sum: ", add(num1, num2))
    elif operation == "-":
        print("Difference: ", min(num1, num2))
    elif operation == "*":
        print("Product: ", mult(num1, num2))
    else:
        print("Quotient: ", div(num1, num2))
except ValueError:
    print("Error- Please enter numbers only!")
except ZeroDivisionError:
    print("Error- You can't enter 0!")
finally:
    print()
    print("Thank You for using Function Calculator!")
    print("===============================================================")

    
