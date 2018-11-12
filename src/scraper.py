import requests
from bs4 import BeautifulSoup
import csv
import os




session = requests.Session()
# Our "human" header; go to https://www.whatismybrowser.com/ to see what the Internet can see about your browser,
# including what your header is. Below are the settings for a browser I used.
header = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "Accept-Language": "es-ES,es;q=0.9,ca;q=0.8,en;q=0.7",
          "Connection": "keep-alive",
          "Referrer": "https://www.google.com/",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/70.0.3538.77 Safari/537.36"}

# The URL we are visiting
url = "http://www.hubertiming.com/results/2018Hope"
page = session.get(url, headers=header).text

# Creates a BeatutifulSoup object
soup = BeautifulSoup(page, "html5lib")

# Find the table individual results
table = soup.find(id="individualResults")

# For each row in the individual results pull up the runner and save it in
# the ranking list
ranking = []
for row in table.find_all("tr"):

    cells = row.find_all("td")

    if len(cells) == 0:

        continue
    else:
        place = cells[0].find(text=True)
        bib = cells[1].find(text=True)
        name = cells[2].find(text=True)
        gender = cells[3].find(text=True)
        city = cells[4].find(text=True)
        state = cells[5].find(text=True)
        chip_time = cells[6].find(text=True)
        chip_pace = cells[7].find(text=True)
        gender_place = cells[8].find(text=True)
        age_group = cells[9].find(text=True)
        age_group_place = cells[10].find(text=True)
        time_to_start = cells[11].find(text=True)
        gun_time = cells[12].find(text=True)
        team = cells[13].find(text=True)

    runner = [place, bib, name, gender, city, state, chip_pace, chip_pace,
              gender_place, age_group, age_group_place, time_to_start, gun_time, team]

    ranking.append(runner)

# Find the headers columns of the table individual results and save it into
# the header list
headers = []
for header_cell in table.find_all("th"):
    headers.append(header_cell.find(text=True))

# Get the current working directory and creates a dir to save the data
path = os.path.abspath(os.path.join(os.getcwd(), "..")) + "/data"
if not os.path.exists(path):
    os.makedirs(path)

# Creates a CSV file with the data 
with open(path + "/ranking.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(header for header in headers)
    for runner in ranking:
        writer.writerow(runner)
