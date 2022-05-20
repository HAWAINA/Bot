import requests
from bs4 import BeautifulSoup


URL = "https://animego.org/"


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0",
}


def get_html(url, params=""):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div", class_="media-body")
    anime = []

    for item in items:
        anime.append(
            {
                # "image":item.find('div', class_="anime-list-lazy lazy").find("img").get("src"),
                "title": item.find(
                    "a",
                ).get("href")
            }
        )
    return anime


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(2015, 2021):
            html = get_html(f"https://animego.org/anime/filter/year-to-{page}/apply")
            anime.extend(get_data(html.text))
        return anime

    else:
        raise Exception("Error in parser function")
