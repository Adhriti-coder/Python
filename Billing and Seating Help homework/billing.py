def total_bill(bill_amount, tip_perc):
    total= bill_amount * (1 + 0.01 * tip_perc)
    total= round(total, 2)
    print(f"Please pay ${total}")
    return total

total_bill(150, 20)

def seating(guests):
    """This function finds the seating arrangements for guests!"""
    if guests==0 or guests==1:
        return 1
    else:
        return guests * seating(guests - 1)

print()
print(seating.__doc__)
print()
print("Seating arrangement for 1 guest: ", seating(1))
print("Seating arrangement for 2 guests: ", seating(2))
print("Seating arrangement for 3 guests: ", seating(3))
print("Seating arrangement for 4 guests: ", seating(4))
print("Seating arrangement for 5 guests: ", seating(5))
