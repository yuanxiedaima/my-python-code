# @Time : 2022/2/1 19:58 
# @Author : Jface 
# @desc :
"""
__str__方法:
    1. 返回值必须是字符串类型
    2. print(对象变量名)  对象变量名的位置替换为__str__()方法返回值的内容
"""


class Dog(object):
    def __init__(self, _name, _age):  # 创建对象时,自动调用的方法
        self.name = _name
        self.age = _age
        print("init方法被调用")

    def __str__(self):  # 打印对象时,自动调用的方法
        # 返回值必须是字符串类型
        return "我叫 %s, 我今年 %d 岁." % (self.name, self.age)


dog1 = Dog("旺财", 3)

# 没有实现__str__方法时,输出 <__main__.Dog object at 0x0000025F9F2B5910>
# 实现了__str__方法后,print(对象)会自动输出__str__的返回字符串.
print(dog1)

# 相当于
# print("我叫 %s, 我今年 %d 岁." % (self.name, self.age))
