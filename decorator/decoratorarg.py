from functools import wraps

def ensure_first_args_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            if args[0] != val:
                return "First args nees to be " + val
            return fn(*args,**kwargs)
        return wrapper
    return inner

# whole this became ensure_first_args_is("burrito") this fun call
# it then returns inner func and to that inner func we passes
# fav_food function
@ensure_first_args_is("burrito")
def fav_food(*foods):
    print(foods)

print(fav_food("burrito","ice cream"))