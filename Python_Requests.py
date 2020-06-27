"""
	Python Requests Tutorial: Request Web Pages, Download Images, POST Data, Read JSON, and More

	https://www.youtube.com/watch?v=tb8gHvYlCFs
	&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=100
"""

import os 
import requests

# __ working with xkcd.com image and saving the file to local drive directory
save_dir = 'C:\\Users\\Joshua\\Desktop\\PERSONAL\\Joshua Harvey\\education\\youtube\\Corey Schafer\\Python Tutorials\\test'
req_resp = requests.get('https://imgs.xkcd.com/comics/python.png')
req_text = req_resp.text

print(dir(requests))
print(dir(req_data))

print(req_resp.status_code)
print(req_resp.content)
print(req_resp.headers)
print()
print(req_resp.headers['Content-Type'])


with open(os.path.join(save_dir, 'comic.png'), 'wb') as save_file:
	save_file.write(req_resp.content)


# __ working with httpbin.org 

# __ httpbin get route
payload = {'page': 2, 'count': 25} 
req_resp = requests.get('https://httpbin.org/get', params=payload)
print(req_resp.url)
print(req_resp.text)

# __ httpbin post route
payload = {'user_name': 'Joshua', 'password': 'testing'} 
req_res = requests.post('https://httpbin.org/post', data=payload)
print(req_resp.text)

req_dict = req_res.json()
print(req_dict)
print()
print(req_dict['form'])

-- an alternative way would be to use the module 'import json' with json.loads(req_res.text)


# __ httpbin authentication

# -- req_get.ok will provide boolean value if code was anything below 400, so 200's or 300's 
resource_auth = 'https://httpbin.org/basic-auth/jdharvey/longpass'

try:
	req_get = requests.get(resource_auth, auth=('jdharvey','longpass'))
	print(req_get.text)
except Exception as e:
	print(f'Error of type: {req_get}')


# __ httpbin for delays with timeout argument in requests.get()
resource_delay = 'https://httpbin.org/delay/5'

try:
	req_get = requests.get(resource_delay, timeout=4)
	print(req_get)
except Exception as e:
	req_get = requests.get(resource_delay, timeout=6)
	print('Your request took longer than expected')
	print()
	print(req_get)


