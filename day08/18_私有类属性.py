# @Time : 2022/2/2 18:56 
# @Author : Jface 
# @desc :
"""
私有的类属性, 不能在类的外部访问, 只能在类的内部访问
"""


class Dog(object):
    # 私有的类属性，不能在类的外部访问，只能在类的内部访问
    __count = 0

    def print_count(self):
        print(self)
        print(Dog.__count)


# print(Dog.__count)
# AttributeError: type object 'Dog' has no attribute '__count'

d1 = Dog()
d1.print_count()
