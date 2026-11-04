#Define a function to find a cube and define another function which let execute the cube function if #the number is divisible by 3
num= int(input("Enter a number: "))
def cube(n):
    num_cube= n*n*n
    return num_cube

def divisible(n):
    if n % 3 == 0:
        return cube(n)
    else:
        return None

print(divisible(num))