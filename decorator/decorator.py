# def be_polite(fn):
#     def wrapper():
#         print("What a pleasure to meet you!")
#         fn()
#         print("Have a great day!")
#     return wrapper

# #@be_polite means we have did this
# # greet = be_polite(greet) and then calling greet()
# @be_polite
# def greet():
#     print("My name is Aniket")


# greet()

# ------------------------------------------------------------------------
# arguements in decorated functions

def shout(fn):
    def wrapper(*args,**kwargs):
        return fn(*args,**kwargs).upper()
    return wrapper

# single arguement vali situation to handel ho jati hai
# variable arguements ko hum *args or *kwargs se handel karte hai
@shout
def greet(name):
    return f"Hi, i'm {name}"

@shout
def order(main,side):
    return f"Hi, i'd like the {main}, with the {side}. please"

print(greet("TOOD"))
print(order("cola","burger"))