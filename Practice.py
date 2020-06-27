
# -- parsing and writing CSV files 
# import csv

# path = 'C:/Users/Joshua/Documents/GitHub/CoreyMSchafer/code_snippets/Python-Patreon-CSV/'

# with open('{}patrons.csv'.format(path), 'r') as file:
# 	file_read = csv.DictReader(file)

	
# 	# next(file_data)

# 	with open('{}practice.csv'.format(path), 'w') as file2:
# 		fields = ['FirstName','LastName', 'Email', 'Pledge', 'Lifetime', 'Status', 'Country', 'Start']
# 		file_write = csv.DictWriter(file2, fieldnames = fields, delimiter = ',')

# 		file_write.writeheader()

# 		for row in file_read:
# 			file_write.writerow(row)


	
import os 
print(os.getcwd())
print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])



# colors = ["red", "green", "blue", "purple"]
# ratios = [0.2, 0.3, 0.1, 0.4]
# for i, color in enumerate(colors):
#     ratio = ratios[i]
#     print("{} - {}% {}".format(i, ratio * 100, color))