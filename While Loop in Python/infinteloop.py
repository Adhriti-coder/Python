print("Now let's safely peek at an infinite loop...")
test_value = 0
safety_counter = 0
while test_value <= 0:
    print("This condition never changes, so this would run forever!")
    test_value+=1