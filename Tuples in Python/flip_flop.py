#Write a program to check whether the given tuple - (1,2,3,3,2,1) is a palindrome or not. If it's a #palindrome, then it is the same after being reversed.
a = (1, 2, 3, 3, 2, 1)
start = 0
end = len(a)-1
palind = True
while start < end:
    if a[start] == a[end]:
        start += 1
        end -=1
    else:
        palind = False
        print("It's not a palindrome")
        break
if palind == True:
    print("It's a palindrome")

