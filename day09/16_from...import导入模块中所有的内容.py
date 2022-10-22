# @Time : 2022/2/2 20:51 
# @Author : Jface 
# @desc :
"""
导入格式：     from 模块名 import *
使用格式：     函数、类、变量   无需通过模块名引用
"""

from random import *

ret = randint(1, 3)
print(ret)

ret = Random()
print(type(ret))

# print(TWOPI)  # TWOPI不在模块的__all__列表中
