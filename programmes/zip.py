midterms = [80,91,78]
finals = [98,89,53]

students = ['a','b','c']

final_grades = {pair[0]:max(pair[1],pair[2]) for pair in zip(students,midterms,finals)}

# or 

grades=dict(
    zip(
        students,
        map(
            lambda pair:max(pair),
            zip(midterms,finals)
        )
    )
)



def interleave(str1,str2):
    my_list = list(zip(str1,str2))
    mystr = ""
    for element in my_list:
        mystr += element[0]+element[1]
    return mystr

# print(interleave("aniket","sayama"))


print(list(filter(lambda x:x%4==0,[1,2,3,4])))