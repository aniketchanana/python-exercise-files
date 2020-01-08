# *
# **
# ***
# ****
# *****

# for i in range(5) :
#     print("*"*(i+1))




#     *
#    **
#   ***
#  ****
# *****
# j=1
# for i in range(5,0,-1) :
#     print(" "*(i-1)+"*"*j)
#     j = j+1



#    *   
#   ***  
#  ***** 
# *******
#  ***** 
#   ***  
#    *   
n = int(input("Enter number of rows "))
spaces = n-1
for i in range(n) :
    print(" "*spaces + "\U0001f600 "*(2*(i+1)-1) + " "*spaces)
    spaces = spaces - 1
spaces = 1
for i in range(n,0,-1) :
    print(" "*spaces + "\U0001f600 "*(2*(i-1)-1) + " "*spaces)
    spaces = spaces+1

print("")