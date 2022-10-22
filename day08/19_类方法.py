# @Time : 2022/2/2 18:59 
# @Author : Jface 
# @desc :
"""
类方法：为了方便处理类属性. 在没有创建实例对象时,也可以调用类方法操作类属性.
    1. 用装饰器 @classmethod 来标识其为类方法
    2. 一般以 cls 作为第一个参数，代表当前这个类，这个参数不用人为传参，解释器会自动处理
    3. 类方法调用：
        3.1 类名.类方法()    推荐用法
        3.2 实例对象名.类方法()
"""


class Dog(object):
    # 类属性
    count = 0

    # 实例方法: 创建实例对象后才能调用的方法
    # def print_count(self):
    # 1.用装饰器 @classmethod 来标识其为类方法
    @classmethod
    # 2. 一般以 cls 作为第一个参数，代表当前这个类，这个参数不用人为传参，解释器会自动处理
    def print_count(cls):
        print(cls.count)


# 类方法调用
# 1. 类名.类方法()    推荐用法
Dog.print_count()
# 2. 实例对象名.类方法()
dog1 = Dog()
dog1.print_count()
