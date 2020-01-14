from random import choice

def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHA','LOL','HEHEHEHE!!'))
        return f"{laugh} {person}"
    
    return get_laugh

laugh_at = make_laugh_at_func("Aniket")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())