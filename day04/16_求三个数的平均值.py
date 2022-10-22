# @Time : 2022/1/25 22:35 
# @Author : Jface 
# @desc :
"""
1. 设计一个函数求三个数的和
2. 设计一个函数求三个数的平均值
    # 2.1 先对3数求和，返回值为求和后的结果
    # 2.2 接着，再求平均值
    # 2.3 最终平均值结果作为函数返回值
"""


# 函数定义
def func_sum(n1, n2, n3):
    """
    求三个数的和
    :param n1: 第一个数
    :param n2: 第二个数
    :param n3: 第三个数
    :return: 返回三个数之和
    """
    return n1 + n2 + n3


def func_avg(n1, n2, n3):
    """
    求三个数的和
    :param n1: 第一个数
    :param n2: 第二个数
    :param n3: 第三个数
    :return: 返回三个数的平均数
    """
    return (n1 + n2 + n3) / 3


# 函数调用
set01 = func_sum(10, 20, 30)
set02 = func_avg(10, 20, 30)

print(set01)
print(set02)
