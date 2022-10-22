# @Time : 2022/2/1 20:55 
# @Author : Jface 
# @desc :
"""
单继承：只有一个父类
"""


class Animal(object):
    def eat(self):
        print("吃东西")


# 定义一个子类，只有一个父类 (单继承)
class Dog(Animal):
    pass


# 创建子类对象
dog1 = Dog()

dog1.eat()
