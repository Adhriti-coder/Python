print("=====CLASSROOM POINTS CALCULATOR=====")
class_1=150
class_2=75
class_3=120
class_4=100
class_5=25

total_points= class_1 + class_2 + class_3 + class_4 + class_5
average_points= total_points / 5

print("Total Points  :", total_points)
print("Average points  :", average_points)

stars_per_point= 5
reward_stars= total_points * stars_per_point

print("Total Reward Stars  :", reward_stars)

boxes= reward_stars // 25
leftovers= reward_stars % 25

print("Full Boxes Packed  :", boxes)
print("Leftover Stars  :", leftovers)

last_week= 500
print("Better than last week?  :", total_points > last_week)
print("Same as last week?  :", last_week == total_points)
print("At least as better?  :", total_points >= last_week)

total_points += 30
print("After bonus Points  :", total_points)

total_points -= 15
print("Points after missed tasks  :", total_points)

reward_stars= total_points * stars_per_point
boxes= reward_stars // 25

print("Final boxes packed  :", boxes)