# 1) Import the `math` module to access built-in mathematical functions.
import math
# 2) Use `math.ceil()` and `math.floor()` on the number 23.56:
#    a) `math.ceil(23.56)` gives the smallest integer greater than or equal to 23.56.
#    b) `math.floor(23.56)` gives the largest integer less than or equal to 23.56.
#    c) Print both results in a single statement.
a=math.ceil(23.56)
b=math.floor(23.56)
print("The Floor and Ceiling value of 23.56 are: " + str(a)+ "," +str(b))

# 3) Create two variables:
#    a) `x = 10`
#    b) `y = -15`

x = 10
y = -15
#using copysign function

# 4) Use `math.copysign(x, y)` to copy the sign of `y` onto `x`:
#    a) Since `y` is negative, the returned value becomes -10.0.
#    b) Print the result.
print("The value of x after copying the sign from y is: " + str(math.copysign(x,y)))



# 5) Use `math.fabs()` to find absolute values:
#    a) `math.fabs(-96)` returns 96.0
#    b) `math.fabs(56)` returns 56.0
#    c) Print both absolute values.

print("Absolute value of -96 and 56 are: " + str(math.fabs(-96)) + ', ' + str(math.fabs(56)))


# 6) Use `math.gcd(24, 56)` to find the Greatest Common Divisor of 24 and 56.
#    Print the GCD result.

print("The Greatest Common Divisor of 24 and 56 is " + str(math.gcd(24, 56)))
