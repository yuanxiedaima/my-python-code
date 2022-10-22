# @Time : 2022/2/1 21:34 
# @Author : Jface 
# @desc :
"""
查看类的继承关系
查看类的继承顺序: 类名.__mro__
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


print(SuperDog.__mro__)
