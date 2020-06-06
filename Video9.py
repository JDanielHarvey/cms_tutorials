#
"""
    Python Tutorial for Beginners 8: Functions

    making changes to the python path environment variable
    using command prompt type:
    export PYTHONPATH="/Users/Joshua/Desktop/"
"""
# import sys
# sys.path.append('C:/Users/Joshua/Desktop/PERSONAL/Joshua Harvey/education/youtube/Corey Schafer/Python Tutorials/test')
#
# import Video9_module as t
#
# from Video9_module import my_name as mn, compute_name as cn
# from Video9_module import * #this is another way to import everything
#
#
# for index, item in enumerate(sys.path, start=1):
#     print(index, item)
#
# print('''calling my_name via import with from as mn (alias)''')
# print(mn())
#
# print('''calling my_name via import with as t (alias)
# ''')
# print(t.my_name())
#
# print('''calling my_name via import with from as cn (alias)
# ''')
# print(cn())

import random
import calendar
import datetime
import os
#import math

years = [2017,2018,2019,2020]
animals = ['duck', 'pig', 'cat', 'dog', 'horse']

print(random.choice(animals))

print(datetime.date.today())

print(os.getcwd())

print(os.__file__)


print('''
''')

for index, year in enumerate(years):
    print(index, year, calendar.isleap(year))