# methods are particular to a given class

# append insert & extend

first_list = [1,2,3,4,5]

# first_list.append([1,2,3])

# print(first_list)
# [1, 2, 3, 4, 5, [1, 2, 3]] simply pushes it inside the list 
# no matter what is that <<append takes in only one arguement>>

# first_list.extend([1,2,3,4])

# print(first_list)

# first_list.insert(2,"hi")
# print(first_list)

# first_list.clear()
# print(first_list)

# print(first_list.pop(first_list.index(3)))

# print(first_list)

# first_list.remove(2)

# print(first_list)

#---------------------------------------------------------------#

# important functions related to list
# list.index(element)
# list.index(element,startIndex)
# list.index(element,startIndex,endIndex)

# list.count(element)

# first_list.reverse()
# print(first_list)

# first_list.sort()
# str = "a,n,i,k,e,t"
# print(str.split(","))
# join works with list of strings
# print(' .'.join(str))