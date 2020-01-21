import sqlite3
import requests
from bs4 import BeautifulSoup
import sqlite3

def get_title(book):
    return book.find_all("h3")[0].find("a")["title"]

def get_price(book):
    price = book.select(".price_color")[0].get_text()
    return float(price.replace("Â£",""))

def get_rating(book):
    paragraph = book.select(".star-rating")[0]
    rating = paragraph.get_attribute_list("class")[-1]
    raiting_dict = {"Zero":0,"One":1,"Two":2,"Three":3,"Four":4,"Five":5}
    return raiting_dict[rating]

def scrape_books(url):
    response = requests.get(url).text
    soup = BeautifulSoup(response,"html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
        title = get_title(book)
        price = get_price(book)
        rating = get_rating(book)
        all_books.append((title,price,rating))
    save_books(all_books)
    return all_books

def save_books(books):
    conn = sqlite3.connect("books.db")
    c = conn.cursor()
    c.execute("CREATE TABLE books (title TEXT,price REAL,rating INTEGER)")
    c.executemany("INSERT INTO books values (?,?,?)",books)
    conn.commit()
    conn.close()

scrape_books("http://books.toscrape.com/")