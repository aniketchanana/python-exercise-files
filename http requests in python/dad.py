import pyfiglet
import termcolor
import requests
import random


print(termcolor.colored(pyfiglet.figlet_format("DAD JOKES 3000"),color="cyan"))

category = input("What kind of joke you want to listen? ")

url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={
        "Accept":"application/json"
    },
    params={
        "term":category
    }
)

data = response.json()

jokes = data["results"]
try :
    if len(jokes) == 1 :
        print("Here is a joke : " + jokes[0]["joke"])
    else :
        print("There are many jokes here is one joke : " + random.choice(jokes)["joke"])
except IndexError :
    print("Jokes not found")