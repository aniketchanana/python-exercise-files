# from time import time

# def speed_test(fn):
#     def wrapper(*args,**kwargs):
#         t1 = time()
#         result = fn(*args,**kwargs)
#         t2 = time()
#         print(f"Time elapsed {t2-t1}")
#         return result
#     return wrapper

# @speed_test
# def sum_nums():
#     return sum(x for x in range(0,1000000))

# @speed_test
# def sum_gen():
#     return sum([x for x in range(0,100000)])    

# print(sum_nums())
# print(sum_gen())

# def test(*args):
#     print(args)
#     print(*args)
#     return len(args)

# print(test(1,2,3))

# print(isinstance((1,2),int))

from time import sleep

sleep(1.2)
print("aniket")