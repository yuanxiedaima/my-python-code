# @Time : 2022/2/1 20:43
# @Author : Jface
# @desc :
"""
私有属性：
    1. __(2个下划线)开头的属性，就是私有属性
    2. 只能在本类的内部访问，在类的外面无法直接访问
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


dog1 = Dog()

# 私有属性 只能在本类的内部访问，在类的外面无法直接访问
# print(dog1.__baby_count)  # AttributeError: 'Dog' object has no attribute '__baby_count'
# 公有属性 在类的内外都能访问
print(dog1.age)

dog1.print_info()
