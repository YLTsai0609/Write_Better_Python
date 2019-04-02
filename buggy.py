# coding=utf-8

my_list = [5, 2, 1, True, "abcdefg", 3, False, 4]

# a slower way to do it
# del my_list[3]
# print(my_list)
# del my_list[4]
# print(my_list)
# del my_list[6]
# print(my_list)

# use pdb
# n for next, interactive with variable name, c for continue
import pdb;pdb.set_trace()
del my_list[3]  # [5, 2, 1, "abcdefg", 3, False, 4]
del my_list[3]  # [5, 2, 1, 3, False, 4]
del my_list[4]  # [5, 2, 1, 3, False, 4]
print(my_list)

