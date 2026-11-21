# Author: Mohamed Shammas
# Date: 21 November 2026
# The program should print out the dates of the bank holidays that happen in northern Ireland.

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
northern_ireland_events = data["northern-ireland"]
other_egions = []

for event in northern_ireland["events"]:
    print(event["date"], event["title"])
