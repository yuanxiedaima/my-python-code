# @Time : 2022/2/2 21:02 
# @Author : Jface 
# @desc :
"""
自定义模块
"""


def my_add(n1, n2):
    """ 实现两个数相加 """
    return n1 + n2


def my_sub(n1, n2):
    """ 实现两个数相减 """
    return n1 - n2


ret = my_add(2, 2)
print('模块中测试代码：my_add(2, 2) = ', ret)

ret = my_sub(10, 2)
print('模块中测试代码：my_sub(10, 2) = ', ret)
