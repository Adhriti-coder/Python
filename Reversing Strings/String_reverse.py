word=input("Please enter a word: ")
length=len(word)-1
reverse=""
for i in range(length, -1, -1):
    print("The reverse is "+ reverse + " letter at position "+ str(i)+ " is "+ word[i])
    reverse=reverse+word[i]
print("The reverse is ", reverse)
    