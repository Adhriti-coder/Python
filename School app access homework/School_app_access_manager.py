CAMERA=1
MICROPHONE=2
STORAGE=4
LOCATION=8

approved_apps=["coding_app","reading_app","maths app","science app"]
student_name=input("Enter your name:  ")
requested_app=input("Enter the app you want to access:  ")

if type(student_name) is str:
    print("The student name is stored as text.")

if type(requested_app) is not int:
    print("The requested app is not stored as a number.")

if requested_app in approved_apps:
    print(requested_app," is an approved app!")
else:
    print(requested_app," is not an approved app!")

restricted_apps=["gaming app","shopping app","social media app"]

if requested_app not in restricted_apps:
    print("The app is not in the restricted list.")
else:
    print("Access denied because because the app is restricted.")

print("\n ---APP PERMISSION SETTINGS--- ")
permissions= CAMERA | MICROPHONE | STORAGE
print("Permission value:  ", permissions)
print("Permission bits:  ", bin(permissions))

if permissions & CAMERA:
    print("Camera permission: Enabled")

if permissions & MICROPHONE:
    print("Microphone permission: Enabled")

if permissions & STORAGE:
    print("Storage permission: Enabled")

if permissions and LOCATION:
    print("Location permission: Enabled")
else:
    print("Location permission: Disabled")

print("\n ---BIT SHIFT DEMONSTRATION--- ")
next_permission= CAMERA << 1
print("Camera bit:  ", bin(CAMERA))
print("After left shift:  ", bin(next_permission))

previous_permission= STORAGE >> 1
print("Storage bit:  ", bin(STORAGE))
print("After right shift:  ", bin(previous_permission))

print("\n ---FINAL ACCESS RESULT--- ")

if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted to ", requested_app)
else:
    print("Access denied to ", requested_app)