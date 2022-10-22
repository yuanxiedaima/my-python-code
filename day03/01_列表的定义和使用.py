# @Time : 2022/1/23 16:12 
# @Author : Jface 
# @desc :
"""
列表定义的格式：
列表变量的名字 = [元素1, 元素2, ……]

使用格式：
    列表变量[位置]
    位置：也叫下标、索引 (可以是正数或者负数)
"""

# 列表的定义
name_list = ['rose', 'mike', 'tom', 'lily', 'jack', 1, 2, 3]

# 最后一个元素取出来
print(name_list[7])
print(name_list[-1])

# 访问列表元素，不要超出范围，不要越界
# 报错: IndexError: list index out of range
# print(name_list[8])
