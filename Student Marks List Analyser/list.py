print("=== STUDENT MARKS LIST ANALYZER ===")
print()

marks = [ 99, 25, 76, 54, 33]
print("Students' Marks : ", marks)
print()

sample_marks = [11, 22, 33, 44] * 2
print("Repeated Sample Marks : ", sample_marks)
print()

print("Number of marks : ", len(marks))
print()

print("First mark : ", marks[0])
print("Last mark  : ", marks[-1])
print()

print("First 3 marks : ", marks[0:3])
print("Reversed marks : ", marks[::-1])
print()

def marks_match(mlist):
    count = 0
    match_marks = []
    for mark in mlist:
        mark_text = str(mark)
        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            match_marks.append(mark)
    print("Marks with first and last digit same : ", match_marks)
    return count

same_digit_count = marks_match([99, 25, 76, 54, 33])
print("Number of matching digits : ", same_digit_count)
print()

total = 0
for mark in marks:
    total += mark
print("Total marks of everyone : ", total)
average = total / len(marks)
print("Average marks : ", average)
print()

marks.sort()

smallest_mark = marks[0]
largest_mark = marks[-1]
print("Smallest mark : ", smallest_mark)
print("Largest mark : ", largest_mark)
print()

print("===== STUDENT MARKS LIST ANALYSER =====")
print("Sorted Marks   :  ", marks)
print("Total Marks    :  ", total)
print("Average Marks  :  ", average)
print("Highest Marks  :  ", largest_mark)
print("Lowest Marks   :  ", smallest_mark)
print("=======================================")