# def count_upto(max):
#     count = 1
#     while count <= max:
#         yield count
#         count+=1

# counter = count_upto(5)

# print(next(counter))
# print(next(counter))
# print(next(counter))

# weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# def week():
#     day = 0
#     while day >= 6:
#         print(weekdays[day])
#         yield weekdays[day]
#         day+=1
# print("fghj")
# for day in week():
#     print(day)


# def make_song(num):
#     count = num
#     for i in range(0,num+1):
#         if count == 1:
#             yield 'Only 1 bottle of kombucha left!'
#         elif count == 0:
#             yield 'No more kombucha!'
#         else :
#             yield str(count) + " bottles of kombucha on the wall"
#         count-=1

# gen  = make_song(5)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

def is_prime(num):
    i = 1
    count = 0
    while i <= num:
        if num%i == 0:
            count+=1
        i+=1
    return count == 2
    
# print(is_prime(3))
    
def next_prime():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num+=1

gen = next_prime()

print(next(gen))
print(next(gen))