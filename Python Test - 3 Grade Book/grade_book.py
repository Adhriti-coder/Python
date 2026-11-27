students = {"Adhriti" : 98, "Aaradhya" : 94, "Avanshika" : 90, "Aarvi" : 97, "Aniya" : 88}          
print(students)
total = 0
for key,value in students.items():
    total += value

average = total / 5
print("Average marks : ", average)

highest = max(students.values)
print("Highest : ", highest)

lowest = min(students.values)
print("Lowest : ", lowest)

student_name = input("Enter a name of a student : ")
if student_name not in students.keys:
    print("That student is not available!")
print(students[student_name])

    



