#Write a program to show students’ grades by entering marks for five subjects, calculating the average, #and checking the grade range using membership operators in and not in. For example, use in to check #whether the average is in the range 91 to 100, 81 to 90, and so on, and use not in to validate marks #outside the allowed range.
maths=int(input("Marks for Maths:"))
english=int(input("Marks for english:"))
hindi=int(input("Marks for hindi:"))
science=int(input("Marks for science:"))
general_knowledge=int(input("Marks for GK:"))
total=maths + english + hindi + science + general_knowledge
print("Total marks: ", total)
average= total / 5
average=int(average)
print("Average: ", average )
if average in range(0 , 100):
    print("Valid Average")
else:
    print("Invalid Average")
if average in range(91 , 100):
    print("A1")
elif average in range(81 , 90):
    print("A2")
elif average in range(71 , 80):
    print("B")
elif average in range(61 , 70):
    print("C")
elif average in range(51 , 60):
    print("D")
else:
    print("Fail")
