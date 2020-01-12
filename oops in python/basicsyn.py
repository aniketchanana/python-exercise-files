# defining a class 

# class User:
#     pass


# user1 = User()


# init method is constructor to a class

# class User:
#     def __init__(self,name):
#         super().__init__()
#         self.name = name
#         print("A new User is created")


# user1 = User("aniket")

# print(user1.name)

# print(dir(user1))


class BankAccount:
    def __init__(self,owner):
        super().__init__()
        self.balance = 0.0
        self.owner = owner
    
    def deposit(self,money):
        self.balance += owner
    
    def withdraw(self,money):
        self.balance -= money

user = BankAccount("aniket")
print(user.balance)
print(user.owner)