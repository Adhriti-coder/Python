rows=int(input("Enter the number of rows: "))
for i in range(rows,0, -1):
    for col in range(1, i+1):
        print("*", end=" ")
    print()