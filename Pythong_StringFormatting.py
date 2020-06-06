import datetime

person_d = {'name': 'Rebecca', 'age': 27}
person_l = ['Rebecca', 27]

# sentence = 'My name is ' + person['name']

# -- using implicit position of arguments to be received in {} placeholders
sentence = 'My name is {} and I am {} years of age!'.format(person_d['name'], person_d['age'])

# -- using numbers for positions of arguments to be received in {} placeholders
sentence = 'My name is {1} and I am {0} years of age!'.format(person_d['age'], person_d['name'])

# -- using number and dict keys for values to be received in {} placeholders
sentence = 'My name is {0[name]} and I am {0[age]} years of age!'.format(person_d)

# -- using number from dict and list to retrieve values for {} placeholders
sentence = 'My name is {0[name]} and I am {1[1]} years of age! (dict & list)'.format(person_d,person_l)

print(sentence)


class Person():

	def __init__(self,name,age):
		self.name = name
		self.age = age

p1 = Person('Joshua', 31)

sentence = 'My name is {0.name} and I am {0.age} years of age! (class attributes)'.format(p1)

print(sentence)



sentence = 'My name is {name} and I am {age} years of age! (set variables)'.format(name='John', age=60)

print(sentence)



person_dict = {'name': 'Diane', 'age': 60}

sentence = 'My name is {name} and I am {age} years of age! (unpack dict)'.format(**person_dict)

print(sentence)


for n in range(1,10):
	nums_sent = 'The value is {:02}'.format(n)
	print(nums_sent)

pi = 3.14159265

# -- print parameter to specified number of decimal places 
sentence = 'Pi is equal to {:.2}'.format(pi)
print(sentence)


# -- formatting large numbers and specifying decimal places
sentence = '1MB consists of {:,.2f} bytes'.format(1000**2)
print(sentence)

my_date = datetime.datetime(2020, 9, 22, 7, 59, 11)

print(my_date)

sentence = '{:%B (%m) %d, %Y} is the current date time'.format(my_date)

print(sentence)

sentence = '{0:%B (%m) %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year!'.format(my_date)

print(sentence)