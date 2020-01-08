my_list = [1,2,3,4,5]
# my_list[start:end:step] ===> end index is always exclusive
# if any start is not mentioned it starts form 0
# if any end is not mentioned it goes till last index
# if steps are not mentioned it takes it by default to be 1
# [1,2,3,4,5]
# slicing completely makes copy from existing list


# print(my_list[1:])
# print(my_list[3:])
# print(my_list[-2:])

# print(my_list[1:3])


# print(my_list[1::2])

# if negative step is given it starts from start index
# it goes on untill end index is touched  round and round tracing the number

print(my_list[2:-2:-1])