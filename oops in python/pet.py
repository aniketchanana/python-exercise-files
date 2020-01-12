class Pet:
    allowed = ["cat","dog"]
    def __init__(self,name,species):
        super().__init__()
        if species not in Pet.allowed :
            raise ValueError(f"you can't have a {species} pet!")
        self.name = name
        self.species = species 


cat = Pet("Blue","cat")
dog = Pet("wyatt","tiger")