'''
	Python Quick Tip: Hiding Passwords and Secret Keys in Environment Variables (Windows)

	https://www.youtube.com/watch?v=IolxqkL7cD8
	&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=56&t=0s
'''

import os 

db_un = os.environ.get('AVP_GCSQL_UN')
db_pw = os.environ.get('AVP_GCSQL_PW')

print(db_un)
print(db_pw)
print()

for item in os.environ:
	print(item)

# db_user = ''
# db_password = ''

# print(db_user)
# print(db_password)

