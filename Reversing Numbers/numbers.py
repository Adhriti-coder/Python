#Write a program to print the numbers in reverse order beginning from #the number entered by the user.
number=int(input("Enter a number: "))
for i in range(number, 0, -1):
    print(i)