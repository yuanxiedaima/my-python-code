# @Time : 2022/2/1 21:49 
# @Author : Jface 
# @desc :
"""
1. 多态：多种形态，调用同一个函数，不同表现

2. 实现多态的步骤:
  1. 实现继承关系
  2. 子类重写父类方法
  3. 通过对象调用该方法
"""


# 定义一个父类， Animal
class Animal(object):
    def eat(self):
        print("吃东西")


# 定义一个子类Dog，继承于Animal
class Dog(Animal):
    def eat(self):
        print("啃骨头")


# 定义一个子类Cat，继承于Animal
class Cat(Animal):
    def eat(self):
        print("吃小鱼")


# 定义一个函数，用于测试多态
def func(temp):
    temp.eat()


# 创建子类对象
d = Dog()
c = Cat()

# 调用一个函数，不同表现
func(d)
func(c)
