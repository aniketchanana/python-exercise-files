from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests

# name = input("Enter the username of the person ")

page_data = requests.get(f"https://github.com/{name}?tab=followers").text


soup = BeautifulSoup(page_data,"html.parser")

user_imgs = soup.select(".avatar")


for user in user_imgs:
    # print(user["alt"][1::])
    # print(user["src"])
    try:
        with open(user["alt"][1::]+".jpg","wb") as file:
            file.write(requests.get(user["src"]).content)
    except ValueError:
        continue


# for img in soup.select(".avatar"):
    # if img["src"] :
    #     urlretrieve(img["src"])
