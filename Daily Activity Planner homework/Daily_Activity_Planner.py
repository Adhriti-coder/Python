homework_time=int(input("Homework time in minutes: "))
if homework_time > 60 :
    print("That is a long homework session!")
else:
    print("That is a short homework session!")
free_time=input("Is there free time after homework? (yes/no): ").lower()
if free_time=="yes":
    freetime_="yes"
    plan="Start homework now"
    print("Reminder: Choose a hobby for free time!")
else:
    freetime_="no"
    plan="Finish homework quickly"

print("=====DAILY ACTIVITY PLANNER=====")
print("Homework minutes  :", homework_time)
print("Plan  :", plan)
print("Free Time  :", freetime_)