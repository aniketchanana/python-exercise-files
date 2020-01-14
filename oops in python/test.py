class GrumpyDict(dict):
    #init is defined automatically
    #if it is not defined explicitly
    def __repr__(self):
        print(self)
        print("None of your business")
        return super().__repr__()
    
    #here we have overridden missing method
    def __missing__(self,key):
        print(self)
        print(f"You want {key} it is not here")

    def __setitem__(self, key, value):
        print("changing the dictionary!!")
        super().__setitem__(key, value)

data = GrumpyDict({"first":"Aniket","last":"Chanana"})

print(data)
data["city"] = "SF"
print(data)