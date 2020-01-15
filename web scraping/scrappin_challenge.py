# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep

url = "https://www.rithmschool.com/blog"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

pages = soup.select(".page")


links = ['blog']
for page in pages:
    try:
        links.append(page.find("a")["href"])
    except TypeError:
        continue    
start = links.pop(0)

with open("blog_data.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["Title","Link","Date"])
    for link in links :
        response = requests.get("https://www.rithmschool.com"+link)
        soup = BeautifulSoup(response.text,"html.parser")
        
        articles = soup.select("article")
        for article in articles:
            a_tag = article.find("a")
            title = a_tag.get_text()
            url = a_tag['href']
            date = article.find("time")["datetime"]
            csv_writer.writerow([title,url,date])
        sleep(5)

