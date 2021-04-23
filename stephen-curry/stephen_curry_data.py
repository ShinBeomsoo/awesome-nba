from pprint import pprint

from bs4 import BeautifulSoup
import requests


curry_profile = requests.get(
    "https://www.nba.com/player/201939/stephen-curry/profile"
)
html = curry_profile.text

soup = BeautifulSoup(html, "html.parser")
a = soup.select(
    "#__next > div.Layout_withNav__2ED2- > div.max-w-screen-xl.mx-auto.p-0.md\:p-7.xxl\:px-0 > section:nth-child(2) > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(4)"
)

pprint(a)

