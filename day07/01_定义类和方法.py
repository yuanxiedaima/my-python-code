# @Time : 2022/1/31 20:32 
# @Author : Jface 
# @desc :
"""
# 1. 定义类，设计一个类型
格式：
#class 类名:
#class 类名(): # 前2个旧式写法，不推荐
class 类名(object):
    方法列表（不是真的是列表，只是多个函数的定义）

# object所有类的祖先
# 类名：大驼峰命名
"""


# 定义类
class Dog(object):
    # 定义类的方法
    def eat(self):
        print("啃骨头")

    def drink(self):
        print("喝汤")


print(Dog)
