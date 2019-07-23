#!python3


import requests
import json
from pprint import pprint

api_key = input("Please enter the API authorization token for Salesforce:\n")

sf_url = 'https://dimensiondata.lightning.force.com/services/data/'

r = requests.get(sf_url)

pprint(r.json())
