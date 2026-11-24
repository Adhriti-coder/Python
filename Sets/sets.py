basket1 = {"Apple", "Orange", "Banana", "Cherry", "Watermelon","Banana"}
basket2 = {"Pineapple", "Orange", "Grapes", "Jackfruit"}
print(basket1)
basket1.add("Strawberry")
print(basket1)
print("The intersection of the 2 baskets is ", basket1.intersection(basket2))
import array as arr
fruits_count = arr.array("i", [3, 6, 4, 8])
print("The array of fruits count is ", fruits_count)
fruits_count.insert(2,1)
fruits_count.append(6)
print(fruits_count)
print(fruits_count.count(6))
fruits_count.reverse()
print(fruits_count)
fruits_count.insert(5,8)
print(fruits_count)


"""
5) Create an array of fruit counts.
   a) Import the `array` module as `arr`.
   b) Create an integer array using `arr.array('i', [...])`.
   c) Store fruit count values inside the array.

6) Add items to the array.
   a) Use `insert()` to add a value at the beginning.
   b) Use `append()` to add a value at the end.
   c) Print the updated array.

7) Count and reverse array values.
   a) Use `count()` to check how many times 4 appears.
   b) Use `reverse()` to reverse the order of the array.
   c) Print the count and reversed array.

8) Print the final summary.
   a) Print the class fruit basket organizer heading.
   b) Display both baskets, shared fruits, and fruit counts.
   c) Print a closing line to complete the summary.
"""