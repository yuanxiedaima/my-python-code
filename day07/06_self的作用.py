# @Time : 2022/1/31 20:46 
# @Author : Jface 
# @desc : self作用：为了区分不同对象的属性和方法
"""
self作用：为了区分不同对象的属性和方法
"""


# 定义类
class Dog(object):
    def eat(self):
        # self作用：为了区分不同对象的属性和方法
        print("%s啃骨头" % (self.name))


# 创建对象，实例化对象
dog1 = Dog()

# 添加属性
dog1.name = "旺财"

# 直接调用方法
dog1.eat()

dog2 = Dog()

dog2.name = "二哈"

dog2.eat()
