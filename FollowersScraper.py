from bs4 import BeautifulSoup
import csv

with open("/Users/andrewhuang/Desktop/DailyPicks/Instagram_Bot/scraped.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

with open("users.csv", "w", newline="") as csvFile:
    writer = csv.writer(csvFile)

    listItems = soup.find_all("ul")

    followersList = listItems[2]

    followers = followersList.find_all("li")

    for f in followers:
        links = f.find_all("a")
        if (len(links) > 1):
            usernameLink = links[1]
            username = usernameLink.text
            writer.writerow([username])
