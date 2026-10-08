#A Weather Outfit Picker that asks about temperature, rain, wind, and #puddles, then uses if and if-else statements to decide what outfit, #umbrella, windbreaker, and shoes to wear, all while keeping every #block properly indented.
temperature= float(input("Enter today's temperature in celcius: "))
if temperature < 20:
    outfit= "jacket"
    print("The weather is cold, kindly wear your ", outfit)
else:
    outfit= "T shirt"
    print("The weather is hot, you can wear your ", outfit)
raining= input("Is it raining? ").lower()
if raining=="yes":
    print("You should carry an umbrella with you!")
wind= int(input("Tell the wind speed km/hr: "))
if wind>30:
    need_windbreaker="yes"
    print("It is windy today, kindly wear a windbreaker over your ", outfit)
else:
    need_windbreaker="no"
    print("It is calm today, you don't need to wear a windbreaker over your ", outfit)
    
# PART 7: Ask whether there are puddles on the ground
has_puddles = input("Are there puddles on the ground? (yes/no): ")
# PART 8: Decide between boots and sneakers
if has_puddles == "yes":
    shoes = "boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes = "sneakers"
    print("The ground is dry.")
    print("Wear", shoes)

# PART 9: This message always prints, no matter what was chosen above
print("")
print("Weather check complete!")

# PART 10: Print the final outfit summary
print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", temperature)
print("Outfit Chosen:", outfit)
print("Raining:", raining)
print("Windbreaker Needed:", need_windbreaker)
print("Shoes Chosen:", shoes)
print("===================================")


