import requests
import json
from bs4 import BeautifulSoup

# Web sitesini
url = "https://www.hurriyet.com.tr/ekonomi/son-dakika-fed-faiz-kararini-acikladi-42333373"

# Sayfanın BeautifulSoup ile işlenmesi
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

# Haber Kaynağından Alınacak İçerikler
title = soup.find("div", {"class": "container"}).find("h1").text
image = soup.find("div", {"class": "news-media"}).find("img")["src"]
description = soup.find("div", {"class": "container"}).find("h2").text
content = soup.find("div", {"class": "news-content readingTime"}).find_all("p")
date = soup.find("div", {"class": "news-inf"}).find("span").text.replace("Oluşturulma Tarihi: ", "").split()

# Tarih Düzenlemesi
month = date[0]
day = date[1][:-1]
year = date[2]
time = date[3]
month_dict = {"Ocak":"01" ,"Şubat":"02", "Mart":"03", "Nisan":"04", "Mayıs":"05", "Haziran":"06",
              "Temmuz":"07", "Ağustos":"08", "Eylül":"09", "Ekim":"10", "Kasım":"11", "Aralık":"12"}
publishDate = f"{day}.{month_dict[month]}.{year} {time}"

# JSON Dosyası
json_file_name = "news.json"

json_data = {
    "Title": title,
    "Image": image,
    "Description": description,
    "Content": [p.get_text() for p in content],
    "Publish Date": publishDate
 }

with open(json_file_name, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)