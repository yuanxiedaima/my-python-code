# @Time : 2022/2/2 20:45 
# @Author : Jface 
# @desc :
"""
模块：就是一个py文件，模块里面有：函数的定义，类的定义，全局变量
导入模块：本质上就是导入一个py文件
导入格式：     import 模块名
使用格式：     模块名.函数  模块名.类名  模块名.变量名
"""

# 导入模块
import random

# 模块名.函数
ret = random.randint(1, 3)
print(ret)

# 模块名.类名
# 创建对象
ret = random.Random()
print(type(ret))

# 模块名.变量名
print(random.TWOPI)

TWOPI = 3.1415926
print(TWOPI)
