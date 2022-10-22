# @Time : 2022/2/2 18:50 
# @Author : Jface 
# @desc :
"""
# 类属性修改，只能通过类名修改，不能通过对象名修改
# 对象名.变量 = 数据 默认操作给实例对象添加实例属性，已经不能操作类属性
# 如果类属性名字和实例属性名字相同，实例对象名只能操作实例属性
"""


class Dog(object):
    # 类属性
    count = 0


d1 = Dog()
print(Dog.count)  # 0 使用类名访问类属性
print(d1.count)  # 0 使用实例对象访问类属性

Dog.count = 1  # 只能使用类名修改类属性
print(Dog.count)  # 1
print(d1.count)  # 1

d1.count = 250  # 使用实例对象添加一个实例属性，只不过名字和类属性名字相同，只能操作实例属性
print(Dog.count)  # 1
print(d1.count)  # 250 由于类属性名字和实例属性名字相同，只能操作实例属性
