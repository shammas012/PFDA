# Author: Mohamed Shammas
# Date: 21 November 2026
# The program should print out the dates of the bank holidays that happen in northern Ireland.

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data.keys())
northern_ireland_events = data["northern-ireland"]
other_region_events = []

# List only the events unique to Northern Ireland, by checking if the event is not in the other regions.

for region in ["england-and-wales", "scotland"]:
    for event in data[region]["events"]:
        other_region_events.append(event["date"],event["title"])

for event in northern_ireland_events["events"]:
    print(event["date"], event["title"])

print(other_region_events)