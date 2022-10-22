# @Time : 2022/2/2 21:14 
# @Author : Jface 
# @desc :
"""
1. 模块中__all__变量，只对from xxx import *这种导入方式有效
2. __all__格式：
    __all__ = ['变量名', '类名', '函数名'……]
3. 模块中__all__变量包含的元素，才会被from xxx import *导入
"""
__all__ = ["num", "my_add"]
num = 666


def my_add(a, b):
    return a + b


def my_sub(a, b):
    return a - b
