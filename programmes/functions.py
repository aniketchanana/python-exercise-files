# from random import randint,random

# def flip_coin():
#     r = random()
#     if r > 0.5 :
#         return "Heads"
#     else :
#         return "Tails"

# print(flip_coin())

# def square(num):
#     return num ** 2

# print(square(5))

# def add(a,b):
#     return a+b
# print(add(1,2))

# if 11>2:
#     name="aniket"
# print(name)

# def exponent(num,power=2):
#     return num**power

# print(exponent(3,3))

# you can set both params as default or can only set only one of the parameter as default
# def add(a,b) :
#     return a+b

# def sub(a,b) :
#     return a-b
# def math(a,b,fb=add):
#     return fb(a,b)



# print(math(2,3,sub))

def test(*args):
    print(type(args))

test(1,2,3,4)