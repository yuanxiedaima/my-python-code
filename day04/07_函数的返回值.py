# @Time : 2022/1/24 22:55 
# @Author : Jface 
# @desc :
"""
函数返回值的作用：函数处理完，返回处理结果给调用者
return 关键词：中断函数，同时也返回一个结果
"""


def func_add(num1, num2):
    result = num1 + num2
    return result


ret = func_add(10, 20)
print(ret)
