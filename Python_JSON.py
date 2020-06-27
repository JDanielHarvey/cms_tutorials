'''
	Python Tutorial: Working with JSON Data using the json Module
	https://www.youtube.com/watch?v=9N6a-VLBa2I

	See encoding on pythong docs
	https://docs.python.org/3/library/json.html#encoders-and-decoders
'''

import json
import os
from urllib.request import urlopen

# __ simply convert a string(valid-json) to python object(dict) and vice versa
calls_data = '''{
	"calls": [
		{
			"name": "Joshua",
			"phone": "+12132228109",
			"email": "joshua.d.harvey@gmail.com",
			"state": "AZ"
		},
		{
			"name": "Rebecca",
			"phone": "+16025504914",
			"email": "rebeccaleewinter@gmail.com",
			"state": "AZ"
		},
		{
			"name": "Diane",
			"phone": "+17275607414",
			"email": null,
			"state": "FL"
		}
	],
	"records": 3,
	"pages": 1
}'''

json_data = json.loads(calls_data)
json_calls = json.loads(calls_data)

print(type(calls_data))
print()
print(type(json_data))
print()
print(json_data)
print()
print(type(json_data['calls']))
print()

for call in json_calls['calls']:
	del call['email']
	print(call)

print()
calls_data_mod = json.dumps(json_calls, indent = 2, sort_keys=True)

print(calls_dad)



# __ load json files into python objects and write back to json

# json_filepath = 'C:/Users/Joshua/Documents/GitHub/CoreyMSchafer/code_snippets/Python-JSON/'
# write_path = 'C:\\Users\\Joshua\\Desktop\\PERSONAL\\Joshua Harvey\\education\\youtube\\Corey Schafer\\Python Tutorials\\test'

# with open(os.path.join(json_filepath,'states.json'),'r') as file_read:
# 	# -- loads method with .read method is alternative to just .load method
# 	# states = json.loads(file_read.read())
# 	states = json.load(file_read)
# 	# print(states)	

# 	for state in states['states']:
# 		del state['area_codes']
# 	# print(states)

# with open(os.path.join(write_path,'jdhJSON.json'),'w') as file_write:
# 	json.dump(states, file_write, indent=2)


# __ pulling an API to work with JSON
pholder_api_path = 'https://jsonplaceholder.typicode.com/posts'

dicty = {}

with urlopen(pholder_api_path) as api_resp:
	
	# for post in json.loads(api_resp):
	# 	print(post)
	
	py_obj = json.load(api_resp)

	js_obj = json.dumps(py_obj, indent=2)

	# print(py_obj)
	# print(len(py_obj))
	# print()
	# print(py_obj)
	# print(js_obj)

	for user in py_obj:
		print(user['userId'], user['id'])
		
		# dicty[user['userId']] = user['id']
		# print(dicty)