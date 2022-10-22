# @Time : 2022/1/23 14:54 
# @Author : Jface 
# @desc :
"""
if 实现三目运算操作，就是简洁版的if else
需求：通过if-else求2个数的最大值
"""

# 1. 定义2个变量，赋值
a = 10
b = 20
# 2. if 用大于比较2个变量大小：
if a > b:
    #  2.1 如果满足条件，把大的那个数保存
    _max = a
# 3. 否则，不满足条件：
else:
    #  3.1 把小的那个数保存
    _max = b
# 4. if 语句的外面，大于最大值
print(_max)

# 通过三目运算符实现同样效果
a = 100
b = 200
_max2 = a if a > b else b
print(_max2)
