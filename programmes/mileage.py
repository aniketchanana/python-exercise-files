#how to  take input in file
print("how many kilometers did you cycle today")
kms = float(input())
miles = round(kms/1.60934,2)
# print(f"ok you said {miles}")

#this is wrong in python because we want just 
#add 2 different types of data types float + string 
#not allowed
print(f"ok you said {miles}")
