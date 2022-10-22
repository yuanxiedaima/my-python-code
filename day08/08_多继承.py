# @Time : 2022/2/1 21:31 
# @Author : Jface 
# @desc :
"""
# 格式： class 子类名(父类1， 父类2, ...)：
"""


# 定义2个类，它们没有继承关系，是平级的
class SmallDog(object):
    def eat(self):
        print("吃小东西")


class BigDog(object):
    def drink(self):
        print("喝王老吉")


# 定义一个子类，继承上面 2 个父类（多继承）
class SuperDog(SmallDog, BigDog):
    pass


# 定义子类对象，调用方法
dog1 = SuperDog()
dog1.eat()
dog1.drink()
