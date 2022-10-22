# @Time : 2022/2/1 19:55 
# @Author : Jface 
# @desc :
"""
__init__方法：
    1. 作用：添加属性
    2. 特点：创建对象的时候，实例化对象，自动调用__init__方法
    3. 设置参数，创建对象时，除了self参数不用人为处理，其它参数需要和__init__参数匹配
        对象名 = 类名(实参1， 实参2) ====》 __init__(self, 形参1, 形参2)
"""

class Dog(object):
    # 用两个下划线包裹的方法叫魔法方法,而且魔法方法的名字是有系统定义,由用户重新实现它.
    def __init__(self, _name):
        # 使用类创建对象时,会自动调用__init__方法
        self.name = _name  # __init__方法的作用是给对象添加属性
        print("init被调用了")

    def eat(self):
        print("%s 啃骨头" % self.name)

    def drink(self):
        print("%s 喝肉汤" % self.name)


# 创建对象，实例化对象，自动调用__init__方法
dog1 = Dog("旺财")    # 自动调用__init__(dog1, "旺财")
dog1.eat()

dog2 = Dog("来福")    # 自动调用__init__(dog2, "来福")
dog2.eat()