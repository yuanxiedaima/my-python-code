# @Time : 2022/2/1 20:03 
# @Author : Jface 
# @desc :
"""
在对象的生命周期结束(对象销毁)时, __del__()方法会自动被调用，做一些清理工作
"""


class Dog(object):
    def __del__(self):
        print("我悄悄离开了")


# 设计一个函数，在函数内容创建对象
def foo():
    # 函数调用完毕，里面创建的对象，生命周期结束，自动调用__del__方法
    dog1 = Dog()  # 1. 函数结束,函数中定义的对象会被销毁


print("函数调用前")
# 调用函数
foo()
print("函数调用后")

print("=" * 10)

dog2 = Dog()
del dog2  # 2. del 对象 --> 销毁对象, 自动调用对象的__del__方法

print("=" * 10)
dog3 = Dog()
