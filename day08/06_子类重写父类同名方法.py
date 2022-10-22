# @Time : 2022/2/1 20:59
# @Author : Jface
# @desc :
"""
1. 父类的方法不能满足子类的需要，可以对父类的方法重写，重写父类方法的目的是为了给他扩展功能
2. 在子类中定义了一个和父类同名的方法(参数也一样)，即为对父类的方法重写
3. 子类调用同名方法，默认只会调用子类的
"""


# 定义父类，Animal
class Animal(object):
    def __init__(self):
        print("Animal 的初始化")
        self.type = "动物"

    def print_type(self):
        print("Animal类中的print_type:", self.type)


# 定义一个子类，继承与Animal
# class Dog(Animal):  # 子类没有实现自己的__init__和print_type,那么使用父类的.
#    pass

class Dog(Animal):
    # 子类写了一个和父类同名的方法, 重写父类方法
    # 使用子类创建对象会默认调用这个__init__()
    def __init__(self):
        print("Dog 类的初始化")
        self.type = "可爱的小狗"

    def print_type(self):
        print("Dog类中的print_type: ", self.type)


# 定义一个子类对象
dog1 = Dog()
dog1.print_type()
