# my_dict = dict(name="aniket",age="20")
# print(my_dict)

user_info = {
    "name":"aniket",
    "age":12,
    "college":"chitkara"
}
# print(user_info)
# user_info["name"] = "jatin"
# print(user_info)

# print(list(user_info.values()))

# for data in list(user_info) :
    # print(user_info[data])

# or you can do this 

# for data in user_info.values() :
#     print(data)

# for key in user_info.keys() :
#     print(key)

for k,v in user_info.items() :
    print(f"key is {k} and value is {v}")