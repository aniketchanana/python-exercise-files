# https://www.rithmschool.com/blog

import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.rithmschool.com/blog"
response = requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

articles = soup.select("article")

with open("blog_data.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["Title","Link","Date"])
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")["datetime"]
        csv_writer.writerow([title,url,date])