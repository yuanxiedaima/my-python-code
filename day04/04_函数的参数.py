# @Time : 2022/1/24 22:46 
# @Author : Jface 
# @desc :
"""
函数定义时的参数叫 形参，函数调用时的参数叫 实参

带参数函数的定义格式：
def 函数名字(形参1，形参2，……):
    函数体代码块

带参数函数的调用格式：
函数名字(实参1，实参2，……)
"""


# 带参数函数的函数定义
def func_sum(num1, num2):
    result = num1 + num2
    print("%d+%d=%d" % (num1, num2, result))


# 带参数函数的调用
func_sum(20, 30)

func_sum(100, 200)
