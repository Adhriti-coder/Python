#about_me = {"Name" : "Adhriti", 
#            "Age" : 11,
#            "School" : "Brighton"}
#print(about_me["Name"])

student_details = {"5406" : {"Name" : "Adhriti", "Class" : 5, "Subject_Taken" : "Maths, Science, English"}, 
                   "5407": {"Name" : "Angad", "Class" : 5, "Subject_Taken" : "Maths, English, Science"},
                   "5408" : {"Name" : "Aniya", "Class": 5, "Subject_Taken" : "Maths, Science, English"},
                   "6541": {"Name" : "Angad", "Class" : 5, "Subject_Taken" : "Maths, English, Science"}}
new_details={}
new_list=[]
for key,value in student_details.items():
    text = (value["Name"], value["Class"], value["Subject_Taken"])
    if text not in new_list:
        new_list.append(text)
        new_details[key]=value
for key,value in new_details.items():
    print(key)
    print(value)