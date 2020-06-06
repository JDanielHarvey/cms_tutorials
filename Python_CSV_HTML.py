"""
	Python Tutorial: Real World Example - Parsing Names From a CSV to an HTML List
	https://www.youtube.com/watch?v=bkpLhQd6YQM
	&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=29
"""

import csv

path = 'C:/Users/Joshua/Documents/GitHub/CoreyMSchafer/code_snippets/Python-Patreon-CSV/'
html_out = ''
names = []

with open('{}patrons.csv'.format(path), 'r') as file_input:
	csv_read = csv.reader(file_input)

	# -- skips over useless first rows
	next(csv_read)
	next(csv_read)

	# -- use list to print all items at once
	# print(list(csv_read))

	# -- using an iterable to display data
	for row in csv_read:
		if row[0] == 'No Reward':
			break
		names.append('{} {}'.format(row[0],row[1]))

# -- this section builds the HTML unordered list
html_out += '<p> There are currently {} contributors on patron. Thank you! </p>'.format(len(names))

html_out += '\n<ul>'

for person in names:
	html_out += '\n\t<li>{}</li>'.format(person)

html_out += '\n</ul>'


print(html_out)





# # -- the indented section was to practice from previous lesson - see Python_CSV.py
# 	# -- this section writes the new csv file
# 	with open('{}jdh_patrons.csv'.format(path), 'w') as patron2:
# 		fields = ['Email', 'FirstName','LastName']
# 		dict_write = csv.DictWriter(patron2, fieldnames=fields)

# 		for row in csv_read:
# 			del row['Lifetime'], row['Country'], row['Start'], row['Pledge'], row['Status']
# 			dict_write.writerow(row)

# 	-- this section prints to the console 
# 	for row in csv_read:
# 		del row['Lifetime'], row['Pledge'], row['Status'], row['Country'], row['Start']
# 		print(row)
# 		print((row['FirstName'], row['LastName']))