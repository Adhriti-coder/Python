items = ["pencil", "eraser", "glue","sharpener","notebook"]
stock_count = [3, 0, 1, 2, 3]
pairs = list(zip(items, stock_count))#list
print(pairs)
available = {a:b for a,b in pairs}#dictionary comprehension
print(available)
in_stock = [i for i in items if available[i]>0]#list comprehension
print(in_stock)
item_to_buy = input("Which item do you want to buy? ")
if item_to_buy != in_stock:
    print("That item is out of stock!")
prices = [10, 10, 30, 10, 50]
increase = int(input("Enter the amount you want to increase in each price: "))
new_price = list(map(lambda x : x+increase, prices))#list
print(new_price)


