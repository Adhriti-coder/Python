print("="*30)
print("Homework Completion Tracker!")
print("="*30)
print()
total_homework=4
print(f"You have {total_homework} assignments to do!")

homework_num=1
homework_completed=0

while homework_num<=total_homework:
    if homework_num==1:
        homework="Maths worksheet"
    elif homework_num==2: 
        homework="Science reading"
    elif homework_num==3: 
        homework="English writing"
    else: 
        homework="Coding homework"

    
    complete=input(f"Have you completed the {homework}? ").lower()
    if complete=="yes":
        homework_completed+=1
        homework_num+=1
        print("Assignment Complete!")

    else:
        print("Complete the assignment fast and check again!")

    print("Assignments left: ", total_homework - homework_completed)
    print()

print("="*50)       
print("Well Done! You have completed all your Homework!")
print("="*50)


