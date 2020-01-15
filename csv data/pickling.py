import pickle

class cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def __repr__(self):
        return self.name+" "+self.breed
cat1 = cat("fghjk",'fghjkl')

# write binary
# with open("pets.pickle","wb") as file:
#     pickle.dump(cat1,file)

with open("pets.pickle","rb") as file :
    my_cat = pickle.load(file)
    print(repr(my_cat))