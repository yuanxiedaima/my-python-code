# @Time : 2022/2/1 21:37 
# @Author : Jface 
# @desc :
"""
子类调用父类同名方法：
1. 父类名.同名方法(self, 形参1, ……)：调用指定的父类
2. super(类名, self).同名方法(形参1, ……)：调用继承顺序中类名的下一个类的同名方法
3. super().同名方法(形参1, ……) ：调用先继承父类的同名方法
"""


class SmallDog(object):
    def eat(self):
        print('吃小东西')


class BigDog(object):
    def eat(self):
        print('啃大骨头')


# 定义一个子类，多继承于上面2个父类
class SuperDog(SmallDog, BigDog):
    def eat(self):
        print("吃蟠桃")
        print("=" * 20)

        # 多继承中子类调用父类同名方法：
        # 1. 父类名.同名方法(self, 形参1, ……)：调用指定的父类
        SmallDog.eat(self)
        print("=" * 20)
        # 2.super(类名, self).同名方法(形参1, ……)：调用继承顺序中类名的下一个类的同名方法
        # (<class '__main__.SuperDog'>, <class '__main__.SmallDog'>, <class '__main__.BigDog'>, <class 'object'>)
        super(SuperDog, self).eat()
        print("=" * 20)
        # 3.super().同名方法(形参1, ……) ：调用先继承父类的同名方法
        super().eat()
        print("=" * 20)


# 创建子类对象并调用方法
dog1 = SuperDog()
dog1.eat()
