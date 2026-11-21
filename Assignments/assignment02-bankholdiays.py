import csv
import requests
from pathlib import Path

FILENAME = "data.csv"
DATADIR = Path(__file__).parent / "Data"

with open(DATADIR / FILENAME, "rt", newline="") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print(line)

with open(DATADIR / FILENAME, "rt", newline="") as fp:
    reader = csv.DictReader(fp, delimiter=",")
    total = 0
    count = 0
    for line in reader:
        total += int(line["Age"])
        count += 1
    print(f"average is {total / count}")

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data)
print(data["northern-ireland"]["events"][0])
