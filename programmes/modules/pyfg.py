import pyfiglet
import termcolor
# help(pyfiglet)
# print(pyfiglet.figlet_format("hello"))


is_name = True

if is_name:
    print("aniket")


msg = input("what would you like to print? ")
color = input("What color? ")
ascii_art = termcolor.colored(pyfiglet.figlet_format(msg), color=color)
print(ascii_art)
