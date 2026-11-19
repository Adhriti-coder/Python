#Write a program to perform the following operations: 1. Create a #tuple with different datatypes 2. Create another tuple of integers 3. #Create a new tuple by adding 9 to the previous tuple 4. Count the #occurrences of an element in the tuple 5. Perform slicing on the tuple
a = (20, "Hello", True, 43.5)
print(a)

b = (1, 10, 20)
print(b)

b = b + (9,)
print(b)

c = (1, 2, 2, 2, 3, 2, 1)
print("The number of 2s in the Tuple is ", c.count(2))

print(c[2:7])