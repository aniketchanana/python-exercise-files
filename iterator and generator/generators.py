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


def make_song(num):
    count = num
    for i in range(0,num+1):
        if count == 1:
            yield 'Only 1 bottle of kombucha left!'
        elif count == 0:
            yield 'No more kombucha!'
        else :
            yield str(count) + " bottles of kombucha on the wall"
        count-=1

gen  = make_song(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))