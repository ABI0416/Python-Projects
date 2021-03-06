import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top"

response = requests.get(url)

print(response)

html = response.content

soup = BeautifulSoup(html, "html.parser")

titles = soup.find_all("td", {"class":"titleColumn"})
ratings = soup.find_all("td", {"class","ratingColumn imdbRating"})

for title, rating in zip(titles, ratings):

    title = title.text
    title = title.strip()
    title = title.replace("\n", "")

    rating = rating.text
    rating = rating.strip()
    rating = rating.replace("\n", "")

    print("Movie Title: ", title, "Movie Rating: ", rating)
