print("===GROCERY BILLING QUEUE===")
print()

low_cost_items=0
medium_cost_items=0
high_cost_items=0

customers_served=0
total_sales=0

billing=True

while billing:
    name=input("Enter your name: ")
    print()
    item_count=int(input(f"Hello, {name}! How many items do you want to buy?"))

    if item_count <=0:
        print("Invalid number. Please enter a positive number.")
        continue

    print(f"Billing items for {name}: ")
    customer_total=0
    item_number=1

    while item_number <= item_count:
        item_name=input("Enter item name: ")
        item_price=int(input("Enter item price: "))
        item_quantity=int(input("Enter quantity: "))
        print()

        if item_price <=0 or item_quantity <=0:
            print("Invalid Price or Quantity, please enter again.")
            print()
            continue

        item_total= item_price * item_quantity
        print(f"{item_name}: {item_quantity} x {item_price}= {item_total}")
        print()
        customer_total+=item_total
        if item_price < 50:
            low_cost_items += item_quantity
        elif item_price <= 100:
            medium_cost_items += item_quantity
        else:
            high_cost_items += item_quantity

        item_number += 1

        customers_served+=1
        total_sales+=customer_total

    print(f"Total bill for {name}: {customer_total}")
    print("Billing Complete!")

    next= input("Are there more customers?").lower()
    if next != "yes":
        billing=False

print("===Grocery Category Report===")

for slot in range(1, 4):

    if slot==1:
        label, total= "Low Price Items ", low_cost_items
    elif slot==2:
        label, total= "Medium Price Items ", medium_cost_items
    else:
        label, total= "High Price Items ", high_cost_items

    if total > 0:
        print(f"{label}: {total}", end=" ")

        for item in range(total):
            print("*", end="")

        print()

print(f"Customers Served: {customers_served}")
print(f"Total sales: {total_sales}")
print("Grocery Billing closed. Goodbye!")
            


