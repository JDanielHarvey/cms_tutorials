"""
	Python Tutorial: OS Module - Use Underlying Operating System Functionality
	https://www.youtube.com/watch?v=tJxcKyFMTGo
	&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=23
"""

import os
from datetime import datetime

path = 'C:/Users/Joshua/Desktop/PERSONAL/Joshua Harvey/education/youtube/Corey Schafer/Python Tutorials/test/'
# -- dir is good on imported modules 

# for item in dir(os):
# 	print(item)


# print(os.getcwd())

# os.chdir(path)

# print(os.getcwd())

# print('\n')

# os.makedirs('level_one/level_two')

# list_dir_items()
# print('\n')

# os.rmdir('level_one')

os.chdir(path)
for items in os.listdir():
	print(items)
	if items == 'stat_file.txt':
		os.remove('stat_file.txt')

with open(f'{path}scat_file.txt', 'w') as write_file:
	write_file.write(f'The follwoing items exist within the following directory path:\n{path}')
	for item in os.listdir():
		write_file.write(item)
		print()
		
os.rename('scat_file.txt', 'stat_file.txt')


# -- this secion works with os.stat()
print(os.stat('stat_file.txt'))

print('\n')

print(os.stat('stat_file.txt').st_size)
print(os.stat('stat_file.txt').st_mtime)
print(datetime.fromtimestamp(os.stat('stat_file.txt').st_mtime))
print('\n')
# for stat in os.stat('stat_file.txt'):
# 	print(stat)

print(os.walk(path))

for dpaths, dnames, files in os.walk(path):
	print(dpaths)
	print(dnames)
	print(files)
	print()

# -- this section works with os.environ and os.path()
# print(os.environ)
print(os.environ.get('PUBLIC'))

fake_path = os.path.join(os.environ.get('PUBLIC'), 'ospathjoin.txt')

full_path = os.path.join(path, 'stat_file.txt')

print(os.path.basename(full_path))

print(os.path.split(full_path))


print(os.path.exists(full_path))
print(os.path.exists(fake_path))
print(os.path.isdir(path))
print(os.path.isfile(full_path))
print(os.path.splitext(os.path.basename(full_path)))
print('\n')
print(dir(os.path))