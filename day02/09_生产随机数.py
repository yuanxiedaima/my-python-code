# @Time : 2022/1/23 15:27 
# @Author : Jface 
# @desc :产生某个范围的随机数

# 1. 导入模块，工具包，后面会学习
import random
# 2. 调用工具里面的函数，返回一个随机值
num = random.randint(1, 3) # [1,3] 范围 1 2 3 中的随机数
print(num)