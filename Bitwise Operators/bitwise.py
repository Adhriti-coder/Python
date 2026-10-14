#bitwise operators works directly on bits rather than treating the #number as 1 whole value.
#left shift multiplies the number by 2
#right shift divides the number by 2
#>> is used for right shift
#<< is used for left shift
a=10
b=-10
print("A right shift on a will result into ", a >> 2)
print("A right shift on b will result into ", b >> 1)
print("A left shift on a will result into ", a << 3)
print("A left shift on b will result into ", b << 3)
#^ is the symbol for xor
print(a ^ b)