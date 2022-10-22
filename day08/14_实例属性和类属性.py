# @Time : 2022/2/1 21:51 
# @Author : Jface 
# @desc :
"""
实例属性：
    1. 通过在__init__方法里面给实例对象添加的属性
    2. 在类的外面，直接通过实例对象添加的属性
    3. 实例属性 必须通过 实例对象 才能访问
类属性：
    1. 定义在 类里面，类方法外面 的变量就是 类属性
    2. 类属性可以使用 类名 或 实例对象 访问，推荐使用类名
"""


class Dog(object):
    def __init__(self, _name):
        # 1. 通过在__init__方法里面给实例对象添加的属性
        # 添加实例属性 : self就是当前对象(实例)本身,self.属性就是实例属性
        self.name = _name


dog1 = Dog("旺财")
# 添加实例属性: 2. 在类的外面，直接通过实例对象添加的属性
dog1.age = 2
# 实例属性必须通过 实例对象 才能访问
print(dog1.name)
print(dog1.age)


# 类属性：
#     1. 定义在 类里面，类方法外面 的变量就是 类属性
#     2. 类属性可以使用 类名 或 实例对象 访问，推荐使用类名

class Cat(object):
    count = 0

    def __init__(self, _name):
        self.name = _name  # 实例属性


# 类属性可以使用 类名 或 实例对象 访问，推荐使用类名
print(Cat.count)
cat1 = Cat("李白")
print(cat1.count)
