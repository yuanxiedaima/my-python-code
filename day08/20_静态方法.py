# @Time : 2022/2/2 19:16 
# @Author : Jface 
# @desc :
"""
静态方法：
    1. 需要通过装饰器@staticmethod来进行修饰默认情况下
    2. 既不传递类对象也不传递实例对象（形参没有self/cls）
    3. 静态方法调用：
        3.1 类名.静态方法()    推荐用法
        3.2 实例对象名.静态方法()
"""


class Dog(object):
    # 1. 需要通过装饰器@staticmethod来进行修饰默认情况下
    @staticmethod
    # 2. 既不传递类对象也不传递实例对象（形参没有self/cls）
    def foo():
        # 实例属性: self.属性
        # 类属性: cls.属性
        print("一个与实例属性和类属性无关的函数")


# 3. 静态方法调用：
# 3.1 类名.静态方法()    推荐用法
Dog.foo()
# 3.2 实例对象名.静态方法()
dog1 = Dog()
dog1.foo()
