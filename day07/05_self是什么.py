# @Time : 2022/1/31 20:42 
# @Author : Jface 
# @desc :
"""
self是什么：哪个对象调用方法，方法中self就是这个对象本身
"""


class Dog(object):
    def print_info(self):
        print("方法中  self 地址: ", id(self))


dog1 = Dog()
print("调用方法前: dog1地址", id(dog1))
dog1.print_info()  # 解释器底层,会自动转换成 dog1.print_info(dog1)

dog2 = Dog()
print("调用方法前: ", id(dog2))
dog2.print_info()  # 解释器底层,会自动转换成 dog2.print_info(dog2)
print("调用方法后: ", id(dog2))