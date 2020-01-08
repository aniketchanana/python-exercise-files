# print(list((1,2,3,4)))

# def fav_colors(**kwargs):
#     print(kwargs)

# fav_colors(name="aniket",age=19,college="chitkara")

# print(*[1,2,3,4])

user = {
    "name":"aniket",
    "age":19
}

def my_fun(**kwargs):
    print(kwargs)
# def my_fun(age,name):
#     print(name,age)

my_fun(**user)
