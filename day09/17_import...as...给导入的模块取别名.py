# @Time : 2022/2/2 20:52 
# @Author : Jface 
# @desc :
"""
模块起别名
导入格式：import 模块 as 模块别名
使用格式：模块别名.工具(工具指函数、类、变量)

模块工具起别名
导入格式：from 模块 import 工具 as 工具别名
使用格式：工具别名  无需通过模块名引用
"""

# 1. 把复杂名字改简单些
# import random as r
# ret = r.randint(1, 3)
# print(ret)

# 2. 把已经同名的名字改一个不同名的名字
from random import TWOPI as TP

TWOPI = 6.28

print(TWOPI)

print(TP)
