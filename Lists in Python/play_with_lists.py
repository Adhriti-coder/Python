#Write a Python program to find the sum and average of the list. The average of the list is defined as #the sum of the elements divided by the number of the elements. Also, find the largest and the smallest #number in the list.
a = [1, 5, 20, 12, 23]
total = 0
average = 0
for num in a:
    total = total + num
print("The total is ", total)
average = total / len(a)
print("The average is ", average)
a.sort()
print("The largest number is ", a[-1])
print("The smallest number is ", a[0])

