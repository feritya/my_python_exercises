import requests
from bs4 import BeautifulSoup

url="https://www.imdb.com/chart/top"
html=requests.get(url).content
soup =BeautifulSoup(html,"html.parser")


list=soup.find("tbody",{"class":"lister-list"}).find_all("tr",limit=19)


count= 0
for tr in list:
    count+=1
    title=tr.find("td",{"class":"titleColumn"}).find("a").text

    year=tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")

    rating=tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    year =int(year)
    if year <2000:
        count-=1
        continue

    print(count,"-",title.ljust(50)," ",year," ",rating)

# output
# 1 - The Dark Knight                                      2008   9.0
# 2 - The Lord of the Rings: The Return of the King        2003   8.9
# 3 - The Lord of the Rings: The Fellowship of the Ring    2001   8.8
# 4 - Spider-Man: Across the Spider-Verse                  2023   8.8
# 5 - The Lord of the Rings: The Two Towers                2002   8.7
# 6 - Inception                                            2010   8.7

