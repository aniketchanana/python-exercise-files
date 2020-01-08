def colorize(color):
    colors = ("red","blue","green")
    if(not isinstance(color,str)):
        raise TypeError("text must be string")
    if(not color in colors):
        raise ValueError("invalid input")
    print(f"printed text in {color}")


colorize("yellow")
# colorize(1)