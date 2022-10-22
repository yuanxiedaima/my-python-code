# @Time : 2022/1/23 20:59 
# @Author : Jface 
# @desc :
"""
if…in：判断某个元素是否在列表中，如果在，if的条件为True
for…in：从头到尾 依次从 列表 中取出 每一个元素，这个元素给name赋值
"""
name_list =['rose', 'tom', 'jack', 'mike']
name = 'tom'
# if…in：判断某个元素是否在列表中，如果在，if的条件为True
if name in name_list:
    print("%s在列表中" % name)

print("========华丽分割线==========")
# for…in：从头到尾 依次从 列表 中取出 每一个元素，这个元素给name赋值
for name in name_list:
    print(name)