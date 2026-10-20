print("===POWER CALCULATOR===")
num=int(input("Enter a number :  "))
power=int(input("Enter a power(Exponent):  "))

result=1

for i in range(1, power+1):
    result= result*num
    print("Step"+ str(i) +" Result= "+ str(result))

print("Answer: "+ str(num) + " to the power "+str(power)+" = ", str(result))