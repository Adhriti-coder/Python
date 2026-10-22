
# PART 1: Set today's total number of chores (no list needed)
total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today!\n")

#A student wants to create a Python program called My Chore Checklist Countdown to keep track of the household chores they need to complete each day.
#The program is designed to manage four chores: Make your bed, Feed the pet, Take out the trash, and Wash the dishes.
'''
Write a Python program to meet the following requirements.

(a) Set the total number of chores to 4 and store the original number of chores in a separate variable. 
Display the total number of chores assigned for the day. [2]

(b) Initialise two variables:
- completed_count to store the number of chores completed.
- chore_num to identify the current chore, starting at 1. [2]
(c) Use a while loop to repeat the program while there are still chores to complete.
 Use if, elif and else statements to assign the correct chore name according to the current chore number. [5]
 (d) Ask the user whether they have completed the current chore by entering "yes" or "no".
- If the answer is "yes", increase completed_count by 1 and move to the next chore.
- Otherwise, display a message asking the user to finish the chore and check again. The program must not move to the next 
chore until the current chore is completed. [4]
(e) After each check, display the number of chores remaining. [2]

(f) When all four chores have been completed, display a congratulatory message confirming that the entire checklist is complete. [2]

(g) Demonstrate how an infinite loop can occur by creating a while loop with a condition that never becomes false. 
Use a safety counter and the break statement to stop the loop after three iterations. Display a warning explaining 
why the loop would otherwise continue indefinitely. [4]

(h) At the end of the program, display a summary showing:
- The original number of chores assigned.
- The number of chores completed.
- The number of chores remaining. [4]'''


# PART 1: Set today's total number of chores (no list needed)
total_chores = 4
original_count = total_chores
print(f"You have {original_count} chores to finish today!\n")
completed_count=0
chore_num=1
while completed_count<=total_chores:
    # PART 4: Work out the current chore's name from its number
    if chore_num == 1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "Feed the pet"
    elif chore_num == 3: next_chore = "Take out the trash"
    else: next_chore = "Wash the dishes"
    completed=input("Have you completed the chore?").lower()
    if completed=="yes":
        completed_count+=1
        chore_num+=1
        print("Chore completed!")
    else:
        print("Please finish it on time!")
    if total_chores>completed_count:
        print("Chores remaining:", total_chores - completed_count)
    print()

print("===== ALL CHORES COMPLETE! =====")
print("Great work finishing your entire checklist today!\n")
        
    