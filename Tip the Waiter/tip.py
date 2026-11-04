#Let's create a function total_calc() that helps us calculate and #print out the total amount paid at a restaurant. Given a bill amount #and the percentage of the bill amount you decide to pay us a tip #(tip_perc ), this function calculates the total amount you should pay.
bill_amount=float(input("Enter the total bill in dollars: "))
tip=float(input("Enter the tip you want to pay: "))

def total_calc(bill, tip):
    """This function calculates the total bill"""
    total= bill + tip / 100 * bill
    return total

value=total_calc(bill_amount, tip)
print(total_calc.__doc__)
print("The final amount is ", value)

