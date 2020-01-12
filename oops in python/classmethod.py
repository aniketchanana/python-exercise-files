class user:
    @classmethod
    def from_string(cls,data_str):
        first,last,age=data_str.split(",")
        return first+"-"+last

print(user.from_string("aniket,chanana,39"))