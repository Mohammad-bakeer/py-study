from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text


# with open ("web/beautiful_Soup/website.html",  encoding='utf-8') as file:
#    contents = file.read()
soup = BeautifulSoup(web_page, "html.parser")
titles = soup.find_all(name="h3", class_="title")
movie_titles = [mov.getText() for mov in titles]
movies = movie_titles[::-1]
with open("web/beautiful_Soup/movies.txt", mode="w", encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")

# print(soup.title)
# print(soup.title.string)

# get first a
# print(soup.a["href"])
# print(soup.a.get("href"))

# all "a"s with specific id or class
# soup.find_all(name="a" , class_= " ", id= "")

# selects first item "a" in "p"
# soup.select_one(selector="p a") or selector="#id" selector=".class"
#  or soup.select()selects all matching items
