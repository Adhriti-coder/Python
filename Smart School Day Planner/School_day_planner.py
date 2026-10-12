# Smart School Day Planner

print("=== Smart School Day Planner ===")
print("Answer 3 quick questions and I will plan your day!\n")
day=input("Enter the day: (Monday to Sunday)").strip().capitalize()
weather=input("Enter the weather(sunny, rainy or cloudy)").strip().lower()
homework=input("Is your homework not done? Yes or no?").strip().lower()

print()
print(f"=== Your Plan for {day} ===")
print("-" * 35)
if day in("SATURDAY","SUNDAY"):
    print("It's the weekend, enjoy your free time!")
elif day=="MONDAY":
    print("It's the start of the week, get your planner ready!")
elif day=="FRIDAY":
    print("It's Friday, return your library books!")
elif day in ("TUESDAY","WEDNESDAY","THURSDAY"):
    print("It's a regular weekday, stay focused!")
if weather=="sunny" and homework=="yes":
    print("Complete your homework in the park!")
elif weather in("rainy","cloudy"):
    print("Take an umbrella with you!")
elif not homework=="yes":
    print("Do your homework before you step out!")
elif not homework=="yes" and weather in("rainy","cloudy"):
    print("You are not allowed to step outside.")
elif weather=="sunny" and homework=="yes" and day in("SATURDAY","SUNDAY"):
    print("Do your homework in the park!")
else:
    print("Plan complete! Have a nice day!")