#!/usr/bin/python3
"""
Write a code to suggest automatically activates for
https://api.ipify.org/?format=json
Get your public IP
Get your location
https://ipinfo.io/<YOUR_IP>/geo
"""

import requests
import pprint
Detect_Location_websit_raw = "https://ipinfo.io/<YOUR_IP>/geo"
My_IP = requests.get("https://api.ipify.org/?format=json").json()["ip"]
print(My_IP)

Detect_Location_website = Detect_Location_websit_raw.replace("<YOUR_IP>" , My_IP)
print(Detect_Location_website)

data = requests.get(Detect_Location_website).json()
pprint.pprint(data)

MyLocation = {}
MyLocation["City"] = data["city"]
MyLocation["country"] = data["country"]
pprint.pprint(MyLocation)