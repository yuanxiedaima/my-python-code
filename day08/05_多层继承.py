# @Time : 2022/2/1 20:58 
# @Author : Jface 
# @desc :
"""
生活中的多层继承：几代人关系，爷爷、父亲、儿子
"""


# 定义一个爷爷类， Animal
class Animal(object):
    def eat(self):
        print("吃东西")


# 定义一个父亲类
class Dog(Animal):
    def drink(self):
        print("喝东西")


# 定义一个儿子类
class Son(Dog):
    pass


# 创建对象
s1 = Son()
s1.eat()
s1.drink()
