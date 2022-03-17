from selenium import webdriver
import urllib.request
import json
import urllib
from datetime import datetime

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.metacritic.com/browse/games/score/metascore/all/pc/filtered?sort=desc")

now = datetime.now()
waktu = now.strftime("%d/%m/%Y %H:%M:%S")

top100pcgames = []
i = 1

for pcgames in driver.find_elements_by_tag_name("tr"):
    print(pcgames.text)
    for banner in pcgames.find_elements_by_tag_name("a"):
        for img in banner.find_elements_by_tag_name("img"):
            print(img.get_attribute("src"))
            top100pcgames.append(
                {"Rating": pcgames.text.split("\n")[0],
                 "No": pcgames.text.split("\n")[1],
                 "Judul": pcgames.text.split("\n")[2],
                 "Release": pcgames.text.split("\n")[4],
                 'Waktu_scrapping':waktu,
                 "Image": img.get_attribute("src")
                 }
            )
hasil = open("F:\hasil2.json", "w")
json.dump(top100pcgames, hasil, indent=5)
hasil.close()

driver.quit()