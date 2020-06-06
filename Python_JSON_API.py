"""
	How to Write Python Scripts to Analyze JSON APIs and Sort Results

	https://www.youtube.com/watch?v=1lxrb_ezP-g
	&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=107
"""
import os 
import requests
import json

# print(dir(json))

req_get = requests.get('https://formulae.brew.sh/api/formula.json')

# print(req_get.ok)
# print()
# print(req_get.status_code)
# print()
# print(req_get.headers)

print(req_get.json())