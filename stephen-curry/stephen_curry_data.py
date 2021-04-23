from pprint import pprint

from bs4 import BeautifulSoup
import requests


curry_profile = requests.get(
    "https://www.basketball-reference.com/players/c/curryst01/gamelog/2021"
)

def get_stat_data(data_stat: str):
    result = []
    html = curry_profile.text
    soup = BeautifulSoup(html, "html.parser")
    points = soup.find_all(attrs={"data-stat": data_stat})
    for point in points:
        try:
            result.append(int(point.string))
        except ValueError:
            pass
    return result



a = get_stat_data("pts")
print("PTS: ", a)
print("PTS average: ", sum(a)/len(a))

a = get_stat_data("fg3")
print("3pa: ", a)
print("3pa average:: ", sum(a)/len(a))
