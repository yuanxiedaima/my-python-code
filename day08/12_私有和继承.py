# @Time : 2022/2/1 21:44 
# @Author : Jface 
# @desc :
"""
私有和继承: 私有属性和方法不能直接继承使用
"""


# 定义一个父类 Animal
class Animal(object):
    def __init__(self):
        # 定义一个私有属性
        self.__type = "动物"

    # 定义一个私有方法
    def __leave(self):
        print("休产假三个月")

    def print_info(self):
        # 通过父类的公有方法可以间接访问父类的私有属性和私有方法
        print(self.__type)
        self.__leave()


# 定义一个子类
class Dog(Animal):
    def test(self):
        # print(self.__type)
        # print(self.__leave)
        pass


# 创建子类对象
dog1 = Dog()
dog1.test()
dog1.print_info()
