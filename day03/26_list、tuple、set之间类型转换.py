# @Time : 2022/1/24 22:24 
# @Author : Jface 
# @desc :
"""
列表类型名：list
元组类型名：tuple
集合类型名：set
list(x):    x转换为列表类型
tuple(x):   x转换为元组类型
set(x):     x转换为集合类型
"""

# 列表转元组、集合 类型
my_list = [1, 2, 3, 5, 3, 5]  # 列表可以修改
# 列表转换为元组类型
my_tuple = tuple(my_list)  # 元组不能修改
print(my_tuple)
# 列表转换为集合类型
my_set = set(my_list)  # 集合不会出现重复
print(my_set)

print('============华丽分割线============')

# 元组转列表、集合 类型
my_tuple = (1, 2, 3, 5, 3, 5)
# 元组转换为列表 类型
my_list = list(my_tuple)
print(my_list)
# 元组转换为集合 类型
my_set = set(my_tuple)
print(my_set)

print('============华丽分割线============')

# 集合转元组、列表 类型
my_set = {1, 2, 3, 5}
# 集合转换为列表 类型
my_list = list(my_set)
print(my_list)
# 集合转换为元组 类型
my_tuple = tuple(my_set)
print(my_tuple)

# 扩展: 字符串转换:
print('============华丽分割线============')
my_str = "hello"
print(list(my_str))
print(tuple(my_str))
print(set(my_str))

my_list = ["h", "e", "l", "l", "o"]
my_str = "".join(my_list)
print(my_str)
