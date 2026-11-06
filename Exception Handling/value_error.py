try:
    num=int(input("Enter a number: "))
    print(num)
except ValueError as e:
    print(e)