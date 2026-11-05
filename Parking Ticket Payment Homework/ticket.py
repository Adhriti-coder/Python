print("===WELCOME TO THE PARKING TICKET PAYMENT===")
print()
cost_of_ticket= 30
print(f"The price of the ticket is Rs. {cost_of_ticket}. ")
print("The Accepted coins are 1, 5, 10 and 25.")
print()
inserted_coins=0
total_coins=0

while True:
    coin=int(input("Insert a coin(1, 5, 10, 25): "))
    if coin not in (1, 5, 10, 25):
        print("Invalid coin. Please enter a valid coin and try again.")
        print()
        continue

    inserted_coins += 1
    total_coins += coin

    if total_coins >= cost_of_ticket:
        break

def calc_change(total, ticket):
    change = total - ticket
    return change
due_change= calc_change(total_coins, cost_of_ticket)
if due_change == 0:
    pass
else:
    print(f"Here's your change: Rs. {due_change}")

print()
print("===== YOUR PARKING TICKET =====")
print(f"Price of Ticket:  Rs.{cost_of_ticket}")
print(f"Coins Inserted: Rs.{inserted_coins}")
print(f"Total Paid: Rs.{total_coins}")
print(f"Change Given: Rs.{due_change}")
print()
print("Payment Complete, Enjoy your day ahead!")
print("="*40)

