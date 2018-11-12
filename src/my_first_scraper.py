from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd

url = "http://observon.blogspot.com/2017/08/clasificaciones-carrera-10k-nocturno.html?m=1"

html = urlopen(url)
soup = BeautifulSoup(html, "html5lib")

# Get all the tables in the web page
tables = soup.find_all("table")

# We only want the general ranking table
table = tables[-1]

ranking = []
for row in table.find_all("tr"):
    cells = row.find_all("td")
    if (len(cells) == 0):
        continue
    else:
        position = cells[0].find(text=True)
        runner = cells[1].find(text=True)
        time = cells[2].find(text=True)
        element = [position, runner, time]
        ranking.append(element)

with open("../data/ranking.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for runner in ranking:
        writer.writerow(runner)