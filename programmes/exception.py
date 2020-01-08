# def get(d,key):
#     try:
#         return d[key]
#     except KeyError:
#         return None

# print(get({"name":"aniket"},"city"))


# try:
#     num = int(input("please enter the number"))
# except:
#     print("Thats not a number")
# else:
#     print("running....else")


def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
        return "divison by zero is not allowed"
    except TypeError:
        return "a and b must be int or float"
print(divide(2,0))