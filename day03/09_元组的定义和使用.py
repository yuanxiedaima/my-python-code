# @Time : 2022/1/23 21:06 
# @Author : Jface 
# @desc :
"""
# 列表：列表变量 = [元素1, 元素2, ……]
# 元组：元组变量 = (元素1, 元素2, ……)
"""
name_list = ["rose", "mike", "lily", "tom"]
print(type(name_list))

name_tuple = ("rose", "mike", "lily", "tom")
print(type(name_tuple))
# 取出第 0 个元素
print(name_tuple[0])

# 元组只有 1 个元素的时候，格式：(元素,)
name_list2 = [250]
print(type(name_list2))

name_tuple2 =(250,)
print(type(name_tuple2))

# 元组的元素只读，不能改
# name_tuple[0] = "jack"
# TypeError: 'tuple' object does not support item assignment
print(name_tuple[0])
print(len(name_tuple))

if "rose" in name_tuple:
    print("%s在元组当中" % "rose")

# 循环遍历和列表一样
for name in name_tuple:
    print(name)