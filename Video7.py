#
'''
    Python Tutorial for Beginners 7: Loops and Iterations - For/While Loops
'''

my_string = 'Joshua'

nums = [101,102,103,104,105,106,107,108,109]

# for index, item in enumerate(nums, start=1):
#     if index >= 8:
#         break
#     print(index, item)
#
# print('''
# ''')
#
# for index, item in enumerate(nums, start=1):
#     if index <= 8:
#         print(index, item)

# print('''
# ''')
#
# for index, item in enumerate(nums, start=1):
#     if index == 3:
#         print(index, '')
#     print(index, item)

# for i in nums:
#     for letter in 'xyz':
#         print(i, letter)

# for i in range(1, len(my_string)+1):
#     for letter in 'abc':
#         print(i, letter)

iterator = 0
end_value = 10

while iterator < end_value + 1:
    if iterator == 3:
        print('')
    print(iterator)
    iterator += 1
