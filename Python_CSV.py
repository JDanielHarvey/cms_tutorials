import csv

path = 'C:/Users/Joshua/Documents/GitHub/CoreyMSchafer/code_snippets/Python-CSV/'

with open('{0}names.csv'.format(path)) as csv_file:
	csv_reader = csv.DictReader(csv_file)

	# -- this method reads row using the index to control which fields to pull
	# for row in csv_reader:
	# 	print((row[0], row[1], row[2]))


	# -- del function or ommitted fields 
	for index, row in enumerate(csv_reader):
		del row['last_name']
		print(row)
		# -- recreates the dictionary with a surrogate key
		# print({'id': index, 'last_name': row['last_name']})
		# print(row['first_name'], row['last_name'])


	# with open('{}dict.csv'.format(path), 'w') as new_file:
	# 	fields = ['first_name', 'last_name', 'email']

	# 	dict_writer = csv.DictWriter(new_file, fieldnames=fields, delimiter=',')

	# 	dict_writer.writeheader()	

	# 	for row in csv_reader:
	# 		dict_writer.writerow(row)

	# with open('{}joshuas_list4.csv'.format(path), 'w') as new_file:
	# 	csv_writer = csv.writer(new_file, delimiter='-')

		# for row in csv_reader:
			# -- this method uses no variables just to show with no abstraction
			# csv.writer(open('{}joshuas_list.csv'.format(path), 'w'), delimiter='-').writerow(row)

			# -- 
			# csv_writer.writerow(row)



	# next(csv_reader)
	# for row in csv_reader:
	# 	print(row)
		# print(row[::-1])
		# print(row[-1:-4:-1])