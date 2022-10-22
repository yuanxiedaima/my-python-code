# @Time : 2022/2/1 20:52 
# @Author : Jface 
# @desc :
"""
继承：复用代码，继承过来的东西可以复用
格式：
class 子类名(父类名)：
    pass

# 父类，也叫基类
# 子类，也叫派生类
"""


# 定义一个父类
class Father(object):
    def __init__(self):
        self.money = 99999

    def print_info(self):
        print(self.money)


# 定义一个子类，继承自 Father
class Son(Father):
    pass


# 子类创建对象
s = Son()

# 子类可以使用父类的属性
print(s.money)
# 子类可以使用父类的方法
s.print_info()
