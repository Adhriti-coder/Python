#A Python program that prints a welcome banner. It asks you to pick a #vehicle — Bike or Car. It uses a nested if-else inside each branch to #ask for a specific model. It prints the name, top speed or seats, and #best use case for the chosen model. It handles invalid input with an #else at the outer level. It closes with a goodbye message.
print("="* 20)
print("CUSTOM RIDE BUILDER")
print("="* 20)
print("Step 1: Pick your vehicle")
print("  1 - Bike")
print("  2 - Car")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice==1:
    # Nested if-else — runs only when choice is 1
    print("Step 2: Pick your bike type")
    print("  1 - Scooty")
    print("  2 - Mountain Bike")
    print()
    model=int(input("Enter 1 or 2: "))
    if model==1:
        print("You picked  : Scooty")
        print("Top speed   : 80 km/h")
        print("Best for    : City roads")
    else:
        print("You picked  : Mountain Bike")
        print("Top speed   : 40 km/h")
        print("Best for    : Off-road trails")
else:
    model=int(input("Enter 1 for Sedan, Enter 2 for SUV: "))

    if model==1:
        print("You picked:  Sedan!")
    else:
        print("You picked:  SUV!")

        