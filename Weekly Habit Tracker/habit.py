print("== WEEKLY HABIT TRACKER ==")
print()

habit = ("Drawing", True, 20, 34.9)
print(habit)

weekly_habits = (1, 1, 0, 1, 0, 0, 1)
print(weekly_habits)
print()

print("Total days tracked : ", len(weekly_habits))
print()

print("Day 1 status : ", weekly_habits[0])
print("Day 4 status : ", weekly_habits[3])
print("First 3 days status : ", weekly_habits[0:3])
print("Weekend days status : ", weekly_habits[5:7])
print()

weekly_habits = weekly_habits + (1,)
print("After adding another day : ", weekly_habits)
print()

completed = 0
missed = 0

for i in range(0, len(weekly_habits)):
    if weekly_habits[i] == 1:
        completed += 1
    else:
        missed += 1
if completed > missed :
    print("You did a great job!")
    print()
else:
    print("You should be more consistent!")
    print()

print("===== WEEKLY HABIT TRACKER =====")
print("Habit         : ", habit[0])
print("Weekly Record : ", weekly_habits)
print("Completed     : ", completed)
print("Missed        : ", missed)
print("================================")

