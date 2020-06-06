'''
	Python Pandas Tutorial (Part 1): Getting Started with Data Analysis - Installation and Loading Data

	https://www.youtube.com/watch?v=ZyhVh-qRZPA
	&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=129&t=0s
'''

import os
import pandas as pd

os.chdir('./data/')
# print(os.getcwd())
# print()
# print(os.listdir())

df = pd.read_csv('./survey_results_public.csv')
df_schema = pd.read_csv('./survey_results_schema.csv')

print(df.shape)
print()
# print(df.info())
# print()

# -- prints all columns or rows (respectively) from data set in data-frame
# pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)
# print(df)

print(df.head(3))
print()
print(df_schema.head(3))

print('\n_________')

print(df.tail(3))
print()
print(df_schema.tail(3))
