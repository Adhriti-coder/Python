print("=== STUDENT SUBJECT RECORD CLEANER ===")
student_details = {"5401" : 
                   {"Name" : "Aaradhya", "Class" : "V", "Subject" : "English, math, science" },
                   "5403" :
                   {"Name" : "Aarvi", "Class" : "V", "Subject" : "English, math, science" },
                   "5406":
                   {"Name" : "Aarvi", "Class" : "V", "Subject" : "English, math, science" },
                   "5410":
                   {"Name" : "Adhriti", "Class" : "V", "Subject" : "English, math, science" }}
print()
print("Original Student Details: ")
print(student_details)
print()
print("Details of 5401: ")
print(student_details.get("5401", "Not Found"))
print("Details of 5411: ")
print(student_details.get("5411", "Not Found"))
print()
student_details["5411"]={
    "Name" : "Dakshita",
    "Class" : "V",
    "Subject" : "English, math, science"
}
print("After adding 1 more student: ")
print(student_details)
print()
student_details["5403"]["Subject"]="English, coding, science"
print("After updating 5403's subject: ")
print(student_details["5403"])
print()

cleaned_data = {}
new_list = []
for student_id,details in student_details.items():
    unique_key=(details["Name"], details["Class"], details["Subject"])
    if unique_key not in new_list:
        new_list.append(unique_key)
        cleaned_data[student_id]=details
student_details = cleaned_data
print("After removing duplicate details: ")
print(student_details)
print()
removed_student = student_details.pop("5401", "Not Found")
print("Removed Student: ")
print(removed_student)
print()
print("Total student details left: ", len(student_details))
print()
print("=== FINAL STUDENTS SUBJECT RECORDS ===")
for student_id,details in student_details.items():
    print(student_id, ":", details)
print("=====================================================")


                   
                   
