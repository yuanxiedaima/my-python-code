# @Time : 2022/2/2 18:55 
# @Author : Jface 
# @desc :
"""
如果类属性和实例属性同名，实例对象名只能操作实例属性
"""


class Dog(object):
    # 类属性
    count = 0

    def __init__(self):
        # 实例属性
        self.count = 250


d1 = Dog()
print(d1.count, Dog.count)
# 250 0
