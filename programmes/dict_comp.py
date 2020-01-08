# generating dict from a range

# dict_list = { value : value for value in range(1,10)}

# print(dict_list)
# -------------------------------------------------------
# user = {
#     "name" : "aniket",
#     "roll" : 12,
#     "college" : "chitkara"
# }

# yelling_user = { k.upper() : v  for k,v in user.items()}

# print(yelling_user)

# ---------------------------------------------------------

# CONDITIONAL LOGIC in dictionary

# CLD = { num : ("even" if num%2 == 0 else "odd") for num in range(1,10)}

# print(CLD)


list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work!
answer = {list1[i]:list2[i] for i in range(0,len(list1))}

print(answer)