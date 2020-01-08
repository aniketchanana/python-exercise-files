# This code picks a random food item:
# from random import choice #DON'T CHANGE!
# food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
# bakery_stock = {
#     "almond croissant" : 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# YOUR CODE GOES BELOW:

# if bakery_stock.get(food) != None :
#     print(str(bakery_stock[food]) + " left")
# else :
#     print("We don't make that")


# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.

numbers = (1,2,3,4)
print(numbers)
# 2 - Create a variable called value which is a tuple with the the value 1 inside.

value = (1)
print(value)
# 3 - Given the following variable:

values = [10,20,30]

# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)
print(static_values)
# 4 - Given the following variable

stuff = [1,3,1,5,2,5,1,2,5]

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)

print(unique_stuff)