"""
	Python Tutorial: Web Scraping with BeautifulSoup and Requests
	youtube.com/watch?v=ng2o98k983k
	&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=46
"""

# -- import resoureces
from bs4 import BeautifulSoup
import requests
import os 
import csv

# -- declare global variables 
# file_path = 'C:/Users/Joshua/Documents/GitHub/CoreyMSchafer/code_snippets/BeautifulSoup'
site = 'https://coreyms.com'
write_path = 'C:/Users/Joshua/Desktop/PERSONAL/Joshua Harvey/education/youtube/Corey Schafer/Python Tutorials/test'

# -- load and parse the simple.html file
# with open(os.path.join(file_path,'simple.html')) as file_load:
# 	file_parse = BeautifulSoup(file_load, 'lxml')

# -- load and parse the coreyms.com website 
site_text = requests.get(site).text
site_parse = BeautifulSoup(site_text, 'lxml')
# print(site_parse)


site_article = site_parse.find_all('article')

with open(os.path.join(write_path,'coreyms_webdata.csv'), 'w') as save_data:
	csv.writer(save_data, delimiter=',').writerow(['title','description', 'video url'])
	for item in site_article:
		# print(item.h2.text)

		article_ptext = item.find('div', class_='entry-content').p.text
		# print(article_ptext)
		# -- replace the below with item.find rather than intem.find_all 
		# for ptag in article_ptext:
		# 	print(ptag.p.text)

		try:
			ytube_id = item.iframe['src'].split('/')[4].split('?')[0]		
			ytube_url = f'https://youtube.com/watch?v={ytube_id}'
		except Exception as e:
			# raise e
			ytube_url = None

		# print(ytube_url)
		
		# -- write the data to a csv file
		# print(item.h2.text, article_ptext, ytube_url)
		
		csv.writer(save_data, delimiter = ',').writerow([item.h2.text,article_ptext,ytube_url])

		# -- if statement was replaced with try/except block above
		# if item.iframe == None:
		# 	pass
		# else:
		# 	ytube_id = item.iframe['src'].split('/')[4].split('?')[0]
		# 	print(f'https://youtube.com/watch?v={ytube_id}')
		# 	print()
		
		# print()


#print(site_article)

# for item in site_div:
# 	print(item.h2.a.text)
# print(site_div)

# 	# -- exploring the different attributes
# 	print(file_parse.div)
# 	print()
# 	print(file_parse.div.h2.text)
# 	print()
# 	print(file_parse.find('div', class_='article').p.text)
# 	print()

# 	for num, item in enumerate(file_parse.find_all('div', class_='article')):
# 		print(f'{num+1}, {item.h2.a.text}')
# 		print()
