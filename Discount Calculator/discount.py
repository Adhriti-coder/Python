print("===Welcome to the Shopping Discount Calculator!===")
valid = False
while not valid:
    try:
        bill=float(input("Enter the bill amount: "))
        discount=float(input("Enter the discount: "))
        people= int(input("Enter the number of people: "))
        discount_amount = bill * discount / 100
        final_bill = bill - discount_amount
        money_per_person = final_bill / people
    except ValueError:
        print("There is a value error - Please enter numbers only!")
    except ZeroDivisionError:
        print("error - The number of people cannot be 0!")
    else:
        print()
        print("FINAL BILL")
        print("Bill : ", bill)
        print("Discount : ", discount)
        print("Final Bill : ", final_bill)
        print("Each Person Pays: ", money_per_person)
        valid = True
    finally:
        print("Attempt Finished.")
        print()
