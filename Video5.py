#
'''
    Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs
'''
#
colleagues = {'name': 'Joshua', 'age': 30, 'duties': ['Digital Ads', 'Reporting']}

print('''
#.get method and adding a key/value''')
print(colleagues.get('height','#N/A'))



colleagues['phone'] = '213-222-8109'
print(colleagues.get('phone'))

colleagues.update({'age': 31, 'duties': ['Digital Ads', 'Reporting', 'Programming']})
print('''
#updated colleagues''')
print(colleagues)

print('''
#delete from colleagues''')
del colleagues['phone']
print(colleagues)

print('''
showing values for keys, values and both''')
print(colleagues.keys())
print(colleagues.values())
print(colleagues.items())
print('''
''')

for key, value in colleagues.items():
    print(key, value)