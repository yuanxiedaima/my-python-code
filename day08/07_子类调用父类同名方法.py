# @Time : 2022/2/1 21:15 
# @Author : Jface 
# @desc :
"""
1. 父类的方法不能满足子类的需要，可以对父类的方法重写，重写父类方法的目的是为了给他扩展功能
2. 在子类中定义了一个和父类同名的方法(参数也一样)，即为对父类的方法重写
3. 子类调用同名方法，默认只会调用子类的
4. 子类调用父类的同名方法
    4.1 父类名.同名方法(self, 形参1, ……)
    4.2 super(子类名, self).同名方法(形参1, ……)
    4.3 super().同名方法(形参1, ……) # 是 4.2 方法的简写
"""


# 定义父类
class Animal(object):
    # 添加 type 属性
    def __init__(self):
        print("Animal类中是__init__")
        self.type = "动物"

    # 定义方法，打印属性
    def print_type(self):
        print("Animal类中的print_type = ", self.type)


# 定义一个子类，继承与Animal
class Dog(Animal):
    def __init__(self):
        print("Dog类中的__init__")
        self.type = "可爱的小狗"

    # print_type和父类的同名，重写父类同名方法
    def print_type(self):
        print("Dog类中的print_type = ", self.type)
        print("=" * 10)

        # 子类中调用父类同名函数的三种方法
        # 方法1： 父类名.同名方法(self, 形参1, ……)
        Animal.__init__(self)
        Animal.print_type(self)
        print("=" * 10)

        # 方法2：super(子类名, self).同名方法(形参1, ……)
        super(Dog, self).__init__()
        super(Dog, self).print_type()
        print("=" * 10)

        # 方法3：super().同名方法(形参1, ……) # 是 4.2 方法的简写
        # 推荐使用的方法
        super().__init__()
        super().print_type()


# 定义一个子类对象
dog1 = Dog()  # 调用子类的__init__
dog1.print_type()  # 调用子类的print_type()
