import csv
from dotenv import dotenv_values
from InstagramDriver import InstagramWebDriver


config = dotenv_values(".env")

USERNAME = config.get("USERNAME")
PASSWORD = config.get("PASSWORD")

instagram = InstagramWebDriver(USERNAME, PASSWORD)
instagram.login()

with open("users.csv", "r",) as file:
    csvReader = csv.reader(file)
    for row in csvReader:
        username = row[0]
        instagram.sendDM(
            username, "Yo what's up main.")
