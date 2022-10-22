# @Time : 2022/2/1 21:36 
# @Author : Jface 
# @desc :
"""

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
# 子类没有实现eat方法, 会按照__mro__继承顺序查询eat方法,
#   由于继承顺序表中SuperDog的下一个类是SmallDog,所以调用SmallDog的eat方法
# # (<class '__main__.SuperDog'>, <class '__main__.SmallDog'>, <class '__main__.BigDog'>, <class 'object'>)
dog1.eat()
dog1.drink()
