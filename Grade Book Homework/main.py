students = {"Adhriti" : 98, "Aaradhya" : 94, "Avanshika" : 90, "Aarvi" : 97, "Aniya" : 88}          
print(students)
total = 0
for key,value in students.items():
    total += value

average = total / 5
print("Average marks : ", average)

highest = 0
for h in students:
    if students[h] > highest:
        highest = students[h]
print("Highest : ", highest)

lowest = 0
for l in students:
    if students[l] < lowest:
        lowest = students[l]
print("Lowest : ", lowest)

student_name = input("Enter a name of a student : ")
if student_name not in students:
    print("That student is not available!")
print("Score : ", students.get(student_name, "Not Found"))

    



