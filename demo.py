import requests
import json
from . import extract
from bs4 import BeautifulSoup


def main():
    url = "http://www.firstpost.com/tag/natural-disaster/page/2"
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    head = soup.select('.list-title')
    i = 0
    response = []
    while i < 4:
        headline = head[i].get_text()
        k = extract.ExtractWord.extract_keywords(headline)
        if k == 1:
            description = soup.select('.list-desc')
            image_url = soup.select('.img-wrap')
            date = soup.select('.text-muted')
            res = {"headline": headline,
                   "description": description[i].get_text(),
                   "img_url": image_url[i].img.get('src'),
                   "date": date[i].get_text()}
            response.append(res)
            print(headline)
            print(description[i].get_text())
            print(image_url[i].img.get('src'))
            print(date[i].get_text())
        i += 1
    return response