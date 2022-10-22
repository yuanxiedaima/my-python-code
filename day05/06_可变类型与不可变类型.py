# @Time : 2022/1/26 22:58 
# @Author : Jface 
# @desc :
"""
可变类型: 列表、字典、集合
不可变类型: 数字类型(int, bool, float)、字符串、元组
可变类型：在地址不变的情况下，可以修改内容
不可变类型: 在地址不变的情况下，不可修改内容
"""
# 验证列表是可变类型
my_list = [1, 2, 3]
print(my_list, id(my_list))
my_list.append(4)
print(my_list, id(my_list))

my_list = [10, 20, 30]  # 引用指向改变
print(my_list, id(my_list))
print("=====分割线=====")
# 验证 int 是不可变类型
a = 10
print(a, id(a))
a = 20
print(a, id(a))

# 元组是不可变类型
my_tuple = (1, 2, 3)
# my_tuple[0] = 20
#  my_tuple[0] = 20 TypeError: 'tuple' object does not support item assignment
