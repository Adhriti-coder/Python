print("=====GROCERY COST COMPARISION TOOL=====")
rice_cost=12
milk_cost=4
fruit_cost=8
number_of_baskets=2
family_members=4
basket_cost_per_person= (rice_cost + milk_cost + fruit_cost) * number_of_baskets / family_members

print("\n Part 1: This week's shop")
print("Cost per person:  ", basket_cost_per_person)

print("\n Part 2: Sharing the Items")
total_items=int(input("Enter the total number of Groceries:  "))
people=int(input("Enter the number of people sharing them:  "))

if people==0:
    print("You cannot share the items between 0 people!")
else:
    if total_items % people == 0:
        print(total_items ," items divide equally among ", people," people- ", total_items // people ," each!")
    else:
        print(total_items ," items do not divide equally among ", people," people- ", total_items % people ," leftover!")

print("\n Part 3: Fixing the Weekly Average")
recorded_average=65
total_weeks=4
wrong_week_cost=50
correct_week_cost=80
recorded_total= recorded_average * total_items
corrected_total= recorded_average - wrong_week_cost + correct_week_cost
corrected_average= corrected_total / total_weeks

print("Recorded total was ", recorded_total)
print("Corrected total is ", corrected_total)
print("Correct Weekly Average:  ", corrected_average)

print("\n Part 4: Comparing the Stores")
store_a_average=70
store_b_average=75
store_c_average=80

print("Store A: ", store_a_average, "| Store B: ", store_b_average, "| Store C: ", store_c_average)

if corrected_average < store_a_average and corrected_average < store_b_average and corrected_average < store_c_average:
    verdict="Cheaper than all 3 stores"
elif corrected_average > store_a_average and corrected_average > store_b_average and corrected_average > store_c_average:
    verdict="More expensive than all 3 stores"
else:
    verdict="Somewhere in between the 3 stores"

print("Your average is ", verdict)

print("\n =====SUMMARY=====")
print("Cost per person this week:  ", basket_cost_per_person)
print("Corrected weekly average:  ", corrected_average)
print("Verdict:  ", verdict)