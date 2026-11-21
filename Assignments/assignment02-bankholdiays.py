# Author: Mohamed Shammas
# Date: 21 November 2026
# The program should print out the dates of the bank holidays that happen in northern Ireland.

import csv
import requests
from pathlib import Path

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data)
print(data["northern-ireland"]["events"][0])
