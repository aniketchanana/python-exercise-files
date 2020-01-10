import requests

url = "https://awesomecolorpicker.herokuapp.com/"

response = requests.get(url)

print(response.text)
# print(response.headers)
# print(response.ok)