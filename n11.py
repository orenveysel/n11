import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li",{"class":"column"})

for li in list:
    name = li.find("div",{"class":"proDetail"}).find_all("a")[0].text
    link = li.div.a.get("href")
    oldprice = li.find("div",{"class":"proDetail"}).find_all("a")[0]
    newprice = li.find("div",{"class":"proDetail"}).find_all("a")[1]

    print(f"Name: {name}, Link: {link}, Old Price: {oldprice}, New Price: {newprice}")

# print(list)
