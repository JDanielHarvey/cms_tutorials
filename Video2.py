#Watching videos with Corey Schafer

	#line1
greeting = "What's up"
firstname = "joshua"
lastname = "harvey"
messageConcat = greeting + ', ' + firstname + ' ' + lastname + ". You are the best at Python! (concat method)"
messageFormat = "{}, {} {}. You are the best at Python {}, {}! (format method)".format(greeting, firstname, lastname, firstname, lastname)
messageString = f'{greeting}, {firstname.upper()} {lastname}. You are the best at Python! (string method)'

# print(firstname.count('jos'))

# print(firstname.find('hua'))

# print(firstname.replace('ua',''))

# print(messageConcat)

# print(messageFormat)

print(messageString)
