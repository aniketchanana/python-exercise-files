class Animal:
    
    def __init__(self,name,species):
        super().__init__()
        self.name = name
        self.species = species

    def make_sound():
        print(f"This animal says {sound}")

class Cat(Animal):
    def __init__(self, name,breed,toy):
        super().__init__(name, species="cat")
        self.breed = breed
        self.toy = toy
    
blue = Cat("Blue","fold","String")

print(blue.__dict__)