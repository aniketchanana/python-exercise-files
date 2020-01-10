# icanhazdadjokes.com

import requests

url = "https://icanhazdadjoke.com"

#  by default it hash text/html
#  by default it hash text/plain
#  by default it hash application/json

response = requests.get(url,headers={
    "Accept":"application/json"
})

# print(response.text)

data = response.json()

print(data["joke"])