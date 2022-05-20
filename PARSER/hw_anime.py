import requests
from bs4 import BeautifulSoup

url = "https://www.kinopoisk.ru/lists/movies/top250/"
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
soup.find("div", class_="styles_root__3a8vf")
