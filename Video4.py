# '''
#     this section is all about lists
# '''

# animals = ['dog', 'cat', 'bird']
# animals2 = ['lizard', 'fish', 'hamster']
# nums = [1,5,2,3,7,4]
#
# animals.append('snake')
# animals.insert(0, 'snake')
#
# animals.extend(animals2)
#
# animals.remove('snake')
#
# animals.pop()
#
# length = len(animals)-1
# length_full = len(animals)
#
#
# print(animals[-1] + """(printing -1 index)
#  """)
#
# animals.reverse()
#
# animals = sorted(animals)
#
# animals.sort(reverse=True)
#
# sorted_animals = sorted(animals)
#
# print(min(animals))
# print(max(animals))
#
# print(animals.index('bird'))
#
# animals.extend(animals2)
# animals_index = animals.index('hamster')
#
# print(animals_index)
#
#
# for number, item in enumerate(animals, start=1):
#     print(number, item)
#
# animals_join = ', '.join(animals)
#
# animals_split = animals_join.split(', ')
#
# print(animals_split[1])

# '''
#     this section is all about tuples and sets
# '''

# family_list = ['Joshua', 'Jazzy', 'Joshua', 'Rebecca', 'John', 'Joshua', 'Diane']
# family_tuple = ('Joshua', 'Jazzy', 'Joshua', 'Rebecca', 'John', 'Joshua', 'Diane')
# family_set = {'Joshua', 'Jazzy', 'Joshua', 'Rebecca', 'John', 'Joshua', 'Diane'}
#
# family_list.extend(['Deborah'])
#
# print(family_list)
# print(family_tuple)
# print(family_set)


# set_one = {'Math', 'Science', 'English', 'History'}
# set_two = {'Geography', 'Math', 'Science', 'History'}

# set_one = {'Math', 'Science', 'English', 'History'}
# set_two = {'Math', 'Anatomy', 'Science', 'History'}

# print(set_one.difference(set_two))

# set_full = set_one.union(set_two)
#
# if ('Geography' in set_full):
#     print("Geography exists here")
# elif ('Math' in set_full):
#     print('but Math does eixst, so we\'re safe')

# for i in range(len(set_full)):
#     print(set_full[0])

# Empty Lists
# empty_list = [] #or empty_list = list()
# empty_tuple = () #or empty_tuple = tuple()
# empty_set = set() #no other option
