print("WELCOME TO THE SNACK VENDING MACHINE!")
total_coins=0
coins_inserted=0
snack_price=float(input("Please enter the cost of this snack: "))
print("The accepted coins are- 1, 2, 5 and 10.")
while True:
    coin=int(input("Insert your coin: (1, 2, 5 or 10) "))
    if coin not in (1, 2, 5, 10):
        print("Invalid coin. Please insert a valid coin.")
        break
    coins_inserted += 1
    total_coins += coin
    if total_coins >= snack_price:
        break

def calc_change(total, snack):
    change_due= total - snack
    return change_due
if total_coins > 0 and snack_price > 0:
    value = calc_change(total_coins, snack_price)
    print("Here's your change: ", value)
print()
print("===PURCHASE SUMMARY===")
print("Snack Price: ", snack_price)
print("Coins Inserted: ", coins_inserted)
print("Total Paid: ", total_coins)
print("Change Given: ", value)
print("Thanks for your purchase!")