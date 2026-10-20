#Write a program to calculate the sum of whole numbers.
number=int(input("Enter a number: "))
sum=0
for c in range(1, number+1):
    print("sum= "+ str(sum) + " and c= "+ str(c))
    sum=sum+c
print(sum)