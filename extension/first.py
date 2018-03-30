# These code snippets use an open-source library. http://unirest.io/python
import requests
import json
import extract

response = requests.get("https://dev132-toi-times-of-india-v1.p.mashape.com/news/topnews",
  headers={
    "X-Mashape-Key": "4dkljZFOAzmshXy5rXgtbU4DmfE5p1e00NxjsncDT6hqCtSKSH",
    "Accept": "application/json"
  }
)
tex = response.text
print(type(tex))
data = json.loads(tex)
headline = []
date = []
cap = []
url = []
photo = []
thumb = []
photo_cap = []
list_of_news = data['NewsItem']
for i in list_of_news:
    h = i['HeadLine']
    k = extract.ExtractWord.extract_keywords(h)
    if k==1:
        headline.append(h)
        date.append(i['DateLine'])
        url.append(i['WebURL'])
        cap.append(i['Caption'])
        photo.append(i['Image']['Photo'])
        photo_cap.append(i['Image']['PhotoCaption'])
        thumb.append(i['Image']['Thumb'])


    else:
        print("No Bad News")

print(headline)
print(date)
print(url)
print(cap)
print(photo)
print(thumb)
print(photo_cap)

