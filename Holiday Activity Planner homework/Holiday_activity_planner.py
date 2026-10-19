print("HOLIDAY ACTIVITY PLANNER")
print("Step-1: Pick your holiday type:")
print("1 For Beach Holiday")
print("2 For Mountain Holiday")
print()
vacation_place=int(input("Enter 1 or 2: "))

if vacation_place==1:
    print("Step-2: Pick your Beach Activity!")
    print("1 For Swimming")
    print("2 For Sandcastle Building")
    activity=int(input("Enter 1 or 2: "))
    print()
    if activity==1:
        print("You picked   :   Swimming")
        print("Best Time    :   Morning")
        print("Remember     :   Carry Sunscreen and Water")
    else:
        print("You picked   :   Sandcastle Building")
        print("Best Time    :   Evening")
        print("Remember     :   Carry a Bucket and Spade")

elif vacation_place==2:
    print("Step-2: Pick your Mountain Activity!")
    print("1 For Hiking")
    print("2 For Camping")
    activity_1=int(input("Enter 1 or 2: "))
    print()
    if activity_1==1:
        print("You picked   :   Hiking")
        print("Best for     :   Exploring Trails")
        print("Remember     :   Wear Comfortable Shoes")
    else:
        print("You picked   :   Camping")
        print("Best for     :   Staying close to nature")
        print("Remember     :   Carry a tent and flashlight")

else:
    print("Invalid input")
    print("Please enter 1 for Beach Holiday and 2 for Mountain Holiday.")

print("="*35)
print("Your holiday activity planner is ready!")
print("Enjoy your holiday!")
print("="*35)