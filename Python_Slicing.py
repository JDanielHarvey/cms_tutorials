ord_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#		    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#		  -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
unord_list = [1,9,2,5,8,4,7,6,3,0]
my_lets = ['a','b','c']

# -- modified list variables
unord_list.sort()

# -- usable parameters
unord_min = min(unord_list)
unord_max = max(unord_list)+1


# -- basic slicing
# print(ord_list[0::2])

# print(ord_list[-2:10:])

# print(ord_list[-1::-1])


# -- reversing a list of numbers with slicing (not sorted() function)
unord_list = unord_list[unord_max:unord_min:-1]

unord_list.append(unord_min)
print(unord_list)


ord_list = sorted(ord_list, reverse=True)
print(ord_list)

