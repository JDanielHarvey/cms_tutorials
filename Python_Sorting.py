"""
    Python Tutorial: Sorting Lists, Tuples, and Objects
    https://www.youtube.com/watch?v=D3JvDWO-BY4
"""

# print(help(sorted))

li = [-5,-9,-1,-3,1,9,4,2,8,2,5,3,8,7]
tup = (1,9,4,2,8,2,5,3,8,7)
di = {'name': 'Joshua', 'job': 'Data Scientist', 'age': 32, 'os': 'Windows 10'}


s_li = sorted(li)
s_tup = sorted(tup)
s_di = sorted(di)

# sorts the list in place and then returns 'None'
print('''
    prints using the sort method on the li variable
    which is limited to list types''')
print(li.sort())
print(li)

print('''
    prints using the sorted function on the li variable
    which can be used on lists and tuples''')
print(s_li)

print('''
    prints using the sorted function with the reverse argument - another advantage of
    using the function over the method''')
print(sorted(li, key=abs))

print('''
    prints using the sorted function on the dictionary''')
print('Dict\t', s_di)

