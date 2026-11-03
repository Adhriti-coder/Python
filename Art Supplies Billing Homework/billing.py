def greeting():
    print("Welcome to the Art Supplies Store!")
    print("Get your, brushes, colours and paper!")
    print()

greeting()

cost_per_item=float(input("Enter the cost of 1 art supply in dollars: "))
items_bought=int(input("Enter the number of supplies: "))

def calculate(cost, items):
    total= cost * items
    return total
total_cost= calculate(cost_per_item, items_bought)

rounded_total= round(total_cost, 2)
print()
print("Total cost: ", rounded_total)

amount_paid= float(input("Enter the amount paid by the customer: "))
def calculate_change(paid, total):
    change = paid - total
    return change

change_due= calculate_change(amount_paid, rounded_total)
change_rounded= round(change_due, 2)

def thank_you(items):
    if items >= 5:
        return "Wow! You bought many supplies for your project! Thanks for shopping with us!"
    else:
        return "Thank you for shopping at our store!"

closing_message= thank_you(items_bought)

print()
print("===== ART SUPPLIES SHOPPING BILL =====")
print("Price per item: ", cost_per_item)
print("Number of items bought: ", items_bought)
print("Total cost: ", rounded_total)
print("Amount paid: ", amount_paid)
print("Change due: ", change_due)
print()
print(closing_message)
print("=" * 100)