def greet_customer():
    print("Welcome, I am Adhriti!")
    print("I am Learning Python!")

greet_customer()

price=float(input("Enter the price of 1 cup of Ice Cream in dollars: "))
cups=int(input("Enter the number of cups: "))


def calculate(p, c):

    total=p * c
    return total

 
value=calculate(price, cups)
print("The total is ", value)

def check_cups(cups):
    if cups > 5:
        print("Thank you for buying!")
    else:
        print("We Hope you buy from us again!")
check_cups(cups)

    


