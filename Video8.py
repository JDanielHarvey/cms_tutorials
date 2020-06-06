#
"""
    Python Tutorial for Beginners 8: Functions
"""

def my_function():
    """testing, can you read this?"""
    x = input('enter your first name: ')
    y = input('enter your last name: ')
    #x = x.upper()
    if x == y:
        return print('''That isnt your real name is it?
        lets try again'''), my_function()
    return x.upper(), y.upper()

print(my_function())




