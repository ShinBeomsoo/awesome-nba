import csv
from typing import Any, Dict

import requests
from bs4 import BeautifulSoup
from requests import Response


def get_stat_data(curry_profile: Response) -> Dict[str, Any]:
    stat_data = {}
    stats = ["pts", "fg3", "fg"]
    html = curry_profile.text
    soup = BeautifulSoup(html, "html.parser")
    for stat in stats:
        points = soup.find_all(attrs={"data-stat": stat})
        total_stat = []
        for point in points:
            try:
                total_stat.append(int(point.string))
            except ValueError:
                pass
        stat_data[stat] = total_stat
    return stat_data


def write_csv_file(stat_data: Dict) -> None:
    filed_names = list(stat_data.keys())
    with open("curry_data.csv", "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=filed_names)
        writer.writeheader()
        writer.writerow(stat_data)


def main():
    curry_profile = requests.get(
        "https://www.basketball-reference.com/players/c/curryst01/gamelog/2021"
    )
    stat_data = get_stat_data(curry_profile)
    # write_csv_file(stat_data)


if __name__ == "__main__":
    main()
