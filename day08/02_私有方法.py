# @Time : 2022/2/1 20:46 
# @Author : Jface 
# @desc :
"""
    1. __(2个下划线)开头的方法，就是私有方法
    2. 只能在本类的内部访问，在类的外面无法直接访问
    3. 在类的内部调用实例方法的语法格式：self.方法名()
"""


class Dog(object):
    def __init__(self):
        # __(2个下划线)开头的属性，就是私有属性
        self.__baby_count = 0
        # 公有属性
        self.age = 1

    def print_info(self):
        # 私有属性，只能在本类内部访问，在类的外面无法直接访问
        print(self.__baby_count)
        self.__leave()

    # 定义一个私有方法: __(2个下划线)开头的方法，就是私有方法
    def __leave(self):
        print("休产假了")


dog1 = Dog()
dog1.print_info()
# AttributeError: 'Dog' object has no attribute '__leave'
# dog1.__leave() # err, 外部不能访问私有方法
