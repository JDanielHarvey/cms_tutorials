



# __ learning various methods and attributes of the datetime module
print(datetime.date.today())
print()
print(datetime.date.today().day)
print()
print(datetime.date.today().weekday())
print(str(datetime.date.today().isoweekday()))

tday = datetime.date.today()
tdelta = datetime.timedelta(days=1)	
date_string = str(tday - tdelta).replace('-','')

# print(dir(date_string))
# print(help(date_string.format_map))