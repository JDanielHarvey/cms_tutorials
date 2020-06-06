"""
	Python Tutorial: File Objects - Reading and Writing to Files
	https://www.youtube.com/watch?v=Uh2ebFW8OYM
	&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=25
"""
import os
import codecs 

path = 'C:/Users/Joshua/Documents/GitHub/CoreyMSchafer/code_snippets/Python-Files/'

file_size = os.path.getsize(f'{path}test.txt')
file_size_comp = round(file_size/4)


with open(f'{path}test.txt' ,'r') as file_read:
	print(file_read.encoding)

	print(f'{len(file_read.read(10))} is remaining data in file')

	print(f'{len(file_read.read(20))} is remaining data in file')

	print('should be 143 remaining characters in the file - that is 30 - 173')

	print(codecs.getencoder(file_read.encoding))
	print(codecs.getreader(file_read.encoding))
	# -- this section illustrates meta data attributes on open() object 
	# print(file_read.name)
	# if file_read.mode == 'r':
	# 	print('Read mode only')
	# print(file_read.closed)

	
	# -- this sections reads all lines or individual lines 
	# print(file_read.readlines())
	# print(file_read.readline())


	# -- this section reads chunks of the file based on characters
	# print(file_read.read(10), end='\n')

	# file_read.seek(0)
	
	# print(file_read.read(10), end='\n')


	# -- this sections writes to a file the data from the read file 
	# file_contents = file_read.read()
	# with open(f'{path}jdh_test.txt', 'w') as file_write:

	# 	file_write.write(file_contents)

		# help(.write('help seek'))

# print(file_read.closed)

# dwn_path = 'C:/Users/Joshua/Downloads/'

# with open(f'{dwn_path}UberEats - Promo.JPG', 'r') as img_read:
# 	print(img_read)


# -- look for other videos to continue learning about files for topics such as 
# -- in-memory files and temporary files