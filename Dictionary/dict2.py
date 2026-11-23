#Write a program to check the frequency of a value in a dictionary - {'Codingal' : 2, 'is' : 2, 'best' #: 2, 'for' : 2, 'Coding' : 1}.
Dict1 = {"Codingal" : 2, "is" : 2, "best" : 2, "for" : 2, "coding" : 1}
count = 0
for key,value in Dict1.items():
    if value == 2:
        count += 1
print(count)
print(Dict1.get("in", "Not found"))