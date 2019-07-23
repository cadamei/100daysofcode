#!python3


import requests
import json
from pprint import pprint

api_key = input("Please enter the API authorization token for Meraki:\n")

sf_url = 'https://api.meraki.com/api/v0/organizations'

r = requests.get(sf_url, headers={'X-Cisco-Meraki-API-Key': api_key, 'Content-Type': 'application/json'})

pprint(r.json())
