# import json

# j = json.dumps(['foo',{'bar':('baz',None,1.0,2)}])

# print(type(j))

# print(type(json.loads(j)))

import jsonpickle


class cat:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def __repr__(self):
        return self.name+" "+self.breed
cat1 = cat("fghjk",'fghjkl')

frozen = jsonpickle.encode(cat1)

with open("cat.json","w") as file:
    frozen = jsonpickle.encode(cat1)
    file.write(frozen)
