swim=input("Do you know how to swim?").strip().lower()
age=int(input("What's your age?"))
instructor=input("Do you have an instructor?").strip().lower()
print("===Swimming Pool Entry===")
if swim=="yes":
    if age>12 and instructor=="yes":
       print("Decision: Yes, you can swim in the deep side of the pool!")
    elif age<12 and instructor=="yes":
        print("Decision: You can swim in the shallow end!")
    elif age>12 and not instructor=="yes":
        print("Decision: You cam swim in the pool, safely!")
    elif age<12 and not instructor=="yes":
        print("Decision: You can only swim in the shallow end, very safely!")
elif not swim=="yes":
    print("Decision: you cannot swim in the deep pool. Swim only in the shallow end, very carefully!!")