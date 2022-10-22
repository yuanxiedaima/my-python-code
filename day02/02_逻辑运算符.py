# @Time : 2022/1/23 14:32 
# @Author : Jface 
# @desc :
"""
and: 并且， 左右2边都为True，结果才为True
or:  或者， 只有有1个为True，结果为True
not: 非，取反，原来是True就变成False
"""
print(True and True)
print(True and False)
print(False and True)
print(False and False)

a = 20
b = 15
print((a > 10 and b > 10))
print("---------------")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print("---------------")
print(not True)
print(not False)

