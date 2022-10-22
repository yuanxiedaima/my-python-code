# @Time : 2022/2/2 20:48 
# @Author : Jface 
# @desc :
"""
导入格式：     from 模块名 import 需使用的函数、类、变量
使用格式：     函数、类、变量   无需通过模块名引用
"""
from random import randint, Random, TWOPI

ret = randint(1, 10)
print(ret)

ret = Random()
print(type(ret))

print(TWOPI)
