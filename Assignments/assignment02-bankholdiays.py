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

# List only the events unique to Northern Ireland, by checking if the event is not in the other regions for the same day.

for region in ["england-and-wales", "scotland"]:
    for event in data[region]["events"]:
        other_region_events.append({"date": event["date"],"title" : event["title"]})

# # Workflow 1 : Compare uniqueness by title and date. uncomment the lines 23 to 26 to see comparison by title and date


# for event in northern_ireland_events["events"]:
#     event_details = (event["title"], event["date"])
#     if event_details not in other_region_events:
#         print(event["date"], event["title"])

# Workflow 2 : Compare uniqueness by title only

for event in northern_ireland_events["events"]:
    holiday_exists = False

    for other_event in other_region_events:
        if event["title"] == other_event["title"]:
            holiday_exists = True

    if not holiday_exists:
        print(event["date"], event["title"])