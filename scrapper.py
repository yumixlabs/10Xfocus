# This scrapper script scrapes 71 quotes and saves them in "data_quotes.txt" file
# From this list, one file is randomly chosen and displayed on the canvas once the main program is run
# Last Line is manually removed to avoid printing empty text
# URL OF THE ORIGINAL DATA = https://graciousquotes.com/focus/

from bs4 import BeautifulSoup
import requests
URL = "https://graciousquotes.com/focus/"
response = requests.get(URL)
webpage = response.content
# print(webpage)
soup = BeautifulSoup(webpage, "html.parser")
# print(soup.prettify(encoding="utf-8"))
info = soup.select("div article div figure")
with open("data_quotes.txt", "w") as quotes:
    for q in info:
        quotes.write(f"{q.getText()} \n")
        # print(q.getText())
