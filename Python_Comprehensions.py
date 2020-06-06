"""
    Python Tutorial: Comprehensions - How they work and why you should be using them
    https://www.youtube.com/watch?v=3dt4OGnU5sM
"""

nums = [1,9,2,4,3,9,4,3,0]

# -- creating list using standard for loop
# my_list = []
# for item in nums:
#     my_list.append(item)
#
# print(my_list)


# -- creating list using comprehension alternative
# my_list = [n for n in nums]
# print(my_list)


# -- creating list of nums**2 using standard for loop
# my_list = []
# for n in nums:
#     my_list.append(n**2)
# print(my_list)


# -- creating list of nums**2 using comprehension alternative
# my_list = [n**2 for n in nums]
# print(my_list)

# my_list = []
# for n in nums:
#     if n%2 == 0:
#         my_list.append(n)
#     else:
#         my_list.append(n+1)
# print(sorted(my_list))


# # if you want the all numbers with each letter once
# my_list = []
# for letter in 'abcd':
#     my_list.append(letter)
#     for num in range(4):
#         my_list.append(num)
# print(my_list)
#
# # or if you want the cartesian product of letters with numbers
# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)
#
# # or the comprehension approach
# my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list)

# character = ['iron man', 'ant man', 'hulk', 'loki', 'thanos']
# color = ['crimson', 'red', 'green/purple', 'black', 'purple']

# dict = {}
# for character,color in zip(character,color):
#     dict[character] = color
# print(dict)

# dict = {character: color for character, color in zip(character,color) if character != 'loki'}
# print(dict)

# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)

# def gen_func(param):
#     for n in param:
#         yield(n**2)
#
# gen_l = gen_func(nums)

gen_l = (n**2 for n in nums)

for i in gen_l:
    print(i)