# @Time : 2022/1/31 20:50 
# @Author : Jface 
# @desc :
"""
__init__方法：
    1. 作用：添加属性
    2. 特点：创建对象的时候，实例化对象，自动调用__init__方法
"""


# 定义类
class Dog(object):
    # 用两个下划线包裹的方法叫魔法方法,而且魔法方法的名字是有系统定义,由用户重新实现它.
    def __init__(self):
        # 使用类创建对象时,会自动调用__init__方法
        self.name = "大黄狗"  # __init__方法的作用是给对象添加属性
        print("init被调用了")

    def eat(self):
        print("%s 啃骨头" % self.name)

    def drink(self):
        print("%s 喝肉汤" % self.name)


# 1. 创建对象，实例化对象，自动调用__init__方法
dog1 = Dog()

dog1.eat()
dog1.drink()
