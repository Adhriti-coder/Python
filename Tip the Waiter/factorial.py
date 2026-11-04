#Write a program to find the factorial using recursive function
def factorial(n):
    """This function finds the factorial"""
    if n==0 or n==1:
        return 1
    else:
        return ( n * factorial(n -1))
        
    
print(factorial.__doc__)
print("factorial of 1 is ",factorial(1))
print("factorial of 0 is ",factorial(0))
print("factorial of 3 is ",factorial(3))
print("factorial of 5 is ",factorial(5))
print("factorial of 4 is ",factorial(4))
print("factorial of 2 is ",factorial(2))
