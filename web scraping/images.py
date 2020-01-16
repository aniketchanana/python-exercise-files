# from bs4 import BeautifulSoup
# import requests
# import urllib.request

# url = "https://aniketchanana.github.io/portfolio/"

# data = requests.get(url).text

# soup = BeautifulSoup(data, "html.parser")

# img_link = soup.select(".myimage")[0]["src"][2::]


# def dl_img(url):
#     urllib.request.urlretrieve(url,"img.jpg")

# dl_img(url+img_link)


import urllib.request
response = urllib.request.urlopen('http://python.org/')
html = response.read()
print(html)