#Create a tuple named weather with these elements - (1, 0, 0, 0, 1, 1, 0). If the element is 1 then #the value of rainy increases by 1 otherwise the value of sunny increases by 1. On the basis of the #value of rainy and sunny, predict the weather.
weather = (1, 0, 0, 0, 1, 1, 0)
rainy = 0
sunny = 0
for i in weather:
    if i == 1:
        rainy += 1
    else:
        sunny += 1 
#rainy = weather.count(1)
#sunny = weather.count(0)
print("Chances of rainy: ", rainy)
print("Chances of sunny: ", sunny)