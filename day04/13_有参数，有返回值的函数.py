# @Time : 2022/1/25 22:25 
# @Author : Jface 
# @desc :
"""
有参数，有返回值的函数
函数定义：
def 函数名字(形参1，形参2，……):
    函数体
    return 返回结果

函数调用：
返回变量 = 函数名字(实参1，实参2，……)

循环累加流程：
# 1. 设置条件变量
# 2. while 条件(i <= n):
    # 3. 累加
    # 4. 条件变量改变
# 5. 循环外面，返回累加的最终结果
"""


# 函数定义
def func_sum(n):
    """
    求 1~n 的累加
    :param n: 累加的数字个数
    :return: 累加的结果
    """
    i = 1
    _sum = 0

    while i < n:
        _sum += i
        # 条件变量改变
        i += 1
    # 返回累加结果
    return _sum


# 函数调用
ret = func_sum(100)
print(ret)
