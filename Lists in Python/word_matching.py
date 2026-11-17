words = ["madam","drone","racecar","adhriti","abcba","pup","cardiac"]
def word_check(w):
    for word in w:
        if word[0] == word[-1]:
            print(f"{word} has the same start and end letter")
        if len(word) > 5:
            print(f"{word} has more than 5 characters!")
word_check(words)

