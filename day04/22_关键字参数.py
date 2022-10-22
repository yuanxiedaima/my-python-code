# @Time : 2022/1/25 22:47 
# @Author : Jface 
# @desc :
"""
# 函数调用时，通过 形参=值 方式为函数形参传值
# 不用按照位置为函数形参传值，这种方式叫关键字参数
"""


# 函数定义
def foo(num1, num2):
    print(num1, num2)


def foo2(num1, num2, num3, num4):
    print(num1, num2, num3, num4)


# 函数调用
foo(num2=100, num1=200)
foo2(1, 2, num4=3, num3=4)

# 注意1: 关键字参数必须在位置参数的右边
# SyntaxError: positional argument follows keyword argument
# foo3(1, num4=3, 2, num3=4)

# 注意2: 对同一个形参不能重复传值
# TypeError: foo2() got multiple values for argument 'num3'
# foo2(1, 2, 3, num3=300, num4=4)
