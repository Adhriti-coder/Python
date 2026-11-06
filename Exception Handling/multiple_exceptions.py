try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter another number: "))
    value = num1 / num2
    print(value)
except ValueError:
    print("there has been a value error - you have not entered an integer value")
except ZeroDivisionError:
    print("A number can never be divided by zero")
except Exception as e:
    print("Error ",e)
else:
    print("The answer was evaluated with no errors ")
finally:
    print("Thank you!")