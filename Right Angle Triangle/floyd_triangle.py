rows=int(input("Enter the number of rows: "))
count=1
for i in range(1, rows+1):
    for col in range(1, i+1):
        print(count, end=" ")
        count+=1
    print()