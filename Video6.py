#
'''
    Python Tutorial for Beginners 6: Conditionals and Booleans - If, Else, and Elif Statements
'''
#

agent = 'biomimicry'

if agent.find('mimic') > 0 or type(agent) == str:
    print('You are authorized to enter')
else:
    print('You are not authorized')

agent
