# @Time : 2022/2/2 20:56 
# @Author : Jface 
# @desc :
"""

"""
# 1. 在当前路径找
import random

ret = random.randint(1, 3)
print(ret)

# 2. 如果当前路径没有，找系统路径
# 模块搜索路径存储在system模块的sys.path变量中
import sys

print(sys.path)